import curses
import json
import re
import subprocess
import time

import IPython.display
import jax
import threading
import os

try:
    import posix
except ModuleNotFoundError:
    posix = None


def is_notebook():
    """Returns True if the code is being run in a notebook, False otherwise."""
    return os.environ.get("IPYTHON") is not None


# Edited version of Jax-SMI from https://github.com/ayaka14732/jax-smi/
def run(note_book=None, interval: float = 1, dir_prefix: str = "/dev/shm", dpr=True):
    """
    The run function is a simple wrapper around the go tool pprof command.
    It runs the command every interval seconds and prints out its output to stdout.
    If you are running this in a Jupyter notebook, it will print to an IPython display object instead of stdout.


    :param note_book: Determine whether the program is running in a notebook or not
    :param interval: float: Specify the interval between each refresh
    :param dir_prefix: str: Specify the directory where the memory
    :param dpr: Determine whether to display the output in a notebook or not
    :return: The output of the pprof command

    """
    if note_book is None:
        note_book = is_notebook()
    std = curses.initscr() if not note_book else None
    try:
        while True:
            if not note_book and dpr:
                std.clear()
            output = subprocess.run(
                args=["go", "tool", "pprof", "-tags", f"{dir_prefix}/memory.prof"],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
            ).stdout.decode("utf-8")
            if not note_book and dpr:
                std.addstr(output)
                std.refresh()
            if note_book and dpr:
                IPython.display.clear_output(True)
                print(output)

            with open(f"{dir_prefix}/memory.json", "w") as fin:
                json.dump({
                    "log": output
                }, fin)
            time.sleep(interval)
    except KeyboardInterrupt:
        curses.endwin()


def get_memory_information(dir_prefix: str = "/dev/shm") -> str:
    """
    The get_memory_information function is a wrapper around the go tool pprof command.
    It takes in an optional argument, dir_prefix, which defaults to /dev/shm.
    The function then runs the go tool pprof command with arguments -tags and {dir_prefix}/memory.prof.
    The output of this command is captured and returned as a string.

    :param dir_prefix: str: Specify the directory prefix for
    :return: A string that contains the memory profile

    """
    return subprocess.run(
        args=["go", "tool", "pprof", "-tags", f"{dir_prefix}/memory.prof"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    ).stdout.decode("utf-8")


def initialise_tracking(interval: float = 1., dir_prefix: str = "/dev/shm") -> None:
    """
    The initialise_tracking function starts a daemon thread that periodically saves the memory profile to disk.
    The outer function starts the daemon thread and returns a context manager that stops it when
    the context exits.  The inner function uses posix.rename() to atomically replace an existing file,
    so we can be sure that any given memory profile was taken at some point during the lifetime of its
    context.

    :param interval: float: Set the time interval between each memory profile
    :param dir_prefix: str: Specify the directory where the memory profile will be saved
    :return: A thread object

    """

    def inner():
        """
        The inner function is a daemon thread that periodically saves the memory profile to disk.
        The outer function starts the daemon thread and returns a context manager that stops it when
        the context exits.  The inner function uses posix.rename() to atomically replace an existing file,
        so we can be sure that any given memory profile was taken at some point during the lifetime of its
        context.

        :return: A thread object

        """
        while True:
            jax.profiler.save_device_memory_profile(f"{dir_prefix}/memory.prof.new")
            if posix is not None:
                os.rename(f"{dir_prefix}/memory.prof.new", f"{dir_prefix}/memory.prof")
            else:
                posix.rename(f"{dir_prefix}/memory.prof.new", f"{dir_prefix}/memory.prof")
            time.sleep(interval)

    thread = threading.Thread(target=inner, daemon=True)
    thread.start()


def threaded_log(interval: float = 1., dir_prefix: str = "/dev/shm", save_mem_json: bool = False) -> threading.Thread:
    """
    The threaded_log function is a wrapper around the get_memory_information function.
    It allows you to monitor your memory usage in real time, and optionally save it to a JSON file.
    The threaded_log function returns a threading.Thread object that can be started with .start() and stopped with .join().


    :param interval: float: Set the time interval between each memory log
    :param dir_prefix: str: Specify the directory to save the memory
    :param save_mem_json: bool: Save the memory information to a json file
    :return: A threading

    """
    note_book = is_notebook()

    def show_():

        std = curses.initscr() if not note_book else None
        try:
            while True:
                mem_info = get_memory_information()
                if not note_book:
                    std.clear()
                    std.addstr(mem_info)
                    std.refresh()
                if note_book:
                    IPython.display.clear_output(True)
                    print(mem_info)
                if save_mem_json:
                    with open(f"{dir_prefix}/memory.json", "w") as fin:
                        json.dump({
                            "log": mem_info
                        }, fin)
                time.sleep(interval)
        except KeyboardInterrupt:
            curses.endwin()

    thread = threading.Thread(
        target=show_
    )
    return thread


def get_capacity_matrix(dir_prefix: str = "/dev/shm") -> dict:
    pattern = r"(\d+\.\d+\wB) \((\d+\.\d+%)\): (\w+)(\(.*?\))?"

    def calculate_full_size(size, percent):
        size_in_gb = float(re.search(r"(\d+\.\d+)GB", size).group(1))
        percent_value = 100 / float(re.search(r"(\d+\.\d+)%", percent).group(1))
        full_size = size_in_gb * percent_value
        return full_size

    matches = re.findall(pattern, get_memory_information(dir_prefix=dir_prefix))
    information = {}
    try:
        for match in matches:
            information[match[2]] = {
                "Used": match[0],
                "Usage Percent": match[1],
                "Process": match[3][1:] if match[3] else "∞",
                "Full Capacity": calculate_full_size(match[0], match[1])
            }
    except (ArithmeticError, AttributeError, KeyError, ValueError):
        ...
    return information
