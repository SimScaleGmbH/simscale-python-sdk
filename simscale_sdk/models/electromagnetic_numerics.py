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


class ElectromagneticNumerics(object):
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
        'nonlinear_residual': 'float',
        'element_accuracy': 'str'
    }

    attribute_map = {
        'nonlinear_residual': 'nonlinearResidual',
        'element_accuracy': 'elementAccuracy'
    }

    def __init__(self, nonlinear_residual=None, element_accuracy=None, local_vars_configuration=None):  # noqa: E501
        """ElectromagneticNumerics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._nonlinear_residual = None
        self._element_accuracy = None
        self.discriminator = None

        if nonlinear_residual is not None:
            self.nonlinear_residual = nonlinear_residual
        if element_accuracy is not None:
            self.element_accuracy = element_accuracy

    @property
    def nonlinear_residual(self):
        """Gets the nonlinear_residual of this ElectromagneticNumerics.  # noqa: E501

        The nonlinear residual error is computed as the difference between the calculated and expected flux density value when a BH curve is specified.  # noqa: E501

        :return: The nonlinear_residual of this ElectromagneticNumerics.  # noqa: E501
        :rtype: float
        """
        return self._nonlinear_residual

    @nonlinear_residual.setter
    def nonlinear_residual(self, nonlinear_residual):
        """Sets the nonlinear_residual of this ElectromagneticNumerics.

        The nonlinear residual error is computed as the difference between the calculated and expected flux density value when a BH curve is specified.  # noqa: E501

        :param nonlinear_residual: The nonlinear_residual of this ElectromagneticNumerics.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                nonlinear_residual is not None and nonlinear_residual < 0):  # noqa: E501
            raise ValueError("Invalid value for `nonlinear_residual`, must be a value greater than or equal to `0`")  # noqa: E501

        self._nonlinear_residual = nonlinear_residual

    @property
    def element_accuracy(self):
        """Gets the element_accuracy of this ElectromagneticNumerics.  # noqa: E501

        Uses second order element shape functions for a higher accuracy. Especially recommended when calculating torques or forces. However this increases memory consumption and computational time.  # noqa: E501

        :return: The element_accuracy of this ElectromagneticNumerics.  # noqa: E501
        :rtype: str
        """
        return self._element_accuracy

    @element_accuracy.setter
    def element_accuracy(self, element_accuracy):
        """Sets the element_accuracy of this ElectromagneticNumerics.

        Uses second order element shape functions for a higher accuracy. Especially recommended when calculating torques or forces. However this increases memory consumption and computational time.  # noqa: E501

        :param element_accuracy: The element_accuracy of this ElectromagneticNumerics.  # noqa: E501
        :type: str
        """
        allowed_values = ["FIRST_ORDER", "SECOND_ORDER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and element_accuracy not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `element_accuracy` ({0}), must be one of {1}"  # noqa: E501
                .format(element_accuracy, allowed_values)
            )

        self._element_accuracy = element_accuracy

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
        if not isinstance(other, ElectromagneticNumerics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElectromagneticNumerics):
            return True

        return self.to_dict() != other.to_dict()
