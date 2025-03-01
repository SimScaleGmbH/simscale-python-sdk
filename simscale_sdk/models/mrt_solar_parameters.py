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


class MrtSolarParameters(object):
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
        'fraction_body_surface': 'OneOfMrtSolarParametersFractionBodySurface',
        'projected_area_factor': 'float',
        'short_wave_absorptivity': 'float'
    }

    attribute_map = {
        'fraction_body_surface': 'fractionBodySurface',
        'projected_area_factor': 'projectedAreaFactor',
        'short_wave_absorptivity': 'shortWaveAbsorptivity'
    }

    def __init__(self, fraction_body_surface=None, projected_area_factor=None, short_wave_absorptivity=None, local_vars_configuration=None):  # noqa: E501
        """MrtSolarParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fraction_body_surface = None
        self._projected_area_factor = None
        self._short_wave_absorptivity = None
        self.discriminator = None

        if fraction_body_surface is not None:
            self.fraction_body_surface = fraction_body_surface
        if projected_area_factor is not None:
            self.projected_area_factor = projected_area_factor
        if short_wave_absorptivity is not None:
            self.short_wave_absorptivity = short_wave_absorptivity

    @property
    def fraction_body_surface(self):
        """Gets the fraction_body_surface of this MrtSolarParameters.  # noqa: E501


        :return: The fraction_body_surface of this MrtSolarParameters.  # noqa: E501
        :rtype: OneOfMrtSolarParametersFractionBodySurface
        """
        return self._fraction_body_surface

    @fraction_body_surface.setter
    def fraction_body_surface(self, fraction_body_surface):
        """Sets the fraction_body_surface of this MrtSolarParameters.


        :param fraction_body_surface: The fraction_body_surface of this MrtSolarParameters.  # noqa: E501
        :type: OneOfMrtSolarParametersFractionBodySurface
        """

        self._fraction_body_surface = fraction_body_surface

    @property
    def projected_area_factor(self):
        """Gets the projected_area_factor of this MrtSolarParameters.  # noqa: E501

        The projected area of a standard person exposed to direct beam sunlight in the range [0, 1]. This projection depends on the time of day and year usually in the range [0, 0.7]. This parameter is not a necessary input if the solar load is computed from time and place since it can be computed.  # noqa: E501

        :return: The projected_area_factor of this MrtSolarParameters.  # noqa: E501
        :rtype: float
        """
        return self._projected_area_factor

    @projected_area_factor.setter
    def projected_area_factor(self, projected_area_factor):
        """Sets the projected_area_factor of this MrtSolarParameters.

        The projected area of a standard person exposed to direct beam sunlight in the range [0, 1]. This projection depends on the time of day and year usually in the range [0, 0.7]. This parameter is not a necessary input if the solar load is computed from time and place since it can be computed.  # noqa: E501

        :param projected_area_factor: The projected_area_factor of this MrtSolarParameters.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                projected_area_factor is not None and projected_area_factor > 1):  # noqa: E501
            raise ValueError("Invalid value for `projected_area_factor`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                projected_area_factor is not None and projected_area_factor < 0):  # noqa: E501
            raise ValueError("Invalid value for `projected_area_factor`, must be a value greater than or equal to `0`")  # noqa: E501

        self._projected_area_factor = projected_area_factor

    @property
    def short_wave_absorptivity(self):
        """Gets the short_wave_absorptivity of this MrtSolarParameters.  # noqa: E501

        The radiation wavelength of a source depends on its temperature. Since the sun is much hotter than surfaces in a typical room, the amount of sun heat absorbed by a person is different than the amount it is able to emit back to its surroundings. Typical values are: <br><li><b> 0.2 </b>: White clothing. <br><li><b> 0.57 </b>: Khaki clothing <br><li><b> 0.57 </b>: White skin <br><li><b> 0.65 </b>: Brown skin <br><li><b> 0.84 </b>: Black skin. <br><li><b> 0.88 </b>: Black clothing.  # noqa: E501

        :return: The short_wave_absorptivity of this MrtSolarParameters.  # noqa: E501
        :rtype: float
        """
        return self._short_wave_absorptivity

    @short_wave_absorptivity.setter
    def short_wave_absorptivity(self, short_wave_absorptivity):
        """Sets the short_wave_absorptivity of this MrtSolarParameters.

        The radiation wavelength of a source depends on its temperature. Since the sun is much hotter than surfaces in a typical room, the amount of sun heat absorbed by a person is different than the amount it is able to emit back to its surroundings. Typical values are: <br><li><b> 0.2 </b>: White clothing. <br><li><b> 0.57 </b>: Khaki clothing <br><li><b> 0.57 </b>: White skin <br><li><b> 0.65 </b>: Brown skin <br><li><b> 0.84 </b>: Black skin. <br><li><b> 0.88 </b>: Black clothing.  # noqa: E501

        :param short_wave_absorptivity: The short_wave_absorptivity of this MrtSolarParameters.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                short_wave_absorptivity is not None and short_wave_absorptivity > 1):  # noqa: E501
            raise ValueError("Invalid value for `short_wave_absorptivity`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                short_wave_absorptivity is not None and short_wave_absorptivity < 0):  # noqa: E501
            raise ValueError("Invalid value for `short_wave_absorptivity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._short_wave_absorptivity = short_wave_absorptivity

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
        if not isinstance(other, MrtSolarParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MrtSolarParameters):
            return True

        return self.to_dict() != other.to_dict()
