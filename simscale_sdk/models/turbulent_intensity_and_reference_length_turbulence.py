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


class TurbulentIntensityAndReferenceLengthTurbulence(object):
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
        'turbulent_intensity': 'float',
        'mixing_length': 'DimensionalLength'
    }

    attribute_map = {
        'type': 'type',
        'turbulent_intensity': 'turbulentIntensity',
        'mixing_length': 'mixingLength'
    }

    def __init__(self, type='TURBULENT_INTENSITY_AND_REFERENCE_LENGTH_TURBULENCE', turbulent_intensity=None, mixing_length=None, local_vars_configuration=None):  # noqa: E501
        """TurbulentIntensityAndReferenceLengthTurbulence - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._turbulent_intensity = None
        self._mixing_length = None
        self.discriminator = None

        self.type = type
        if turbulent_intensity is not None:
            self.turbulent_intensity = turbulent_intensity
        if mixing_length is not None:
            self.mixing_length = mixing_length

    @property
    def type(self):
        """Gets the type of this TurbulentIntensityAndReferenceLengthTurbulence.  # noqa: E501

        Schema name: TurbulentIntensityAndReferenceLengthTurbulence  # noqa: E501

        :return: The type of this TurbulentIntensityAndReferenceLengthTurbulence.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TurbulentIntensityAndReferenceLengthTurbulence.

        Schema name: TurbulentIntensityAndReferenceLengthTurbulence  # noqa: E501

        :param type: The type of this TurbulentIntensityAndReferenceLengthTurbulence.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def turbulent_intensity(self):
        """Gets the turbulent_intensity of this TurbulentIntensityAndReferenceLengthTurbulence.  # noqa: E501

        This provides a <b>turbulent intensity</b> boundary condition. The turbulent intensity is defined as the ratio of the root-mean-square of the velocity fluctuations to the mean flow velocity  # noqa: E501

        :return: The turbulent_intensity of this TurbulentIntensityAndReferenceLengthTurbulence.  # noqa: E501
        :rtype: float
        """
        return self._turbulent_intensity

    @turbulent_intensity.setter
    def turbulent_intensity(self, turbulent_intensity):
        """Sets the turbulent_intensity of this TurbulentIntensityAndReferenceLengthTurbulence.

        This provides a <b>turbulent intensity</b> boundary condition. The turbulent intensity is defined as the ratio of the root-mean-square of the velocity fluctuations to the mean flow velocity  # noqa: E501

        :param turbulent_intensity: The turbulent_intensity of this TurbulentIntensityAndReferenceLengthTurbulence.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                turbulent_intensity is not None and turbulent_intensity > 1):  # noqa: E501
            raise ValueError("Invalid value for `turbulent_intensity`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                turbulent_intensity is not None and turbulent_intensity <= 0):  # noqa: E501
            raise ValueError("Invalid value for `turbulent_intensity`, must be a value greater than `0`")  # noqa: E501

        self._turbulent_intensity = turbulent_intensity

    @property
    def mixing_length(self):
        """Gets the mixing_length of this TurbulentIntensityAndReferenceLengthTurbulence.  # noqa: E501


        :return: The mixing_length of this TurbulentIntensityAndReferenceLengthTurbulence.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._mixing_length

    @mixing_length.setter
    def mixing_length(self, mixing_length):
        """Sets the mixing_length of this TurbulentIntensityAndReferenceLengthTurbulence.


        :param mixing_length: The mixing_length of this TurbulentIntensityAndReferenceLengthTurbulence.  # noqa: E501
        :type: DimensionalLength
        """

        self._mixing_length = mixing_length

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
        if not isinstance(other, TurbulentIntensityAndReferenceLengthTurbulence):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TurbulentIntensityAndReferenceLengthTurbulence):
            return True

        return self.to_dict() != other.to_dict()
