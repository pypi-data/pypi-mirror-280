from jax import jacrev
from jax.scipy.linalg import solve_triangular
from jax.numpy import sum as arraysum

from .util import GaussianProcessType, batched_vmap


def compute_divergence_function(x, xu, gp_type, L, cov_func, batch_size=100):
    """
    Compute the divergence function for a Gaussian Process (GP) given its type,
    covariance function, and other parameters.

    Parameters
    ----------
    x : array-like, shape (n_samples, n_features)
        Data points for the Gaussian Process.
    xu : array-like, shape (n_inducing_points, n_features)
        Inducing points for sparse Gaussian Processes.
    gp_type : GaussianProcessType enum
        Specifies the type of Gaussian Process. Can be FULL or SPARSE_CHOLESKY.
    L : array-like, shape (n_samples, n_samples) or (n_inducing_points, n_inducing_points)
        Cholesky decomposition of the covariance matrix for the Gaussian Process.
    cov_func : callable
        Covariance function for the Gaussian Process.
    batch_size : int, optional
        The size of the batches for batched computation. Default is 100.

    Returns
    -------
    divergence : callable
        Function that computes the divergence of the Gaussian Process, based on the GP type.
        Accepts `state` as input, which could be either a vector or a matrix depending on the GP type.

    Raises
    ------
    NotImplementedError
        If the provided gp_type is not supported.

    Examples
    --------
    >>> def my_cov_func(x, y):
    ...     return np.exp(-0.5 * np.sum((x - y) ** 2))
    >>> x = np.random.rand(100, 2)
    >>> xu = np.random.rand(20, 2)
    >>> L = np.linalg.cholesky(my_cov_matrix)
    >>> divergence_function = compute_divergence_function(x, xu, GaussianProcessType.FULL, L, my_cov_func)
    >>> state = np.random.rand(100, 100)
    >>> divergence_value = divergence_function(state)

    Notes
    -----
    The function uses batched computation via `batched_vmap` to efficiently compute gradients
    and divergences while conserving memory.
    """

    def compute_cov_grads(y, target):
        return jacrev(cov_func)(y[None, :], target)

    if gp_type == GaussianProcessType.FULL:
        out_shape = (x.shape[0], x.shape[0], x.shape[1])
        cov_grads = batched_vmap(
            compute_cov_grads, x, x, batch_size=batch_size
        ).reshape(out_shape)

        def divergence(state):
            weights = solve_triangular(L.T, solve_triangular(L, state, lower=True))
            return arraysum(
                cov_grads[..., None] * weights[None, :, None, :], axis=(1, 2, 3)
            )

    elif gp_type == GaussianProcessType.SPARSE_CHOLESKY:
        out_shape = (x.shape[0], xu.shape[0], x.shape[1])
        cov_grads = batched_vmap(
            compute_cov_grads, x, xu, batch_size=batch_size
        ).reshape(out_shape)

        def divergence(state):
            weights = solve_triangular(L.T, state)
            return arraysum(
                cov_grads[..., None] * weights[None, :, None, :], axis=(1, 2, 3)
            )

    else:
        raise NotImplementedError(
            f"Model divergence computation not implemented for gp_type {gp_type}."
        )

    return divergence
