import enum

import chex
import jax.numpy as np
from flax.training import common_utils
from jax.scipy.special import logsumexp
import jax
from jax import numpy as jnp, Array
from typing import Mapping, Optional, Tuple, Union
from functools import reduce
from operator import mul


# Mean Squared Error
def mse(labels, predictions):
    """
    The mse function computes the mean squared error between two arrays.

    :param labels: Pass in the actual values of the data, and predictions is used to pass in our predicted values
    :param predictions: Store the predictions made by the model
    :return: The mean squared error (mse) between the labels and predictions
    
    """
    return np.mean((labels - predictions) ** 2)


# Mean Absolute Error
def mae(labels, predictions):
    """
    The mae function calculates the mean absolute error between two lists of numbers.

    :param labels: Store the actual values of the data
    :param predictions: Store the predictions from the model
    :return: The mean absolute error between the labels and predictions
    
    """
    return np.mean(np.abs(labels - predictions))


# Cross Entropy
def cross_entropy(labels, predictions, ignore_index=None):
    """
    The cross_entropy function computes the cross entropy loss between a set of labels and predictions.

    :param labels: Calculate the cross entropy loss
    :param predictions: Calculate the log_softmax
    :param ignore_index: Mask out the loss from a specific class
    :return: The average cross entropy over the batch
    
    """
    labels = jax.nn.one_hot(labels, predictions.shape[-1])
    if ignore_index is not None:
        mask = np.ones_like(labels)
        mask = np.where(labels == ignore_index, 0, mask)
        labels = labels * mask
        predictions = predictions * mask
    log_softmax = predictions - logsumexp(predictions, axis=-1, keepdims=True)
    return -np.sum(labels * log_softmax) / labels.shape[0]


# Binary Cross Entropy
def binary_cross_entropy(labels, predictions):
    """
    The binary_cross_entropy function computes the binary cross entropy loss between
    the labels and predictions. The function takes two arguments:
        1) labels: a tensor of shape (batch_size, num_classes) containing the ground truth class indices for each
        example in the batch.
        2) predictions: a tensor of shape (batch_size, num_classes) containing model output probabilities for each
        example in the batch.

    :param labels: Specify the true class of each example
    :param predictions: Calculate the loss
    :return: The cross-entropy loss for binary classification
    
    """
    labels = jax.nn.one_hot(labels, predictions.shape[-1])
    return -np.mean(labels * np.log(predictions + 1e-8) + (1 - labels) * np.log(1 - predictions + 1e-8))


# Negative Log Likelihood
def nll(labels, predictions):
    """
    The nll function computes the negative log likelihood of a set of predictions.

    :param labels: Calculate the loss
    :param predictions: Calculate the loss
    :return: The negative log likelihood of the predictions
    
    """
    return -np.sum(labels * np.log(predictions + 1e-8))


# L2 Loss
def l2(labels, predictions):
    """
    The l2 function computes the sum of squared differences between labels and predictions.

    :param labels: Calculate the difference between the labels and predictions
    :param predictions: Calculate the difference between the labels and predictions
    :return: The sum of the squared differences between labels and predictions
    
    """
    return np.sum((labels - predictions) ** 2)


# Hinge Loss
def hinge(labels, predictions):
    """
    The hinge function is a loss function used for training classifiers.
    The hinge loss is used for &quot;maximum-margin&quot; classification, most notably
    for support vector machines (SVMs).
    For an intended output t = + 1 or - 1 and a classifier score y, the hinge loss of the prediction y is defined as:

    :param labels: Calculate the hinge loss
    :param predictions: Calculate the hinge loss
    :return: The average loss over the training set
    
    """
    return np.mean(np.maximum(0, 1 - labels * predictions))


# Log-Cosh Loss
def log_cosh(labels, predictions):
    """
    The log_cosh function is a loss function that takes in two arguments: labels and predictions.
    The log_cosh function returns the mean of the logarithm of the hyperbolic cosine of (predictions - labels).
    This loss function is used to measure how well our model performs on data it has not seen before.

    :param labels: Pass the actual values of the data
    :param predictions: Pass the predictions of your model
    :return: The logarithm of the hyperbolic cosine of the prediction error
    
    """

    def cosh(x):
        return (np.exp(x) + np.exp(-x)) / 2

    return np.mean(np.log(cosh(predictions - labels)))


def binary_cross_entropy_onehot(labels, predictions):
    """
    The binary_cross_entropy_onehot function takes in two arguments:
        labels: a 1D array of integers, where each integer is the index of the correct class for that example.
        predictions: a 2D array of floats, where each row represents an example and each column represents a class.

    :param labels: Determine the correct class of each image
    :param predictions: Calculate the loss
    :return: The binary cross entropy loss between the labels and predictions
    
    """
    labels = jax.nn.one_hot(labels, predictions.shape[-1])
    return -np.mean(labels * np.log(predictions + 1e-8) + (1 - labels) * np.log(1 - predictions + 1e-8))


def cross_entropy_onehot(labels, predictions):
    """
    The cross_entropy_onehot function takes two arguments:
    labels - a 1D array of integers in the range [0, num_classes)
    predictions - a 2D array of floats with shape (num_examples, num_classes)
    The function returns the cross entropy loss between labels and predictions. The loss is averaged over all examples.

    :param labels: Compute the one-hot encoding of the labels
    :param predictions: Calculate the log_softmax
    :return: The cross entropy loss
    
    """
    labels = jax.nn.one_hot(labels, predictions.shape[-1])
    log_softmax = predictions - logsumexp(predictions, axis=-1, keepdims=True)
    return -np.sum(labels * log_softmax) / labels.shape[0]


def mse_loss(val, target, valid=None):
    """
    The mse_loss function computes the mean squared error between two arrays.

    :param val: Store the output of the model
    :param target: Calculate the loss
    :param valid: Mask out the loss of certain pixels
    :return: The mean square error of the input and target
    
    """
    if valid is None:
        valid = jnp.ones((*target.shape[:2], 1))
    valid = valid.astype(jnp.float32)
    loss = jnp.mean(
        jnp.where(
            valid > 0.0,
            jnp.square(val - target),
            0.0
        )
    )
    return loss


def cross_entropy_loss_and_accuracy(logits: chex.Array, tokens: chex.Array, valid: chex.Array = None):
    """

    :param logits: Logits
    :param tokens: labels
    :param valid: attention_mask
    :return: loss and accuracy
    """
    if valid is None:
        valid = jnp.ones(tokens.shape[:2])
    valid = valid.astype(jnp.float32)
    valid_text_length = jnp.maximum(jnp.sum(valid, axis=-1), 1e-10)
    logits = logits.astype(jnp.float32)  # for numerical stability
    token_log_prob = jnp.squeeze(
        jnp.take_along_axis(
            jax.nn.log_softmax(logits, axis=-1),
            jnp.expand_dims(tokens, -1),
            axis=-1,
        ),
        -1,
    )
    token_log_prob = jnp.where(valid > 0.0, token_log_prob, jnp.array(0.0))
    loss = -jnp.mean(jnp.sum(token_log_prob, axis=-1) / valid_text_length)
    correct = jnp.where(
        valid > 0.0,
        jnp.argmax(logits, axis=-1) == tokens,
        jnp.array(False)
    )
    accuracy = jnp.mean(jnp.sum(correct, axis=-1) / valid_text_length)
    return loss, accuracy


def fused_cross_entropy_loss_and_accuracy(logits: chex.Array, tokens: chex.Array, valid: chex.Array = None):
    """

    :param logits: Logits
    :param tokens: labels
    :param valid: attention_mask
    :return: loss and accuracy
    """
    if valid is None:
        valid = jnp.ones(tokens.shape[:2])
    valid = valid.astype(jnp.float32)
    valid_text_length = jnp.maximum(jnp.sum(valid, axis=-1), 1e-10)
    logits = logits.astype(jnp.float32)
    log_probs = jax.nn.log_softmax(logits, axis=-1)
    token_log_prob = jnp.squeeze(
        jnp.take_along_axis(
            log_probs,
            jnp.expand_dims(tokens, -1),
            axis=-1,
        ),
        -1,
    )
    token_log_prob = jnp.where(valid > 0.0, token_log_prob, jnp.array(0.0))
    loss = -jnp.mean(jnp.sum(token_log_prob, axis=-1) / valid_text_length)
    correct = jnp.where(
        valid > 0.0,
        jnp.argmax(logits, axis=-1) == tokens,
        jnp.array(False)
    )
    accuracy = jnp.mean(jnp.sum(correct, axis=-1) / valid_text_length)
    return loss, accuracy


@jax.custom_vjp
def cross_entropy_with_logits(logits: jnp.ndarray, targets: jnp.ndarray,
                              z_loss: float) -> Tuple[jnp.ndarray, jnp.ndarray]:
    """Computes cross entropy loss with stable custom gradient.

    Computes a stabilized-gradient version of:
      -jnp.sum(targets * nn.log_softmax(logits), axis=-1)

    If z_loss > 0, then an auxiliary loss equal to z_loss*log(z)^2
    will be added to the cross entropy loss (z = softmax normalization constant).
    The two uses of z_loss are:
    1. To keep the logits from drifting too far from zero, which can cause
       unacceptable roundoff errors in bfloat16.
    2. To encourage the logits to be normalized log-probabilities.

    Args:
      logits: [batch, length, num_classes] float array.
      targets: categorical one-hot targets [batch, length, num_classes] float
        array.
      z_loss: coefficient for auxilliary z-loss loss term.

    Returns:
      tuple with the total loss and the z_loss, both
      float arrays with shape [batch, length].
    """
    logits_sum = jax.scipy.special.logsumexp(logits, axis=-1, keepdims=True)
    log_softmax = logits - logits_sum
    loss = -jnp.sum(targets * log_softmax, axis=-1)
    # Add auxilliary z-loss term.
    log_z = jnp.squeeze(logits_sum, axis=-1)
    total_z_loss = z_loss * jax.lax.square(log_z)
    loss += total_z_loss
    return loss, total_z_loss


def _cross_entropy_with_logits_fwd(
        logits: jnp.ndarray,
        targets: jnp.ndarray,
        z_loss: float = 0.0
) -> Tuple[Tuple[Array, Array], Tuple[Array, Array, float, Array, Array, Array, Array]]:
    """Forward-mode of `cross_entropy_with_logits`."""
    max_logit = logits.max(axis=-1, keepdims=True)
    shifted = logits - max_logit
    exp_shifted = jnp.exp(shifted)
    sum_exp = jnp.sum(exp_shifted, axis=-1, keepdims=True)
    log_softmax = shifted - jnp.log(sum_exp)
    loss = -jnp.sum(targets * log_softmax, axis=-1)
    # Add auxilliary z-loss term.
    log_z = jnp.squeeze(jnp.log(sum_exp) + max_logit, axis=-1)
    total_z_loss = z_loss * jax.lax.square(log_z)
    loss += total_z_loss
    return (loss, total_z_loss), (logits, targets, z_loss, exp_shifted, sum_exp, log_softmax, log_z)


def _cross_entropy_with_logits_bwd(
        res: Tuple[jnp.ndarray, jnp.ndarray, jnp.ndarray, jnp.ndarray, jnp.ndarray,
        jnp.ndarray, jnp.ndarray], g: Tuple[jnp.ndarray, jnp.ndarray]
) -> Tuple[jnp.ndarray, jnp.ndarray, jnp.ndarray]:
    """Backward-mode of `cross_entropy_with_logits`."""
    g = g[0]  # Ignore z_loss component as that is only used for logging.
    logits, targets, z_loss, exp_shifted, sum_exp, log_softmax, log_z = res
    # z-loss term adds the (2 * z_loss * log_z) factor.
    deriv = (
            jnp.expand_dims(1 + 2 * z_loss * log_z, -1) * exp_shifted / sum_exp -
            targets)
    g_logits = jnp.expand_dims(g, axis=-1) * deriv
    g_targets = -jnp.expand_dims(g, axis=-1) * log_softmax
    return (jnp.asarray(g_logits,
                        logits.dtype), jnp.asarray(g_targets, targets.dtype),
            jnp.array(0.0))  # sets z-loss coeff gradient to 0


cross_entropy_with_logits.defvjp(_cross_entropy_with_logits_fwd,
                                 _cross_entropy_with_logits_bwd)


def compute_weighted_cross_entropy(
        logits: jnp.ndarray,
        targets: jnp.ndarray,
        weights: Optional[jnp.ndarray] = None,
        label_smoothing: float = 0.0,
        z_loss: float = 0.0,
        loss_normalizing_factor: Optional[float] = None
) -> Tuple[jnp.ndarray, jnp.ndarray, jnp.ndarray]:
    """Compute weighted cross entropy and entropy for log probs and targets.

    Args:
     logits: [batch, length, num_classes] float array.
     targets: categorical targets [batch, length] int array.
     weights: None or array of shape [batch, length].
     label_smoothing: label smoothing constant, used to determine the on and off
       values.
     z_loss: coefficient for auxiliary z-loss loss term.
     loss_normalizing_factor: Constant to divide loss by. If not specified, loss
       will not be normalized. Intended for backward compatibility with T5-MTF
       training. Should not normally be used.

    Returns:
      Tuple of scalar loss, z_loss, and weight sum.
    """
    if logits.ndim != targets.ndim + 1:
        raise ValueError('Incorrect shapes. Got shape %s logits and %s targets' %
                         (str(logits.shape), str(targets.shape)))
    vocab_size = logits.shape[-1]
    confidence = 1.0 - label_smoothing
    low_confidence = (1.0 - confidence) / (vocab_size - 1)
    normalizing_constant = -(
            confidence * jnp.log(confidence) +
            (vocab_size - 1) * low_confidence * jnp.log(low_confidence + 1e-20))
    soft_targets = common_utils.onehot(
        targets, vocab_size, on_value=confidence, off_value=low_confidence)
    total_loss, total_z_loss = cross_entropy_with_logits(
        logits, soft_targets, z_loss=z_loss)
    total_loss = total_loss - normalizing_constant

    shape_dtype_struct = jax.eval_shape(lambda x: x, targets)
    weight_sum = reduce(mul, shape_dtype_struct.shape, 1)
    if weights is not None:
        total_loss = total_loss * weights
        total_z_loss = total_z_loss * weights
        weight_sum = jnp.sum(weights)

    # By default, we do not normalize loss based on anything.
    # We don't normalize based on batch size because the optimizers we use are
    # pretty much scale invariant, so this simplifies things.
    # We don't normalize based on number of non-padding tokens in order to treat
    # each token as equally important regardless of sequence length.
    if loss_normalizing_factor is not None:
        total_loss /= loss_normalizing_factor
        total_z_loss /= loss_normalizing_factor
    return jnp.sum(total_loss), jnp.sum(total_z_loss), weight_sum


def compute_weighted_cross_entropy_and_accuracy(
        logits: jnp.ndarray,
        targets: jnp.ndarray,
        weights: Optional[jnp.ndarray] = None,
        label_smoothing: float = 0.0,
        z_loss: float = 0.0,
        loss_normalizing_factor: Optional[float] = None,
) -> Tuple[jnp.ndarray, jnp.ndarray, jnp.ndarray, jnp.ndarray]:
    """Compute weighted cross entropy and entropy for log probs and targets.

    Args:
     logits: [batch, length, num_classes] float array.
     targets: categorical targets [batch, length] int array.
     weights: None or array of shape [batch, length].
     label_smoothing: label smoothing constant, used to determine the on and off
       values.
     z_loss: coefficient for auxiliary z-loss loss term.
     loss_normalizing_factor: Constant to divide loss by. If not specified, loss
       will not be normalized. Intended for backward compatibility with T5-MTF
       training. Should not normally be used.

    Returns:
      Tuple of scalar loss, z_loss, weight sum and accuracy
    """
    total_loss, total_z_loss, weight_sum = compute_weighted_cross_entropy(
        logits, targets, weights, label_smoothing, z_loss, loss_normalizing_factor)

    predictions = jnp.argmax(logits, axis=-1)
    correct_predictions = jnp.equal(predictions, targets).astype(jnp.float32)
    accuracy = jnp.sum(correct_predictions * weights) / weight_sum

    return total_loss, total_z_loss, weight_sum, accuracy


@enum.unique
class SpecialLossNormalizingFactor(enum.Enum):
    """Specially calculated loss_normalizing_factors, that are not a constant.

    Attributes:
      NUM_REAL_TARGET_TOKENS: Whether to divide the loss by the number of real
        (non-padding) tokens in the current target batch. If
        'decoder_loss_weights' are specified, it will be the sum of the weights.
        Otherwise it will be the number of non-zero 'decoder_target_tokens'.
      NUM_TOTAL_TARGET_TOKENS: Whether to divide the loss by the total number of
        target tokens, i.e., batch_size * target_seq_length (including padding).
      AVERAGE_PER_SEQUENCE: This will first compute the per-sequence loss
        (averaged over the number of real target tokens in the sequence), and then
        compute the average of that over the sequences. This can be preferable to
        NUM_REAL_TARGET_TOKENS for finetuning, because it will weigh all examples
        equally, regardless of sequence length (which can be especially important
        for multi-task finetuning).
    """
    NUM_REAL_TARGET_TOKENS = 1
    NUM_TOTAL_TARGET_TOKENS = 2
    AVERAGE_PER_SEQUENCE = 3


def convert_special_loss_normalizing_factor_to_enum(
        x: str) -> SpecialLossNormalizingFactor:
    """Converts stringified version of LNF to an enum.

    This is useful because gin dynamic registration does not (currently)
    have support for enum.

    Args:
      x: stringified version of SpecialLossNormalizingFactor enum.

    Returns:
      SpecialLossNormalizingFactor enum instance.
    """
    x = x.upper()
    if x == 'NUM_REAL_TARGET_TOKENS':
        return SpecialLossNormalizingFactor.NUM_REAL_TARGET_TOKENS
    if x == 'NUM_TOTAL_TARGET_TOKENS':
        return SpecialLossNormalizingFactor.NUM_TOTAL_TARGET_TOKENS
    if x == 'AVERAGE_PER_SEQUENCE':
        return SpecialLossNormalizingFactor.AVERAGE_PER_SEQUENCE
    raise ValueError(
        'Could not convert string \"%s\" to SpecialLossNormalizingFactor' % x)


@jax.vmap
def _sum_weights_per_segment(positions: jnp.ndarray, segment_ids: jnp.ndarray,
                             weights: jnp.ndarray) -> jnp.ndarray:
    """Sums weights per packed segment to produce a normalizing vector."""

    # NB: Assumes padding only occurs at the end of a sequence.

    def _repeat_last_nonnegative(xs, reverse=False):
        def fn(prev, x):
            y = jnp.where(x == 0, prev, x)
            return y, y

        return jax.lax.scan(fn, jnp.zeros_like(xs[0]), xs, reverse=reverse)[1]

    # Compute final positions per sequence.
    start_positions = positions == 0
    final_positions = jnp.concatenate([start_positions[1:], jnp.ones(1)])
    # Clear padded positions.
    final_positions *= segment_ids != 0
    # Compute cumulative weights, clearing all but final position per sequence.
    final_cumulative_weights = final_positions * jnp.cumsum(weights)
    # Subtract sequences' final weights from cumulative weights of following ones.
    final_total_weights = jnp.concatenate([
        final_cumulative_weights[0:1],
        jnp.diff(_repeat_last_nonnegative(final_cumulative_weights))
    ])
    # Copy final sequence weight to all positions in sequence.
    normalizer = _repeat_last_nonnegative(final_total_weights, reverse=True)
    return normalizer


def get_loss_normalizing_factor_and_weights(
        loss_normalizing_factor: Optional[Union[float, int, str,
        SpecialLossNormalizingFactor]],
        batch: Mapping[str, jnp.ndarray]
):
    """Get the float loss_normalizing_factor and loss weights.

    If loss_normalizing_factor is float or None, this will simply return the
    input loss_normalizing_factor and batch.

    If loss_normalizing_factor is a SpecialLossNormalizingFactor, it will
    return a float loss_normalizing_factor and loss weights corresponding to
    the special LNF. See SpecialLossNormalizingFactor for more details.

    Args:
      loss_normalizing_factor: The input LNF, which may be a float, None, or
        SpecialLossNormalizingFactor (or a stringified SLNF).
      batch: Input data batch.

    Returns:
      Tuple of (output_loss_normalizing_factor, loss_weights).
        'output_loss_normalizing_factor' is a scalar float (Python float
        or jnp float).
        'loss_weights' is the per token loss weight JNP array.
    """

    loss_weights = batch.get('decoder_loss_weights', None)
    if (loss_normalizing_factor is None or
            not isinstance(loss_normalizing_factor,
                           (str, SpecialLossNormalizingFactor))):
        return (loss_normalizing_factor, loss_weights)

    if isinstance(loss_normalizing_factor, str):
        loss_normalizing_factor = convert_special_loss_normalizing_factor_to_enum(
            loss_normalizing_factor)

    # If `loss_weights` are not provided, we assume that the padding id is 0 and
    # that non-padding tokens in the decoder all correspond to the positions
    # where loss should be taken. If more fine-grained behavior (e.g., taking
    # loss on subset of 'decoder_target_tokens') is desired, provide
    # `loss_weights` that account for this.
    if loss_weights is None:
        loss_weights = jnp.asarray(batch['decoder_target_tokens'] > 0, jnp.float32)

    output_normalizing_factor = None
    if loss_normalizing_factor == SpecialLossNormalizingFactor.NUM_REAL_TARGET_TOKENS:
        output_normalizing_factor = jnp.sum(loss_weights)
    elif loss_normalizing_factor == SpecialLossNormalizingFactor.NUM_TOTAL_TARGET_TOKENS:
        output_normalizing_factor = np.prod(batch['decoder_target_tokens'].shape)
    elif loss_normalizing_factor == SpecialLossNormalizingFactor.AVERAGE_PER_SEQUENCE:
        if 'decoder_segment_ids' in batch:  # is packed
            norm_vec = _sum_weights_per_segment(batch['decoder_positions'],
                                                batch['decoder_segment_ids'],
                                                loss_weights)
        else:
            norm_vec = jnp.sum(loss_weights, axis=-1, keepdims=True)
        # Handle divide-by-zero.
        loss_weights = jnp.nan_to_num(
            loss_weights / norm_vec, nan=0, posinf=0, neginf=0)
        output_normalizing_factor = jnp.sum(loss_weights)
    else:
        raise ValueError('Unsupported value of loss_normalizing_factor: %s' %
                         str(loss_normalizing_factor))

    return output_normalizing_factor, loss_weights


def auxiliary_load_balancing_loss_func(
        gate_logits: chex.Array,
        num_experts: int,
        top_k: int,
        attention_mask: Optional[chex.Array],
) -> chex.Array:
    r"""
    Computes auxiliary load balancing loss as in Switch Transformer - implemented in JAX.
    See Switch Transformer (https://arxiv.org/abs/2101.03961) for more details. This function implements the loss
    function presented in equations (4) - (6) of the paper. It aims at penalizing cases where the routing between
    experts is too unbalanced.
    :param gate_logits :Union[Array, Tuple[Array]: Logits from the `gate`, should be a tuple of
     model.config.num_hidden_layers tensors of shape [batch_size X sequence_length, num_experts].
    :param num_experts :int:Number of experts.
    :param top_k :int: The number of experts each token is routed to.
    :param attention_mask: Optional[chex.Array] : The attention_mask used in forward function shape
        [batch_size X sequence_length] if not None.

    :return loss: chex.Array: The auxiliary loss.
    """
    if gate_logits is None or not isinstance(gate_logits, tuple):
        return jnp.array(0.0, dtype=jnp.float32)
    elif isinstance(gate_logits, tuple):
        concatenated_gate_logits = jnp.concatenate(gate_logits, axis=0)
    else:
        return jnp.array(0.0, dtype=jnp.float32)
    routing_weights = jax.nn.softmax(
        concatenated_gate_logits,
        axis=-1
    )

    _, selected_experts = jax.lax.top_k(routing_weights, top_k)

    expert_mask = jax.nn.one_hot(selected_experts, num_experts)

    if attention_mask is None:
        tokens_per_expert = jnp.mean(expert_mask.astype(jnp.float32), axis=0)
        router_prob_per_expert = jnp.mean(routing_weights, axis=0)
    else:
        batch_size, sequence_length = attention_mask.shape
        num_hidden_layers = concatenated_gate_logits.shape[0] // (batch_size * sequence_length)

        expert_attention_mask = jnp.broadcast_to(
            attention_mask[jnp.newaxis, :, :, jnp.newaxis, jnp.newaxis],
            (num_hidden_layers, batch_size, sequence_length, top_k, num_experts)
        ).reshape(-1, top_k, num_experts)

        tokens_per_expert = jnp.sum(
            expert_mask.astype(jnp.float32) * expert_attention_mask, axis=0
        ) / jnp.sum(expert_attention_mask, axis=0)

        router_per_expert_attention_mask = jnp.broadcast_to(
            attention_mask[jnp.newaxis, :, :, jnp.newaxis],
            (num_hidden_layers, batch_size, sequence_length, num_experts)
        ).reshape(-1, num_experts)

        # Compute the average probability of routing to these experts
        router_prob_per_expert = jnp.sum(
            routing_weights * router_per_expert_attention_mask,
            axis=0
        ) / jnp.sum(router_per_expert_attention_mask, axis=0)

    overall_loss = jnp.sum(tokens_per_expert * jnp.expand_dims(router_prob_per_expert, 0))
    return overall_loss * num_experts
