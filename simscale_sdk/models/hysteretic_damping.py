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


class HystereticDamping(object):
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
        'damping_level': 'float'
    }

    attribute_map = {
        'type': 'type',
        'damping_level': 'dampingLevel'
    }

    def __init__(self, type='HYSTERETIC', damping_level=None, local_vars_configuration=None):  # noqa: E501
        """HystereticDamping - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._damping_level = None
        self.discriminator = None

        self.type = type
        if damping_level is not None:
            self.damping_level = damping_level

    @property
    def type(self):
        """Gets the type of this HystereticDamping.  # noqa: E501

        Schema name: HystereticDamping  # noqa: E501

        :return: The type of this HystereticDamping.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HystereticDamping.

        Schema name: HystereticDamping  # noqa: E501

        :param type: The type of this HystereticDamping.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def damping_level(self):
        """Gets the damping_level of this HystereticDamping.  # noqa: E501

        Specify the level of damping to be applied as a percentage of critical damping.  # noqa: E501

        :return: The damping_level of this HystereticDamping.  # noqa: E501
        :rtype: float
        """
        return self._damping_level

    @damping_level.setter
    def damping_level(self, damping_level):
        """Sets the damping_level of this HystereticDamping.

        Specify the level of damping to be applied as a percentage of critical damping.  # noqa: E501

        :param damping_level: The damping_level of this HystereticDamping.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                damping_level is not None and damping_level < 0):  # noqa: E501
            raise ValueError("Invalid value for `damping_level`, must be a value greater than or equal to `0`")  # noqa: E501

        self._damping_level = damping_level

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
        if not isinstance(other, HystereticDamping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HystereticDamping):
            return True

        return self.to_dict() != other.to_dict()
