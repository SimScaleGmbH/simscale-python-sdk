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


class EntityAttribute(object):
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
        'attribute': 'str',
        'value': 'str'
    }

    attribute_map = {
        'attribute': 'attribute',
        'value': 'value'
    }

    def __init__(self, attribute=None, value=None, local_vars_configuration=None):  # noqa: E501
        """EntityAttribute - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attribute = None
        self._value = None
        self.discriminator = None

        if attribute is not None:
            self.attribute = attribute
        if value is not None:
            self.value = value

    @property
    def attribute(self):
        """Gets the attribute of this EntityAttribute.  # noqa: E501


        :return: The attribute of this EntityAttribute.  # noqa: E501
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this EntityAttribute.


        :param attribute: The attribute of this EntityAttribute.  # noqa: E501
        :type: str
        """

        self._attribute = attribute

    @property
    def value(self):
        """Gets the value of this EntityAttribute.  # noqa: E501


        :return: The value of this EntityAttribute.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this EntityAttribute.


        :param value: The value of this EntityAttribute.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, EntityAttribute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntityAttribute):
            return True

        return self.to_dict() != other.to_dict()
