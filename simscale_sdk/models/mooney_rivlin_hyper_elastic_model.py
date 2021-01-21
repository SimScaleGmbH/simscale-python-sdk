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


class MooneyRivlinHyperElasticModel(object):
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
        'c10': 'DimensionalPressure',
        'c01': 'DimensionalPressure',
        'd1': 'DimensionalInvPressure'
    }

    attribute_map = {
        'type': 'type',
        'c10': 'c10',
        'c01': 'c01',
        'd1': 'd1'
    }

    def __init__(self, type='MOONEY_RIVLIN', c10=None, c01=None, d1=None, local_vars_configuration=None):  # noqa: E501
        """MooneyRivlinHyperElasticModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._c10 = None
        self._c01 = None
        self._d1 = None
        self.discriminator = None

        self.type = type
        if c10 is not None:
            self.c10 = c10
        if c01 is not None:
            self.c01 = c01
        if d1 is not None:
            self.d1 = d1

    @property
    def type(self):
        """Gets the type of this MooneyRivlinHyperElasticModel.  # noqa: E501


        :return: The type of this MooneyRivlinHyperElasticModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MooneyRivlinHyperElasticModel.


        :param type: The type of this MooneyRivlinHyperElasticModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def c10(self):
        """Gets the c10 of this MooneyRivlinHyperElasticModel.  # noqa: E501


        :return: The c10 of this MooneyRivlinHyperElasticModel.  # noqa: E501
        :rtype: DimensionalPressure
        """
        return self._c10

    @c10.setter
    def c10(self, c10):
        """Sets the c10 of this MooneyRivlinHyperElasticModel.


        :param c10: The c10 of this MooneyRivlinHyperElasticModel.  # noqa: E501
        :type: DimensionalPressure
        """

        self._c10 = c10

    @property
    def c01(self):
        """Gets the c01 of this MooneyRivlinHyperElasticModel.  # noqa: E501


        :return: The c01 of this MooneyRivlinHyperElasticModel.  # noqa: E501
        :rtype: DimensionalPressure
        """
        return self._c01

    @c01.setter
    def c01(self, c01):
        """Sets the c01 of this MooneyRivlinHyperElasticModel.


        :param c01: The c01 of this MooneyRivlinHyperElasticModel.  # noqa: E501
        :type: DimensionalPressure
        """

        self._c01 = c01

    @property
    def d1(self):
        """Gets the d1 of this MooneyRivlinHyperElasticModel.  # noqa: E501


        :return: The d1 of this MooneyRivlinHyperElasticModel.  # noqa: E501
        :rtype: DimensionalInvPressure
        """
        return self._d1

    @d1.setter
    def d1(self, d1):
        """Sets the d1 of this MooneyRivlinHyperElasticModel.


        :param d1: The d1 of this MooneyRivlinHyperElasticModel.  # noqa: E501
        :type: DimensionalInvPressure
        """

        self._d1 = d1

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
        if not isinstance(other, MooneyRivlinHyperElasticModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MooneyRivlinHyperElasticModel):
            return True

        return self.to_dict() != other.to_dict()
