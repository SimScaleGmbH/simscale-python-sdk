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


class EmbeddedBoundary(object):
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
        'is_internal_flow': 'bool',
        'model': 'FluidModel',
        'materials': 'CoupledConjugateHeatTransferMaterials',
        'initial_conditions': 'FluidInitialConditions',
        'boundary_conditions': 'list[OneOfEmbeddedBoundaryBoundaryConditions]',
        'advanced_concepts': 'AdvancedConcepts',
        'numerics': 'FluidNumerics',
        'simulation_control': 'FluidSimulationControl',
        'result_control': 'FluidResultControls',
        'embedded_boundary_meshing': 'EmbeddedBoundaryMeshing',
        'is_compressible': 'bool',
        'enable_radiation': 'bool',
        'enable_joule_heating': 'bool',
        'turbulence_model': 'str',
        'time_dependency': 'OneOfEmbeddedBoundaryTimeDependency'
    }

    attribute_map = {
        'type': 'type',
        'is_internal_flow': 'isInternalFlow',
        'model': 'model',
        'materials': 'materials',
        'initial_conditions': 'initialConditions',
        'boundary_conditions': 'boundaryConditions',
        'advanced_concepts': 'advancedConcepts',
        'numerics': 'numerics',
        'simulation_control': 'simulationControl',
        'result_control': 'resultControl',
        'embedded_boundary_meshing': 'embeddedBoundaryMeshing',
        'is_compressible': 'isCompressible',
        'enable_radiation': 'enableRadiation',
        'enable_joule_heating': 'enableJouleHeating',
        'turbulence_model': 'turbulenceModel',
        'time_dependency': 'timeDependency'
    }

    def __init__(self, type='EMBEDDED_BOUNDARY', is_internal_flow=None, model=None, materials=None, initial_conditions=None, boundary_conditions=None, advanced_concepts=None, numerics=None, simulation_control=None, result_control=None, embedded_boundary_meshing=None, is_compressible=None, enable_radiation=None, enable_joule_heating=None, turbulence_model=None, time_dependency=None, local_vars_configuration=None):  # noqa: E501
        """EmbeddedBoundary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._is_internal_flow = None
        self._model = None
        self._materials = None
        self._initial_conditions = None
        self._boundary_conditions = None
        self._advanced_concepts = None
        self._numerics = None
        self._simulation_control = None
        self._result_control = None
        self._embedded_boundary_meshing = None
        self._is_compressible = None
        self._enable_radiation = None
        self._enable_joule_heating = None
        self._turbulence_model = None
        self._time_dependency = None
        self.discriminator = None

        self.type = type
        if is_internal_flow is not None:
            self.is_internal_flow = is_internal_flow
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
        if embedded_boundary_meshing is not None:
            self.embedded_boundary_meshing = embedded_boundary_meshing
        if is_compressible is not None:
            self.is_compressible = is_compressible
        if enable_radiation is not None:
            self.enable_radiation = enable_radiation
        if enable_joule_heating is not None:
            self.enable_joule_heating = enable_joule_heating
        if turbulence_model is not None:
            self.turbulence_model = turbulence_model
        if time_dependency is not None:
            self.time_dependency = time_dependency

    @property
    def type(self):
        """Gets the type of this EmbeddedBoundary.  # noqa: E501

        Schema name: EmbeddedBoundary  # noqa: E501

        :return: The type of this EmbeddedBoundary.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EmbeddedBoundary.

        Schema name: EmbeddedBoundary  # noqa: E501

        :param type: The type of this EmbeddedBoundary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def is_internal_flow(self):
        """Gets the is_internal_flow of this EmbeddedBoundary.  # noqa: E501

        If active it indicates that the fluid region is contained within the uploaded geometry.  # noqa: E501

        :return: The is_internal_flow of this EmbeddedBoundary.  # noqa: E501
        :rtype: bool
        """
        return self._is_internal_flow

    @is_internal_flow.setter
    def is_internal_flow(self, is_internal_flow):
        """Sets the is_internal_flow of this EmbeddedBoundary.

        If active it indicates that the fluid region is contained within the uploaded geometry.  # noqa: E501

        :param is_internal_flow: The is_internal_flow of this EmbeddedBoundary.  # noqa: E501
        :type: bool
        """

        self._is_internal_flow = is_internal_flow

    @property
    def model(self):
        """Gets the model of this EmbeddedBoundary.  # noqa: E501


        :return: The model of this EmbeddedBoundary.  # noqa: E501
        :rtype: FluidModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this EmbeddedBoundary.


        :param model: The model of this EmbeddedBoundary.  # noqa: E501
        :type: FluidModel
        """

        self._model = model

    @property
    def materials(self):
        """Gets the materials of this EmbeddedBoundary.  # noqa: E501


        :return: The materials of this EmbeddedBoundary.  # noqa: E501
        :rtype: CoupledConjugateHeatTransferMaterials
        """
        return self._materials

    @materials.setter
    def materials(self, materials):
        """Sets the materials of this EmbeddedBoundary.


        :param materials: The materials of this EmbeddedBoundary.  # noqa: E501
        :type: CoupledConjugateHeatTransferMaterials
        """

        self._materials = materials

    @property
    def initial_conditions(self):
        """Gets the initial_conditions of this EmbeddedBoundary.  # noqa: E501


        :return: The initial_conditions of this EmbeddedBoundary.  # noqa: E501
        :rtype: FluidInitialConditions
        """
        return self._initial_conditions

    @initial_conditions.setter
    def initial_conditions(self, initial_conditions):
        """Sets the initial_conditions of this EmbeddedBoundary.


        :param initial_conditions: The initial_conditions of this EmbeddedBoundary.  # noqa: E501
        :type: FluidInitialConditions
        """

        self._initial_conditions = initial_conditions

    @property
    def boundary_conditions(self):
        """Gets the boundary_conditions of this EmbeddedBoundary.  # noqa: E501


        :return: The boundary_conditions of this EmbeddedBoundary.  # noqa: E501
        :rtype: list[OneOfEmbeddedBoundaryBoundaryConditions]
        """
        return self._boundary_conditions

    @boundary_conditions.setter
    def boundary_conditions(self, boundary_conditions):
        """Sets the boundary_conditions of this EmbeddedBoundary.


        :param boundary_conditions: The boundary_conditions of this EmbeddedBoundary.  # noqa: E501
        :type: list[OneOfEmbeddedBoundaryBoundaryConditions]
        """

        self._boundary_conditions = boundary_conditions

    @property
    def advanced_concepts(self):
        """Gets the advanced_concepts of this EmbeddedBoundary.  # noqa: E501


        :return: The advanced_concepts of this EmbeddedBoundary.  # noqa: E501
        :rtype: AdvancedConcepts
        """
        return self._advanced_concepts

    @advanced_concepts.setter
    def advanced_concepts(self, advanced_concepts):
        """Sets the advanced_concepts of this EmbeddedBoundary.


        :param advanced_concepts: The advanced_concepts of this EmbeddedBoundary.  # noqa: E501
        :type: AdvancedConcepts
        """

        self._advanced_concepts = advanced_concepts

    @property
    def numerics(self):
        """Gets the numerics of this EmbeddedBoundary.  # noqa: E501


        :return: The numerics of this EmbeddedBoundary.  # noqa: E501
        :rtype: FluidNumerics
        """
        return self._numerics

    @numerics.setter
    def numerics(self, numerics):
        """Sets the numerics of this EmbeddedBoundary.


        :param numerics: The numerics of this EmbeddedBoundary.  # noqa: E501
        :type: FluidNumerics
        """

        self._numerics = numerics

    @property
    def simulation_control(self):
        """Gets the simulation_control of this EmbeddedBoundary.  # noqa: E501


        :return: The simulation_control of this EmbeddedBoundary.  # noqa: E501
        :rtype: FluidSimulationControl
        """
        return self._simulation_control

    @simulation_control.setter
    def simulation_control(self, simulation_control):
        """Sets the simulation_control of this EmbeddedBoundary.


        :param simulation_control: The simulation_control of this EmbeddedBoundary.  # noqa: E501
        :type: FluidSimulationControl
        """

        self._simulation_control = simulation_control

    @property
    def result_control(self):
        """Gets the result_control of this EmbeddedBoundary.  # noqa: E501


        :return: The result_control of this EmbeddedBoundary.  # noqa: E501
        :rtype: FluidResultControls
        """
        return self._result_control

    @result_control.setter
    def result_control(self, result_control):
        """Sets the result_control of this EmbeddedBoundary.


        :param result_control: The result_control of this EmbeddedBoundary.  # noqa: E501
        :type: FluidResultControls
        """

        self._result_control = result_control

    @property
    def embedded_boundary_meshing(self):
        """Gets the embedded_boundary_meshing of this EmbeddedBoundary.  # noqa: E501


        :return: The embedded_boundary_meshing of this EmbeddedBoundary.  # noqa: E501
        :rtype: EmbeddedBoundaryMeshing
        """
        return self._embedded_boundary_meshing

    @embedded_boundary_meshing.setter
    def embedded_boundary_meshing(self, embedded_boundary_meshing):
        """Sets the embedded_boundary_meshing of this EmbeddedBoundary.


        :param embedded_boundary_meshing: The embedded_boundary_meshing of this EmbeddedBoundary.  # noqa: E501
        :type: EmbeddedBoundaryMeshing
        """

        self._embedded_boundary_meshing = embedded_boundary_meshing

    @property
    def is_compressible(self):
        """Gets the is_compressible of this EmbeddedBoundary.  # noqa: E501

        <ul><li>Toggle off <em>Compressible</em> for small temperature variations within the domain, for example, in natural convection simulations (Boussinesq approximation). Use Gauge pressure (0 Pa). </li><li>Toggle on <em>Compressible</em> to calculate resulting density variations within the domain based on pressure and temperature. Use Absolute pressure (for example, 101325 Pa at sea level)</li></ul>  # noqa: E501

        :return: The is_compressible of this EmbeddedBoundary.  # noqa: E501
        :rtype: bool
        """
        return self._is_compressible

    @is_compressible.setter
    def is_compressible(self, is_compressible):
        """Sets the is_compressible of this EmbeddedBoundary.

        <ul><li>Toggle off <em>Compressible</em> for small temperature variations within the domain, for example, in natural convection simulations (Boussinesq approximation). Use Gauge pressure (0 Pa). </li><li>Toggle on <em>Compressible</em> to calculate resulting density variations within the domain based on pressure and temperature. Use Absolute pressure (for example, 101325 Pa at sea level)</li></ul>  # noqa: E501

        :param is_compressible: The is_compressible of this EmbeddedBoundary.  # noqa: E501
        :type: bool
        """

        self._is_compressible = is_compressible

    @property
    def enable_radiation(self):
        """Gets the enable_radiation of this EmbeddedBoundary.  # noqa: E501

        Heat transfer through radiation takes place in the form of electromagnetic waves and it can be calculated in the simulation. This phenomenon becomes more important when the temperature differences in the simulation domain are large. <a href='https://www.simscale.com/docs/analysis-types/convective-heat-transfer-analysis/radiation/' target='_blank'>Learn more</a>.  # noqa: E501

        :return: The enable_radiation of this EmbeddedBoundary.  # noqa: E501
        :rtype: bool
        """
        return self._enable_radiation

    @enable_radiation.setter
    def enable_radiation(self, enable_radiation):
        """Sets the enable_radiation of this EmbeddedBoundary.

        Heat transfer through radiation takes place in the form of electromagnetic waves and it can be calculated in the simulation. This phenomenon becomes more important when the temperature differences in the simulation domain are large. <a href='https://www.simscale.com/docs/analysis-types/convective-heat-transfer-analysis/radiation/' target='_blank'>Learn more</a>.  # noqa: E501

        :param enable_radiation: The enable_radiation of this EmbeddedBoundary.  # noqa: E501
        :type: bool
        """

        self._enable_radiation = enable_radiation

    @property
    def enable_joule_heating(self):
        """Gets the enable_joule_heating of this EmbeddedBoundary.  # noqa: E501

        Enabling <b>Joule heating</b> gives you the possibility to solve a coupled electric conduction and conjugate heat transfer problem in a single simulation.  # noqa: E501

        :return: The enable_joule_heating of this EmbeddedBoundary.  # noqa: E501
        :rtype: bool
        """
        return self._enable_joule_heating

    @enable_joule_heating.setter
    def enable_joule_heating(self, enable_joule_heating):
        """Sets the enable_joule_heating of this EmbeddedBoundary.

        Enabling <b>Joule heating</b> gives you the possibility to solve a coupled electric conduction and conjugate heat transfer problem in a single simulation.  # noqa: E501

        :param enable_joule_heating: The enable_joule_heating of this EmbeddedBoundary.  # noqa: E501
        :type: bool
        """

        self._enable_joule_heating = enable_joule_heating

    @property
    def turbulence_model(self):
        """Gets the turbulence_model of this EmbeddedBoundary.  # noqa: E501

        Choose a turbulence model for your CFD analysis:<ul><li><strong>No turbulence</strong>: Laminar</li><li><strong>RANS</strong>: <a href='https://www.simscale.com/docs/simulation-setup/global-settings/k-epsilon/' target='_blank'>k-epsilon</a>, <a href='https://www.simscale.com/docs/simulation-setup/global-settings/k-omega-sst/' target='_blank'>k-omega and k-omega SST</a></li><li><strong>LES</strong>: Smagorinsky, Spalart-Allmaras</li></ul><p><p><a href='https://www.simscale.com/blog/2017/12/turbulence-cfd-analysis/' target='_blank'>Learn more</a>.</p>  # noqa: E501

        :return: The turbulence_model of this EmbeddedBoundary.  # noqa: E501
        :rtype: str
        """
        return self._turbulence_model

    @turbulence_model.setter
    def turbulence_model(self, turbulence_model):
        """Sets the turbulence_model of this EmbeddedBoundary.

        Choose a turbulence model for your CFD analysis:<ul><li><strong>No turbulence</strong>: Laminar</li><li><strong>RANS</strong>: <a href='https://www.simscale.com/docs/simulation-setup/global-settings/k-epsilon/' target='_blank'>k-epsilon</a>, <a href='https://www.simscale.com/docs/simulation-setup/global-settings/k-omega-sst/' target='_blank'>k-omega and k-omega SST</a></li><li><strong>LES</strong>: Smagorinsky, Spalart-Allmaras</li></ul><p><p><a href='https://www.simscale.com/blog/2017/12/turbulence-cfd-analysis/' target='_blank'>Learn more</a>.</p>  # noqa: E501

        :param turbulence_model: The turbulence_model of this EmbeddedBoundary.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "KOMEGASST"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and turbulence_model not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `turbulence_model` ({0}), must be one of {1}"  # noqa: E501
                .format(turbulence_model, allowed_values)
            )

        self._turbulence_model = turbulence_model

    @property
    def time_dependency(self):
        """Gets the time_dependency of this EmbeddedBoundary.  # noqa: E501


        :return: The time_dependency of this EmbeddedBoundary.  # noqa: E501
        :rtype: OneOfEmbeddedBoundaryTimeDependency
        """
        return self._time_dependency

    @time_dependency.setter
    def time_dependency(self, time_dependency):
        """Sets the time_dependency of this EmbeddedBoundary.


        :param time_dependency: The time_dependency of this EmbeddedBoundary.  # noqa: E501
        :type: OneOfEmbeddedBoundaryTimeDependency
        """

        self._time_dependency = time_dependency

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
        if not isinstance(other, EmbeddedBoundary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmbeddedBoundary):
            return True

        return self.to_dict() != other.to_dict()
