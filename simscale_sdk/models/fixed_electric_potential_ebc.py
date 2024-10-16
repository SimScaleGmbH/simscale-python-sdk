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


class FixedElectricPotentialEBC(object):
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
        'potential_function': 'DimensionalFunctionElectricPotential'
    }

    attribute_map = {
        'type': 'type',
        'potential_function': 'potentialFunction'
    }

    def __init__(self, type='FIXED_ELECTRIC_POTENTIAL', potential_function=None, local_vars_configuration=None):  # noqa: E501
        """FixedElectricPotentialEBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._potential_function = None
        self.discriminator = None

        self.type = type
        if potential_function is not None:
            self.potential_function = potential_function

    @property
    def type(self):
        """Gets the type of this FixedElectricPotentialEBC.  # noqa: E501

        Schema name: FixedElectricPotentialEBC  # noqa: E501

        :return: The type of this FixedElectricPotentialEBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FixedElectricPotentialEBC.

        Schema name: FixedElectricPotentialEBC  # noqa: E501

        :param type: The type of this FixedElectricPotentialEBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def potential_function(self):
        """Gets the potential_function of this FixedElectricPotentialEBC.  # noqa: E501


        :return: The potential_function of this FixedElectricPotentialEBC.  # noqa: E501
        :rtype: DimensionalFunctionElectricPotential
        """
        return self._potential_function

    @potential_function.setter
    def potential_function(self, potential_function):
        """Sets the potential_function of this FixedElectricPotentialEBC.


        :param potential_function: The potential_function of this FixedElectricPotentialEBC.  # noqa: E501
        :type: DimensionalFunctionElectricPotential
        """

        self._potential_function = potential_function

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
        if not isinstance(other, FixedElectricPotentialEBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FixedElectricPotentialEBC):
            return True

        return self.to_dict() != other.to_dict()
