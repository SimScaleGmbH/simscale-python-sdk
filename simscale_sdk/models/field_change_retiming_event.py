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


class FieldChangeRetimingEvent(object):
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
        'field_selection': 'OneOfFieldChangeRetimingEventFieldSelection',
        'threshold_value': 'float',
        'timestep_calculation_type': 'OneOfFieldChangeRetimingEventTimestepCalculationType'
    }

    attribute_map = {
        'type': 'type',
        'field_selection': 'fieldSelection',
        'threshold_value': 'thresholdValue',
        'timestep_calculation_type': 'timestepCalculationType'
    }

    def __init__(self, type='FIELD_CHANGE', field_selection=None, threshold_value=None, timestep_calculation_type=None, local_vars_configuration=None):  # noqa: E501
        """FieldChangeRetimingEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._field_selection = None
        self._threshold_value = None
        self._timestep_calculation_type = None
        self.discriminator = None

        self.type = type
        if field_selection is not None:
            self.field_selection = field_selection
        if threshold_value is not None:
            self.threshold_value = threshold_value
        if timestep_calculation_type is not None:
            self.timestep_calculation_type = timestep_calculation_type

    @property
    def type(self):
        """Gets the type of this FieldChangeRetimingEvent.  # noqa: E501

        <p>Select the event for the time step adaptation. Currently there are four different events possible that trigger a time step adaptation:</p><ul><li><p><b>Error</b>: This is the case of a general error like for example non-convergence or singular matrix errors.</p></ul><ul><li><p><b>Collision</b>: This event is triggered if in a computation with physical contact a contact state change from open to closed is noticed. This time step adaptation is especially useful in dynamics to reduce the effect of artificial oscillations due to inexact collision detection.</p></ul><ul><li><p><b>Field Change</b>: The user can define the maximum delta that a field is allowed to change within one time step, if the defined threshold is exceeded the time step is adapted. This time stepping criteria is especially useful to capture material nonlinearitier more exact.</p></ul><ul><li><p><b>Non-monotonous residual</b>: This event is triggered if the residual has not been reduced within three iterations . This criteria is mostly used to reduce runtime by detecting diverging time steps before reaching the maximum number of allowed newton iterations.</p></ul>  Schema name: FieldChangeRetimingEvent  # noqa: E501

        :return: The type of this FieldChangeRetimingEvent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FieldChangeRetimingEvent.

        <p>Select the event for the time step adaptation. Currently there are four different events possible that trigger a time step adaptation:</p><ul><li><p><b>Error</b>: This is the case of a general error like for example non-convergence or singular matrix errors.</p></ul><ul><li><p><b>Collision</b>: This event is triggered if in a computation with physical contact a contact state change from open to closed is noticed. This time step adaptation is especially useful in dynamics to reduce the effect of artificial oscillations due to inexact collision detection.</p></ul><ul><li><p><b>Field Change</b>: The user can define the maximum delta that a field is allowed to change within one time step, if the defined threshold is exceeded the time step is adapted. This time stepping criteria is especially useful to capture material nonlinearitier more exact.</p></ul><ul><li><p><b>Non-monotonous residual</b>: This event is triggered if the residual has not been reduced within three iterations . This criteria is mostly used to reduce runtime by detecting diverging time steps before reaching the maximum number of allowed newton iterations.</p></ul>  Schema name: FieldChangeRetimingEvent  # noqa: E501

        :param type: The type of this FieldChangeRetimingEvent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def field_selection(self):
        """Gets the field_selection of this FieldChangeRetimingEvent.  # noqa: E501


        :return: The field_selection of this FieldChangeRetimingEvent.  # noqa: E501
        :rtype: OneOfFieldChangeRetimingEventFieldSelection
        """
        return self._field_selection

    @field_selection.setter
    def field_selection(self, field_selection):
        """Sets the field_selection of this FieldChangeRetimingEvent.


        :param field_selection: The field_selection of this FieldChangeRetimingEvent.  # noqa: E501
        :type: OneOfFieldChangeRetimingEventFieldSelection
        """

        self._field_selection = field_selection

    @property
    def threshold_value(self):
        """Gets the threshold_value of this FieldChangeRetimingEvent.  # noqa: E501

        <p>This value defines the maximum allowed change of the defined target field component within each time increment. If this threshold is exceeded the time step is adapted according to the selected settings in the *Timestep Calculation Type*.</p>  # noqa: E501

        :return: The threshold_value of this FieldChangeRetimingEvent.  # noqa: E501
        :rtype: float
        """
        return self._threshold_value

    @threshold_value.setter
    def threshold_value(self, threshold_value):
        """Sets the threshold_value of this FieldChangeRetimingEvent.

        <p>This value defines the maximum allowed change of the defined target field component within each time increment. If this threshold is exceeded the time step is adapted according to the selected settings in the *Timestep Calculation Type*.</p>  # noqa: E501

        :param threshold_value: The threshold_value of this FieldChangeRetimingEvent.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                threshold_value is not None and threshold_value < 0):  # noqa: E501
            raise ValueError("Invalid value for `threshold_value`, must be a value greater than or equal to `0`")  # noqa: E501

        self._threshold_value = threshold_value

    @property
    def timestep_calculation_type(self):
        """Gets the timestep_calculation_type of this FieldChangeRetimingEvent.  # noqa: E501


        :return: The timestep_calculation_type of this FieldChangeRetimingEvent.  # noqa: E501
        :rtype: OneOfFieldChangeRetimingEventTimestepCalculationType
        """
        return self._timestep_calculation_type

    @timestep_calculation_type.setter
    def timestep_calculation_type(self, timestep_calculation_type):
        """Sets the timestep_calculation_type of this FieldChangeRetimingEvent.


        :param timestep_calculation_type: The timestep_calculation_type of this FieldChangeRetimingEvent.  # noqa: E501
        :type: OneOfFieldChangeRetimingEventTimestepCalculationType
        """

        self._timestep_calculation_type = timestep_calculation_type

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
        if not isinstance(other, FieldChangeRetimingEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FieldChangeRetimingEvent):
            return True

        return self.to_dict() != other.to_dict()
