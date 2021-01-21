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


class ShipDesignAnalysisSBM(object):
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
        'center_of_gravity': 'DimensionalVectorLength',
        'model_scale_ratio': 'float',
        'max_roll_amplitude': 'DimensionalAngle',
        'min_roll_amplitude': 'DimensionalAngle',
        'heave_amplitude': 'DimensionalLength',
        'sway_amplitude': 'DimensionalLength',
        'damping_coefficient': 'float',
        'time_period_for_liquid': 'DimensionalTime',
        'natural_period_of_ship': 'DimensionalTime',
        'reference_time_step': 'DimensionalTime',
        'increase_in_liquid_per_time_step': 'float'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'center_of_gravity': 'centerOfGravity',
        'model_scale_ratio': 'modelScaleRatio',
        'max_roll_amplitude': 'maxRollAmplitude',
        'min_roll_amplitude': 'minRollAmplitude',
        'heave_amplitude': 'heaveAmplitude',
        'sway_amplitude': 'swayAmplitude',
        'damping_coefficient': 'dampingCoefficient',
        'time_period_for_liquid': 'timePeriodForLiquid',
        'natural_period_of_ship': 'naturalPeriodOfShip',
        'reference_time_step': 'referenceTimeStep',
        'increase_in_liquid_per_time_step': 'increaseInLiquidPerTimeStep'
    }

    def __init__(self, type='SHIP_DESIGN_ANALYSIS', name=None, center_of_gravity=None, model_scale_ratio=None, max_roll_amplitude=None, min_roll_amplitude=None, heave_amplitude=None, sway_amplitude=None, damping_coefficient=None, time_period_for_liquid=None, natural_period_of_ship=None, reference_time_step=None, increase_in_liquid_per_time_step=None, local_vars_configuration=None):  # noqa: E501
        """ShipDesignAnalysisSBM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._center_of_gravity = None
        self._model_scale_ratio = None
        self._max_roll_amplitude = None
        self._min_roll_amplitude = None
        self._heave_amplitude = None
        self._sway_amplitude = None
        self._damping_coefficient = None
        self._time_period_for_liquid = None
        self._natural_period_of_ship = None
        self._reference_time_step = None
        self._increase_in_liquid_per_time_step = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if center_of_gravity is not None:
            self.center_of_gravity = center_of_gravity
        if model_scale_ratio is not None:
            self.model_scale_ratio = model_scale_ratio
        if max_roll_amplitude is not None:
            self.max_roll_amplitude = max_roll_amplitude
        if min_roll_amplitude is not None:
            self.min_roll_amplitude = min_roll_amplitude
        if heave_amplitude is not None:
            self.heave_amplitude = heave_amplitude
        if sway_amplitude is not None:
            self.sway_amplitude = sway_amplitude
        if damping_coefficient is not None:
            self.damping_coefficient = damping_coefficient
        if time_period_for_liquid is not None:
            self.time_period_for_liquid = time_period_for_liquid
        if natural_period_of_ship is not None:
            self.natural_period_of_ship = natural_period_of_ship
        if reference_time_step is not None:
            self.reference_time_step = reference_time_step
        if increase_in_liquid_per_time_step is not None:
            self.increase_in_liquid_per_time_step = increase_in_liquid_per_time_step

    @property
    def type(self):
        """Gets the type of this ShipDesignAnalysisSBM.  # noqa: E501


        :return: The type of this ShipDesignAnalysisSBM.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShipDesignAnalysisSBM.


        :param type: The type of this ShipDesignAnalysisSBM.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this ShipDesignAnalysisSBM.  # noqa: E501


        :return: The name of this ShipDesignAnalysisSBM.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShipDesignAnalysisSBM.


        :param name: The name of this ShipDesignAnalysisSBM.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def center_of_gravity(self):
        """Gets the center_of_gravity of this ShipDesignAnalysisSBM.  # noqa: E501


        :return: The center_of_gravity of this ShipDesignAnalysisSBM.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._center_of_gravity

    @center_of_gravity.setter
    def center_of_gravity(self, center_of_gravity):
        """Sets the center_of_gravity of this ShipDesignAnalysisSBM.


        :param center_of_gravity: The center_of_gravity of this ShipDesignAnalysisSBM.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._center_of_gravity = center_of_gravity

    @property
    def model_scale_ratio(self):
        """Gets the model_scale_ratio of this ShipDesignAnalysisSBM.  # noqa: E501


        :return: The model_scale_ratio of this ShipDesignAnalysisSBM.  # noqa: E501
        :rtype: float
        """
        return self._model_scale_ratio

    @model_scale_ratio.setter
    def model_scale_ratio(self, model_scale_ratio):
        """Sets the model_scale_ratio of this ShipDesignAnalysisSBM.


        :param model_scale_ratio: The model_scale_ratio of this ShipDesignAnalysisSBM.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                model_scale_ratio is not None and model_scale_ratio < 1):  # noqa: E501
            raise ValueError("Invalid value for `model_scale_ratio`, must be a value greater than or equal to `1`")  # noqa: E501

        self._model_scale_ratio = model_scale_ratio

    @property
    def max_roll_amplitude(self):
        """Gets the max_roll_amplitude of this ShipDesignAnalysisSBM.  # noqa: E501


        :return: The max_roll_amplitude of this ShipDesignAnalysisSBM.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._max_roll_amplitude

    @max_roll_amplitude.setter
    def max_roll_amplitude(self, max_roll_amplitude):
        """Sets the max_roll_amplitude of this ShipDesignAnalysisSBM.


        :param max_roll_amplitude: The max_roll_amplitude of this ShipDesignAnalysisSBM.  # noqa: E501
        :type: DimensionalAngle
        """

        self._max_roll_amplitude = max_roll_amplitude

    @property
    def min_roll_amplitude(self):
        """Gets the min_roll_amplitude of this ShipDesignAnalysisSBM.  # noqa: E501


        :return: The min_roll_amplitude of this ShipDesignAnalysisSBM.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._min_roll_amplitude

    @min_roll_amplitude.setter
    def min_roll_amplitude(self, min_roll_amplitude):
        """Sets the min_roll_amplitude of this ShipDesignAnalysisSBM.


        :param min_roll_amplitude: The min_roll_amplitude of this ShipDesignAnalysisSBM.  # noqa: E501
        :type: DimensionalAngle
        """

        self._min_roll_amplitude = min_roll_amplitude

    @property
    def heave_amplitude(self):
        """Gets the heave_amplitude of this ShipDesignAnalysisSBM.  # noqa: E501


        :return: The heave_amplitude of this ShipDesignAnalysisSBM.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._heave_amplitude

    @heave_amplitude.setter
    def heave_amplitude(self, heave_amplitude):
        """Sets the heave_amplitude of this ShipDesignAnalysisSBM.


        :param heave_amplitude: The heave_amplitude of this ShipDesignAnalysisSBM.  # noqa: E501
        :type: DimensionalLength
        """

        self._heave_amplitude = heave_amplitude

    @property
    def sway_amplitude(self):
        """Gets the sway_amplitude of this ShipDesignAnalysisSBM.  # noqa: E501


        :return: The sway_amplitude of this ShipDesignAnalysisSBM.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._sway_amplitude

    @sway_amplitude.setter
    def sway_amplitude(self, sway_amplitude):
        """Sets the sway_amplitude of this ShipDesignAnalysisSBM.


        :param sway_amplitude: The sway_amplitude of this ShipDesignAnalysisSBM.  # noqa: E501
        :type: DimensionalLength
        """

        self._sway_amplitude = sway_amplitude

    @property
    def damping_coefficient(self):
        """Gets the damping_coefficient of this ShipDesignAnalysisSBM.  # noqa: E501


        :return: The damping_coefficient of this ShipDesignAnalysisSBM.  # noqa: E501
        :rtype: float
        """
        return self._damping_coefficient

    @damping_coefficient.setter
    def damping_coefficient(self, damping_coefficient):
        """Sets the damping_coefficient of this ShipDesignAnalysisSBM.


        :param damping_coefficient: The damping_coefficient of this ShipDesignAnalysisSBM.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                damping_coefficient is not None and damping_coefficient < 0):  # noqa: E501
            raise ValueError("Invalid value for `damping_coefficient`, must be a value greater than or equal to `0`")  # noqa: E501

        self._damping_coefficient = damping_coefficient

    @property
    def time_period_for_liquid(self):
        """Gets the time_period_for_liquid of this ShipDesignAnalysisSBM.  # noqa: E501


        :return: The time_period_for_liquid of this ShipDesignAnalysisSBM.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._time_period_for_liquid

    @time_period_for_liquid.setter
    def time_period_for_liquid(self, time_period_for_liquid):
        """Sets the time_period_for_liquid of this ShipDesignAnalysisSBM.


        :param time_period_for_liquid: The time_period_for_liquid of this ShipDesignAnalysisSBM.  # noqa: E501
        :type: DimensionalTime
        """

        self._time_period_for_liquid = time_period_for_liquid

    @property
    def natural_period_of_ship(self):
        """Gets the natural_period_of_ship of this ShipDesignAnalysisSBM.  # noqa: E501


        :return: The natural_period_of_ship of this ShipDesignAnalysisSBM.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._natural_period_of_ship

    @natural_period_of_ship.setter
    def natural_period_of_ship(self, natural_period_of_ship):
        """Sets the natural_period_of_ship of this ShipDesignAnalysisSBM.


        :param natural_period_of_ship: The natural_period_of_ship of this ShipDesignAnalysisSBM.  # noqa: E501
        :type: DimensionalTime
        """

        self._natural_period_of_ship = natural_period_of_ship

    @property
    def reference_time_step(self):
        """Gets the reference_time_step of this ShipDesignAnalysisSBM.  # noqa: E501


        :return: The reference_time_step of this ShipDesignAnalysisSBM.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._reference_time_step

    @reference_time_step.setter
    def reference_time_step(self, reference_time_step):
        """Sets the reference_time_step of this ShipDesignAnalysisSBM.


        :param reference_time_step: The reference_time_step of this ShipDesignAnalysisSBM.  # noqa: E501
        :type: DimensionalTime
        """

        self._reference_time_step = reference_time_step

    @property
    def increase_in_liquid_per_time_step(self):
        """Gets the increase_in_liquid_per_time_step of this ShipDesignAnalysisSBM.  # noqa: E501


        :return: The increase_in_liquid_per_time_step of this ShipDesignAnalysisSBM.  # noqa: E501
        :rtype: float
        """
        return self._increase_in_liquid_per_time_step

    @increase_in_liquid_per_time_step.setter
    def increase_in_liquid_per_time_step(self, increase_in_liquid_per_time_step):
        """Sets the increase_in_liquid_per_time_step of this ShipDesignAnalysisSBM.


        :param increase_in_liquid_per_time_step: The increase_in_liquid_per_time_step of this ShipDesignAnalysisSBM.  # noqa: E501
        :type: float
        """

        self._increase_in_liquid_per_time_step = increase_in_liquid_per_time_step

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
        if not isinstance(other, ShipDesignAnalysisSBM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShipDesignAnalysisSBM):
            return True

        return self.to_dict() != other.to_dict()
