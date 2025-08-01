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
        'is_compressible': 'bool',
        'enable_radiation': 'bool',
        'enable_solar_load': 'bool',
        'enable_humidity_model': 'bool',
        'enable_joule_heating': 'bool',
        'turbulence_model': 'str',
        'time_dependency': 'OneOfCoupledConjugateHeatTransferTimeDependency',
        'num_of_passive_species': 'int',
        'connection_groups': 'list[FluidInterface]',
        'model': 'FluidModel',
        'solar_calculator': 'SolarCalculator',
        'materials': 'CoupledConjugateHeatTransferMaterials',
        'initial_conditions': 'FluidInitialConditions',
        'boundary_conditions': 'list[OneOfCoupledConjugateHeatTransferBoundaryConditions]',
        'advanced_concepts': 'AdvancedConcepts',
        'numerics': 'FluidNumerics',
        'simulation_control': 'FluidSimulationControl',
        'result_control': 'FluidResultControls',
        'contact_handling_mode': 'str'
    }

    attribute_map = {
        'type': 'type',
        'is_compressible': 'isCompressible',
        'enable_radiation': 'enableRadiation',
        'enable_solar_load': 'enableSolarLoad',
        'enable_humidity_model': 'enableHumidityModel',
        'enable_joule_heating': 'enableJouleHeating',
        'turbulence_model': 'turbulenceModel',
        'time_dependency': 'timeDependency',
        'num_of_passive_species': 'numOfPassiveSpecies',
        'connection_groups': 'connectionGroups',
        'model': 'model',
        'solar_calculator': 'solarCalculator',
        'materials': 'materials',
        'initial_conditions': 'initialConditions',
        'boundary_conditions': 'boundaryConditions',
        'advanced_concepts': 'advancedConcepts',
        'numerics': 'numerics',
        'simulation_control': 'simulationControl',
        'result_control': 'resultControl',
        'contact_handling_mode': 'contactHandlingMode'
    }

    def __init__(self, type='COUPLED_CONJUGATE_HEAT_TRANSFER', is_compressible=None, enable_radiation=None, enable_solar_load=None, enable_humidity_model=None, enable_joule_heating=None, turbulence_model=None, time_dependency=None, num_of_passive_species=None, connection_groups=None, model=None, solar_calculator=None, materials=None, initial_conditions=None, boundary_conditions=None, advanced_concepts=None, numerics=None, simulation_control=None, result_control=None, contact_handling_mode=None, local_vars_configuration=None):  # noqa: E501
        """CoupledConjugateHeatTransfer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._is_compressible = None
        self._enable_radiation = None
        self._enable_solar_load = None
        self._enable_humidity_model = None
        self._enable_joule_heating = None
        self._turbulence_model = None
        self._time_dependency = None
        self._num_of_passive_species = None
        self._connection_groups = None
        self._model = None
        self._solar_calculator = None
        self._materials = None
        self._initial_conditions = None
        self._boundary_conditions = None
        self._advanced_concepts = None
        self._numerics = None
        self._simulation_control = None
        self._result_control = None
        self._contact_handling_mode = None
        self.discriminator = None

        self.type = type
        if is_compressible is not None:
            self.is_compressible = is_compressible
        if enable_radiation is not None:
            self.enable_radiation = enable_radiation
        if enable_solar_load is not None:
            self.enable_solar_load = enable_solar_load
        if enable_humidity_model is not None:
            self.enable_humidity_model = enable_humidity_model
        if enable_joule_heating is not None:
            self.enable_joule_heating = enable_joule_heating
        if turbulence_model is not None:
            self.turbulence_model = turbulence_model
        if time_dependency is not None:
            self.time_dependency = time_dependency
        if num_of_passive_species is not None:
            self.num_of_passive_species = num_of_passive_species
        if connection_groups is not None:
            self.connection_groups = connection_groups
        if model is not None:
            self.model = model
        if solar_calculator is not None:
            self.solar_calculator = solar_calculator
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

    @property
    def type(self):
        """Gets the type of this CoupledConjugateHeatTransfer.  # noqa: E501

        Schema name: CoupledConjugateHeatTransfer  # noqa: E501

        :return: The type of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CoupledConjugateHeatTransfer.

        Schema name: CoupledConjugateHeatTransfer  # noqa: E501

        :param type: The type of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def is_compressible(self):
        """Gets the is_compressible of this CoupledConjugateHeatTransfer.  # noqa: E501

        <ul><li>Toggle off <em>Compressible</em> for small temperature variations within the domain, for example, in natural convection simulations (Boussinesq approximation). Use Gauge pressure (0 Pa). </li><li>Toggle on <em>Compressible</em> to calculate resulting density variations within the domain based on pressure and temperature. Use Absolute pressure (for example, 101325 Pa at sea level)</li></ul>  # noqa: E501

        :return: The is_compressible of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: bool
        """
        return self._is_compressible

    @is_compressible.setter
    def is_compressible(self, is_compressible):
        """Sets the is_compressible of this CoupledConjugateHeatTransfer.

        <ul><li>Toggle off <em>Compressible</em> for small temperature variations within the domain, for example, in natural convection simulations (Boussinesq approximation). Use Gauge pressure (0 Pa). </li><li>Toggle on <em>Compressible</em> to calculate resulting density variations within the domain based on pressure and temperature. Use Absolute pressure (for example, 101325 Pa at sea level)</li></ul>  # noqa: E501

        :param is_compressible: The is_compressible of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: bool
        """

        self._is_compressible = is_compressible

    @property
    def enable_radiation(self):
        """Gets the enable_radiation of this CoupledConjugateHeatTransfer.  # noqa: E501

        Heat transfer through radiation takes place in the form of electromagnetic waves and it can be calculated in the simulation. This phenomenon becomes more important when the temperature differences in the simulation domain are large. <a href='https://www.simscale.com/docs/analysis-types/convective-heat-transfer-analysis/radiation/' target='_blank'>Learn more</a>.  # noqa: E501

        :return: The enable_radiation of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: bool
        """
        return self._enable_radiation

    @enable_radiation.setter
    def enable_radiation(self, enable_radiation):
        """Sets the enable_radiation of this CoupledConjugateHeatTransfer.

        Heat transfer through radiation takes place in the form of electromagnetic waves and it can be calculated in the simulation. This phenomenon becomes more important when the temperature differences in the simulation domain are large. <a href='https://www.simscale.com/docs/analysis-types/convective-heat-transfer-analysis/radiation/' target='_blank'>Learn more</a>.  # noqa: E501

        :param enable_radiation: The enable_radiation of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: bool
        """

        self._enable_radiation = enable_radiation

    @property
    def enable_solar_load(self):
        """Gets the enable_solar_load of this CoupledConjugateHeatTransfer.  # noqa: E501

        Enables the <b>solar load</b> model in the simulation. <b>Diffuse</b> and/or <b>directional</b> solar load contributions are specified in the <b>solar calculator</b>. The solar load terms will heat the external faces of the simulation domain. Moreover, if transparent and/or semi-transparent boundaries are present, internal surfaces of the domain might also be heated. All <b>internal solids</b> will be considered <b>opaque</b>. <a href='https://www.simscale.com/docs/analysis-types/conjugate-heat-transfer-analysis/solar-load/' target='_blank'>Learn more</a>.  # noqa: E501

        :return: The enable_solar_load of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: bool
        """
        return self._enable_solar_load

    @enable_solar_load.setter
    def enable_solar_load(self, enable_solar_load):
        """Sets the enable_solar_load of this CoupledConjugateHeatTransfer.

        Enables the <b>solar load</b> model in the simulation. <b>Diffuse</b> and/or <b>directional</b> solar load contributions are specified in the <b>solar calculator</b>. The solar load terms will heat the external faces of the simulation domain. Moreover, if transparent and/or semi-transparent boundaries are present, internal surfaces of the domain might also be heated. All <b>internal solids</b> will be considered <b>opaque</b>. <a href='https://www.simscale.com/docs/analysis-types/conjugate-heat-transfer-analysis/solar-load/' target='_blank'>Learn more</a>.  # noqa: E501

        :param enable_solar_load: The enable_solar_load of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: bool
        """

        self._enable_solar_load = enable_solar_load

    @property
    def enable_humidity_model(self):
        """Gets the enable_humidity_model of this CoupledConjugateHeatTransfer.  # noqa: E501

        <b>Humidity model</b> to simulate wet air. First turn on the <em>compressible</em> toggle to enable it. The simulation will take the effect of humid air on the flow field into account. Dry air is heavier than wet air and hence sinks. The model does not account for condensation and evaporation and is not applicable in cases where this is of concern, for example dehumidifiers. It is suitable for HVAC analysis and for temperature ranges of <b>0° to 100°C</b>. </li></ul></p><a href= https://www.simscale.com/docs/simulation-setup/global-settings/humidity-modeling/' target='_blank'>Learn more</a>.  # noqa: E501

        :return: The enable_humidity_model of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: bool
        """
        return self._enable_humidity_model

    @enable_humidity_model.setter
    def enable_humidity_model(self, enable_humidity_model):
        """Sets the enable_humidity_model of this CoupledConjugateHeatTransfer.

        <b>Humidity model</b> to simulate wet air. First turn on the <em>compressible</em> toggle to enable it. The simulation will take the effect of humid air on the flow field into account. Dry air is heavier than wet air and hence sinks. The model does not account for condensation and evaporation and is not applicable in cases where this is of concern, for example dehumidifiers. It is suitable for HVAC analysis and for temperature ranges of <b>0° to 100°C</b>. </li></ul></p><a href= https://www.simscale.com/docs/simulation-setup/global-settings/humidity-modeling/' target='_blank'>Learn more</a>.  # noqa: E501

        :param enable_humidity_model: The enable_humidity_model of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: bool
        """

        self._enable_humidity_model = enable_humidity_model

    @property
    def enable_joule_heating(self):
        """Gets the enable_joule_heating of this CoupledConjugateHeatTransfer.  # noqa: E501

        Enabling <b>Joule heating</b> gives you the possibility to solve a coupled electric conduction and conjugate heat transfer problem in a single simulation.  # noqa: E501

        :return: The enable_joule_heating of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: bool
        """
        return self._enable_joule_heating

    @enable_joule_heating.setter
    def enable_joule_heating(self, enable_joule_heating):
        """Sets the enable_joule_heating of this CoupledConjugateHeatTransfer.

        Enabling <b>Joule heating</b> gives you the possibility to solve a coupled electric conduction and conjugate heat transfer problem in a single simulation.  # noqa: E501

        :param enable_joule_heating: The enable_joule_heating of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: bool
        """

        self._enable_joule_heating = enable_joule_heating

    @property
    def turbulence_model(self):
        """Gets the turbulence_model of this CoupledConjugateHeatTransfer.  # noqa: E501

        Choose a turbulence model for your CFD analysis:<ul><li><strong>No turbulence</strong>: Laminar</li><li><strong>RANS</strong>: <a href='https://www.simscale.com/docs/simulation-setup/global-settings/k-omega-sst/' target='_blank'>k-omega SST</a> ,<a href='https://www.simscale.com/docs/simulation-setup/global-settings/k-epsilon/#standard-k-epsilon-model' target='_blank'>k-epsilon</a></p>  # noqa: E501

        :return: The turbulence_model of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: str
        """
        return self._turbulence_model

    @turbulence_model.setter
    def turbulence_model(self, turbulence_model):
        """Sets the turbulence_model of this CoupledConjugateHeatTransfer.

        Choose a turbulence model for your CFD analysis:<ul><li><strong>No turbulence</strong>: Laminar</li><li><strong>RANS</strong>: <a href='https://www.simscale.com/docs/simulation-setup/global-settings/k-omega-sst/' target='_blank'>k-omega SST</a> ,<a href='https://www.simscale.com/docs/simulation-setup/global-settings/k-epsilon/#standard-k-epsilon-model' target='_blank'>k-epsilon</a></p>  # noqa: E501

        :param turbulence_model: The turbulence_model of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "KEPSILON", "KOMEGASST"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and turbulence_model not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `turbulence_model` ({0}), must be one of {1}"  # noqa: E501
                .format(turbulence_model, allowed_values)
            )

        self._turbulence_model = turbulence_model

    @property
    def time_dependency(self):
        """Gets the time_dependency of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The time_dependency of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: OneOfCoupledConjugateHeatTransferTimeDependency
        """
        return self._time_dependency

    @time_dependency.setter
    def time_dependency(self, time_dependency):
        """Sets the time_dependency of this CoupledConjugateHeatTransfer.


        :param time_dependency: The time_dependency of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: OneOfCoupledConjugateHeatTransferTimeDependency
        """

        self._time_dependency = time_dependency

    @property
    def num_of_passive_species(self):
        """Gets the num_of_passive_species of this CoupledConjugateHeatTransfer.  # noqa: E501

        Select the number of passive species involved in the simulation. Passive species allow you to simulate the transport of a scalar quantity within a fluid flow without affecting it. <a href='https://www.simscale.com/docs/simulation-setup/global-settings/#passive-species' target='_blank'>Learn more</a>.  # noqa: E501

        :return: The num_of_passive_species of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: int
        """
        return self._num_of_passive_species

    @num_of_passive_species.setter
    def num_of_passive_species(self, num_of_passive_species):
        """Sets the num_of_passive_species of this CoupledConjugateHeatTransfer.

        Select the number of passive species involved in the simulation. Passive species allow you to simulate the transport of a scalar quantity within a fluid flow without affecting it. <a href='https://www.simscale.com/docs/simulation-setup/global-settings/#passive-species' target='_blank'>Learn more</a>.  # noqa: E501

        :param num_of_passive_species: The num_of_passive_species of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and num_of_passive_species not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `num_of_passive_species` ({0}), must be one of {1}"  # noqa: E501
                .format(num_of_passive_species, allowed_values)
            )

        self._num_of_passive_species = num_of_passive_species

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
    def solar_calculator(self):
        """Gets the solar_calculator of this CoupledConjugateHeatTransfer.  # noqa: E501


        :return: The solar_calculator of this CoupledConjugateHeatTransfer.  # noqa: E501
        :rtype: SolarCalculator
        """
        return self._solar_calculator

    @solar_calculator.setter
    def solar_calculator(self, solar_calculator):
        """Sets the solar_calculator of this CoupledConjugateHeatTransfer.


        :param solar_calculator: The solar_calculator of this CoupledConjugateHeatTransfer.  # noqa: E501
        :type: SolarCalculator
        """

        self._solar_calculator = solar_calculator

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
