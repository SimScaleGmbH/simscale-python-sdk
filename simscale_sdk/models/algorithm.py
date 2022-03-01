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


class Algorithm(object):
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
        'sizing': 'OneOfHexDominantSnappySizing',
        'refinements': 'list[OneOfHexDominantSnappyRefinements]',
        'cell_zones': 'list[SimmetrixCellZones]',
        'automatic_layer_settings': 'OneOfSimmetrixMeshingFluidAutomaticLayerSettings',
        'physics_based_meshing': 'bool',
        'hex_core': 'bool',
        'num_of_processors': 'int',
        'advanced_simmetrix_settings': 'AdvancedSimmetrixSolidSettings',
        'second_order': 'bool',
        'enable_shell_meshing': 'bool',
        'surface_element_type': 'str',
        'meshing_mode': 'str'
    }

    attribute_map = {
        'type': 'type',
        'sizing': 'sizing',
        'refinements': 'refinements',
        'cell_zones': 'cellZones',
        'automatic_layer_settings': 'automaticLayerSettings',
        'physics_based_meshing': 'physicsBasedMeshing',
        'hex_core': 'hexCore',
        'num_of_processors': 'numOfProcessors',
        'advanced_simmetrix_settings': 'advancedSimmetrixSettings',
        'second_order': 'secondOrder',
        'enable_shell_meshing': 'enableShellMeshing',
        'surface_element_type': 'surfaceElementType',
        'meshing_mode': 'meshingMode'
    }

    discriminator_value_class_map = {
        'SIMMETRIX_MESHING_FLUID_V16': 'SimmetrixMeshingFluid',
        'SIMMETRIX_MESHING_SOLID': 'SimmetrixMeshingSolid',
        'HEX_DOMINANT_SNAPPY_V5': 'HexDominantSnappy'
    }

    def __init__(self, type='HEX_DOMINANT_SNAPPY_V5', sizing=None, refinements=None, cell_zones=None, automatic_layer_settings=None, physics_based_meshing=None, hex_core=None, num_of_processors=None, advanced_simmetrix_settings=None, second_order=None, enable_shell_meshing=None, surface_element_type=None, meshing_mode=None, local_vars_configuration=None):  # noqa: E501
        """Algorithm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._sizing = None
        self._refinements = None
        self._cell_zones = None
        self._automatic_layer_settings = None
        self._physics_based_meshing = None
        self._hex_core = None
        self._num_of_processors = None
        self._advanced_simmetrix_settings = None
        self._second_order = None
        self._enable_shell_meshing = None
        self._surface_element_type = None
        self._meshing_mode = None
        self.discriminator = 'type'

        self.type = type
        if sizing is not None:
            self.sizing = sizing
        if refinements is not None:
            self.refinements = refinements
        if cell_zones is not None:
            self.cell_zones = cell_zones
        if automatic_layer_settings is not None:
            self.automatic_layer_settings = automatic_layer_settings
        if physics_based_meshing is not None:
            self.physics_based_meshing = physics_based_meshing
        if hex_core is not None:
            self.hex_core = hex_core
        if num_of_processors is not None:
            self.num_of_processors = num_of_processors
        if advanced_simmetrix_settings is not None:
            self.advanced_simmetrix_settings = advanced_simmetrix_settings
        if second_order is not None:
            self.second_order = second_order
        if enable_shell_meshing is not None:
            self.enable_shell_meshing = enable_shell_meshing
        if surface_element_type is not None:
            self.surface_element_type = surface_element_type
        if meshing_mode is not None:
            self.meshing_mode = meshing_mode

    @property
    def type(self):
        """Gets the type of this Algorithm.  # noqa: E501

        Schema name: HexDominantSnappy  # noqa: E501

        :return: The type of this Algorithm.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Algorithm.

        Schema name: HexDominantSnappy  # noqa: E501

        :param type: The type of this Algorithm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def sizing(self):
        """Gets the sizing of this Algorithm.  # noqa: E501


        :return: The sizing of this Algorithm.  # noqa: E501
        :rtype: OneOfHexDominantSnappySizing
        """
        return self._sizing

    @sizing.setter
    def sizing(self, sizing):
        """Sets the sizing of this Algorithm.


        :param sizing: The sizing of this Algorithm.  # noqa: E501
        :type: OneOfHexDominantSnappySizing
        """

        self._sizing = sizing

    @property
    def refinements(self):
        """Gets the refinements of this Algorithm.  # noqa: E501


        :return: The refinements of this Algorithm.  # noqa: E501
        :rtype: list[OneOfHexDominantSnappyRefinements]
        """
        return self._refinements

    @refinements.setter
    def refinements(self, refinements):
        """Sets the refinements of this Algorithm.


        :param refinements: The refinements of this Algorithm.  # noqa: E501
        :type: list[OneOfHexDominantSnappyRefinements]
        """

        self._refinements = refinements

    @property
    def cell_zones(self):
        """Gets the cell_zones of this Algorithm.  # noqa: E501


        :return: The cell_zones of this Algorithm.  # noqa: E501
        :rtype: list[SimmetrixCellZones]
        """
        return self._cell_zones

    @cell_zones.setter
    def cell_zones(self, cell_zones):
        """Sets the cell_zones of this Algorithm.


        :param cell_zones: The cell_zones of this Algorithm.  # noqa: E501
        :type: list[SimmetrixCellZones]
        """

        self._cell_zones = cell_zones

    @property
    def automatic_layer_settings(self):
        """Gets the automatic_layer_settings of this Algorithm.  # noqa: E501


        :return: The automatic_layer_settings of this Algorithm.  # noqa: E501
        :rtype: OneOfSimmetrixMeshingFluidAutomaticLayerSettings
        """
        return self._automatic_layer_settings

    @automatic_layer_settings.setter
    def automatic_layer_settings(self, automatic_layer_settings):
        """Sets the automatic_layer_settings of this Algorithm.


        :param automatic_layer_settings: The automatic_layer_settings of this Algorithm.  # noqa: E501
        :type: OneOfSimmetrixMeshingFluidAutomaticLayerSettings
        """

        self._automatic_layer_settings = automatic_layer_settings

    @property
    def physics_based_meshing(self):
        """Gets the physics_based_meshing of this Algorithm.  # noqa: E501

        Physics-based meshing takes setup information like materials, boundary conditions, and source terms into account to size the mesh accordingly. When enabled, the following adaptations will be made:</p><ul><li>Refinements on inlets and outlets</li><li>Different sizing for solid and fluid regions in CHT simulations</li></ul> <br>When toggled on users don’t have to worry about creating a <a href='https://www.simscale.com/docs/simulation-setup/simulation-control/' target='_blank'>separate cell zone</a>.  # noqa: E501

        :return: The physics_based_meshing of this Algorithm.  # noqa: E501
        :rtype: bool
        """
        return self._physics_based_meshing

    @physics_based_meshing.setter
    def physics_based_meshing(self, physics_based_meshing):
        """Sets the physics_based_meshing of this Algorithm.

        Physics-based meshing takes setup information like materials, boundary conditions, and source terms into account to size the mesh accordingly. When enabled, the following adaptations will be made:</p><ul><li>Refinements on inlets and outlets</li><li>Different sizing for solid and fluid regions in CHT simulations</li></ul> <br>When toggled on users don’t have to worry about creating a <a href='https://www.simscale.com/docs/simulation-setup/simulation-control/' target='_blank'>separate cell zone</a>.  # noqa: E501

        :param physics_based_meshing: The physics_based_meshing of this Algorithm.  # noqa: E501
        :type: bool
        """

        self._physics_based_meshing = physics_based_meshing

    @property
    def hex_core(self):
        """Gets the hex_core of this Algorithm.  # noqa: E501

        <p>If <a href='https://www.simscale.com/docs/simulation-setup/meshing/standard/#hexcore' target='_blank'><b>Hex element core</b></a> is activated, the interior of the mesh gets covered by <a href='https://www.simscale.com/docs/simulation-setup/meshing/standard/#hexcore' target='_blank'><b>hexahedral elements</b></a>. The transition to the triangulated surface mesh is covered by tetrahedral and pyramid elements.<img src=\"/spec/resources/help/imgs/simmetrix-hexcore.png\" class=\"helpPopupImage\"/>Meshclip through a hex-core mesh.</p>  # noqa: E501

        :return: The hex_core of this Algorithm.  # noqa: E501
        :rtype: bool
        """
        return self._hex_core

    @hex_core.setter
    def hex_core(self, hex_core):
        """Sets the hex_core of this Algorithm.

        <p>If <a href='https://www.simscale.com/docs/simulation-setup/meshing/standard/#hexcore' target='_blank'><b>Hex element core</b></a> is activated, the interior of the mesh gets covered by <a href='https://www.simscale.com/docs/simulation-setup/meshing/standard/#hexcore' target='_blank'><b>hexahedral elements</b></a>. The transition to the triangulated surface mesh is covered by tetrahedral and pyramid elements.<img src=\"/spec/resources/help/imgs/simmetrix-hexcore.png\" class=\"helpPopupImage\"/>Meshclip through a hex-core mesh.</p>  # noqa: E501

        :param hex_core: The hex_core of this Algorithm.  # noqa: E501
        :type: bool
        """

        self._hex_core = hex_core

    @property
    def num_of_processors(self):
        """Gets the num_of_processors of this Algorithm.  # noqa: E501

        <p>Selecting more processor cores might speed up the meshing process. Choosing a smaller computation instance will save core hours. <a href='https://www.simscale.com/docs/simulation-setup/meshing/#number-of-processors' target='_blank'>Learn more</a>.</p>  # noqa: E501

        :return: The num_of_processors of this Algorithm.  # noqa: E501
        :rtype: int
        """
        return self._num_of_processors

    @num_of_processors.setter
    def num_of_processors(self, num_of_processors):
        """Sets the num_of_processors of this Algorithm.

        <p>Selecting more processor cores might speed up the meshing process. Choosing a smaller computation instance will save core hours. <a href='https://www.simscale.com/docs/simulation-setup/meshing/#number-of-processors' target='_blank'>Learn more</a>.</p>  # noqa: E501

        :param num_of_processors: The num_of_processors of this Algorithm.  # noqa: E501
        :type: int
        """
        allowed_values = [-1, 4, 8, 16, 32, 64, 96]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and num_of_processors not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `num_of_processors` ({0}), must be one of {1}"  # noqa: E501
                .format(num_of_processors, allowed_values)
            )

        self._num_of_processors = num_of_processors

    @property
    def advanced_simmetrix_settings(self):
        """Gets the advanced_simmetrix_settings of this Algorithm.  # noqa: E501


        :return: The advanced_simmetrix_settings of this Algorithm.  # noqa: E501
        :rtype: AdvancedSimmetrixSolidSettings
        """
        return self._advanced_simmetrix_settings

    @advanced_simmetrix_settings.setter
    def advanced_simmetrix_settings(self, advanced_simmetrix_settings):
        """Sets the advanced_simmetrix_settings of this Algorithm.


        :param advanced_simmetrix_settings: The advanced_simmetrix_settings of this Algorithm.  # noqa: E501
        :type: AdvancedSimmetrixSolidSettings
        """

        self._advanced_simmetrix_settings = advanced_simmetrix_settings

    @property
    def second_order(self):
        """Gets the second_order of this Algorithm.  # noqa: E501

        <p>The <a href='https://www.simscale.com/docs/simulation-setup/meshing/standard/#order' target='_blank'><b>mesh order</b></a> defines the shape and the number of nodes of the mesh elements. For a fast, rough analysis choose <i>first order</i> only. Activate <i>2nd order elements</i> for higher quality results</p>  # noqa: E501

        :return: The second_order of this Algorithm.  # noqa: E501
        :rtype: bool
        """
        return self._second_order

    @second_order.setter
    def second_order(self, second_order):
        """Sets the second_order of this Algorithm.

        <p>The <a href='https://www.simscale.com/docs/simulation-setup/meshing/standard/#order' target='_blank'><b>mesh order</b></a> defines the shape and the number of nodes of the mesh elements. For a fast, rough analysis choose <i>first order</i> only. Activate <i>2nd order elements</i> for higher quality results</p>  # noqa: E501

        :param second_order: The second_order of this Algorithm.  # noqa: E501
        :type: bool
        """

        self._second_order = second_order

    @property
    def enable_shell_meshing(self):
        """Gets the enable_shell_meshing of this Algorithm.  # noqa: E501


        :return: The enable_shell_meshing of this Algorithm.  # noqa: E501
        :rtype: bool
        """
        return self._enable_shell_meshing

    @enable_shell_meshing.setter
    def enable_shell_meshing(self, enable_shell_meshing):
        """Sets the enable_shell_meshing of this Algorithm.


        :param enable_shell_meshing: The enable_shell_meshing of this Algorithm.  # noqa: E501
        :type: bool
        """

        self._enable_shell_meshing = enable_shell_meshing

    @property
    def surface_element_type(self):
        """Gets the surface_element_type of this Algorithm.  # noqa: E501


        :return: The surface_element_type of this Algorithm.  # noqa: E501
        :rtype: str
        """
        return self._surface_element_type

    @surface_element_type.setter
    def surface_element_type(self, surface_element_type):
        """Sets the surface_element_type of this Algorithm.


        :param surface_element_type: The surface_element_type of this Algorithm.  # noqa: E501
        :type: str
        """
        allowed_values = ["TRIANGULAR", "QUADDOMINANT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and surface_element_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `surface_element_type` ({0}), must be one of {1}"  # noqa: E501
                .format(surface_element_type, allowed_values)
            )

        self._surface_element_type = surface_element_type

    @property
    def meshing_mode(self):
        """Gets the meshing_mode of this Algorithm.  # noqa: E501

        <p>The <a href='https://www.simscale.com/docs/simulation-setup/meshing/hex-dominant/#meshing-mode' target='_blank'>meshing mode</a> defines how the mesher should generate the mesh.</p><ul><li>The <b>Internal</b> mode will create the mesh <u>inside</u> of the geometry body. If the CAD consists of multiple solids, the mesher will attempt to create a multiregion mesh which is suitable for conjugate heat transfer analyses. Use this mode if the CAD model already represents the final fluid domain.</li><li><b>External</b> meshing will create the mesh <u>outside</u> of the bodies. The absolute dimensions of the mesh are determined by the <i>Background Mesh Box</i>. Use this mode in case you want to extract the fluid domain around your model.</li><li>The option <b>Material point</b> allows you to define a point inside the domain where the mesh will be placed. It can be used to select which part (or enclosed volume) of the model or should be meshed. The mesh will surround the material point and extend until the boundaries of the body. The location of the material point is defined by the <i>Material Point</i> geometry primitive.</li></ul>  # noqa: E501

        :return: The meshing_mode of this Algorithm.  # noqa: E501
        :rtype: str
        """
        return self._meshing_mode

    @meshing_mode.setter
    def meshing_mode(self, meshing_mode):
        """Sets the meshing_mode of this Algorithm.

        <p>The <a href='https://www.simscale.com/docs/simulation-setup/meshing/hex-dominant/#meshing-mode' target='_blank'>meshing mode</a> defines how the mesher should generate the mesh.</p><ul><li>The <b>Internal</b> mode will create the mesh <u>inside</u> of the geometry body. If the CAD consists of multiple solids, the mesher will attempt to create a multiregion mesh which is suitable for conjugate heat transfer analyses. Use this mode if the CAD model already represents the final fluid domain.</li><li><b>External</b> meshing will create the mesh <u>outside</u> of the bodies. The absolute dimensions of the mesh are determined by the <i>Background Mesh Box</i>. Use this mode in case you want to extract the fluid domain around your model.</li><li>The option <b>Material point</b> allows you to define a point inside the domain where the mesh will be placed. It can be used to select which part (or enclosed volume) of the model or should be meshed. The mesh will surround the material point and extend until the boundaries of the body. The location of the material point is defined by the <i>Material Point</i> geometry primitive.</li></ul>  # noqa: E501

        :param meshing_mode: The meshing_mode of this Algorithm.  # noqa: E501
        :type: str
        """
        allowed_values = ["INTERNAL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and meshing_mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `meshing_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(meshing_mode, allowed_values)
            )

        self._meshing_mode = meshing_mode

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
        if not isinstance(other, Algorithm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Algorithm):
            return True

        return self.to_dict() != other.to_dict()