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


class CoulombFriction(object):
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
        'nonlinearity_resolution': 'OneOfCoulombFrictionNonlinearityResolution'
    }

    attribute_map = {
        'type': 'type',
        'nonlinearity_resolution': 'nonlinearityResolution'
    }

    def __init__(self, type='COULOMB_FRICTION', nonlinearity_resolution=None, local_vars_configuration=None):  # noqa: E501
        """CoulombFriction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._nonlinearity_resolution = None
        self.discriminator = None

        self.type = type
        if nonlinearity_resolution is not None:
            self.nonlinearity_resolution = nonlinearity_resolution

    @property
    def type(self):
        """Gets the type of this CoulombFriction.  # noqa: E501

        Schema name: CoulombFriction  # noqa: E501

        :return: The type of this CoulombFriction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CoulombFriction.

        Schema name: CoulombFriction  # noqa: E501

        :param type: The type of this CoulombFriction.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def nonlinearity_resolution(self):
        """Gets the nonlinearity_resolution of this CoulombFriction.  # noqa: E501


        :return: The nonlinearity_resolution of this CoulombFriction.  # noqa: E501
        :rtype: OneOfCoulombFrictionNonlinearityResolution
        """
        return self._nonlinearity_resolution

    @nonlinearity_resolution.setter
    def nonlinearity_resolution(self, nonlinearity_resolution):
        """Sets the nonlinearity_resolution of this CoulombFriction.


        :param nonlinearity_resolution: The nonlinearity_resolution of this CoulombFriction.  # noqa: E501
        :type: OneOfCoulombFrictionNonlinearityResolution
        """

        self._nonlinearity_resolution = nonlinearity_resolution

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
        if not isinstance(other, CoulombFriction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CoulombFriction):
            return True

        return self.to_dict() != other.to_dict()
