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


class ConstantContactAnglePFBC(object):
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
        'equilibrium_contact_angle': 'DimensionalAngle',
        'limit': 'str'
    }

    attribute_map = {
        'type': 'type',
        'equilibrium_contact_angle': 'equilibriumContactAngle',
        'limit': 'limit'
    }

    def __init__(self, type='CONSTANT_CONTACT_ANGLE', equilibrium_contact_angle=None, limit=None, local_vars_configuration=None):  # noqa: E501
        """ConstantContactAnglePFBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._equilibrium_contact_angle = None
        self._limit = None
        self.discriminator = None

        self.type = type
        if equilibrium_contact_angle is not None:
            self.equilibrium_contact_angle = equilibrium_contact_angle
        if limit is not None:
            self.limit = limit

    @property
    def type(self):
        """Gets the type of this ConstantContactAnglePFBC.  # noqa: E501


        :return: The type of this ConstantContactAnglePFBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConstantContactAnglePFBC.


        :param type: The type of this ConstantContactAnglePFBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def equilibrium_contact_angle(self):
        """Gets the equilibrium_contact_angle of this ConstantContactAnglePFBC.  # noqa: E501


        :return: The equilibrium_contact_angle of this ConstantContactAnglePFBC.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._equilibrium_contact_angle

    @equilibrium_contact_angle.setter
    def equilibrium_contact_angle(self, equilibrium_contact_angle):
        """Sets the equilibrium_contact_angle of this ConstantContactAnglePFBC.


        :param equilibrium_contact_angle: The equilibrium_contact_angle of this ConstantContactAnglePFBC.  # noqa: E501
        :type: DimensionalAngle
        """

        self._equilibrium_contact_angle = equilibrium_contact_angle

    @property
    def limit(self):
        """Gets the limit of this ConstantContactAnglePFBC.  # noqa: E501


        :return: The limit of this ConstantContactAnglePFBC.  # noqa: E501
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ConstantContactAnglePFBC.


        :param limit: The limit of this ConstantContactAnglePFBC.  # noqa: E501
        :type: str
        """
        allowed_values = ["GRADIENT", "NONE", "PHASE_FRACTION", "ZERO_GRADIENT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and limit not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `limit` ({0}), must be one of {1}"  # noqa: E501
                .format(limit, allowed_values)
            )

        self._limit = limit

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
        if not isinstance(other, ConstantContactAnglePFBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConstantContactAnglePFBC):
            return True

        return self.to_dict() != other.to_dict()
