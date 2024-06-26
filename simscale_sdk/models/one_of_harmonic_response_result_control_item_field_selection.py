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


class OneOfHarmonicResponseResultControlItemFieldSelection(object):
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
        'displacement_type': 'OneOfDisplacementFieldSelectionDisplacementType',
        'component_selection': 'str',
        'output_method': 'str',
        'strain_type': 'OneOfStrainFieldSelectionStrainType',
        'stress_type': 'OneOfStressFieldSelectionStressType',
        'velocity_type': 'OneOfVelocityFieldSelectionVelocityType',
        'acceleration_type': 'OneOfAccelerationFieldSelectionAccelerationType'
    }

    attribute_map = {
        'type': 'type',
        'displacement_type': 'displacementType',
        'component_selection': 'componentSelection',
        'output_method': 'outputMethod',
        'strain_type': 'strainType',
        'stress_type': 'stressType',
        'velocity_type': 'velocityType',
        'acceleration_type': 'accelerationType'
    }

    discriminator_value_class_map = {
        'DISPLACEMENT': 'DisplacementFieldSelection',
        'STRAIN': 'StrainFieldSelection',
        'STRESS': 'StressFieldSelection',
        'VELOCITY': 'VelocityFieldSelection',
        'ACCELERATION': 'AccelerationFieldSelection'
    }

    def __init__(self, type='ACCELERATION', displacement_type=None, component_selection=None, output_method=None, strain_type=None, stress_type=None, velocity_type=None, acceleration_type=None, local_vars_configuration=None):  # noqa: E501
        """OneOfHarmonicResponseResultControlItemFieldSelection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._displacement_type = None
        self._component_selection = None
        self._output_method = None
        self._strain_type = None
        self._stress_type = None
        self._velocity_type = None
        self._acceleration_type = None
        self.discriminator = 'type'

        self.type = type
        if displacement_type is not None:
            self.displacement_type = displacement_type
        if component_selection is not None:
            self.component_selection = component_selection
        if output_method is not None:
            self.output_method = output_method
        if strain_type is not None:
            self.strain_type = strain_type
        if stress_type is not None:
            self.stress_type = stress_type
        if velocity_type is not None:
            self.velocity_type = velocity_type
        if acceleration_type is not None:
            self.acceleration_type = acceleration_type

    @property
    def type(self):
        """Gets the type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501

        Schema name: AccelerationFieldSelection  # noqa: E501

        :return: The type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfHarmonicResponseResultControlItemFieldSelection.

        Schema name: AccelerationFieldSelection  # noqa: E501

        :param type: The type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def displacement_type(self):
        """Gets the displacement_type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501


        :return: The displacement_type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501
        :rtype: OneOfDisplacementFieldSelectionDisplacementType
        """
        return self._displacement_type

    @displacement_type.setter
    def displacement_type(self, displacement_type):
        """Sets the displacement_type of this OneOfHarmonicResponseResultControlItemFieldSelection.


        :param displacement_type: The displacement_type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501
        :type: OneOfDisplacementFieldSelectionDisplacementType
        """

        self._displacement_type = displacement_type

    @property
    def component_selection(self):
        """Gets the component_selection of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501


        :return: The component_selection of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501
        :rtype: str
        """
        return self._component_selection

    @component_selection.setter
    def component_selection(self, component_selection):
        """Sets the component_selection of this OneOfHarmonicResponseResultControlItemFieldSelection.


        :param component_selection: The component_selection of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501
        :type: str
        """
        allowed_values = ["X", "Y", "Z", "ALL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and component_selection not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `component_selection` ({0}), must be one of {1}"  # noqa: E501
                .format(component_selection, allowed_values)
            )

        self._component_selection = component_selection

    @property
    def output_method(self):
        """Gets the output_method of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501

        <p>This option allows to control the output frequency and accuracy:</p><ul><li><p><b>Post simulation:</b> Point data output is synchronised with global solution fields. Data is interpolated from nodes surrounding the geometry primitive.</p></ul><ul><li><p><b>Live:</b> Point data is output continuously during the simulation at all computed timesteps. Data is taken directly from the nearest mesh node and no interpolation is performed.</p></ul>  # noqa: E501

        :return: The output_method of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501
        :rtype: str
        """
        return self._output_method

    @output_method.setter
    def output_method(self, output_method):
        """Sets the output_method of this OneOfHarmonicResponseResultControlItemFieldSelection.

        <p>This option allows to control the output frequency and accuracy:</p><ul><li><p><b>Post simulation:</b> Point data output is synchronised with global solution fields. Data is interpolated from nodes surrounding the geometry primitive.</p></ul><ul><li><p><b>Live:</b> Point data is output continuously during the simulation at all computed timesteps. Data is taken directly from the nearest mesh node and no interpolation is performed.</p></ul>  # noqa: E501

        :param output_method: The output_method of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501
        :type: str
        """
        allowed_values = ["POST_SIMULATION", "LIVE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and output_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `output_method` ({0}), must be one of {1}"  # noqa: E501
                .format(output_method, allowed_values)
            )

        self._output_method = output_method

    @property
    def strain_type(self):
        """Gets the strain_type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501


        :return: The strain_type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501
        :rtype: OneOfStrainFieldSelectionStrainType
        """
        return self._strain_type

    @strain_type.setter
    def strain_type(self, strain_type):
        """Sets the strain_type of this OneOfHarmonicResponseResultControlItemFieldSelection.


        :param strain_type: The strain_type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501
        :type: OneOfStrainFieldSelectionStrainType
        """

        self._strain_type = strain_type

    @property
    def stress_type(self):
        """Gets the stress_type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501


        :return: The stress_type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501
        :rtype: OneOfStressFieldSelectionStressType
        """
        return self._stress_type

    @stress_type.setter
    def stress_type(self, stress_type):
        """Sets the stress_type of this OneOfHarmonicResponseResultControlItemFieldSelection.


        :param stress_type: The stress_type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501
        :type: OneOfStressFieldSelectionStressType
        """

        self._stress_type = stress_type

    @property
    def velocity_type(self):
        """Gets the velocity_type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501


        :return: The velocity_type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501
        :rtype: OneOfVelocityFieldSelectionVelocityType
        """
        return self._velocity_type

    @velocity_type.setter
    def velocity_type(self, velocity_type):
        """Sets the velocity_type of this OneOfHarmonicResponseResultControlItemFieldSelection.


        :param velocity_type: The velocity_type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501
        :type: OneOfVelocityFieldSelectionVelocityType
        """

        self._velocity_type = velocity_type

    @property
    def acceleration_type(self):
        """Gets the acceleration_type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501


        :return: The acceleration_type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501
        :rtype: OneOfAccelerationFieldSelectionAccelerationType
        """
        return self._acceleration_type

    @acceleration_type.setter
    def acceleration_type(self, acceleration_type):
        """Sets the acceleration_type of this OneOfHarmonicResponseResultControlItemFieldSelection.


        :param acceleration_type: The acceleration_type of this OneOfHarmonicResponseResultControlItemFieldSelection.  # noqa: E501
        :type: OneOfAccelerationFieldSelectionAccelerationType
        """

        self._acceleration_type = acceleration_type

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
        if not isinstance(other, OneOfHarmonicResponseResultControlItemFieldSelection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfHarmonicResponseResultControlItemFieldSelection):
            return True

        return self.to_dict() != other.to_dict()
