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


class OneOfFluidResultControlsFieldCalculations(object):
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
        'pressure_type': 'OneOfFieldCalculationsPressureResultControlPressureType',
        'result_type': 'TotalTurbulenceIntensity',
        'age_of_fluid_diffusion': 'bool',
        'turbulent_schmidt_number': 'float',
        'diffusion_coefficient': 'DimensionalKinematicViscosity',
        'clothing_coefficient_factor': 'float',
        'metabolic_rate_factor': 'float',
        'relative_humidity_factor': 'float',
        'mrt_solar_parameters': 'MrtSolarParameters',
        'compute_sensitivities_to': 'str',
        'optimization_force_direction': 'DecimalVector',
        'topological_reference': 'TopologicalReference',
        'compute_heat_transfer_coefficient': 'bool',
        'reference_temperature_result_type': 'OneOfFieldCalculationsWallHeatFluxResultControlReferenceTemperatureResultType',
        'compute_nusselt_number': 'bool',
        'reference_nusselt_number_length': 'DimensionalLength'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'pressure_type': 'pressureType',
        'result_type': 'resultType',
        'age_of_fluid_diffusion': 'ageOfFluidDiffusion',
        'turbulent_schmidt_number': 'turbulentSchmidtNumber',
        'diffusion_coefficient': 'diffusionCoefficient',
        'clothing_coefficient_factor': 'clothingCoefficientFactor',
        'metabolic_rate_factor': 'metabolicRateFactor',
        'relative_humidity_factor': 'relativeHumidityFactor',
        'mrt_solar_parameters': 'mrtSolarParameters',
        'compute_sensitivities_to': 'computeSensitivitiesTo',
        'optimization_force_direction': 'optimizationForceDirection',
        'topological_reference': 'topologicalReference',
        'compute_heat_transfer_coefficient': 'computeHeatTransferCoefficient',
        'reference_temperature_result_type': 'referenceTemperatureResultType',
        'compute_nusselt_number': 'computeNusseltNumber',
        'reference_nusselt_number_length': 'referenceNusseltNumberLength'
    }

    discriminator_value_class_map = {
        'PRESSURE': 'FieldCalculationsPressureResultControl',
        'TURBULENCE': 'FieldCalculationsTurbulenceResultControl',
        'VELOCITY': 'FieldCalculationsVelocityResultControl',
        'FRICTION_VELOCITY_U_TAU': 'FieldCalculationsFrictionVelocityResultControl',
        'SURFACE_NORMALS': 'FieldCalculationsSurfaceNormalsResultControl',
        'WALL_FLUXES': 'FieldCalculationsWallFluxesResultControl',
        'AGE_OF_FLUID': 'FieldCalculationsMeanAgeOfFluidResultControl',
        'THERMAL_COMFORT': 'FieldCalculationsThermalComfortResultControl',
        'ADJOINT_SENSITIVITIES': 'FieldCalculationsAdjointSensitivitiesResultControl',
        'WALL_HEAT_FLUX': 'FieldCalculationsWallHeatFluxResultControl',
        'MEAN_RADIANT_TEMPERATURE': 'FieldCalculationsMeanRadiantTemperatureResultControl',
        'OPERATIVE_TEMPERATURE': 'FieldCalculationsOperativeTemperatureResultControl',
        'RESOLVED_TURBULENT_KINETIC_ENERGY': 'FieldCalculationsResolvedTKEResultControl',
        'TOTAL_TURBULENT_KINETIC_ENERGY': 'FieldCalculationsTotalTKEResultControl',
        'MODELED_TURBULENCE_INTENSITY': 'FieldCalculationsModeledTIResultControl',
        'RESOLVED_TURBULENCE_INTENSITY': 'FieldCalculationsResolvedTIResultControl',
        'TOTAL_TURBULENCE_INTENSITY': 'FieldCalculationsTotalTIResultControl'
    }

    def __init__(self, type='TOTAL_TURBULENCE_INTENSITY', name=None, pressure_type=None, result_type=None, age_of_fluid_diffusion=None, turbulent_schmidt_number=None, diffusion_coefficient=None, clothing_coefficient_factor=None, metabolic_rate_factor=None, relative_humidity_factor=None, mrt_solar_parameters=None, compute_sensitivities_to=None, optimization_force_direction=None, topological_reference=None, compute_heat_transfer_coefficient=None, reference_temperature_result_type=None, compute_nusselt_number=None, reference_nusselt_number_length=None, local_vars_configuration=None):  # noqa: E501
        """OneOfFluidResultControlsFieldCalculations - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._pressure_type = None
        self._result_type = None
        self._age_of_fluid_diffusion = None
        self._turbulent_schmidt_number = None
        self._diffusion_coefficient = None
        self._clothing_coefficient_factor = None
        self._metabolic_rate_factor = None
        self._relative_humidity_factor = None
        self._mrt_solar_parameters = None
        self._compute_sensitivities_to = None
        self._optimization_force_direction = None
        self._topological_reference = None
        self._compute_heat_transfer_coefficient = None
        self._reference_temperature_result_type = None
        self._compute_nusselt_number = None
        self._reference_nusselt_number_length = None
        self.discriminator = 'type'

        self.type = type
        if name is not None:
            self.name = name
        if pressure_type is not None:
            self.pressure_type = pressure_type
        if result_type is not None:
            self.result_type = result_type
        if age_of_fluid_diffusion is not None:
            self.age_of_fluid_diffusion = age_of_fluid_diffusion
        if turbulent_schmidt_number is not None:
            self.turbulent_schmidt_number = turbulent_schmidt_number
        if diffusion_coefficient is not None:
            self.diffusion_coefficient = diffusion_coefficient
        if clothing_coefficient_factor is not None:
            self.clothing_coefficient_factor = clothing_coefficient_factor
        if metabolic_rate_factor is not None:
            self.metabolic_rate_factor = metabolic_rate_factor
        if relative_humidity_factor is not None:
            self.relative_humidity_factor = relative_humidity_factor
        if mrt_solar_parameters is not None:
            self.mrt_solar_parameters = mrt_solar_parameters
        if compute_sensitivities_to is not None:
            self.compute_sensitivities_to = compute_sensitivities_to
        if optimization_force_direction is not None:
            self.optimization_force_direction = optimization_force_direction
        if topological_reference is not None:
            self.topological_reference = topological_reference
        if compute_heat_transfer_coefficient is not None:
            self.compute_heat_transfer_coefficient = compute_heat_transfer_coefficient
        if reference_temperature_result_type is not None:
            self.reference_temperature_result_type = reference_temperature_result_type
        if compute_nusselt_number is not None:
            self.compute_nusselt_number = compute_nusselt_number
        if reference_nusselt_number_length is not None:
            self.reference_nusselt_number_length = reference_nusselt_number_length

    @property
    def type(self):
        """Gets the type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501

        Schema name: FieldCalculationsTotalTIResultControl  # noqa: E501

        :return: The type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfFluidResultControlsFieldCalculations.

        Schema name: FieldCalculationsTotalTIResultControl  # noqa: E501

        :param type: The type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The name of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfFluidResultControlsFieldCalculations.


        :param name: The name of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[A-Za-z()][-+0-9a-zA-Z_()\h]{0,199}$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[A-Za-z()][-+0-9a-zA-Z_()\h]{0,199}$/`")  # noqa: E501

        self._name = name

    @property
    def pressure_type(self):
        """Gets the pressure_type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The pressure_type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: OneOfFieldCalculationsPressureResultControlPressureType
        """
        return self._pressure_type

    @pressure_type.setter
    def pressure_type(self, pressure_type):
        """Sets the pressure_type of this OneOfFluidResultControlsFieldCalculations.


        :param pressure_type: The pressure_type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: OneOfFieldCalculationsPressureResultControlPressureType
        """

        self._pressure_type = pressure_type

    @property
    def result_type(self):
        """Gets the result_type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The result_type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: TotalTurbulenceIntensity
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        """Sets the result_type of this OneOfFluidResultControlsFieldCalculations.


        :param result_type: The result_type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: TotalTurbulenceIntensity
        """

        self._result_type = result_type

    @property
    def age_of_fluid_diffusion(self):
        """Gets the age_of_fluid_diffusion of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501

        <p>Enable or disable the diffusion term in the age of fluid equation. The exclusion of the diffusion term can be valid for laminar flows but tends to overestimate the age of fluid for turbulent flows.</p>  # noqa: E501

        :return: The age_of_fluid_diffusion of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: bool
        """
        return self._age_of_fluid_diffusion

    @age_of_fluid_diffusion.setter
    def age_of_fluid_diffusion(self, age_of_fluid_diffusion):
        """Sets the age_of_fluid_diffusion of this OneOfFluidResultControlsFieldCalculations.

        <p>Enable or disable the diffusion term in the age of fluid equation. The exclusion of the diffusion term can be valid for laminar flows but tends to overestimate the age of fluid for turbulent flows.</p>  # noqa: E501

        :param age_of_fluid_diffusion: The age_of_fluid_diffusion of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: bool
        """

        self._age_of_fluid_diffusion = age_of_fluid_diffusion

    @property
    def turbulent_schmidt_number(self):
        """Gets the turbulent_schmidt_number of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501

        <p>The <b>turbulent Schmidt number</b> characteristic of the flow. For HVAC applications it is recommended to maintain the default value of 0.7.</p>  # noqa: E501

        :return: The turbulent_schmidt_number of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: float
        """
        return self._turbulent_schmidt_number

    @turbulent_schmidt_number.setter
    def turbulent_schmidt_number(self, turbulent_schmidt_number):
        """Sets the turbulent_schmidt_number of this OneOfFluidResultControlsFieldCalculations.

        <p>The <b>turbulent Schmidt number</b> characteristic of the flow. For HVAC applications it is recommended to maintain the default value of 0.7.</p>  # noqa: E501

        :param turbulent_schmidt_number: The turbulent_schmidt_number of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                turbulent_schmidt_number is not None and turbulent_schmidt_number <= 1.0E-12):  # noqa: E501
            raise ValueError("Invalid value for `turbulent_schmidt_number`, must be a value greater than `1.0E-12`")  # noqa: E501

        self._turbulent_schmidt_number = turbulent_schmidt_number

    @property
    def diffusion_coefficient(self):
        """Gets the diffusion_coefficient of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The diffusion_coefficient of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: DimensionalKinematicViscosity
        """
        return self._diffusion_coefficient

    @diffusion_coefficient.setter
    def diffusion_coefficient(self, diffusion_coefficient):
        """Sets the diffusion_coefficient of this OneOfFluidResultControlsFieldCalculations.


        :param diffusion_coefficient: The diffusion_coefficient of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: DimensionalKinematicViscosity
        """

        self._diffusion_coefficient = diffusion_coefficient

    @property
    def clothing_coefficient_factor(self):
        """Gets the clothing_coefficient_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The clothing_coefficient_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: float
        """
        return self._clothing_coefficient_factor

    @clothing_coefficient_factor.setter
    def clothing_coefficient_factor(self, clothing_coefficient_factor):
        """Sets the clothing_coefficient_factor of this OneOfFluidResultControlsFieldCalculations.


        :param clothing_coefficient_factor: The clothing_coefficient_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                clothing_coefficient_factor is not None and clothing_coefficient_factor > 2):  # noqa: E501
            raise ValueError("Invalid value for `clothing_coefficient_factor`, must be a value less than or equal to `2`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                clothing_coefficient_factor is not None and clothing_coefficient_factor < 0):  # noqa: E501
            raise ValueError("Invalid value for `clothing_coefficient_factor`, must be a value greater than or equal to `0`")  # noqa: E501

        self._clothing_coefficient_factor = clothing_coefficient_factor

    @property
    def metabolic_rate_factor(self):
        """Gets the metabolic_rate_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The metabolic_rate_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: float
        """
        return self._metabolic_rate_factor

    @metabolic_rate_factor.setter
    def metabolic_rate_factor(self, metabolic_rate_factor):
        """Sets the metabolic_rate_factor of this OneOfFluidResultControlsFieldCalculations.


        :param metabolic_rate_factor: The metabolic_rate_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                metabolic_rate_factor is not None and metabolic_rate_factor > 4):  # noqa: E501
            raise ValueError("Invalid value for `metabolic_rate_factor`, must be a value less than or equal to `4`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                metabolic_rate_factor is not None and metabolic_rate_factor < 0.8):  # noqa: E501
            raise ValueError("Invalid value for `metabolic_rate_factor`, must be a value greater than or equal to `0.8`")  # noqa: E501

        self._metabolic_rate_factor = metabolic_rate_factor

    @property
    def relative_humidity_factor(self):
        """Gets the relative_humidity_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The relative_humidity_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: float
        """
        return self._relative_humidity_factor

    @relative_humidity_factor.setter
    def relative_humidity_factor(self, relative_humidity_factor):
        """Sets the relative_humidity_factor of this OneOfFluidResultControlsFieldCalculations.


        :param relative_humidity_factor: The relative_humidity_factor of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                relative_humidity_factor is not None and relative_humidity_factor > 100):  # noqa: E501
            raise ValueError("Invalid value for `relative_humidity_factor`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                relative_humidity_factor is not None and relative_humidity_factor < 0):  # noqa: E501
            raise ValueError("Invalid value for `relative_humidity_factor`, must be a value greater than or equal to `0`")  # noqa: E501

        self._relative_humidity_factor = relative_humidity_factor

    @property
    def mrt_solar_parameters(self):
        """Gets the mrt_solar_parameters of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The mrt_solar_parameters of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: MrtSolarParameters
        """
        return self._mrt_solar_parameters

    @mrt_solar_parameters.setter
    def mrt_solar_parameters(self, mrt_solar_parameters):
        """Sets the mrt_solar_parameters of this OneOfFluidResultControlsFieldCalculations.


        :param mrt_solar_parameters: The mrt_solar_parameters of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: MrtSolarParameters
        """

        self._mrt_solar_parameters = mrt_solar_parameters

    @property
    def compute_sensitivities_to(self):
        """Gets the compute_sensitivities_to of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The compute_sensitivities_to of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: str
        """
        return self._compute_sensitivities_to

    @compute_sensitivities_to.setter
    def compute_sensitivities_to(self, compute_sensitivities_to):
        """Sets the compute_sensitivities_to of this OneOfFluidResultControlsFieldCalculations.


        :param compute_sensitivities_to: The compute_sensitivities_to of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: str
        """
        allowed_values = ["MAXIMIZE_FORCE", "MINIMIZE_FORCE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and compute_sensitivities_to not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `compute_sensitivities_to` ({0}), must be one of {1}"  # noqa: E501
                .format(compute_sensitivities_to, allowed_values)
            )

        self._compute_sensitivities_to = compute_sensitivities_to

    @property
    def optimization_force_direction(self):
        """Gets the optimization_force_direction of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The optimization_force_direction of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: DecimalVector
        """
        return self._optimization_force_direction

    @optimization_force_direction.setter
    def optimization_force_direction(self, optimization_force_direction):
        """Sets the optimization_force_direction of this OneOfFluidResultControlsFieldCalculations.


        :param optimization_force_direction: The optimization_force_direction of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: DecimalVector
        """

        self._optimization_force_direction = optimization_force_direction

    @property
    def topological_reference(self):
        """Gets the topological_reference of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The topological_reference of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this OneOfFluidResultControlsFieldCalculations.


        :param topological_reference: The topological_reference of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def compute_heat_transfer_coefficient(self):
        """Gets the compute_heat_transfer_coefficient of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501

        Computes the <b>heat transfer coefficient</b> [W/(m²K)] at every wall. Radiation effects are not included. Two modes are available for the <b>reference temperature</b> calculation: <ul><li> <b>Wall adjacent cell</b>: Uses the temperature of the first adjacent cell. </li> <li><b>Fixed</b>: Uses a custom value.</li></ul>  # noqa: E501

        :return: The compute_heat_transfer_coefficient of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: bool
        """
        return self._compute_heat_transfer_coefficient

    @compute_heat_transfer_coefficient.setter
    def compute_heat_transfer_coefficient(self, compute_heat_transfer_coefficient):
        """Sets the compute_heat_transfer_coefficient of this OneOfFluidResultControlsFieldCalculations.

        Computes the <b>heat transfer coefficient</b> [W/(m²K)] at every wall. Radiation effects are not included. Two modes are available for the <b>reference temperature</b> calculation: <ul><li> <b>Wall adjacent cell</b>: Uses the temperature of the first adjacent cell. </li> <li><b>Fixed</b>: Uses a custom value.</li></ul>  # noqa: E501

        :param compute_heat_transfer_coefficient: The compute_heat_transfer_coefficient of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: bool
        """

        self._compute_heat_transfer_coefficient = compute_heat_transfer_coefficient

    @property
    def reference_temperature_result_type(self):
        """Gets the reference_temperature_result_type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The reference_temperature_result_type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: OneOfFieldCalculationsWallHeatFluxResultControlReferenceTemperatureResultType
        """
        return self._reference_temperature_result_type

    @reference_temperature_result_type.setter
    def reference_temperature_result_type(self, reference_temperature_result_type):
        """Sets the reference_temperature_result_type of this OneOfFluidResultControlsFieldCalculations.


        :param reference_temperature_result_type: The reference_temperature_result_type of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: OneOfFieldCalculationsWallHeatFluxResultControlReferenceTemperatureResultType
        """

        self._reference_temperature_result_type = reference_temperature_result_type

    @property
    def compute_nusselt_number(self):
        """Gets the compute_nusselt_number of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501

        Computes the <b>Nusselt Number</b> at every wall. The specified heat transfer coefficient mode will be used.  # noqa: E501

        :return: The compute_nusselt_number of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: bool
        """
        return self._compute_nusselt_number

    @compute_nusselt_number.setter
    def compute_nusselt_number(self, compute_nusselt_number):
        """Sets the compute_nusselt_number of this OneOfFluidResultControlsFieldCalculations.

        Computes the <b>Nusselt Number</b> at every wall. The specified heat transfer coefficient mode will be used.  # noqa: E501

        :param compute_nusselt_number: The compute_nusselt_number of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: bool
        """

        self._compute_nusselt_number = compute_nusselt_number

    @property
    def reference_nusselt_number_length(self):
        """Gets the reference_nusselt_number_length of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501


        :return: The reference_nusselt_number_length of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._reference_nusselt_number_length

    @reference_nusselt_number_length.setter
    def reference_nusselt_number_length(self, reference_nusselt_number_length):
        """Sets the reference_nusselt_number_length of this OneOfFluidResultControlsFieldCalculations.


        :param reference_nusselt_number_length: The reference_nusselt_number_length of this OneOfFluidResultControlsFieldCalculations.  # noqa: E501
        :type: DimensionalLength
        """

        self._reference_nusselt_number_length = reference_nusselt_number_length

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
        if not isinstance(other, OneOfFluidResultControlsFieldCalculations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfFluidResultControlsFieldCalculations):
            return True

        return self.to_dict() != other.to_dict()
