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


class CoupledConjugateHeatTransfer(object):
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
        'mesh_spec_id': 'str',
        'connection_groups': 'list[FluidInterface]',
        'model': 'FluidModel',
        'materials': 'CoupledConjugateHeatTransferMaterials',
        'initial_conditions': 'FluidInitialConditions',
        'boundary_conditions': 'list[OneOfCoupledConjugateHeatTransferBoundaryConditions]',
        'advanced_concepts': 'AdvancedConcepts',
        'numerics': 'FluidNumerics',
        'simulation_control': 'FluidSimulationControl',
        'result_control': 'FluidResultControls',
        'contact_handling_mode': 'str',
        'is_compressible': 'bool',
        'enable_radiation': 'bool',
        'time_dependency': 'StationaryTimeDependency',
        'turbulence_model': 'str'
    }

    attribute_map = {
        'type': 'type',
        'mesh_spec_id': 'meshSpecId',
        'connection_groups': 'connectionGroups',
        'model': 'model',
        'materials': 'materials',
        'initial_conditions': 'initialConditions',
        'boundary_conditions': 'boundaryConditions',
        'advanced_concepts': 'advancedConcepts',
        'numerics': 'numerics',
        'simulation_control': 'simulationControl',
        'result_control': 'resultControl',
        'contact_handling_mode': 'contactHandlingMode',
        'is_compressible': 'isCompressible',
        'enable_radiation': 'enableRadiation',
        'time_dependency': 'timeDependency',
        'turbulence_model': 'turbulenceModel'
    }

    def __init__(self, type='COUPLED_CONJUGATE_HEAT_TRANSFER', mesh_spec_id=None, connection_groups=None, model=None, materials=None, initial_conditions=None, boundary_conditions=None, advanced_concepts=None, numerics=None, simulation_control=None, result_control=None, contact_handling_mode=None, is_compressible=False, enable_radiation=False, time_dependency=None, turbulence_model=None, local_vars_configuration=None):  # noqa: E501
        """CoupledConjugateHeatTransfer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._mesh_spec_id = None
        self._connection_groups = None
        self._model = None
        self._materials = None
        self._initial_conditions = None
        self._boundary_conditions = None
        self._advanced_concepts = None
        self._numerics = None
        self._simulation_control = None
        self._result_control = None
        self._contact_handling_mode = None
        self._is_compressible = None
        self._enable_radiation = None
        self._time_dependency = None
        self._turbulence_model = None
        self.discriminator = None

        self.type = type
        if mesh_spec_id is not None:
            self.mesh_spec_id = mesh_spec_id
        if connection_groups is not None:
            self.connection_groups = connection_groups
        if model is not None:
            self.model = model
        if materials is not None:
            self.materials = materials
        if initial_conditions is not None:
            self.initial_conditions = initial_conditions
        if boundary_conditions is not None:
            self.boundary_conditions = boundary_conditions
        if advanced_concepts is not None:
            self.advanced_concepts = advanced_concepts
        if numerics is not None:
            self.numerics = numerics
        if simulation_control is not None:
            self.simulation_control = simulation_control
        if result_control is not None:
            self.result_control = result_control
        if contact_handling_mode is not None:
            self.contact_handling_mode = contact_handling_mode
        self.is_compressible = is_compressible
        self.enable_radiation = enable_radiation
        if time_dependency is not None:
            self.time_dependency = time_dependency
        if turbulence_model is not None:
            self.turbulence_model = turbulence_model

    @property
    def type(self):
        """Gets the type of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The type of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CoupledConjugateHeatTransfer.


        :param type: The type of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def mesh_spec_id(self):
        """Gets the mesh_spec_id of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The mesh_spec_id of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: str
        """
        return self._mesh_spec_id

    @mesh_spec_id.setter
    def mesh_spec_id(self, mesh_spec_id):
        """Sets the mesh_spec_id of this CoupledConjugateHeatTransfer.


        :param mesh_spec_id: The mesh_spec_id of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: str
        """

        self._mesh_spec_id = mesh_spec_id

    @property
    def connection_groups(self):
        """Gets the connection_groups of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The connection_groups of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: list[FluidInterface]
        """
        return self._connection_groups

    @connection_groups.setter
    def connection_groups(self, connection_groups):
        """Sets the connection_groups of this CoupledConjugateHeatTransfer.


        :param connection_groups: The connection_groups of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: list[FluidInterface]
        """

        self._connection_groups = connection_groups

    @property
    def model(self):
        """Gets the model of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The model of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: FluidModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this CoupledConjugateHeatTransfer.


        :param model: The model of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: FluidModel
        """

        self._model = model

    @property
    def materials(self):
        """Gets the materials of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The materials of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: CoupledConjugateHeatTransferMaterials
        """
        return self._materials

    @materials.setter
    def materials(self, materials):
        """Sets the materials of this CoupledConjugateHeatTransfer.


        :param materials: The materials of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: CoupledConjugateHeatTransferMaterials
        """

        self._materials = materials

    @property
    def initial_conditions(self):
        """Gets the initial_conditions of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The initial_conditions of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: FluidInitialConditions
        """
        return self._initial_conditions

    @initial_conditions.setter
    def initial_conditions(self, initial_conditions):
        """Sets the initial_conditions of this CoupledConjugateHeatTransfer.


        :param initial_conditions: The initial_conditions of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: FluidInitialConditions
        """

        self._initial_conditions = initial_conditions

    @property
    def boundary_conditions(self):
        """Gets the boundary_conditions of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The boundary_conditions of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: list[OneOfCoupledConjugateHeatTransferBoundaryConditions]
        """
        return self._boundary_conditions

    @boundary_conditions.setter
    def boundary_conditions(self, boundary_conditions):
        """Sets the boundary_conditions of this CoupledConjugateHeatTransfer.


        :param boundary_conditions: The boundary_conditions of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: list[OneOfCoupledConjugateHeatTransferBoundaryConditions]
        """

        self._boundary_conditions = boundary_conditions

    @property
    def advanced_concepts(self):
        """Gets the advanced_concepts of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The advanced_concepts of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: AdvancedConcepts
        """
        return self._advanced_concepts

    @advanced_concepts.setter
    def advanced_concepts(self, advanced_concepts):
        """Sets the advanced_concepts of this CoupledConjugateHeatTransfer.


        :param advanced_concepts: The advanced_concepts of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: AdvancedConcepts
        """

        self._advanced_concepts = advanced_concepts

    @property
    def numerics(self):
        """Gets the numerics of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The numerics of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: FluidNumerics
        """
        return self._numerics

    @numerics.setter
    def numerics(self, numerics):
        """Sets the numerics of this CoupledConjugateHeatTransfer.


        :param numerics: The numerics of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: FluidNumerics
        """

        self._numerics = numerics

    @property
    def simulation_control(self):
        """Gets the simulation_control of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The simulation_control of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: FluidSimulationControl
        """
        return self._simulation_control

    @simulation_control.setter
    def simulation_control(self, simulation_control):
        """Sets the simulation_control of this CoupledConjugateHeatTransfer.


        :param simulation_control: The simulation_control of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: FluidSimulationControl
        """

        self._simulation_control = simulation_control

    @property
    def result_control(self):
        """Gets the result_control of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The result_control of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: FluidResultControls
        """
        return self._result_control

    @result_control.setter
    def result_control(self, result_control):
        """Sets the result_control of this CoupledConjugateHeatTransfer.


        :param result_control: The result_control of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: FluidResultControls
        """

        self._result_control = result_control

    @property
    def contact_handling_mode(self):
        """Gets the contact_handling_mode of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The contact_handling_mode of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: str
        """
        return self._contact_handling_mode

    @contact_handling_mode.setter
    def contact_handling_mode(self, contact_handling_mode):
        """Sets the contact_handling_mode of this CoupledConjugateHeatTransfer.


        :param contact_handling_mode: The contact_handling_mode of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: str
        """
        allowed_values = ["MANUAL", "AUTO"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and contact_handling_mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `contact_handling_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(contact_handling_mode, allowed_values)
            )

        self._contact_handling_mode = contact_handling_mode

    @property
    def is_compressible(self):
        """Gets the is_compressible of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The is_compressible of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: bool
        """
        return self._is_compressible

    @is_compressible.setter
    def is_compressible(self, is_compressible):
        """Sets the is_compressible of this CoupledConjugateHeatTransfer.


        :param is_compressible: The is_compressible of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_compressible is None:  # noqa: E501
            raise ValueError("Invalid value for `is_compressible`, must not be `None`")  # noqa: E501

        self._is_compressible = is_compressible

    @property
    def enable_radiation(self):
        """Gets the enable_radiation of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The enable_radiation of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: bool
        """
        return self._enable_radiation

    @enable_radiation.setter
    def enable_radiation(self, enable_radiation):
        """Sets the enable_radiation of this CoupledConjugateHeatTransfer.


        :param enable_radiation: The enable_radiation of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_radiation is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_radiation`, must not be `None`")  # noqa: E501

        self._enable_radiation = enable_radiation

    @property
    def time_dependency(self):
        """Gets the time_dependency of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The time_dependency of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: StationaryTimeDependency
        """
        return self._time_dependency

    @time_dependency.setter
    def time_dependency(self, time_dependency):
        """Sets the time_dependency of this CoupledConjugateHeatTransfer.


        :param time_dependency: The time_dependency of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: StationaryTimeDependency
        """

        self._time_dependency = time_dependency

    @property
    def turbulence_model(self):
        """Gets the turbulence_model of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The turbulence_model of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: str
        """
        return self._turbulence_model

    @turbulence_model.setter
    def turbulence_model(self, turbulence_model):
        """Sets the turbulence_model of this CoupledConjugateHeatTransfer.


        :param turbulence_model: The turbulence_model of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "KOMEGASST"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and turbulence_model not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `turbulence_model` ({0}), must be one of {1}"  # noqa: E501
                .format(turbulence_model, allowed_values)
            )

        self._turbulence_model = turbulence_model

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
        if not isinstance(other, CoupledConjugateHeatTransfer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CoupledConjugateHeatTransfer):
            return True

        return self.to_dict() != other.to_dict()
