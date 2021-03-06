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


class IncompletePreconditionerV33(object):
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
        'matrix_completeness': 'int',
        'preconditioner_matrix_growth': 'float'
    }

    attribute_map = {
        'type': 'type',
        'matrix_completeness': 'matrixCompleteness',
        'preconditioner_matrix_growth': 'preconditionerMatrixGrowth'
    }

    def __init__(self, type='INCOMPLETE_LDLT_V33', matrix_completeness=None, preconditioner_matrix_growth=None, local_vars_configuration=None):  # noqa: E501
        """IncompletePreconditionerV33 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._matrix_completeness = None
        self._preconditioner_matrix_growth = None
        self.discriminator = None

        self.type = type
        if matrix_completeness is not None:
            self.matrix_completeness = matrix_completeness
        if preconditioner_matrix_growth is not None:
            self.preconditioner_matrix_growth = preconditioner_matrix_growth

    @property
    def type(self):
        """Gets the type of this IncompletePreconditionerV33.  # noqa: E501

        Schema name: IncompletePreconditionerV33  # noqa: E501

        :return: The type of this IncompletePreconditionerV33.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IncompletePreconditionerV33.

        Schema name: IncompletePreconditionerV33  # noqa: E501

        :param type: The type of this IncompletePreconditionerV33.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def matrix_completeness(self):
        """Gets the matrix_completeness of this IncompletePreconditionerV33.  # noqa: E501

        Set the level of completeness for the incomplete Cholesky decomposition. The larger this value is, the better the preconditioning Matrix P approximates K<sup>-1</sup>, but also the memory usage and computation time increase. If the solution does not converge or uses a lot of iterations it could help to increase this parameter.  # noqa: E501

        :return: The matrix_completeness of this IncompletePreconditionerV33.  # noqa: E501
        :rtype: int
        """
        return self._matrix_completeness

    @matrix_completeness.setter
    def matrix_completeness(self, matrix_completeness):
        """Sets the matrix_completeness of this IncompletePreconditionerV33.

        Set the level of completeness for the incomplete Cholesky decomposition. The larger this value is, the better the preconditioning Matrix P approximates K<sup>-1</sup>, but also the memory usage and computation time increase. If the solution does not converge or uses a lot of iterations it could help to increase this parameter.  # noqa: E501

        :param matrix_completeness: The matrix_completeness of this IncompletePreconditionerV33.  # noqa: E501
        :type: int
        """

        self._matrix_completeness = matrix_completeness

    @property
    def preconditioner_matrix_growth(self):
        """Gets the preconditioner_matrix_growth of this IncompletePreconditionerV33.  # noqa: E501

        Set the growth rate of the filling for the incomplete decomposition matrix. If this parameter is set to 1.0 PETSc estimates the matrix storage size from the first level of completeness. If this estimate is too low, PETSC increases the allocated memory on the fly, but this is more expensive.  # noqa: E501

        :return: The preconditioner_matrix_growth of this IncompletePreconditionerV33.  # noqa: E501
        :rtype: float
        """
        return self._preconditioner_matrix_growth

    @preconditioner_matrix_growth.setter
    def preconditioner_matrix_growth(self, preconditioner_matrix_growth):
        """Sets the preconditioner_matrix_growth of this IncompletePreconditionerV33.

        Set the growth rate of the filling for the incomplete decomposition matrix. If this parameter is set to 1.0 PETSc estimates the matrix storage size from the first level of completeness. If this estimate is too low, PETSC increases the allocated memory on the fly, but this is more expensive.  # noqa: E501

        :param preconditioner_matrix_growth: The preconditioner_matrix_growth of this IncompletePreconditionerV33.  # noqa: E501
        :type: float
        """

        self._preconditioner_matrix_growth = preconditioner_matrix_growth

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
        if not isinstance(other, IncompletePreconditionerV33):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IncompletePreconditionerV33):
            return True

        return self.to_dict() != other.to_dict()
