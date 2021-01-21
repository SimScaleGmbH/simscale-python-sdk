# coding: utf-8

"""
    SimScale API

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from simscale_sdk.configuration import Configuration


class OneOfSolidNumericsSolver(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'force_symmetric': 'bool',
        'preconditioner': 'OneOfPETSCSolverPreconditioner',
        'max_iterations': 'int',
        'convergence_threshold': 'float',
        'precision_singularity_detection': 'int',
        'stop_if_singular': 'bool',
        'matrix_type': 'str',
        'memory_percentage_for_pivoting': 'float',
        'linear_system_relative_residual': 'float',
        'matrix_filtering_threshold': 'float',
        'single_precision': 'bool',
        'preprocessing': 'bool',
        'renumbering_method': 'str',
        'postprocessing': 'str',
        'distributed_matrix_storage': 'bool',
        'memory_management': 'str',
        'eliminate_lagrange_multipliers': 'bool',
        'algorithm': 'str'
    }

    attribute_map = {
        'type': 'type',
        'force_symmetric': 'forceSymmetric',
        'preconditioner': 'preconditioner',
        'max_iterations': 'maxIterations',
        'convergence_threshold': 'convergenceThreshold',
        'precision_singularity_detection': 'precisionSingularityDetection',
        'stop_if_singular': 'stopIfSingular',
        'matrix_type': 'matrixType',
        'memory_percentage_for_pivoting': 'memoryPercentageForPivoting',
        'linear_system_relative_residual': 'linearSystemRelativeResidual',
        'matrix_filtering_threshold': 'matrixFilteringThreshold',
        'single_precision': 'singlePrecision',
        'preprocessing': 'preprocessing',
        'renumbering_method': 'renumberingMethod',
        'postprocessing': 'postprocessing',
        'distributed_matrix_storage': 'distributedMatrixStorage',
        'memory_management': 'memoryManagement',
        'eliminate_lagrange_multipliers': 'eliminateLagrangeMultipliers',
        'algorithm': 'algorithm'
    }

    discriminator_value_class_map = {
        'GCPC': 'GCPCSolver',
        'LDLT_V33': 'LDLTSolverV33',
        'MUMPS': 'MUMPSSolver',
        'MULTIFRONT': 'MultifrontalSolver',
        'PETSC': 'PETSCSolver'
    }

    def __init__(self, type='PETSC', force_symmetric=None, preconditioner=None, max_iterations=None, convergence_threshold=None, precision_singularity_detection=None, stop_if_singular=True, matrix_type=None, memory_percentage_for_pivoting=None, linear_system_relative_residual=None, matrix_filtering_threshold=None, single_precision=None, preprocessing=True, renumbering_method=None, postprocessing=None, distributed_matrix_storage=None, memory_management=None, eliminate_lagrange_multipliers=None, algorithm=None, local_vars_configuration=None):  # noqa: E501
        """OneOfSolidNumericsSolver - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._force_symmetric = None
        self._preconditioner = None
        self._max_iterations = None
        self._convergence_threshold = None
        self._precision_singularity_detection = None
        self._stop_if_singular = None
        self._matrix_type = None
        self._memory_percentage_for_pivoting = None
        self._linear_system_relative_residual = None
        self._matrix_filtering_threshold = None
        self._single_precision = None
        self._preprocessing = None
        self._renumbering_method = None
        self._postprocessing = None
        self._distributed_matrix_storage = None
        self._memory_management = None
        self._eliminate_lagrange_multipliers = None
        self._algorithm = None
        self.discriminator = 'type'

        self.type = type
        if force_symmetric is not None:
            self.force_symmetric = force_symmetric
        if preconditioner is not None:
            self.preconditioner = preconditioner
        if max_iterations is not None:
            self.max_iterations = max_iterations
        if convergence_threshold is not None:
            self.convergence_threshold = convergence_threshold
        if precision_singularity_detection is not None:
            self.precision_singularity_detection = precision_singularity_detection
        self.stop_if_singular = stop_if_singular
        if matrix_type is not None:
            self.matrix_type = matrix_type
        if memory_percentage_for_pivoting is not None:
            self.memory_percentage_for_pivoting = memory_percentage_for_pivoting
        if linear_system_relative_residual is not None:
            self.linear_system_relative_residual = linear_system_relative_residual
        if matrix_filtering_threshold is not None:
            self.matrix_filtering_threshold = matrix_filtering_threshold
        if single_precision is not None:
            self.single_precision = single_precision
        self.preprocessing = preprocessing
        if renumbering_method is not None:
            self.renumbering_method = renumbering_method
        if postprocessing is not None:
            self.postprocessing = postprocessing
        if distributed_matrix_storage is not None:
            self.distributed_matrix_storage = distributed_matrix_storage
        if memory_management is not None:
            self.memory_management = memory_management
        if eliminate_lagrange_multipliers is not None:
            self.eliminate_lagrange_multipliers = eliminate_lagrange_multipliers
        if algorithm is not None:
            self.algorithm = algorithm

    @property
    def type(self):
        """Gets the type of this OneOfSolidNumericsSolver.  # noqa: E501


        :return: The type of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfSolidNumericsSolver.


        :param type: The type of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def force_symmetric(self):
        """Gets the force_symmetric of this OneOfSolidNumericsSolver.  # noqa: E501

        Choose if you want to enforce a symmetric matrix.  # noqa: E501

        :return: The force_symmetric of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: bool
        """
        return self._force_symmetric

    @force_symmetric.setter
    def force_symmetric(self, force_symmetric):
        """Sets the force_symmetric of this OneOfSolidNumericsSolver.

        Choose if you want to enforce a symmetric matrix.  # noqa: E501

        :param force_symmetric: The force_symmetric of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: bool
        """

        self._force_symmetric = force_symmetric

    @property
    def preconditioner(self):
        """Gets the preconditioner of this OneOfSolidNumericsSolver.  # noqa: E501


        :return: The preconditioner of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: OneOfPETSCSolverPreconditioner
        """
        return self._preconditioner

    @preconditioner.setter
    def preconditioner(self, preconditioner):
        """Sets the preconditioner of this OneOfSolidNumericsSolver.


        :param preconditioner: The preconditioner of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: OneOfPETSCSolverPreconditioner
        """

        self._preconditioner = preconditioner

    @property
    def max_iterations(self):
        """Gets the max_iterations of this OneOfSolidNumericsSolver.  # noqa: E501

        Set the maximum number of iterations for the iterative solver. If set to 0 PETSC sets an estimate of the maximum number of iterations.  # noqa: E501

        :return: The max_iterations of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: int
        """
        return self._max_iterations

    @max_iterations.setter
    def max_iterations(self, max_iterations):
        """Sets the max_iterations of this OneOfSolidNumericsSolver.

        Set the maximum number of iterations for the iterative solver. If set to 0 PETSC sets an estimate of the maximum number of iterations.  # noqa: E501

        :param max_iterations: The max_iterations of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_iterations is not None and max_iterations < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_iterations`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_iterations = max_iterations

    @property
    def convergence_threshold(self):
        """Gets the convergence_threshold of this OneOfSolidNumericsSolver.  # noqa: E501

        Set the threshold value for convergence detection for the relative convergence criteria.  # noqa: E501

        :return: The convergence_threshold of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: float
        """
        return self._convergence_threshold

    @convergence_threshold.setter
    def convergence_threshold(self, convergence_threshold):
        """Sets the convergence_threshold of this OneOfSolidNumericsSolver.

        Set the threshold value for convergence detection for the relative convergence criteria.  # noqa: E501

        :param convergence_threshold: The convergence_threshold of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                convergence_threshold is not None and convergence_threshold < 0):  # noqa: E501
            raise ValueError("Invalid value for `convergence_threshold`, must be a value greater than or equal to `0`")  # noqa: E501

        self._convergence_threshold = convergence_threshold

    @property
    def precision_singularity_detection(self):
        """Gets the precision_singularity_detection of this OneOfSolidNumericsSolver.  # noqa: E501

        Define the precision value for the detection of a singular matrix.  # noqa: E501

        :return: The precision_singularity_detection of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: int
        """
        return self._precision_singularity_detection

    @precision_singularity_detection.setter
    def precision_singularity_detection(self, precision_singularity_detection):
        """Sets the precision_singularity_detection of this OneOfSolidNumericsSolver.

        Define the precision value for the detection of a singular matrix.  # noqa: E501

        :param precision_singularity_detection: The precision_singularity_detection of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: int
        """

        self._precision_singularity_detection = precision_singularity_detection

    @property
    def stop_if_singular(self):
        """Gets the stop_if_singular of this OneOfSolidNumericsSolver.  # noqa: E501

        Choose if the calculation should be stopped if the problem turns out to be singular.  # noqa: E501

        :return: The stop_if_singular of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: bool
        """
        return self._stop_if_singular

    @stop_if_singular.setter
    def stop_if_singular(self, stop_if_singular):
        """Sets the stop_if_singular of this OneOfSolidNumericsSolver.

        Choose if the calculation should be stopped if the problem turns out to be singular.  # noqa: E501

        :param stop_if_singular: The stop_if_singular of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and stop_if_singular is None:  # noqa: E501
            raise ValueError("Invalid value for `stop_if_singular`, must not be `None`")  # noqa: E501

        self._stop_if_singular = stop_if_singular

    @property
    def matrix_type(self):
        """Gets the matrix_type of this OneOfSolidNumericsSolver.  # noqa: E501

        <p>Choose the type of your system matrix either by directly selecting the appropriate type or using the <b>automatic detection</b>. With the selection <b>automatic detection</b> the matrix type <b>symmetric positive indifinite</b> is selected if a symmetric system matrix is detected, and <b>asymmetric</b> else.  # noqa: E501

        :return: The matrix_type of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: str
        """
        return self._matrix_type

    @matrix_type.setter
    def matrix_type(self, matrix_type):
        """Sets the matrix_type of this OneOfSolidNumericsSolver.

        <p>Choose the type of your system matrix either by directly selecting the appropriate type or using the <b>automatic detection</b>. With the selection <b>automatic detection</b> the matrix type <b>symmetric positive indifinite</b> is selected if a symmetric system matrix is detected, and <b>asymmetric</b> else.  # noqa: E501

        :param matrix_type: The matrix_type of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: str
        """
        allowed_values = ["ASYMMETRIC", "AUTOMATIC_DETECTION", "SYMMETRIC_POSITIVE_INDEFINITE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and matrix_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `matrix_type` ({0}), must be one of {1}"  # noqa: E501
                .format(matrix_type, allowed_values)
            )

        self._matrix_type = matrix_type

    @property
    def memory_percentage_for_pivoting(self):
        """Gets the memory_percentage_for_pivoting of this OneOfSolidNumericsSolver.  # noqa: E501

        Define how much additional memory should be reserved for the pivoting operations. If MUMPS estimates that the necessary space for factorising the matrix would be 100, choosing a value of 20 would mean that MUMPS allocates a memory space of 120.  # noqa: E501

        :return: The memory_percentage_for_pivoting of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: float
        """
        return self._memory_percentage_for_pivoting

    @memory_percentage_for_pivoting.setter
    def memory_percentage_for_pivoting(self, memory_percentage_for_pivoting):
        """Sets the memory_percentage_for_pivoting of this OneOfSolidNumericsSolver.

        Define how much additional memory should be reserved for the pivoting operations. If MUMPS estimates that the necessary space for factorising the matrix would be 100, choosing a value of 20 would mean that MUMPS allocates a memory space of 120.  # noqa: E501

        :param memory_percentage_for_pivoting: The memory_percentage_for_pivoting of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: float
        """

        self._memory_percentage_for_pivoting = memory_percentage_for_pivoting

    @property
    def linear_system_relative_residual(self):
        """Gets the linear_system_relative_residual of this OneOfSolidNumericsSolver.  # noqa: E501

        Choose a value for the maximum relative residual for each linear system resolution compared to the exact solution. In a nonlinear calculation the user can deactivate this check by selecting a negative value (for example -1.0, since the qualitiy of the solution is controlled within the Newton loop.  # noqa: E501

        :return: The linear_system_relative_residual of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: float
        """
        return self._linear_system_relative_residual

    @linear_system_relative_residual.setter
    def linear_system_relative_residual(self, linear_system_relative_residual):
        """Sets the linear_system_relative_residual of this OneOfSolidNumericsSolver.

        Choose a value for the maximum relative residual for each linear system resolution compared to the exact solution. In a nonlinear calculation the user can deactivate this check by selecting a negative value (for example -1.0, since the qualitiy of the solution is controlled within the Newton loop.  # noqa: E501

        :param linear_system_relative_residual: The linear_system_relative_residual of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: float
        """

        self._linear_system_relative_residual = linear_system_relative_residual

    @property
    def matrix_filtering_threshold(self):
        """Gets the matrix_filtering_threshold of this OneOfSolidNumericsSolver.  # noqa: E501

        This parameter allows a filtration of the matrix entries that are saved and possibly passed to the nonlinear algorithm (Newton) and is similar to a relaxation mechanism. If the given threshold value is strictly positive, MUMPS only saves the matrix entries that satisfy the following condition: |K<sub>ij</sub>| value*(|K<sub>ii</sub>|+|K<sub>jj</sub>|). Thus using this functionality might save computation time as well as memory consumption, but the effects strongly depend on the given value and is only advised for the experienced user.  # noqa: E501

        :return: The matrix_filtering_threshold of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: float
        """
        return self._matrix_filtering_threshold

    @matrix_filtering_threshold.setter
    def matrix_filtering_threshold(self, matrix_filtering_threshold):
        """Sets the matrix_filtering_threshold of this OneOfSolidNumericsSolver.

        This parameter allows a filtration of the matrix entries that are saved and possibly passed to the nonlinear algorithm (Newton) and is similar to a relaxation mechanism. If the given threshold value is strictly positive, MUMPS only saves the matrix entries that satisfy the following condition: |K<sub>ij</sub>| value*(|K<sub>ii</sub>|+|K<sub>jj</sub>|). Thus using this functionality might save computation time as well as memory consumption, but the effects strongly depend on the given value and is only advised for the experienced user.  # noqa: E501

        :param matrix_filtering_threshold: The matrix_filtering_threshold of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: float
        """

        self._matrix_filtering_threshold = matrix_filtering_threshold

    @property
    def single_precision(self):
        """Gets the single_precision of this OneOfSolidNumericsSolver.  # noqa: E501

        If this option is activated the matrix factorisation is done with single precision and thus a reduction in memory consumption (often about 50%) and computation time is gained if the problem is well conditioned. If the problem is ill-conditioned one risks that in a nonlinear computation the newton algorithm fails to converge.  # noqa: E501

        :return: The single_precision of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: bool
        """
        return self._single_precision

    @single_precision.setter
    def single_precision(self, single_precision):
        """Sets the single_precision of this OneOfSolidNumericsSolver.

        If this option is activated the matrix factorisation is done with single precision and thus a reduction in memory consumption (often about 50%) and computation time is gained if the problem is well conditioned. If the problem is ill-conditioned one risks that in a nonlinear computation the newton algorithm fails to converge.  # noqa: E501

        :param single_precision: The single_precision of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: bool
        """

        self._single_precision = single_precision

    @property
    def preprocessing(self):
        """Gets the preprocessing of this OneOfSolidNumericsSolver.  # noqa: E501

        If this option is activated MUMPS performs a pre-processing on order to identify the best parameter setting for some internal parameters adapted to the current problem.  # noqa: E501

        :return: The preprocessing of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: bool
        """
        return self._preprocessing

    @preprocessing.setter
    def preprocessing(self, preprocessing):
        """Sets the preprocessing of this OneOfSolidNumericsSolver.

        If this option is activated MUMPS performs a pre-processing on order to identify the best parameter setting for some internal parameters adapted to the current problem.  # noqa: E501

        :param preprocessing: The preprocessing of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and preprocessing is None:  # noqa: E501
            raise ValueError("Invalid value for `preprocessing`, must not be `None`")  # noqa: E501

        self._preprocessing = preprocessing

    @property
    def renumbering_method(self):
        """Gets the renumbering_method of this OneOfSolidNumericsSolver.  # noqa: E501

        Choose a renumbering method for the solution process.<br/>For large models around and above 50000 degrees of freedom you should consider using MDA.  # noqa: E501

        :return: The renumbering_method of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: str
        """
        return self._renumbering_method

    @renumbering_method.setter
    def renumbering_method(self, renumbering_method):
        """Sets the renumbering_method of this OneOfSolidNumericsSolver.

        Choose a renumbering method for the solution process.<br/>For large models around and above 50000 degrees of freedom you should consider using MDA.  # noqa: E501

        :param renumbering_method: The renumbering_method of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: str
        """
        allowed_values = ["MDA", "MD"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and renumbering_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `renumbering_method` ({0}), must be one of {1}"  # noqa: E501
                .format(renumbering_method, allowed_values)
            )

        self._renumbering_method = renumbering_method

    @property
    def postprocessing(self):
        """Gets the postprocessing of this OneOfSolidNumericsSolver.  # noqa: E501

        With this option the user can control the iterative refinement of the linear system solution. This option only has an effect if the value of the <b> linear system relative residual</b> given by the user is greater than zero, otherwise it is ignored. If it is <b>activate</b> MUMPS carries out at least one additional iteration of the linear system resolution and at most 10 iterations. The process is stopped if the residual isn't reduced by at least a factor of 5. If this option is set to be <b>inactive</b> no additional iteration is done and if <b>automatic</b> is chosen MUMPS automatically decides if additional iterations should be done and the maximum number of iterations is set to 4.  # noqa: E501

        :return: The postprocessing of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: str
        """
        return self._postprocessing

    @postprocessing.setter
    def postprocessing(self, postprocessing):
        """Sets the postprocessing of this OneOfSolidNumericsSolver.

        With this option the user can control the iterative refinement of the linear system solution. This option only has an effect if the value of the <b> linear system relative residual</b> given by the user is greater than zero, otherwise it is ignored. If it is <b>activate</b> MUMPS carries out at least one additional iteration of the linear system resolution and at most 10 iterations. The process is stopped if the residual isn't reduced by at least a factor of 5. If this option is set to be <b>inactive</b> no additional iteration is done and if <b>automatic</b> is chosen MUMPS automatically decides if additional iterations should be done and the maximum number of iterations is set to 4.  # noqa: E501

        :param postprocessing: The postprocessing of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: str
        """
        allowed_values = ["INACTIVE", "ACTIVE", "AUTOMATIC"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and postprocessing not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `postprocessing` ({0}), must be one of {1}"  # noqa: E501
                .format(postprocessing, allowed_values)
            )

        self._postprocessing = postprocessing

    @property
    def distributed_matrix_storage(self):
        """Gets the distributed_matrix_storage of this OneOfSolidNumericsSolver.  # noqa: E501

        Choose this parameter as <b>true</b> to ensure that the system matrix saving is distributed among the processors of the computation. If multiple cores are used only the relevant part for each core is saved. If it is set to false the whole matrix is saved for each processor.  # noqa: E501

        :return: The distributed_matrix_storage of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: bool
        """
        return self._distributed_matrix_storage

    @distributed_matrix_storage.setter
    def distributed_matrix_storage(self, distributed_matrix_storage):
        """Sets the distributed_matrix_storage of this OneOfSolidNumericsSolver.

        Choose this parameter as <b>true</b> to ensure that the system matrix saving is distributed among the processors of the computation. If multiple cores are used only the relevant part for each core is saved. If it is set to false the whole matrix is saved for each processor.  # noqa: E501

        :param distributed_matrix_storage: The distributed_matrix_storage of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: bool
        """

        self._distributed_matrix_storage = distributed_matrix_storage

    @property
    def memory_management(self):
        """Gets the memory_management of this OneOfSolidNumericsSolver.  # noqa: E501

        Choose the memory managment priority of the MUMPS solver. If <b>in-core</b> is used the memory managment is optimized with respect to the calculation time by saving all objects in the RAM. If <b>out-of-core</b> is chosen, the memory managment is optimized for a minimal RAM usage. If <b>automatic</b> is selected, MUMPS choses automatically a reasonable memory managment mode. The option <b>memory demand evaluation</b> is helpful to estimate the RAM consumption. This estimate is written to the solver log file. In this case the solution process aborts after the memory usage is estimated, allowing the user to start a new run with the best settings.  # noqa: E501

        :return: The memory_management of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: str
        """
        return self._memory_management

    @memory_management.setter
    def memory_management(self, memory_management):
        """Sets the memory_management of this OneOfSolidNumericsSolver.

        Choose the memory managment priority of the MUMPS solver. If <b>in-core</b> is used the memory managment is optimized with respect to the calculation time by saving all objects in the RAM. If <b>out-of-core</b> is chosen, the memory managment is optimized for a minimal RAM usage. If <b>automatic</b> is selected, MUMPS choses automatically a reasonable memory managment mode. The option <b>memory demand evaluation</b> is helpful to estimate the RAM consumption. This estimate is written to the solver log file. In this case the solution process aborts after the memory usage is estimated, allowing the user to start a new run with the best settings.  # noqa: E501

        :param memory_management: The memory_management of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTOMATIC", "IN_CORE", "MEMORY_DEMAND_EVALUATION", "OUT_OF_CORE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and memory_management not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `memory_management` ({0}), must be one of {1}"  # noqa: E501
                .format(memory_management, allowed_values)
            )

        self._memory_management = memory_management

    @property
    def eliminate_lagrange_multipliers(self):
        """Gets the eliminate_lagrange_multipliers of this OneOfSolidNumericsSolver.  # noqa: E501

        This option makes it possible to eliminate the Lagrange Multipliers which are introduced by generalized boundary conditions like bonded contact, remote boundary conditions and symmetry conditions. If activated, this option removes the Lagrange Multipliers which leads to a reduction of the total number of unknowns and can increase the robustness of iterative solvers.  # noqa: E501

        :return: The eliminate_lagrange_multipliers of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: bool
        """
        return self._eliminate_lagrange_multipliers

    @eliminate_lagrange_multipliers.setter
    def eliminate_lagrange_multipliers(self, eliminate_lagrange_multipliers):
        """Sets the eliminate_lagrange_multipliers of this OneOfSolidNumericsSolver.

        This option makes it possible to eliminate the Lagrange Multipliers which are introduced by generalized boundary conditions like bonded contact, remote boundary conditions and symmetry conditions. If activated, this option removes the Lagrange Multipliers which leads to a reduction of the total number of unknowns and can increase the robustness of iterative solvers.  # noqa: E501

        :param eliminate_lagrange_multipliers: The eliminate_lagrange_multipliers of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: bool
        """

        self._eliminate_lagrange_multipliers = eliminate_lagrange_multipliers

    @property
    def algorithm(self):
        """Gets the algorithm of this OneOfSolidNumericsSolver.  # noqa: E501

        Choose the iterative solver method: <ul><li><p><b>GMRES</b>: <i>Minimal Generalised RESidual</i>, best compromise between robustness and computational speed.</p></ul><ul><li><p><b>CG</b>: <i>Conjugate Gradient</i>, only useful for symmetric matrices</p></ul><ul><li><p><b>CR</b>: <i>Conjugate Residual</i>, only useful for symmetric matrices</p></ul><ul><li><p><b>GCR</b>: <i>Generalised Conjugate Residual</i>, treats general matrices</p></ul>All available methods are of <i>Krylov</i> type.  # noqa: E501

        :return: The algorithm of this OneOfSolidNumericsSolver.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this OneOfSolidNumericsSolver.

        Choose the iterative solver method: <ul><li><p><b>GMRES</b>: <i>Minimal Generalised RESidual</i>, best compromise between robustness and computational speed.</p></ul><ul><li><p><b>CG</b>: <i>Conjugate Gradient</i>, only useful for symmetric matrices</p></ul><ul><li><p><b>CR</b>: <i>Conjugate Residual</i>, only useful for symmetric matrices</p></ul><ul><li><p><b>GCR</b>: <i>Generalised Conjugate Residual</i>, treats general matrices</p></ul>All available methods are of <i>Krylov</i> type.  # noqa: E501

        :param algorithm: The algorithm of this OneOfSolidNumericsSolver.  # noqa: E501
        :type: str
        """
        allowed_values = ["CG", "CR", "GCR", "GMRES"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and algorithm not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(algorithm, allowed_values)
            )

        self._algorithm = algorithm

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OneOfSolidNumericsSolver):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfSolidNumericsSolver):
            return True

        return self.to_dict() != other.to_dict()
