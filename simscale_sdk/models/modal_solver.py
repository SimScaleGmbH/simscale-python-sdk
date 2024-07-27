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


class ModalSolver(object):
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
        'solver': 'OneOfModalSolverSolver',
        'solver_model': 'object',
        'eigen_solver': 'OneOfModalSolverEigenSolver',
        'calculate_frequency': 'CalculateFrequency',
        'eigen_mode': 'EigenModeVerification',
        'enhanced_accuracy': 'bool'
    }

    attribute_map = {
        'solver': 'solver',
        'solver_model': 'solverModel',
        'eigen_solver': 'eigenSolver',
        'calculate_frequency': 'calculateFrequency',
        'eigen_mode': 'eigenMode',
        'enhanced_accuracy': 'enhancedAccuracy'
    }

    def __init__(self, solver=None, solver_model=None, eigen_solver=None, calculate_frequency=None, eigen_mode=None, enhanced_accuracy=None, local_vars_configuration=None):  # noqa: E501
        """ModalSolver - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._solver = None
        self._solver_model = None
        self._eigen_solver = None
        self._calculate_frequency = None
        self._eigen_mode = None
        self._enhanced_accuracy = None
        self.discriminator = None

        if solver is not None:
            self.solver = solver
        if solver_model is not None:
            self.solver_model = solver_model
        if eigen_solver is not None:
            self.eigen_solver = eigen_solver
        if calculate_frequency is not None:
            self.calculate_frequency = calculate_frequency
        if eigen_mode is not None:
            self.eigen_mode = eigen_mode
        if enhanced_accuracy is not None:
            self.enhanced_accuracy = enhanced_accuracy

    @property
    def solver(self):
        """Gets the solver of this ModalSolver.  # noqa: E501


        :return: The solver of this ModalSolver.  # noqa: E501
        :rtype: OneOfModalSolverSolver
        """
        return self._solver

    @solver.setter
    def solver(self, solver):
        """Sets the solver of this ModalSolver.


        :param solver: The solver of this ModalSolver.  # noqa: E501
        :type: OneOfModalSolverSolver
        """

        self._solver = solver

    @property
    def solver_model(self):
        """Gets the solver_model of this ModalSolver.  # noqa: E501


        :return: The solver_model of this ModalSolver.  # noqa: E501
        :rtype: object
        """
        return self._solver_model

    @solver_model.setter
    def solver_model(self, solver_model):
        """Sets the solver_model of this ModalSolver.


        :param solver_model: The solver_model of this ModalSolver.  # noqa: E501
        :type: object
        """

        self._solver_model = solver_model

    @property
    def eigen_solver(self):
        """Gets the eigen_solver of this ModalSolver.  # noqa: E501


        :return: The eigen_solver of this ModalSolver.  # noqa: E501
        :rtype: OneOfModalSolverEigenSolver
        """
        return self._eigen_solver

    @eigen_solver.setter
    def eigen_solver(self, eigen_solver):
        """Sets the eigen_solver of this ModalSolver.


        :param eigen_solver: The eigen_solver of this ModalSolver.  # noqa: E501
        :type: OneOfModalSolverEigenSolver
        """

        self._eigen_solver = eigen_solver

    @property
    def calculate_frequency(self):
        """Gets the calculate_frequency of this ModalSolver.  # noqa: E501


        :return: The calculate_frequency of this ModalSolver.  # noqa: E501
        :rtype: CalculateFrequency
        """
        return self._calculate_frequency

    @calculate_frequency.setter
    def calculate_frequency(self, calculate_frequency):
        """Sets the calculate_frequency of this ModalSolver.


        :param calculate_frequency: The calculate_frequency of this ModalSolver.  # noqa: E501
        :type: CalculateFrequency
        """

        self._calculate_frequency = calculate_frequency

    @property
    def eigen_mode(self):
        """Gets the eigen_mode of this ModalSolver.  # noqa: E501


        :return: The eigen_mode of this ModalSolver.  # noqa: E501
        :rtype: EigenModeVerification
        """
        return self._eigen_mode

    @eigen_mode.setter
    def eigen_mode(self, eigen_mode):
        """Sets the eigen_mode of this ModalSolver.


        :param eigen_mode: The eigen_mode of this ModalSolver.  # noqa: E501
        :type: EigenModeVerification
        """

        self._eigen_mode = eigen_mode

    @property
    def enhanced_accuracy(self):
        """Gets the enhanced_accuracy of this ModalSolver.  # noqa: E501

        Further increase the accuracy of the results by running two simulations. The results of the first one will be used as input for the second one to fine-tune the setup.  # noqa: E501

        :return: The enhanced_accuracy of this ModalSolver.  # noqa: E501
        :rtype: bool
        """
        return self._enhanced_accuracy

    @enhanced_accuracy.setter
    def enhanced_accuracy(self, enhanced_accuracy):
        """Sets the enhanced_accuracy of this ModalSolver.

        Further increase the accuracy of the results by running two simulations. The results of the first one will be used as input for the second one to fine-tune the setup.  # noqa: E501

        :param enhanced_accuracy: The enhanced_accuracy of this ModalSolver.  # noqa: E501
        :type: bool
        """

        self._enhanced_accuracy = enhanced_accuracy

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
        if not isinstance(other, ModalSolver):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModalSolver):
            return True

        return self.to_dict() != other.to_dict()