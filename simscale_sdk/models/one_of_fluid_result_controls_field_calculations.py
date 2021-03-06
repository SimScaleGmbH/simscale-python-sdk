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


class OneOfFluidResultControlsFieldCalculations(object):
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
        'name': 'str',
        'pressure_type': 'OneOfFieldCalculationsPressureResultControlPressureType',
        'result_type': 'WallShearStressResultType',
        'clothing_coefficient_factor': 'float',
        'metabolic_rate_factor': 'float',
        'relative_humidity_factor': 'float'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'pressure_type': 'pressureType',
        'result_type': 'resultType',
        'clothing_coefficient_factor': 'clothingCoefficientFactor',
        'metabolic_rate_factor': 'metabolicRateFactor',
        'relative_humidity_factor': 'relativeHumidityFactor'
    }

    discriminator_value_class_map = {
        'PRESSURE': 'FieldCalculationsPressureResultControl',
        'TURBULENCE': 'FieldCalculationsTurbulenceResultControl',
        'VELOCITY': 'FieldCalculationsVelocityResultControl',
        'FRICTION_VELOCITY_U_TAU': 'FieldCalculationsFrictionVelocityResultControl',
        'SURFACE_NORMALS': 'FieldCalculationsSurfaceNormalsResultControl',
        'WALL_FLUXES': 'FieldCalculationsWallFluxesResultControl',
        'THERMAL_COMFORT': 'FieldCalculationsThermalComfortResultControl'
    }

    def __init__(self, type='THERMAL_COMFORT', name=None, pressure_type=None, result_type=None, clothing_coefficient_factor=None, metabolic_rate_factor=None, relative_humidity_factor=None, local_vars_configuration=None):  # noqa: E501
        """OneOfFluidResultControlsFieldCalculations - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._pressure_type = None
        self._result_type = None
        self._clothing_coefficient_factor = None
        self._metabolic_rate_factor = None
        self._relative_humidity_factor = None
        self.discriminator = 'type'

        self.type = type
        if name is not None:
            self.name = name
        if pressure_type is not None:
            self.pressure_type = pressure_type
        if result_type is not None:
            self.result_type = result_type
        if clothing_coefficient_factor is not None:
            self.clothing_coefficient_factor = clothing_coefficient_factor
        if metabolic_rate_factor is not None:
            self.metabolic_rate_factor = metabolic_rate_factor
        if relative_humidity_factor is not None:
            self.relative_humidity_factor = relative_humidity_factor

    @property
    def type(self):
        """Gets the type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501

        Schema name: FieldCalculationsThermalComfortResultControl  # noqa: E501

        :return: The type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfFluidResultControlsFieldCalculations.

        Schema name: FieldCalculationsThermalComfortResultControl  # noqa: E501

        :param type: The type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The name of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfFluidResultControlsFieldCalculations.


        :param name: The name of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[A-Za-z()][-+0-9a-zA-Z_()\h]{0,199}$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[A-Za-z()][-+0-9a-zA-Z_()\h]{0,199}$/`")  # noqa: E501

        self._name = name

    @property
    def pressure_type(self):
        """Gets the pressure_type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The pressure_type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: OneOfFieldCalculationsPressureResultControlPressureType
        """
        return self._pressure_type

    @pressure_type.setter
    def pressure_type(self, pressure_type):
        """Sets the pressure_type of this OneOfFluidResultControlsFieldCalculations.


        :param pressure_type: The pressure_type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: OneOfFieldCalculationsPressureResultControlPressureType
        """

        self._pressure_type = pressure_type

    @property
    def result_type(self):
        """Gets the result_type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The result_type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: WallShearStressResultType
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        """Sets the result_type of this OneOfFluidResultControlsFieldCalculations.


        :param result_type: The result_type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: WallShearStressResultType
        """

        self._result_type = result_type

    @property
    def clothing_coefficient_factor(self):
        """Gets the clothing_coefficient_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The clothing_coefficient_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: float
        """
        return self._clothing_coefficient_factor

    @clothing_coefficient_factor.setter
    def clothing_coefficient_factor(self, clothing_coefficient_factor):
        """Sets the clothing_coefficient_factor of this OneOfFluidResultControlsFieldCalculations.


        :param clothing_coefficient_factor: The clothing_coefficient_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                clothing_coefficient_factor is not None and clothing_coefficient_factor > 2):  # noqa: E501
            raise ValueError("Invalid value for `clothing_coefficient_factor`, must be a value less than or equal to `2`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                clothing_coefficient_factor is not None and clothing_coefficient_factor < 0):  # noqa: E501
            raise ValueError("Invalid value for `clothing_coefficient_factor`, must be a value greater than or equal to `0`")  # noqa: E501

        self._clothing_coefficient_factor = clothing_coefficient_factor

    @property
    def metabolic_rate_factor(self):
        """Gets the metabolic_rate_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The metabolic_rate_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: float
        """
        return self._metabolic_rate_factor

    @metabolic_rate_factor.setter
    def metabolic_rate_factor(self, metabolic_rate_factor):
        """Sets the metabolic_rate_factor of this OneOfFluidResultControlsFieldCalculations.


        :param metabolic_rate_factor: The metabolic_rate_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                metabolic_rate_factor is not None and metabolic_rate_factor > 4):  # noqa: E501
            raise ValueError("Invalid value for `metabolic_rate_factor`, must be a value less than or equal to `4`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                metabolic_rate_factor is not None and metabolic_rate_factor < 0.8):  # noqa: E501
            raise ValueError("Invalid value for `metabolic_rate_factor`, must be a value greater than or equal to `0.8`")  # noqa: E501

        self._metabolic_rate_factor = metabolic_rate_factor

    @property
    def relative_humidity_factor(self):
        """Gets the relative_humidity_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The relative_humidity_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: float
        """
        return self._relative_humidity_factor

    @relative_humidity_factor.setter
    def relative_humidity_factor(self, relative_humidity_factor):
        """Sets the relative_humidity_factor of this OneOfFluidResultControlsFieldCalculations.


        :param relative_humidity_factor: The relative_humidity_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                relative_humidity_factor is not None and relative_humidity_factor > 100):  # noqa: E501
            raise ValueError("Invalid value for `relative_humidity_factor`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                relative_humidity_factor is not None and relative_humidity_factor < 0):  # noqa: E501
            raise ValueError("Invalid value for `relative_humidity_factor`, must be a value greater than or equal to `0`")  # noqa: E501

        self._relative_humidity_factor = relative_humidity_factor

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, OneOfFluidResultControlsFieldCalculations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfFluidResultControlsFieldCalculations):
            return True

        return self.to_dict() != other.to_dict()
