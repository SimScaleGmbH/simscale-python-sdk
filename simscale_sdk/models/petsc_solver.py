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


class PETSCSolver(object):
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
        'convergence_threshold': 'float',
        'max_iterations': 'int',
        'advanced_petsc_settings': 'AdvancedPETSCSettings'
    }

    attribute_map = {
        'type': 'type',
        'convergence_threshold': 'convergenceThreshold',
        'max_iterations': 'maxIterations',
        'advanced_petsc_settings': 'advancedPetscSettings'
    }

    def __init__(self, type='PETSC', convergence_threshold=None, max_iterations=None, advanced_petsc_settings=None, local_vars_configuration=None):  # noqa: E501
        """PETSCSolver - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._convergence_threshold = None
        self._max_iterations = None
        self._advanced_petsc_settings = None
        self.discriminator = None

        self.type = type
        if convergence_threshold is not None:
            self.convergence_threshold = convergence_threshold
        if max_iterations is not None:
            self.max_iterations = max_iterations
        if advanced_petsc_settings is not None:
            self.advanced_petsc_settings = advanced_petsc_settings

    @property
    def type(self):
        """Gets the type of this PETSCSolver.  # noqa: E501

        Schema name: PETSCSolver  # noqa: E501

        :return: The type of this PETSCSolver.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PETSCSolver.

        Schema name: PETSCSolver  # noqa: E501

        :param type: The type of this PETSCSolver.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def convergence_threshold(self):
        """Gets the convergence_threshold of this PETSCSolver.  # noqa: E501

        Set the threshold value for convergence detection for the relative convergence criteria.  # noqa: E501

        :return: The convergence_threshold of this PETSCSolver.  # noqa: E501
        :rtype: float
        """
        return self._convergence_threshold

    @convergence_threshold.setter
    def convergence_threshold(self, convergence_threshold):
        """Sets the convergence_threshold of this PETSCSolver.

        Set the threshold value for convergence detection for the relative convergence criteria.  # noqa: E501

        :param convergence_threshold: The convergence_threshold of this PETSCSolver.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                convergence_threshold is not None and convergence_threshold < 0):  # noqa: E501
            raise ValueError("Invalid value for `convergence_threshold`, must be a value greater than or equal to `0`")  # noqa: E501

        self._convergence_threshold = convergence_threshold

    @property
    def max_iterations(self):
        """Gets the max_iterations of this PETSCSolver.  # noqa: E501

        Set the maximum number of iterations for the iterative solver. If set to 0 PETSC sets an estimate of the maximum number of iterations.  # noqa: E501

        :return: The max_iterations of this PETSCSolver.  # noqa: E501
        :rtype: int
        """
        return self._max_iterations

    @max_iterations.setter
    def max_iterations(self, max_iterations):
        """Sets the max_iterations of this PETSCSolver.

        Set the maximum number of iterations for the iterative solver. If set to 0 PETSC sets an estimate of the maximum number of iterations.  # noqa: E501

        :param max_iterations: The max_iterations of this PETSCSolver.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_iterations is not None and max_iterations < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_iterations`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_iterations = max_iterations

    @property
    def advanced_petsc_settings(self):
        """Gets the advanced_petsc_settings of this PETSCSolver.  # noqa: E501


        :return: The advanced_petsc_settings of this PETSCSolver.  # noqa: E501
        :rtype: AdvancedPETSCSettings
        """
        return self._advanced_petsc_settings

    @advanced_petsc_settings.setter
    def advanced_petsc_settings(self, advanced_petsc_settings):
        """Sets the advanced_petsc_settings of this PETSCSolver.


        :param advanced_petsc_settings: The advanced_petsc_settings of this PETSCSolver.  # noqa: E501
        :type: AdvancedPETSCSettings
        """

        self._advanced_petsc_settings = advanced_petsc_settings

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
        if not isinstance(other, PETSCSolver):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PETSCSolver):
            return True

        return self.to_dict() != other.to_dict()
