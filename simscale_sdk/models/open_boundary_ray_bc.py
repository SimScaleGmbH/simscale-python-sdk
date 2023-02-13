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


class OpenBoundaryRayBC(object):
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
        'farfield_black_body_temperature': 'DimensionalTemperature'
    }

    attribute_map = {
        'type': 'type',
        'farfield_black_body_temperature': 'farfieldBlackBodyTemperature'
    }

    def __init__(self, type='OPEN_BOUNDARY_RAY', farfield_black_body_temperature=None, local_vars_configuration=None):  # noqa: E501
        """OpenBoundaryRayBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._farfield_black_body_temperature = None
        self.discriminator = None

        self.type = type
        if farfield_black_body_temperature is not None:
            self.farfield_black_body_temperature = farfield_black_body_temperature

    @property
    def type(self):
        """Gets the type of this OpenBoundaryRayBC.  # noqa: E501

        <p><b>Radiative behaviour of the wall</b>. The Kirchhoff's law of thermal radiation is applied in all options. This means that the <b>absorptivity of the surface is equal to its emissivity</b>. <br> <ul><li><b>Opaque</b> is applied to surfaces with transmissivity equal to 0. The radiation that hits the surface will be absorbed and reflected, but not transmitted, e.g.: brick or concrete walls.</li><li><b>Transparent</b> is applied to surfaces with transmissivity equal to 1. The radiation that hits the surface will be fully transmitted to the other side, e.g.: inlets, outlets or regular windows.</li><li><b>Semi-transparent</b> is applied to non-fully transparent surfaces. The radiation that hits the surface will be absorbed, reflected and transmitted, e.g. some stained glass windows.</li></ul></p>  Schema name: OpenBoundaryRayBC  # noqa: E501

        :return: The type of this OpenBoundaryRayBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OpenBoundaryRayBC.

        <p><b>Radiative behaviour of the wall</b>. The Kirchhoff's law of thermal radiation is applied in all options. This means that the <b>absorptivity of the surface is equal to its emissivity</b>. <br> <ul><li><b>Opaque</b> is applied to surfaces with transmissivity equal to 0. The radiation that hits the surface will be absorbed and reflected, but not transmitted, e.g.: brick or concrete walls.</li><li><b>Transparent</b> is applied to surfaces with transmissivity equal to 1. The radiation that hits the surface will be fully transmitted to the other side, e.g.: inlets, outlets or regular windows.</li><li><b>Semi-transparent</b> is applied to non-fully transparent surfaces. The radiation that hits the surface will be absorbed, reflected and transmitted, e.g. some stained glass windows.</li></ul></p>  Schema name: OpenBoundaryRayBC  # noqa: E501

        :param type: The type of this OpenBoundaryRayBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def farfield_black_body_temperature(self):
        """Gets the farfield_black_body_temperature of this OpenBoundaryRayBC.  # noqa: E501


        :return: The farfield_black_body_temperature of this OpenBoundaryRayBC.  # noqa: E501
        :rtype: DimensionalTemperature
        """
        return self._farfield_black_body_temperature

    @farfield_black_body_temperature.setter
    def farfield_black_body_temperature(self, farfield_black_body_temperature):
        """Sets the farfield_black_body_temperature of this OpenBoundaryRayBC.


        :param farfield_black_body_temperature: The farfield_black_body_temperature of this OpenBoundaryRayBC.  # noqa: E501
        :type: DimensionalTemperature
        """

        self._farfield_black_body_temperature = farfield_black_body_temperature

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
        if not isinstance(other, OpenBoundaryRayBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OpenBoundaryRayBC):
            return True

        return self.to_dict() != other.to_dict()
