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


class PinConnector(object):
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
        'interaction': 'str',
        'kinematic_behavior': 'PinKinematicBehavior',
        'advanced_pin_settings': 'AdvancedConnectorSettings',
        'topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'interaction': 'interaction',
        'kinematic_behavior': 'kinematicBehavior',
        'advanced_pin_settings': 'advancedPinSettings',
        'topological_reference': 'topologicalReference'
    }

    def __init__(self, type='PIN_CONNECTOR', name=None, interaction=None, kinematic_behavior=None, advanced_pin_settings=None, topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """PinConnector - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._interaction = None
        self._kinematic_behavior = None
        self._advanced_pin_settings = None
        self._topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if interaction is not None:
            self.interaction = interaction
        if kinematic_behavior is not None:
            self.kinematic_behavior = kinematic_behavior
        if advanced_pin_settings is not None:
            self.advanced_pin_settings = advanced_pin_settings
        if topological_reference is not None:
            self.topological_reference = topological_reference

    @property
    def type(self):
        """Gets the type of this PinConnector.  # noqa: E501

        <p>Connect multiple bodies via a virtual pin <br /><br /><b>Usage</b>: <br /><ul><li>Define a separate pin connector item for each virtual pin</li><li>Assign only cylindrical surfaces</li></ul><b>Behavior</b>:<br /><ul><li>Option to connect bodies to bodies or bodies to the ground via virtual pins</li><li>Bodies freely rotate relative to one another about the virtual pin axis</li><li>Users have full control over axial translation and rotation of the connection with the ability to define torsional and axial spring stiffness</li></ul></p>  Schema name: PinConnector  # noqa: E501

        :return: The type of this PinConnector.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PinConnector.

        <p>Connect multiple bodies via a virtual pin <br /><br /><b>Usage</b>: <br /><ul><li>Define a separate pin connector item for each virtual pin</li><li>Assign only cylindrical surfaces</li></ul><b>Behavior</b>:<br /><ul><li>Option to connect bodies to bodies or bodies to the ground via virtual pins</li><li>Bodies freely rotate relative to one another about the virtual pin axis</li><li>Users have full control over axial translation and rotation of the connection with the ability to define torsional and axial spring stiffness</li></ul></p>  Schema name: PinConnector  # noqa: E501

        :param type: The type of this PinConnector.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this PinConnector.  # noqa: E501


        :return: The name of this PinConnector.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PinConnector.


        :param name: The name of this PinConnector.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def interaction(self):
        """Gets the interaction of this PinConnector.  # noqa: E501

        <p>Select an interaction option<br /><ul><li><b>Body to body</b> - Two or more bodies may be connected to each other via a single virtual pin. The pin will move with the bodies.</li><li><b>Body to ground</b> - Two or more bodies may be connected to the ground via a single virtual pin. The pin remains stationary.</li></ul></p>  # noqa: E501

        :return: The interaction of this PinConnector.  # noqa: E501
        :rtype: str
        """
        return self._interaction

    @interaction.setter
    def interaction(self, interaction):
        """Sets the interaction of this PinConnector.

        <p>Select an interaction option<br /><ul><li><b>Body to body</b> - Two or more bodies may be connected to each other via a single virtual pin. The pin will move with the bodies.</li><li><b>Body to ground</b> - Two or more bodies may be connected to the ground via a single virtual pin. The pin remains stationary.</li></ul></p>  # noqa: E501

        :param interaction: The interaction of this PinConnector.  # noqa: E501
        :type: str
        """
        allowed_values = ["BODY_TO_BODY", "BODY_TO_GROUND"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and interaction not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `interaction` ({0}), must be one of {1}"  # noqa: E501
                .format(interaction, allowed_values)
            )

        self._interaction = interaction

    @property
    def kinematic_behavior(self):
        """Gets the kinematic_behavior of this PinConnector.  # noqa: E501


        :return: The kinematic_behavior of this PinConnector.  # noqa: E501
        :rtype: PinKinematicBehavior
        """
        return self._kinematic_behavior

    @kinematic_behavior.setter
    def kinematic_behavior(self, kinematic_behavior):
        """Sets the kinematic_behavior of this PinConnector.


        :param kinematic_behavior: The kinematic_behavior of this PinConnector.  # noqa: E501
        :type: PinKinematicBehavior
        """

        self._kinematic_behavior = kinematic_behavior

    @property
    def advanced_pin_settings(self):
        """Gets the advanced_pin_settings of this PinConnector.  # noqa: E501


        :return: The advanced_pin_settings of this PinConnector.  # noqa: E501
        :rtype: AdvancedConnectorSettings
        """
        return self._advanced_pin_settings

    @advanced_pin_settings.setter
    def advanced_pin_settings(self, advanced_pin_settings):
        """Sets the advanced_pin_settings of this PinConnector.


        :param advanced_pin_settings: The advanced_pin_settings of this PinConnector.  # noqa: E501
        :type: AdvancedConnectorSettings
        """

        self._advanced_pin_settings = advanced_pin_settings

    @property
    def topological_reference(self):
        """Gets the topological_reference of this PinConnector.  # noqa: E501


        :return: The topological_reference of this PinConnector.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this PinConnector.


        :param topological_reference: The topological_reference of this PinConnector.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

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
        if not isinstance(other, PinConnector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PinConnector):
            return True

        return self.to_dict() != other.to_dict()
