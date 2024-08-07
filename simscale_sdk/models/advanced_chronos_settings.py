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


class AdvancedChronosSettings(object):
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
        'force_fsai': 'bool',
        'algorithm': 'str',
        'smoother': 'str',
        'prolongation': 'str',
        'improve_test_space': 'bool',
        'test_space_iterations': 'int',
        'preconditioner_recycling': 'float',
        'restart_gmres': 'int',
        'distributed_matrix_storage': 'bool',
        'num_of_threads': 'int',
        'verbosity': 'int',
        'write_coords_and_matrix': 'int'
    }

    attribute_map = {
        'force_fsai': 'forceFsai',
        'algorithm': 'algorithm',
        'smoother': 'smoother',
        'prolongation': 'prolongation',
        'improve_test_space': 'improveTestSpace',
        'test_space_iterations': 'testSpaceIterations',
        'preconditioner_recycling': 'preconditionerRecycling',
        'restart_gmres': 'restartGmres',
        'distributed_matrix_storage': 'distributedMatrixStorage',
        'num_of_threads': 'numOfThreads',
        'verbosity': 'verbosity',
        'write_coords_and_matrix': 'writeCoordsAndMatrix'
    }

    def __init__(self, force_fsai=None, algorithm=None, smoother=None, prolongation=None, improve_test_space=None, test_space_iterations=None, preconditioner_recycling=None, restart_gmres=None, distributed_matrix_storage=None, num_of_threads=None, verbosity=None, write_coords_and_matrix=None, local_vars_configuration=None):  # noqa: E501
        """AdvancedChronosSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._force_fsai = None
        self._algorithm = None
        self._smoother = None
        self._prolongation = None
        self._improve_test_space = None
        self._test_space_iterations = None
        self._preconditioner_recycling = None
        self._restart_gmres = None
        self._distributed_matrix_storage = None
        self._num_of_threads = None
        self._verbosity = None
        self._write_coords_and_matrix = None
        self.discriminator = None

        if force_fsai is not None:
            self.force_fsai = force_fsai
        if algorithm is not None:
            self.algorithm = algorithm
        if smoother is not None:
            self.smoother = smoother
        if prolongation is not None:
            self.prolongation = prolongation
        if improve_test_space is not None:
            self.improve_test_space = improve_test_space
        if test_space_iterations is not None:
            self.test_space_iterations = test_space_iterations
        if preconditioner_recycling is not None:
            self.preconditioner_recycling = preconditioner_recycling
        if restart_gmres is not None:
            self.restart_gmres = restart_gmres
        if distributed_matrix_storage is not None:
            self.distributed_matrix_storage = distributed_matrix_storage
        if num_of_threads is not None:
            self.num_of_threads = num_of_threads
        if verbosity is not None:
            self.verbosity = verbosity
        if write_coords_and_matrix is not None:
            self.write_coords_and_matrix = write_coords_and_matrix

    @property
    def force_fsai(self):
        """Gets the force_fsai of this AdvancedChronosSettings.  # noqa: E501

        Force the usage of <b>FSAI</b> preconditioning. This can make sense for small and simple problems, because setting up the problem might be faster with FSAI than with AMG.<br>Otherwise, Chronos selects itself the most suitable preconditioner, depending on the characteristics of the problem. In this case, <b>AMG</b> is preferred over <b>FSAI</b>.  # noqa: E501

        :return: The force_fsai of this AdvancedChronosSettings.  # noqa: E501
        :rtype: bool
        """
        return self._force_fsai

    @force_fsai.setter
    def force_fsai(self, force_fsai):
        """Sets the force_fsai of this AdvancedChronosSettings.

        Force the usage of <b>FSAI</b> preconditioning. This can make sense for small and simple problems, because setting up the problem might be faster with FSAI than with AMG.<br>Otherwise, Chronos selects itself the most suitable preconditioner, depending on the characteristics of the problem. In this case, <b>AMG</b> is preferred over <b>FSAI</b>.  # noqa: E501

        :param force_fsai: The force_fsai of this AdvancedChronosSettings.  # noqa: E501
        :type: bool
        """

        self._force_fsai = force_fsai

    @property
    def algorithm(self):
        """Gets the algorithm of this AdvancedChronosSettings.  # noqa: E501

        The algorithm for the prolongation becomes more elaborate from Jacobi over light, medium to heavy FSAI. The stability increases as well as the computational cost. It is recommended to increase it when the problem has distored elements, is ill-conditioned  or has incompressible materials.  # noqa: E501

        :return: The algorithm of this AdvancedChronosSettings.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this AdvancedChronosSettings.

        The algorithm for the prolongation becomes more elaborate from Jacobi over light, medium to heavy FSAI. The stability increases as well as the computational cost. It is recommended to increase it when the problem has distored elements, is ill-conditioned  or has incompressible materials.  # noqa: E501

        :param algorithm: The algorithm of this AdvancedChronosSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["FSAI_LIGHT", "FSAI_MEDIUM", "FSAI_HEAVY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and algorithm not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(algorithm, allowed_values)
            )

        self._algorithm = algorithm

    @property
    def smoother(self):
        """Gets the smoother of this AdvancedChronosSettings.  # noqa: E501

        The algorithm for the prolongation becomes more elaborate from Jacobi over light, medium to heavy FSAI. The stability increases as well as the computational cost. It is recommended to increase it when the problem has distored elements, is ill-conditioned  or has incompressible materials.  # noqa: E501

        :return: The smoother of this AdvancedChronosSettings.  # noqa: E501
        :rtype: str
        """
        return self._smoother

    @smoother.setter
    def smoother(self, smoother):
        """Sets the smoother of this AdvancedChronosSettings.

        The algorithm for the prolongation becomes more elaborate from Jacobi over light, medium to heavy FSAI. The stability increases as well as the computational cost. It is recommended to increase it when the problem has distored elements, is ill-conditioned  or has incompressible materials.  # noqa: E501

        :param smoother: The smoother of this AdvancedChronosSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["JACOBI", "FSAI_LIGHT", "FSAI_MEDIUM", "FSAI_HEAVY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and smoother not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `smoother` ({0}), must be one of {1}"  # noqa: E501
                .format(smoother, allowed_values)
            )

        self._smoother = smoother

    @property
    def prolongation(self):
        """Gets the prolongation of this AdvancedChronosSettings.  # noqa: E501

        The algorithm for the prolongation becomes more elaborate from unsmoothed, smoothed to energy-minimization. The stability increases as well as the computational cost. It is recommended to increase it when the problem has small number of BCs and large number of elements  # noqa: E501

        :return: The prolongation of this AdvancedChronosSettings.  # noqa: E501
        :rtype: str
        """
        return self._prolongation

    @prolongation.setter
    def prolongation(self, prolongation):
        """Sets the prolongation of this AdvancedChronosSettings.

        The algorithm for the prolongation becomes more elaborate from unsmoothed, smoothed to energy-minimization. The stability increases as well as the computational cost. It is recommended to increase it when the problem has small number of BCs and large number of elements  # noqa: E501

        :param prolongation: The prolongation of this AdvancedChronosSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNSMOOTHED", "SMOOTHED", "ENERGY_MINIMIZATION"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and prolongation not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `prolongation` ({0}), must be one of {1}"  # noqa: E501
                .format(prolongation, allowed_values)
            )

        self._prolongation = prolongation

    @property
    def improve_test_space(self):
        """Gets the improve_test_space of this AdvancedChronosSettings.  # noqa: E501

        This should be enabled only for very complex/ill-conditioned problems, e.g. highly constrained with many BCs, incompressible/hyperelastic materials.  # noqa: E501

        :return: The improve_test_space of this AdvancedChronosSettings.  # noqa: E501
        :rtype: bool
        """
        return self._improve_test_space

    @improve_test_space.setter
    def improve_test_space(self, improve_test_space):
        """Sets the improve_test_space of this AdvancedChronosSettings.

        This should be enabled only for very complex/ill-conditioned problems, e.g. highly constrained with many BCs, incompressible/hyperelastic materials.  # noqa: E501

        :param improve_test_space: The improve_test_space of this AdvancedChronosSettings.  # noqa: E501
        :type: bool
        """

        self._improve_test_space = improve_test_space

    @property
    def test_space_iterations(self):
        """Gets the test_space_iterations of this AdvancedChronosSettings.  # noqa: E501

        Defaults to 20, can be increased to 50 for complicated cases.  # noqa: E501

        :return: The test_space_iterations of this AdvancedChronosSettings.  # noqa: E501
        :rtype: int
        """
        return self._test_space_iterations

    @test_space_iterations.setter
    def test_space_iterations(self, test_space_iterations):
        """Sets the test_space_iterations of this AdvancedChronosSettings.

        Defaults to 20, can be increased to 50 for complicated cases.  # noqa: E501

        :param test_space_iterations: The test_space_iterations of this AdvancedChronosSettings.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                test_space_iterations is not None and test_space_iterations < 0):  # noqa: E501
            raise ValueError("Invalid value for `test_space_iterations`, must be a value greater than or equal to `0`")  # noqa: E501

        self._test_space_iterations = test_space_iterations

    @property
    def preconditioner_recycling(self):
        """Gets the preconditioner_recycling of this AdvancedChronosSettings.  # noqa: E501

        Specify the recycling of the preconditioner. This can have a significant impact on the performance. The input is as follows: <ul><li><p><b> < 0.0</b> Never recycle the preconditioner.</p></ul><ul><li><p><b>0.0</b> Recycle the preconditioner every second iteration.</p></ul><ul><li><p><b>< 1.0</b> Recycle the preconditioner more often than the optimal way.</p></ul><ul><li><p><b>== 1.0</b> recycle the preconditioner in the optimal way.</p></ul><ul><li><p><b>> 1.0</b> recycle the preconditioner less often than the optimal way.</p></ul>  # noqa: E501

        :return: The preconditioner_recycling of this AdvancedChronosSettings.  # noqa: E501
        :rtype: float
        """
        return self._preconditioner_recycling

    @preconditioner_recycling.setter
    def preconditioner_recycling(self, preconditioner_recycling):
        """Sets the preconditioner_recycling of this AdvancedChronosSettings.

        Specify the recycling of the preconditioner. This can have a significant impact on the performance. The input is as follows: <ul><li><p><b> < 0.0</b> Never recycle the preconditioner.</p></ul><ul><li><p><b>0.0</b> Recycle the preconditioner every second iteration.</p></ul><ul><li><p><b>< 1.0</b> Recycle the preconditioner more often than the optimal way.</p></ul><ul><li><p><b>== 1.0</b> recycle the preconditioner in the optimal way.</p></ul><ul><li><p><b>> 1.0</b> recycle the preconditioner less often than the optimal way.</p></ul>  # noqa: E501

        :param preconditioner_recycling: The preconditioner_recycling of this AdvancedChronosSettings.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                preconditioner_recycling is not None and preconditioner_recycling > 2):  # noqa: E501
            raise ValueError("Invalid value for `preconditioner_recycling`, must be a value less than or equal to `2`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                preconditioner_recycling is not None and preconditioner_recycling < -1):  # noqa: E501
            raise ValueError("Invalid value for `preconditioner_recycling`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._preconditioner_recycling = preconditioner_recycling

    @property
    def restart_gmres(self):
        """Gets the restart_gmres of this AdvancedChronosSettings.  # noqa: E501

        Choose after how many iterations the GMRES solver should be restarted.<br>By default, Chronos uses a <b>PCG</b> iterative solution method. Depending on the characteristics of the problem, it might internally switch to <b>GMRES</b>. With GMRES, the iterations become more expensive the more they grow. Therefore, it is restarted if a certain threshold is reached. Default is 50, can be increased to 100 for complicated cases.  # noqa: E501

        :return: The restart_gmres of this AdvancedChronosSettings.  # noqa: E501
        :rtype: int
        """
        return self._restart_gmres

    @restart_gmres.setter
    def restart_gmres(self, restart_gmres):
        """Sets the restart_gmres of this AdvancedChronosSettings.

        Choose after how many iterations the GMRES solver should be restarted.<br>By default, Chronos uses a <b>PCG</b> iterative solution method. Depending on the characteristics of the problem, it might internally switch to <b>GMRES</b>. With GMRES, the iterations become more expensive the more they grow. Therefore, it is restarted if a certain threshold is reached. Default is 50, can be increased to 100 for complicated cases.  # noqa: E501

        :param restart_gmres: The restart_gmres of this AdvancedChronosSettings.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                restart_gmres is not None and restart_gmres < 0):  # noqa: E501
            raise ValueError("Invalid value for `restart_gmres`, must be a value greater than or equal to `0`")  # noqa: E501

        self._restart_gmres = restart_gmres

    @property
    def distributed_matrix_storage(self):
        """Gets the distributed_matrix_storage of this AdvancedChronosSettings.  # noqa: E501

        Choose this parameter as <b>true</b> to ensure that the system matrix saving is distributed among the processors of the computation. If multiple cores are used only the relevant part for each core is saved. If it is set to false the whole matrix is saved for each processor. Enabling this can significantly reductions in memory consumption, but introduces numerical instability in rare occasions.  # noqa: E501

        :return: The distributed_matrix_storage of this AdvancedChronosSettings.  # noqa: E501
        :rtype: bool
        """
        return self._distributed_matrix_storage

    @distributed_matrix_storage.setter
    def distributed_matrix_storage(self, distributed_matrix_storage):
        """Sets the distributed_matrix_storage of this AdvancedChronosSettings.

        Choose this parameter as <b>true</b> to ensure that the system matrix saving is distributed among the processors of the computation. If multiple cores are used only the relevant part for each core is saved. If it is set to false the whole matrix is saved for each processor. Enabling this can significantly reductions in memory consumption, but introduces numerical instability in rare occasions.  # noqa: E501

        :param distributed_matrix_storage: The distributed_matrix_storage of this AdvancedChronosSettings.  # noqa: E501
        :type: bool
        """

        self._distributed_matrix_storage = distributed_matrix_storage

    @property
    def num_of_threads(self):
        """Gets the num_of_threads of this AdvancedChronosSettings.  # noqa: E501

        Sets the number of threads for Chronos to be used for shared memory parallelization.<br>The shared memory parallelization of Chronos is independent of the shared memory parallelization of Code_Aster.<br>Ideally, the number of threads multiplied with the number of (MPI) processes (Number of parallel processes under Simulation control) should be set to the number of cores available on the machine.<br>Set it to 0 to automatically choose the best setting.<br>Note that reducing the number of MPI-processes and increasing the number of threads can significantly reduce memory and disk space consumption.  # noqa: E501

        :return: The num_of_threads of this AdvancedChronosSettings.  # noqa: E501
        :rtype: int
        """
        return self._num_of_threads

    @num_of_threads.setter
    def num_of_threads(self, num_of_threads):
        """Sets the num_of_threads of this AdvancedChronosSettings.

        Sets the number of threads for Chronos to be used for shared memory parallelization.<br>The shared memory parallelization of Chronos is independent of the shared memory parallelization of Code_Aster.<br>Ideally, the number of threads multiplied with the number of (MPI) processes (Number of parallel processes under Simulation control) should be set to the number of cores available on the machine.<br>Set it to 0 to automatically choose the best setting.<br>Note that reducing the number of MPI-processes and increasing the number of threads can significantly reduce memory and disk space consumption.  # noqa: E501

        :param num_of_threads: The num_of_threads of this AdvancedChronosSettings.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                num_of_threads is not None and num_of_threads > 192):  # noqa: E501
            raise ValueError("Invalid value for `num_of_threads`, must be a value less than or equal to `192`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                num_of_threads is not None and num_of_threads < 0):  # noqa: E501
            raise ValueError("Invalid value for `num_of_threads`, must be a value greater than or equal to `0`")  # noqa: E501

        self._num_of_threads = num_of_threads

    @property
    def verbosity(self):
        """Gets the verbosity of this AdvancedChronosSettings.  # noqa: E501

        This is a DEVELOPER option to specify the amount of output from Chronos. Its only purpose is debugging. Don't use it for regular runs, as it will slow down the simulation a lot! 0 means no output, 1-3 means more and more output.  # noqa: E501

        :return: The verbosity of this AdvancedChronosSettings.  # noqa: E501
        :rtype: int
        """
        return self._verbosity

    @verbosity.setter
    def verbosity(self, verbosity):
        """Sets the verbosity of this AdvancedChronosSettings.

        This is a DEVELOPER option to specify the amount of output from Chronos. Its only purpose is debugging. Don't use it for regular runs, as it will slow down the simulation a lot! 0 means no output, 1-3 means more and more output.  # noqa: E501

        :param verbosity: The verbosity of this AdvancedChronosSettings.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                verbosity is not None and verbosity > 3):  # noqa: E501
            raise ValueError("Invalid value for `verbosity`, must be a value less than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                verbosity is not None and verbosity < 0):  # noqa: E501
            raise ValueError("Invalid value for `verbosity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._verbosity = verbosity

    @property
    def write_coords_and_matrix(self):
        """Gets the write_coords_and_matrix of this AdvancedChronosSettings.  # noqa: E501

        This is a DEVELOPER option to output the coordinates and the matrix to a file. Its only purpose is debugging. Don't use it for regular runs, as it will slow down the simulation a lot! 0 means no output, 1 means to output the latest coords/matrix, and 2 means to output the coords/matrix for every solve (aka every iteration).  # noqa: E501

        :return: The write_coords_and_matrix of this AdvancedChronosSettings.  # noqa: E501
        :rtype: int
        """
        return self._write_coords_and_matrix

    @write_coords_and_matrix.setter
    def write_coords_and_matrix(self, write_coords_and_matrix):
        """Sets the write_coords_and_matrix of this AdvancedChronosSettings.

        This is a DEVELOPER option to output the coordinates and the matrix to a file. Its only purpose is debugging. Don't use it for regular runs, as it will slow down the simulation a lot! 0 means no output, 1 means to output the latest coords/matrix, and 2 means to output the coords/matrix for every solve (aka every iteration).  # noqa: E501

        :param write_coords_and_matrix: The write_coords_and_matrix of this AdvancedChronosSettings.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                write_coords_and_matrix is not None and write_coords_and_matrix > 5):  # noqa: E501
            raise ValueError("Invalid value for `write_coords_and_matrix`, must be a value less than or equal to `5`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                write_coords_and_matrix is not None and write_coords_and_matrix < 0):  # noqa: E501
            raise ValueError("Invalid value for `write_coords_and_matrix`, must be a value greater than or equal to `0`")  # noqa: E501

        self._write_coords_and_matrix = write_coords_and_matrix

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
        if not isinstance(other, AdvancedChronosSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdvancedChronosSettings):
            return True

        return self.to_dict() != other.to_dict()
