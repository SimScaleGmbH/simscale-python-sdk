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


class OneOfStaticAnalysisConnectors(object):
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
        'topological_reference': 'TopologicalReference',
        'bolt_type': 'str',
        'shank_diameter': 'DimensionalLength',
        'mechanical_properties': 'BoltMechanicalProperties',
        'enable_bolt_preload': 'bool',
        'preload': 'ForcePreload',
        'advanced_bolt_settings': 'AdvancedConnectorSettings',
        'master_topological_reference': 'TopologicalReference',
        'slave_topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'interaction': 'interaction',
        'kinematic_behavior': 'kinematicBehavior',
        'advanced_pin_settings': 'advancedPinSettings',
        'topological_reference': 'topologicalReference',
        'bolt_type': 'boltType',
        'shank_diameter': 'shankDiameter',
        'mechanical_properties': 'mechanicalProperties',
        'enable_bolt_preload': 'enableBoltPreload',
        'preload': 'preload',
        'advanced_bolt_settings': 'advancedBoltSettings',
        'master_topological_reference': 'masterTopologicalReference',
        'slave_topological_reference': 'slaveTopologicalReference'
    }

    discriminator_value_class_map = {
        'PIN_CONNECTOR': 'PinConnector',
        'BOLT_CONNECTOR': 'BoltConnector'
    }

    def __init__(self, type='BOLT_CONNECTOR', name=None, interaction=None, kinematic_behavior=None, advanced_pin_settings=None, topological_reference=None, bolt_type=None, shank_diameter=None, mechanical_properties=None, enable_bolt_preload=None, preload=None, advanced_bolt_settings=None, master_topological_reference=None, slave_topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """OneOfStaticAnalysisConnectors - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._interaction = None
        self._kinematic_behavior = None
        self._advanced_pin_settings = None
        self._topological_reference = None
        self._bolt_type = None
        self._shank_diameter = None
        self._mechanical_properties = None
        self._enable_bolt_preload = None
        self._preload = None
        self._advanced_bolt_settings = None
        self._master_topological_reference = None
        self._slave_topological_reference = None
        self.discriminator = 'type'

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
        if bolt_type is not None:
            self.bolt_type = bolt_type
        if shank_diameter is not None:
            self.shank_diameter = shank_diameter
        if mechanical_properties is not None:
            self.mechanical_properties = mechanical_properties
        if enable_bolt_preload is not None:
            self.enable_bolt_preload = enable_bolt_preload
        if preload is not None:
            self.preload = preload
        if advanced_bolt_settings is not None:
            self.advanced_bolt_settings = advanced_bolt_settings
        if master_topological_reference is not None:
            self.master_topological_reference = master_topological_reference
        if slave_topological_reference is not None:
            self.slave_topological_reference = slave_topological_reference

    @property
    def type(self):
        """Gets the type of this OneOfStaticAnalysisConnectors.  # noqa: E501

        <p>Connect multiple bodies via a virtual bolt <br /><br /><b>Usage</b>: <br /><ul><li>Define a separate bolt connector item for each virtual bolt</li><li>Assign entities must be coaxial</li></ul><b>Behavior</b>:<br /><ul><li>Bolt connectors mimic physical bolts using beam formulations. Relative translations and rotations of the connected entities are computed based on the defined bolt mechanical properties</li><li>Ability to apply preload</li></ul></p>  Schema name: BoltConnector  # noqa: E501

        :return: The type of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfStaticAnalysisConnectors.

        <p>Connect multiple bodies via a virtual bolt <br /><br /><b>Usage</b>: <br /><ul><li>Define a separate bolt connector item for each virtual bolt</li><li>Assign entities must be coaxial</li></ul><b>Behavior</b>:<br /><ul><li>Bolt connectors mimic physical bolts using beam formulations. Relative translations and rotations of the connected entities are computed based on the defined bolt mechanical properties</li><li>Ability to apply preload</li></ul></p>  Schema name: BoltConnector  # noqa: E501

        :param type: The type of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this OneOfStaticAnalysisConnectors.  # noqa: E501


        :return: The name of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfStaticAnalysisConnectors.


        :param name: The name of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def interaction(self):
        """Gets the interaction of this OneOfStaticAnalysisConnectors.  # noqa: E501

        <p>Select an interaction option<br /><ul><li><b>Body to body</b> - Two or more bodies may be connected to each other via a single virtual pin. The pin will move with the bodies.</li><li><b>Body to ground</b> - Two or more bodies may be connected to the ground via a single virtual pin. The pin remains stationary.</li></ul></p>  # noqa: E501

        :return: The interaction of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :rtype: str
        """
        return self._interaction

    @interaction.setter
    def interaction(self, interaction):
        """Sets the interaction of this OneOfStaticAnalysisConnectors.

        <p>Select an interaction option<br /><ul><li><b>Body to body</b> - Two or more bodies may be connected to each other via a single virtual pin. The pin will move with the bodies.</li><li><b>Body to ground</b> - Two or more bodies may be connected to the ground via a single virtual pin. The pin remains stationary.</li></ul></p>  # noqa: E501

        :param interaction: The interaction of this OneOfStaticAnalysisConnectors.  # noqa: E501
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
        """Gets the kinematic_behavior of this OneOfStaticAnalysisConnectors.  # noqa: E501


        :return: The kinematic_behavior of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :rtype: PinKinematicBehavior
        """
        return self._kinematic_behavior

    @kinematic_behavior.setter
    def kinematic_behavior(self, kinematic_behavior):
        """Sets the kinematic_behavior of this OneOfStaticAnalysisConnectors.


        :param kinematic_behavior: The kinematic_behavior of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :type: PinKinematicBehavior
        """

        self._kinematic_behavior = kinematic_behavior

    @property
    def advanced_pin_settings(self):
        """Gets the advanced_pin_settings of this OneOfStaticAnalysisConnectors.  # noqa: E501


        :return: The advanced_pin_settings of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :rtype: AdvancedConnectorSettings
        """
        return self._advanced_pin_settings

    @advanced_pin_settings.setter
    def advanced_pin_settings(self, advanced_pin_settings):
        """Sets the advanced_pin_settings of this OneOfStaticAnalysisConnectors.


        :param advanced_pin_settings: The advanced_pin_settings of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :type: AdvancedConnectorSettings
        """

        self._advanced_pin_settings = advanced_pin_settings

    @property
    def topological_reference(self):
        """Gets the topological_reference of this OneOfStaticAnalysisConnectors.  # noqa: E501


        :return: The topological_reference of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this OneOfStaticAnalysisConnectors.


        :param topological_reference: The topological_reference of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def bolt_type(self):
        """Gets the bolt_type of this OneOfStaticAnalysisConnectors.  # noqa: E501

        <p>Select your desired type of fastener<br /><br /><ul><li><b>Bolt and nut</b> - a virtual connection between a bolt head and nut location</li><li><b>Screw</b> - a virtual connection between a screw head location and a cylindrical surface representing a threaded section</li></ul></p>  # noqa: E501

        :return: The bolt_type of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :rtype: str
        """
        return self._bolt_type

    @bolt_type.setter
    def bolt_type(self, bolt_type):
        """Sets the bolt_type of this OneOfStaticAnalysisConnectors.

        <p>Select your desired type of fastener<br /><br /><ul><li><b>Bolt and nut</b> - a virtual connection between a bolt head and nut location</li><li><b>Screw</b> - a virtual connection between a screw head location and a cylindrical surface representing a threaded section</li></ul></p>  # noqa: E501

        :param bolt_type: The bolt_type of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :type: str
        """
        allowed_values = ["BOLT_AND_NUT", "SCREW"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and bolt_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `bolt_type` ({0}), must be one of {1}"  # noqa: E501
                .format(bolt_type, allowed_values)
            )

        self._bolt_type = bolt_type

    @property
    def shank_diameter(self):
        """Gets the shank_diameter of this OneOfStaticAnalysisConnectors.  # noqa: E501


        :return: The shank_diameter of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._shank_diameter

    @shank_diameter.setter
    def shank_diameter(self, shank_diameter):
        """Sets the shank_diameter of this OneOfStaticAnalysisConnectors.


        :param shank_diameter: The shank_diameter of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :type: DimensionalLength
        """

        self._shank_diameter = shank_diameter

    @property
    def mechanical_properties(self):
        """Gets the mechanical_properties of this OneOfStaticAnalysisConnectors.  # noqa: E501


        :return: The mechanical_properties of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :rtype: BoltMechanicalProperties
        """
        return self._mechanical_properties

    @mechanical_properties.setter
    def mechanical_properties(self, mechanical_properties):
        """Sets the mechanical_properties of this OneOfStaticAnalysisConnectors.


        :param mechanical_properties: The mechanical_properties of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :type: BoltMechanicalProperties
        """

        self._mechanical_properties = mechanical_properties

    @property
    def enable_bolt_preload(self):
        """Gets the enable_bolt_preload of this OneOfStaticAnalysisConnectors.  # noqa: E501

        Enable the definition of pretension within the virtual bolt.  # noqa: E501

        :return: The enable_bolt_preload of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :rtype: bool
        """
        return self._enable_bolt_preload

    @enable_bolt_preload.setter
    def enable_bolt_preload(self, enable_bolt_preload):
        """Sets the enable_bolt_preload of this OneOfStaticAnalysisConnectors.

        Enable the definition of pretension within the virtual bolt.  # noqa: E501

        :param enable_bolt_preload: The enable_bolt_preload of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :type: bool
        """

        self._enable_bolt_preload = enable_bolt_preload

    @property
    def preload(self):
        """Gets the preload of this OneOfStaticAnalysisConnectors.  # noqa: E501


        :return: The preload of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :rtype: ForcePreload
        """
        return self._preload

    @preload.setter
    def preload(self, preload):
        """Sets the preload of this OneOfStaticAnalysisConnectors.


        :param preload: The preload of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :type: ForcePreload
        """

        self._preload = preload

    @property
    def advanced_bolt_settings(self):
        """Gets the advanced_bolt_settings of this OneOfStaticAnalysisConnectors.  # noqa: E501


        :return: The advanced_bolt_settings of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :rtype: AdvancedConnectorSettings
        """
        return self._advanced_bolt_settings

    @advanced_bolt_settings.setter
    def advanced_bolt_settings(self, advanced_bolt_settings):
        """Sets the advanced_bolt_settings of this OneOfStaticAnalysisConnectors.


        :param advanced_bolt_settings: The advanced_bolt_settings of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :type: AdvancedConnectorSettings
        """

        self._advanced_bolt_settings = advanced_bolt_settings

    @property
    def master_topological_reference(self):
        """Gets the master_topological_reference of this OneOfStaticAnalysisConnectors.  # noqa: E501


        :return: The master_topological_reference of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._master_topological_reference

    @master_topological_reference.setter
    def master_topological_reference(self, master_topological_reference):
        """Sets the master_topological_reference of this OneOfStaticAnalysisConnectors.


        :param master_topological_reference: The master_topological_reference of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :type: TopologicalReference
        """

        self._master_topological_reference = master_topological_reference

    @property
    def slave_topological_reference(self):
        """Gets the slave_topological_reference of this OneOfStaticAnalysisConnectors.  # noqa: E501


        :return: The slave_topological_reference of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._slave_topological_reference

    @slave_topological_reference.setter
    def slave_topological_reference(self, slave_topological_reference):
        """Sets the slave_topological_reference of this OneOfStaticAnalysisConnectors.


        :param slave_topological_reference: The slave_topological_reference of this OneOfStaticAnalysisConnectors.  # noqa: E501
        :type: TopologicalReference
        """

        self._slave_topological_reference = slave_topological_reference

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
        if not isinstance(other, OneOfStaticAnalysisConnectors):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfStaticAnalysisConnectors):
            return True

        return self.to_dict() != other.to_dict()
