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


class QZ(object):
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
        'type_qz': 'str'
    }

    attribute_map = {
        'type': 'type',
        'type_qz': 'typeQZ'
    }

    def __init__(self, type='QZ', type_qz=None, local_vars_configuration=None):  # noqa: E501
        """QZ - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._type_qz = None
        self.discriminator = None

        self.type = type
        if type_qz is not None:
            self.type_qz = type_qz

    @property
    def type(self):
        """Gets the type of this QZ.  # noqa: E501

        Schema name: QZ  # noqa: E501

        :return: The type of this QZ.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QZ.

        Schema name: QZ  # noqa: E501

        :param type: The type of this QZ.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def type_qz(self):
        """Gets the type_qz of this QZ.  # noqa: E501


        :return: The type_qz of this QZ.  # noqa: E501
        :rtype: str
        """
        return self._type_qz

    @type_qz.setter
    def type_qz(self, type_qz):
        """Sets the type_qz of this QZ.


        :param type_qz: The type_qz of this QZ.  # noqa: E501
        :type: str
        """
        allowed_values = ["QZ_SIMPLE", "QZ_EQUI", "QZ_QR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type_qz not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type_qz` ({0}), must be one of {1}"  # noqa: E501
                .format(type_qz, allowed_values)
            )

        self._type_qz = type_qz

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
        if not isinstance(other, QZ):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QZ):
            return True

        return self.to_dict() != other.to_dict()
