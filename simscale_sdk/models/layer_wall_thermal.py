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


class LayerWallThermal(object):
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
        'conductivity_thickness_pairs': 'list[ConductivityThicknessPair]'
    }

    attribute_map = {
        'type': 'type',
        'conductivity_thickness_pairs': 'conductivityThicknessPairs'
    }

    def __init__(self, type='CONTACT_INTERFACE_MATERIAL', conductivity_thickness_pairs=None, local_vars_configuration=None):  # noqa: E501
        """LayerWallThermal - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._conductivity_thickness_pairs = None
        self.discriminator = None

        self.type = type
        if conductivity_thickness_pairs is not None:
            self.conductivity_thickness_pairs = conductivity_thickness_pairs

    @property
    def type(self):
        """Gets the type of this LayerWallThermal.  # noqa: E501


        :return: The type of this LayerWallThermal.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LayerWallThermal.


        :param type: The type of this LayerWallThermal.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def conductivity_thickness_pairs(self):
        """Gets the conductivity_thickness_pairs of this LayerWallThermal.  # noqa: E501


        :return: The conductivity_thickness_pairs of this LayerWallThermal.  # noqa: E501
        :rtype: list[ConductivityThicknessPair]
        """
        return self._conductivity_thickness_pairs

    @conductivity_thickness_pairs.setter
    def conductivity_thickness_pairs(self, conductivity_thickness_pairs):
        """Sets the conductivity_thickness_pairs of this LayerWallThermal.


        :param conductivity_thickness_pairs: The conductivity_thickness_pairs of this LayerWallThermal.  # noqa: E501
        :type: list[ConductivityThicknessPair]
        """

        self._conductivity_thickness_pairs = conductivity_thickness_pairs

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
        if not isinstance(other, LayerWallThermal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LayerWallThermal):
            return True

        return self.to_dict() != other.to_dict()
