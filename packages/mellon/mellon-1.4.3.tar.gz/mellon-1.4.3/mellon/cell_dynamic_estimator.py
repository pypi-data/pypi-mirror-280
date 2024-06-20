import logging
from .base_model import BaseEstimator, DEFAULT_COV_FUNC
from .inference import (
    compute_transform,
    compute_loss_func,
    compute_log_density_x,
    compute_conditional,
    DEFAULT_N_ITER,
    DEFAULT_INIT_LEARN_RATE,
    DEFAULT_JIT,
    DEFAULT_OPTIMIZER,
)
from .parameters import (
    compute_d,
    compute_mu,
    compute_initial_zeros,
    compute_initial_ones,
    compute_time_derivatives,
    compute_density_gradient,
    compute_density_diffusion,
)
from .util import (
    DEFAULT_JITTER,
)
from .validation import (
    validate_array,
)
from .divergence import compute_divergence_function


logger = logging.getLogger("mellon")

DEFAULT_BATCH_SIZE = 100


class CellDynamicEstimator(BaseEstimator):
    R"""
    A class for non-parametric estimation for the vector field describing
    cell-state dynamics. It performs Bayesian inference with
    a Gaussian process prior. The infered vector field minimizes the
    required amount of proliferation and apoptosis to maintain homeostasis
    of the provided density or comply with the dynamics of a provided
    time-sensitive density.

    Parameters
    ----------
    cov_func_curry : function or type
        The generator of the Gaussian process covariance function.
        This must be a curry that takes one length scale argument and returns a
        covariance function of the form k(x, y) :math:`\rightarrow` float.
        Defaults to Matern52.

    n_landmarks : int
        The number of landmark/inducing points. Only used if a sparse GP is indicated
        through gp_type. If 0 or equal to the number of training points, inducing points
        will not be computed or used. Defaults to 5000.

    rank : int or float
        The rank of the approximate covariance matrix for the Nyström rank reduction.
        If rank is an int, an :math:`n \times`
        rank matrix :math:`L` is computed such that :math:`L L^\top \approx K`, where `K` is the
        exact :math:`n \times n` covariance matrix. If rank is a float 0.0 :math:`\le` rank
        :math:`\le` 1.0, the rank/size of :math:`L` is selected such that the included eigenvalues
        of the covariance between landmark points account for the specified percentage of the sum
        of eigenvalues. It is ignored if gp_type does not indicate a Nyström rank reduction.
        Defaults to 0.99.

    gp_type : str or GaussianProcessType
        The type of sparcification used for the Gaussian Process
         - 'full' None-sparse Gaussian Process
         - 'full_nystroem' Sparse GP with Nyström rank reduction without landmarks,
            which lowers the computational complexity.
         - 'sparse_cholesky' Sparse GP using landmarks/inducing points,
            typically employed to enable scalable GP models.
         - 'sparse_nystroem' Sparse GP using landmarks or inducing points,
            along with an improved Nyström rank reduction method.

        The value can be either a string matching one of the above options or an instance of
        the `mellon.util.GaussianProcessType` Enum. If a partial match is found with the
        Enum, a warning will be logged, and the closest match will be used.
        Defaults to 'sparse_cholesky'.

    jitter : float
        A small amount added to the diagonal of the covariance matrix to bind eigenvalues
        numerically away from 0, ensuring numerical stability. Defaults to 1e-6.

    optimizer : str
        The optimizer for the maximum a posteriori or posterior density estimation. Options are
        'L-BFGS-B', stochastic optimizer 'adam', or automatic differentiation variational
        inference 'advi'. Defaults to 'L-BFGS-B'.

    n_iter : int
        The number of optimization iterations. Defaults to 100.

    init_learn_rate : float
        The initial learning rate. Defaults to 1.

    landmarks : array-like or None
        The points used to quantize the data for the approximate covariance. If None,
        landmarks are set as k-means centroids with k=n_landmarks. This is ignored if n_landmarks
        is greater than or equal to the number of training points. Defaults to None.

    nn_distances : array-like or None
        The nearest neighbor distances at each data point. If None, the nearest neighbor
        distances are computed automatically, using a KDTree if the dimensionality of the data
        is less than 20, or a BallTree otherwise. Defaults to None.

    metric : str, optional
        The metric to use for computing distances. Supported options are:
         - 'euclidean' or 'l2' (default): Euclidean distance
         - 'manhattan' or 'l1': Manhattan distance
         - 'chebyshev': Chebyshev distance
         - 'hyperbolic': Hyperbolic distance
        Defaults to 'euclidean'.

    distance_func : function, optional
        A custom distance function to compute distances between points.
        If None, the distance function is determined by the `metric` parameter.
        The custom distance function should take two 2D arrays (each with shape (1, n_features)) as input
        and return a single scalar distance. Defaults to None.

    ls : float or None
        The length scale of the Gaussian process covariance function. If None, `ls` is set to
        the geometric mean of the nearest neighbor distances times a constant. If `cov_func`
        is supplied explicitly, `ls` has no effect. Defaults to None.

    ls_factor : float, optional
        A scaling factor applied to the length scale when it's automatically
        selected. It is used to manually adjust the automatically chosen length
        scale for finer control over the model's sensitivity to variations in the data.

    cov_func : mellon.Covaraince or None
        The Gaussian process covariance function as instance of :class:`mellon.Covaraince`.
        If None, the covariance function `cov_func` is automatically generated as `cov_func_curry(ls)`.
        Defaults to None.

    Lp : array-like or None
        A matrix such that :math:`L_p L_p^\top = \Sigma_p`, where :math:`\Sigma_p` is the
        covariance matrix of the inducing points (all cells in non-sparse GP).
        Not used when Nyström rank reduction is employed. Defaults to None.

    L : array-like or None
        A matrix such that :math:`L L^\top \approx K`, where :math:`K` is the covariance matrix.
        If None, `L` is computed automatically. Defaults to None.

    initial_value : array-like or None
        The initial guess for optimization. If None, we assume it to be the zero vector field.
        Defaults to None.

    predictor_with_uncertainty : bool
        If set to True, computes the predictor instance `.predict` with its predictive uncertainty.
        The uncertainty comes from two sources:

        1) `.predict.mean_covariance`:
            Uncertainty arising from the posterior distribution of the Bayesian inference.
            This component quantifies uncertainties inherent in the model's parameters and structure.
            Available only if `.pre_transformation_std` is defined (e.g., using `optimizer="advi"`),
            which reflects the standard deviation of the latent variables before transformation.

        2) `.predict.covariance`:
            Uncertainty for out-of-bag states originating from the compressed function representation
            in the Gaussian Process. Specifically, this uncertainty corresponds to locations that are
            not inducing points of the Gaussian Process and represents the covariance of the
            conditional normal distribution.

    jit : bool
        Use jax just-in-time compilation for loss and its gradient during optimization.
        Defaults to False.

    check_rank : bool
        Weather to check if landmarks allow sufficient complexity by checking the approximate
        rank of the covariance matrix. This only applies to the non-Nyström gp_types.
        If set to None the rank check is only performed if n_landmarks >= n_samples/10.
        Defaults to None.
    """

    def __init__(
        self,
        density_predictor=None,
        time_derivatives=None,
        density_gradient=None,
        density_diffusion=None,
        cost_proliferation=None,
        cost_apoptosis=None,
        cov_func_curry=DEFAULT_COV_FUNC,
        n_landmarks=None,
        rank=None,
        gp_type=None,
        jitter=DEFAULT_JITTER,
        optimizer=DEFAULT_OPTIMIZER,
        n_iter=DEFAULT_N_ITER,
        init_learn_rate=DEFAULT_INIT_LEARN_RATE,
        landmarks=None,
        nn_distances=None,
        metric=None,
        distance_func=None,
        ls=None,
        ls_factor=1,
        cov_func=None,
        Lp=None,
        L=None,
        initial_value=None,
        predictor_with_uncertainty=False,
        jit=DEFAULT_JIT,
        check_rank=None,
    ):
        super().__init__(
            cov_func_curry=cov_func_curry,
            n_landmarks=n_landmarks,
            rank=rank,
            jitter=jitter,
            gp_type=gp_type,
            optimizer=optimizer,
            n_iter=n_iter,
            init_learn_rate=init_learn_rate,
            landmarks=landmarks,
            nn_distances=nn_distances,
            metric=metric,
            distance_func=distance_func,
            ls=ls,
            ls_factor=ls_factor,
            cov_func=cov_func,
            Lp=Lp,
            L=L,
            initial_value=initial_value,
            predictor_with_uncertainty=predictor_with_uncertainty,
            jit=jit,
            check_rank=check_rank,
        )
        self.density_predictor = density_predictor
        self.time_derivatives = time_derivatives
        self.density_gradient = density_gradient
        self.density_diffusion = density_diffusion
        self.cost_proliferation = cost_proliferation
        self.cost_apoptosis = cost_apoptosis
        self.batch_size = DEFAULT_BATCH_SIZE
        self.transform = None
        self.divergence_function = None
        self.loss_func = None
        self.opt_state = None
        self.losses = None
        self.pre_transformation = None
        self.pre_transformation_std = None
        self.log_density_x = None
        self.log_density_func = None

    def set_times(self, times):
        """
        Sets the training instances (x) for the model and validates that they are
        formatted correctly.

        Parameters
        ----------
        times : array-like of shape (n_samples, )
            The time points of the training instances where `n_samples` is the number of sample.

        Returns
        -------
        array-like of shape (n_samples, )
            The validated training instances.
        """
        n_samp = self.x.shape[0]
        if times.shape[0] != n_samp:
            n_times = times.shap[0]
            message = (
                f"Number of time points in `times` ({n_times:,}) "
                f"does not agree with the number of samples in `x` ({n_samp:,})."
            )
            error = ValueError(message)
            logger.error(error)
            raise error
        if self.times is not None and times is not None and self.times is not times:
            message = "self.times has been set already, but is not equal to the argument times."
            error = ValueError(message)
            logger.error(error)
            raise error
        if self.times is None and times is None:
            message = (
                "Required argument times is missing and self.times has not been set."
            )
            error = ValueError(message)
            logger.error(error)
            raise error
        if times is None:
            times = self.times
        self.times = validate_array(times, "times", ndim=1)
        return self.times

    def _compute_divergence_function(self):
        x = self.x
        xu = self.landmarks
        gp_type = self.gp_type
        L = self.Lp
        cov_func = self.cov_func
        batch_size = self.batch_size
        div_func = compute_divergence_function(
            x, xu, gp_type, L, cov_func, batch_size=batch_size
        )
        return div_func

    def _compute_density_predictor(self):
        x = self.x
        times = self.times
        raise NotImplementedError("Implement with detection for time sensitivity.")

    def _compute_time_derivatives(self):
        x = self.x
        times = self.times
        predictor = self.density_predictor
        derivatives = compute_time_derivatives(predictor, x, times)
        return derivatives

    def _compute_density_gradient(self):
        x = self.x
        times = self.times
        predictor = self.density_predictor
        derivatives = compute_density_gradient(predictor, x, times)
        return derivatives

    def _compute_density_diffusion(self):
        x = self.x
        times = self.times
        predictor = self.density_predictor
        diffusion = compute_density_diffusion(predictor, x, times)
        return diffusion

    def _compute_initial_value(self):
        x = self.x
        L = self.L
        initial_value = compute_initial_zeros(x, L)
        return initial_value

    def _compute_cost_proliferation(self):
        x = self.x
        cost = compute_initial_ones(x)
        return cost

    def _compute_cost_apoptosis(self):
        x = self.x
        cost = compute_initial_ones(x)
        return cost

    def _compute_transform(self):
        mu = 0
        L = self.L
        transform = compute_transform(mu, L)
        return transform

    def _compute_loss_func(self):
        nn_distances = self.nn_distances
        d = self.d
        transform = self.transform
        k = self.initial_value.shape[0]
        loss_func = compute_loss_func(nn_distances, d, transform, k)
        return loss_func

    def _set_log_density_x(self):
        pre_transformation = self.pre_transformation
        transform = self.transform
        log_density_x = compute_log_density_x(pre_transformation, transform)
        self.log_density_x = log_density_x

    def _set_log_density_func(self):
        x = self.x
        landmarks = self.landmarks
        pre_transformation = self.pre_transformation
        pre_transformation_std = self.pre_transformation_std
        log_density_x = self.log_density_x
        mu = 0
        cov_func = self.cov_func
        L = self.L
        Lp = self.Lp
        jitter = self.jitter
        with_uncertainty = self.predictor_with_uncertainty
        logger.info("Computing predictive function.")
        log_density_func = compute_conditional(
            x,
            landmarks,
            pre_transformation,
            pre_transformation_std,
            log_density_x,
            mu,
            cov_func,
            L,
            Lp,
            sigma=None,
            jitter=jitter,
            y_is_mean=True,
            with_uncertainty=with_uncertainty,
        )
        self.log_density_func = log_density_func

    def prepare_inference(self, x, times=None):
        R"""
        Set all attributes in preparation for optimization, but do not
        perform Bayesian inference. It is not necessary to call this
        function before calling fit.

        :param x: The training instances to estimate density function.
        :type x: array-like
        :return: loss_func, initial_value - The Bayesian loss function and
            initial guess for optimization.
        :rtype: function, array-like
        """
        if x is None:
            x = self.x
            if self.x is None:
                message = "Required argument x is missing and self.x has not been set."
                raise ValueError(message)
        else:
            if self.x is not None and self.x is not x:
                message = (
                    "self.x has been set already, but is not equal to the argument x."
                )
                raise ValueError(message)

        x = self.set_x(x)
        times = self.set_times(times)
        self._prepare_attribute("n_landmarks")
        self._prepare_attribute("rank")
        self._prepare_attribute("gp_type")
        self.validate_parameter()
        self._prepare_attribute("density_predictor")
        self._prepare_attribute("time_derivatives")
        self._prepare_attribute("density_gradient")
        self._prepare_attribute("density_diffusion")
        self._prepare_attribute("cost_proliferation")
        self._prepare_attribute("cost_apoptosis")
        self._prepare_attribute("distance_func")
        self._prepare_attribute("nn_distances")
        self._prepare_attribute("ls")
        self._prepare_attribute("cov_func")
        self._prepare_attribute("landmarks")
        self._prepare_attribute("Lp")
        self._prepare_attribute("L")
        self._prepare_attribute("transform")
        self._prepare_attribute("divergence_function")
        self._prepare_attribute("loss_func")
        return self.loss_func, self.initial_value

    def run_inference(self, loss_func=None, initial_value=None, optimizer=None):
        R"""
        Perform Bayesian inference, optimizing the pre_transformation parameters.
        If you would like to run your own inference procedure, use the loss_function
        and initial_value attributes and set pre_transformation to the optimized
        parameters.

        :param loss_func: The Bayesian loss function. If None, uses the stored
            loss_func attribute.
        :type loss_func: function
        :param initial_value: The initial guess for optimization. If None, uses
            the stored initial_value attribute.
        :type initial_value: array-like
        :return: pre_transformation - The optimized parameters.
        :rtype: array-like
        """
        if loss_func is not None:
            self.loss_func = loss_func
        if initial_value is not None:
            self.initial_value = initial_value
        if optimizer is not None:
            self.optimizer = optimizer
        self._run_inference()
        return self.pre_transformation

    def process_inference(self, pre_transformation=None, build_predict=True):
        R"""
        Use the optimized parameters to compute the log density at the
        training points. If build_predict, also build the prediction function.

        :param pre_transformation: The optimized parameters. If None, uses the stored
            pre_transformation attribute.
        :type pre_transformation: array-like
        :param build_predict: Whether or not to build the prediction function.
            Defaults to True.
        :type build_predict: bool
        :return: log_density_x - The log density
        :rtype: array-like
        """
        if pre_transformation is not None:
            self.pre_transformation = validate_array(
                pre_transformation, "pre_transformation"
            )
        self._set_log_density_x()
        if build_predict:
            self._set_log_density_func()
        return self.log_density_x

    def fit(self, x=None, times=None, build_predict=True):
        """
        Trains the model from end to end. This includes preparing the model for inference,
        running the inference, and post-processing the inference results.

        Parameters
        ----------
        x : array-like of shape (n_samples, n_features), default=None
            The training instances where `n_samples` is the number of samples and `n_features`
            is the number of features.

        build_predict : bool, default=True
            Whether to build the prediction function after training.

        Returns
        -------
        self : object
            This method returns self for chaining.
        """
        self.prepare_inference(x, times)
        self.run_inference()
        self.process_inference(build_predict=build_predict)
        return self

    @property
    def predict(self):
        """
        A property that returns an instance of the :class:`mellon.Predictor` class. This predictor can
        be used to predict the log density for new data points by calling the instance like a function.

        The predictor instance also supports serialization features, which allow for saving and loading
        the predictor's state. For more details, refer to the :class:`mellon.Predictor` documentation.

        Returns
        -------
        mellon.Predictor
            A predictor instance that computes the log density at each new data point.

        Example
        -------

        >>> log_density = model.predict(Xnew)

        """
        if self.log_density_func is None:
            self._set_log_density_func()
        return self.log_density_func

    def fit_predict(self, x=None, times=None, build_predict=False):
        """
        Trains the model and predicts the log density at the training points.

        Parameters
        ----------
        x : array-like of shape (n_samples, n_features), default=None
            The training instances where `n_samples` is the number of samples and `n_features`
            is the number of features.

        build_predict : bool, default=False
            Whether to build the prediction function after training.

        Raises
        ------
        ValueError
            If the input `x` is not consistent with the training data used before.

        Returns
        -------
        array-like
            The log density at each training point in `x`.
        """

        self.fit(x, build_predict=build_predict)
        return self.log_density_x
