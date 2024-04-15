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


class OneOfCoupledConjugateHeatTransferMaterialsFluids(object):
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
        'fluid_type': 'OneOfFluidCompressibleMaterialFluidType',
        'associated_phase': 'str',
        'viscosity_model': 'OneOfFluidCompressibleMaterialViscosityModel',
        'density': 'DimensionalDensity',
        'thermal_expansion_coefficient': 'DimensionalThermalExpansionRate',
        'reference_temperature': 'DimensionalTemperature',
        'laminar_prandtl_number': 'float',
        'laminar_prandtl_number_function': 'DimensionalFunctionDimensionless',
        'turbulent_prandtl_number': 'float',
        'specific_heat': 'DimensionalSpecificHeat',
        'specific_heat_function': 'DimensionalFunctionSpecificHeat',
        'molar_weight': 'DimensionalMolarMass',
        'cavitation': 'Cavitation',
        'topological_reference': 'TopologicalReference',
        'geometry_primitive_uuids': 'list[str]',
        'built_in_material': 'str',
        'material_library_reference': 'MaterialLibraryReference',
        'specie': 'SpecieDefault',
        'transport': 'OneOfFluidCompressibleMaterialTransport',
        'schmidt_number': 'float',
        'equation_of_state': 'OneOfFluidCompressibleMaterialEquationOfState'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'fluid_type': 'fluidType',
        'associated_phase': 'associatedPhase',
        'viscosity_model': 'viscosityModel',
        'density': 'density',
        'thermal_expansion_coefficient': 'thermalExpansionCoefficient',
        'reference_temperature': 'referenceTemperature',
        'laminar_prandtl_number': 'laminarPrandtlNumber',
        'laminar_prandtl_number_function': 'laminarPrandtlNumberFunction',
        'turbulent_prandtl_number': 'turbulentPrandtlNumber',
        'specific_heat': 'specificHeat',
        'specific_heat_function': 'specificHeatFunction',
        'molar_weight': 'molarWeight',
        'cavitation': 'cavitation',
        'topological_reference': 'topologicalReference',
        'geometry_primitive_uuids': 'geometryPrimitiveUuids',
        'built_in_material': 'builtInMaterial',
        'material_library_reference': 'materialLibraryReference',
        'specie': 'specie',
        'transport': 'transport',
        'schmidt_number': 'schmidtNumber',
        'equation_of_state': 'equationOfState'
    }

    discriminator_value_class_map = {
        'INCOMPRESSIBLE': 'IncompressibleMaterial',
        'COMPRESSIBLE': 'FluidCompressibleMaterial'
    }

    def __init__(self, type='COMPRESSIBLE', name=None, fluid_type=None, associated_phase=None, viscosity_model=None, density=None, thermal_expansion_coefficient=None, reference_temperature=None, laminar_prandtl_number=None, laminar_prandtl_number_function=None, turbulent_prandtl_number=None, specific_heat=None, specific_heat_function=None, molar_weight=None, cavitation=None, topological_reference=None, geometry_primitive_uuids=None, built_in_material=None, material_library_reference=None, specie=None, transport=None, schmidt_number=None, equation_of_state=None, local_vars_configuration=None):  # noqa: E501
        """OneOfCoupledConjugateHeatTransferMaterialsFluids - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._fluid_type = None
        self._associated_phase = None
        self._viscosity_model = None
        self._density = None
        self._thermal_expansion_coefficient = None
        self._reference_temperature = None
        self._laminar_prandtl_number = None
        self._laminar_prandtl_number_function = None
        self._turbulent_prandtl_number = None
        self._specific_heat = None
        self._specific_heat_function = None
        self._molar_weight = None
        self._cavitation = None
        self._topological_reference = None
        self._geometry_primitive_uuids = None
        self._built_in_material = None
        self._material_library_reference = None
        self._specie = None
        self._transport = None
        self._schmidt_number = None
        self._equation_of_state = None
        self.discriminator = 'type'

        self.type = type
        if name is not None:
            self.name = name
        if fluid_type is not None:
            self.fluid_type = fluid_type
        if associated_phase is not None:
            self.associated_phase = associated_phase
        if viscosity_model is not None:
            self.viscosity_model = viscosity_model
        if density is not None:
            self.density = density
        if thermal_expansion_coefficient is not None:
            self.thermal_expansion_coefficient = thermal_expansion_coefficient
        if reference_temperature is not None:
            self.reference_temperature = reference_temperature
        if laminar_prandtl_number is not None:
            self.laminar_prandtl_number = laminar_prandtl_number
        if laminar_prandtl_number_function is not None:
            self.laminar_prandtl_number_function = laminar_prandtl_number_function
        if turbulent_prandtl_number is not None:
            self.turbulent_prandtl_number = turbulent_prandtl_number
        if specific_heat is not None:
            self.specific_heat = specific_heat
        if specific_heat_function is not None:
            self.specific_heat_function = specific_heat_function
        if molar_weight is not None:
            self.molar_weight = molar_weight
        if cavitation is not None:
            self.cavitation = cavitation
        if topological_reference is not None:
            self.topological_reference = topological_reference
        if geometry_primitive_uuids is not None:
            self.geometry_primitive_uuids = geometry_primitive_uuids
        if built_in_material is not None:
            self.built_in_material = built_in_material
        if material_library_reference is not None:
            self.material_library_reference = material_library_reference
        if specie is not None:
            self.specie = specie
        if transport is not None:
            self.transport = transport
        if schmidt_number is not None:
            self.schmidt_number = schmidt_number
        if equation_of_state is not None:
            self.equation_of_state = equation_of_state

    @property
    def type(self):
        """Gets the type of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501

        Schema name: FluidCompressibleMaterial  # noqa: E501

        :return: The type of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfCoupledConjugateHeatTransferMaterialsFluids.

        Schema name: FluidCompressibleMaterial  # noqa: E501

        :param type: The type of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The name of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param name: The name of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def fluid_type(self):
        """Gets the fluid_type of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The fluid_type of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: OneOfFluidCompressibleMaterialFluidType
        """
        return self._fluid_type

    @fluid_type.setter
    def fluid_type(self, fluid_type):
        """Sets the fluid_type of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param fluid_type: The fluid_type of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: OneOfFluidCompressibleMaterialFluidType
        """

        self._fluid_type = fluid_type

    @property
    def associated_phase(self):
        """Gets the associated_phase of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501

        <p>Select the corresponding phase for this material:</p><p><b>Phase 0</b> would mean this material is represented by the phase fraction value of 0. Hence, a phase fraction of '0' in your setup corresponds to 100% of this fluid material.</p><p><b>Phase 1</b> would mean this material is represented by the phase fraction value of 1. Hence, a phase fraction of '1' in your setup corresponds to 100% of this fluid material.</p>  # noqa: E501

        :return: The associated_phase of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: str
        """
        return self._associated_phase

    @associated_phase.setter
    def associated_phase(self, associated_phase):
        """Sets the associated_phase of this OneOfCoupledConjugateHeatTransferMaterialsFluids.

        <p>Select the corresponding phase for this material:</p><p><b>Phase 0</b> would mean this material is represented by the phase fraction value of 0. Hence, a phase fraction of '0' in your setup corresponds to 100% of this fluid material.</p><p><b>Phase 1</b> would mean this material is represented by the phase fraction value of 1. Hence, a phase fraction of '1' in your setup corresponds to 100% of this fluid material.</p>  # noqa: E501

        :param associated_phase: The associated_phase of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: str
        """
        allowed_values = ["PHASE_0", "PHASE_1"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and associated_phase not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `associated_phase` ({0}), must be one of {1}"  # noqa: E501
                .format(associated_phase, allowed_values)
            )

        self._associated_phase = associated_phase

    @property
    def viscosity_model(self):
        """Gets the viscosity_model of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The viscosity_model of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: OneOfFluidCompressibleMaterialViscosityModel
        """
        return self._viscosity_model

    @viscosity_model.setter
    def viscosity_model(self, viscosity_model):
        """Sets the viscosity_model of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param viscosity_model: The viscosity_model of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: OneOfFluidCompressibleMaterialViscosityModel
        """

        self._viscosity_model = viscosity_model

    @property
    def density(self):
        """Gets the density of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The density of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: DimensionalDensity
        """
        return self._density

    @density.setter
    def density(self, density):
        """Sets the density of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param density: The density of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: DimensionalDensity
        """

        self._density = density

    @property
    def thermal_expansion_coefficient(self):
        """Gets the thermal_expansion_coefficient of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The thermal_expansion_coefficient of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: DimensionalThermalExpansionRate
        """
        return self._thermal_expansion_coefficient

    @thermal_expansion_coefficient.setter
    def thermal_expansion_coefficient(self, thermal_expansion_coefficient):
        """Sets the thermal_expansion_coefficient of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param thermal_expansion_coefficient: The thermal_expansion_coefficient of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: DimensionalThermalExpansionRate
        """

        self._thermal_expansion_coefficient = thermal_expansion_coefficient

    @property
    def reference_temperature(self):
        """Gets the reference_temperature of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The reference_temperature of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: DimensionalTemperature
        """
        return self._reference_temperature

    @reference_temperature.setter
    def reference_temperature(self, reference_temperature):
        """Sets the reference_temperature of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param reference_temperature: The reference_temperature of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: DimensionalTemperature
        """

        self._reference_temperature = reference_temperature

    @property
    def laminar_prandtl_number(self):
        """Gets the laminar_prandtl_number of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501

        Laminar Prandtl number is used to calculate the heat transfer in the domain.  # noqa: E501

        :return: The laminar_prandtl_number of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: float
        """
        return self._laminar_prandtl_number

    @laminar_prandtl_number.setter
    def laminar_prandtl_number(self, laminar_prandtl_number):
        """Sets the laminar_prandtl_number of this OneOfCoupledConjugateHeatTransferMaterialsFluids.

        Laminar Prandtl number is used to calculate the heat transfer in the domain.  # noqa: E501

        :param laminar_prandtl_number: The laminar_prandtl_number of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                laminar_prandtl_number is not None and laminar_prandtl_number <= 0):  # noqa: E501
            raise ValueError("Invalid value for `laminar_prandtl_number`, must be a value greater than `0`")  # noqa: E501

        self._laminar_prandtl_number = laminar_prandtl_number

    @property
    def laminar_prandtl_number_function(self):
        """Gets the laminar_prandtl_number_function of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The laminar_prandtl_number_function of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: DimensionalFunctionDimensionless
        """
        return self._laminar_prandtl_number_function

    @laminar_prandtl_number_function.setter
    def laminar_prandtl_number_function(self, laminar_prandtl_number_function):
        """Sets the laminar_prandtl_number_function of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param laminar_prandtl_number_function: The laminar_prandtl_number_function of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: DimensionalFunctionDimensionless
        """

        self._laminar_prandtl_number_function = laminar_prandtl_number_function

    @property
    def turbulent_prandtl_number(self):
        """Gets the turbulent_prandtl_number of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501

        Turbulent Prandtl number is used to calculate the heat transfer due to turbulent effects in the domain.  # noqa: E501

        :return: The turbulent_prandtl_number of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: float
        """
        return self._turbulent_prandtl_number

    @turbulent_prandtl_number.setter
    def turbulent_prandtl_number(self, turbulent_prandtl_number):
        """Sets the turbulent_prandtl_number of this OneOfCoupledConjugateHeatTransferMaterialsFluids.

        Turbulent Prandtl number is used to calculate the heat transfer due to turbulent effects in the domain.  # noqa: E501

        :param turbulent_prandtl_number: The turbulent_prandtl_number of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                turbulent_prandtl_number is not None and turbulent_prandtl_number <= 0):  # noqa: E501
            raise ValueError("Invalid value for `turbulent_prandtl_number`, must be a value greater than `0`")  # noqa: E501

        self._turbulent_prandtl_number = turbulent_prandtl_number

    @property
    def specific_heat(self):
        """Gets the specific_heat of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The specific_heat of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: DimensionalSpecificHeat
        """
        return self._specific_heat

    @specific_heat.setter
    def specific_heat(self, specific_heat):
        """Sets the specific_heat of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param specific_heat: The specific_heat of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: DimensionalSpecificHeat
        """

        self._specific_heat = specific_heat

    @property
    def specific_heat_function(self):
        """Gets the specific_heat_function of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The specific_heat_function of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: DimensionalFunctionSpecificHeat
        """
        return self._specific_heat_function

    @specific_heat_function.setter
    def specific_heat_function(self, specific_heat_function):
        """Sets the specific_heat_function of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param specific_heat_function: The specific_heat_function of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: DimensionalFunctionSpecificHeat
        """

        self._specific_heat_function = specific_heat_function

    @property
    def molar_weight(self):
        """Gets the molar_weight of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The molar_weight of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: DimensionalMolarMass
        """
        return self._molar_weight

    @molar_weight.setter
    def molar_weight(self, molar_weight):
        """Sets the molar_weight of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param molar_weight: The molar_weight of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: DimensionalMolarMass
        """

        self._molar_weight = molar_weight

    @property
    def cavitation(self):
        """Gets the cavitation of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The cavitation of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: Cavitation
        """
        return self._cavitation

    @cavitation.setter
    def cavitation(self, cavitation):
        """Sets the cavitation of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param cavitation: The cavitation of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: Cavitation
        """

        self._cavitation = cavitation

    @property
    def topological_reference(self):
        """Gets the topological_reference of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The topological_reference of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param topological_reference: The topological_reference of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def geometry_primitive_uuids(self):
        """Gets the geometry_primitive_uuids of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The geometry_primitive_uuids of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: list[str]
        """
        return self._geometry_primitive_uuids

    @geometry_primitive_uuids.setter
    def geometry_primitive_uuids(self, geometry_primitive_uuids):
        """Sets the geometry_primitive_uuids of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param geometry_primitive_uuids: The geometry_primitive_uuids of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: list[str]
        """

        self._geometry_primitive_uuids = geometry_primitive_uuids

    @property
    def built_in_material(self):
        """Gets the built_in_material of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The built_in_material of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: str
        """
        return self._built_in_material

    @built_in_material.setter
    def built_in_material(self, built_in_material):
        """Sets the built_in_material of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param built_in_material: The built_in_material of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: str
        """

        self._built_in_material = built_in_material

    @property
    def material_library_reference(self):
        """Gets the material_library_reference of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The material_library_reference of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: MaterialLibraryReference
        """
        return self._material_library_reference

    @material_library_reference.setter
    def material_library_reference(self, material_library_reference):
        """Sets the material_library_reference of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param material_library_reference: The material_library_reference of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: MaterialLibraryReference
        """

        self._material_library_reference = material_library_reference

    @property
    def specie(self):
        """Gets the specie of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The specie of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: SpecieDefault
        """
        return self._specie

    @specie.setter
    def specie(self, specie):
        """Sets the specie of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param specie: The specie of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: SpecieDefault
        """

        self._specie = specie

    @property
    def transport(self):
        """Gets the transport of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The transport of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: OneOfFluidCompressibleMaterialTransport
        """
        return self._transport

    @transport.setter
    def transport(self, transport):
        """Sets the transport of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param transport: The transport of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: OneOfFluidCompressibleMaterialTransport
        """

        self._transport = transport

    @property
    def schmidt_number(self):
        """Gets the schmidt_number of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501

        The Schmidt number is a dimensionless number defined as the ratio of viscous diffusion to molecular mass diffusion. In dilute flows where a dominant carrier gas advects other species, it is assumed to be constant and a typical value is Sc = 5/6.  # noqa: E501

        :return: The schmidt_number of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: float
        """
        return self._schmidt_number

    @schmidt_number.setter
    def schmidt_number(self, schmidt_number):
        """Sets the schmidt_number of this OneOfCoupledConjugateHeatTransferMaterialsFluids.

        The Schmidt number is a dimensionless number defined as the ratio of viscous diffusion to molecular mass diffusion. In dilute flows where a dominant carrier gas advects other species, it is assumed to be constant and a typical value is Sc = 5/6.  # noqa: E501

        :param schmidt_number: The schmidt_number of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                schmidt_number is not None and schmidt_number <= 0):  # noqa: E501
            raise ValueError("Invalid value for `schmidt_number`, must be a value greater than `0`")  # noqa: E501

        self._schmidt_number = schmidt_number

    @property
    def equation_of_state(self):
        """Gets the equation_of_state of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501


        :return: The equation_of_state of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: OneOfFluidCompressibleMaterialEquationOfState
        """
        return self._equation_of_state

    @equation_of_state.setter
    def equation_of_state(self, equation_of_state):
        """Sets the equation_of_state of this OneOfCoupledConjugateHeatTransferMaterialsFluids.


        :param equation_of_state: The equation_of_state of this OneOfCoupledConjugateHeatTransferMaterialsFluids.  # noqa: E501
        :type: OneOfFluidCompressibleMaterialEquationOfState
        """

        self._equation_of_state = equation_of_state

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
        if not isinstance(other, OneOfCoupledConjugateHeatTransferMaterialsFluids):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfCoupledConjugateHeatTransferMaterialsFluids):
            return True

        return self.to_dict() != other.to_dict()
