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


class Compressible(object):
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
        'turbulence_model': 'str',
        'time_dependency': 'OneOfCompressibleTimeDependency',
        'model': 'FluidModel',
        'materials': 'CompressibleFluidMaterials',
        'initial_conditions': 'FluidInitialConditions',
        'boundary_conditions': 'list[OneOfCompressibleBoundaryConditions]',
        'advanced_concepts': 'AdvancedConcepts',
        'numerics': 'FluidNumerics',
        'simulation_control': 'FluidSimulationControl',
        'result_control': 'FluidResultControls'
    }

    attribute_map = {
        'type': 'type',
        'turbulence_model': 'turbulenceModel',
        'time_dependency': 'timeDependency',
        'model': 'model',
        'materials': 'materials',
        'initial_conditions': 'initialConditions',
        'boundary_conditions': 'boundaryConditions',
        'advanced_concepts': 'advancedConcepts',
        'numerics': 'numerics',
        'simulation_control': 'simulationControl',
        'result_control': 'resultControl'
    }

    def __init__(self, type='COMPRESSIBLE', turbulence_model=None, time_dependency=None, model=None, materials=None, initial_conditions=None, boundary_conditions=None, advanced_concepts=None, numerics=None, simulation_control=None, result_control=None, local_vars_configuration=None):  # noqa: E501
        """Compressible - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._turbulence_model = None
        self._time_dependency = None
        self._model = None
        self._materials = None
        self._initial_conditions = None
        self._boundary_conditions = None
        self._advanced_concepts = None
        self._numerics = None
        self._simulation_control = None
        self._result_control = None
        self.discriminator = None

        self.type = type
        if turbulence_model is not None:
            self.turbulence_model = turbulence_model
        if time_dependency is not None:
            self.time_dependency = time_dependency
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

    @property
    def type(self):
        """Gets the type of this Compressible.  # noqa: E501

        Schema name: Compressible  # noqa: E501

        :return: The type of this Compressible.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Compressible.

        Schema name: Compressible  # noqa: E501

        :param type: The type of this Compressible.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def turbulence_model(self):
        """Gets the turbulence_model of this Compressible.  # noqa: E501

        Choose a turbulence model for your CFD analysis:<ul><li><strong>No turbulence</strong>: Laminar</li><li><strong>RANS</strong>: <a href='https://www.simscale.com/docs/simulation-setup/global-settings/k-epsilon/#standard-k-epsilon-model' target='_blank'>k-epsilon</a>, <a href='https://www.simscale.com/docs/simulation-setup/global-settings/k-epsilon/#realizable-k-epsilon-model' target='_blank'>Realizable k-epsilon</a>, <a href='https://www.simscale.com/docs/simulation-setup/global-settings/k-omega-sst/' target='_blank'>k-omega and k-omega SST</a></li><li><strong>LES</strong>: Smagorinsky, Spalart-Allmaras</li></ul><p><p><a href='https://www.simscale.com/blog/2017/12/turbulence-cfd-analysis/' target='_blank'>Learn more</a>.</p>  # noqa: E501

        :return: The turbulence_model of this Compressible.  # noqa: E501
        :rtype: str
        """
        return self._turbulence_model

    @turbulence_model.setter
    def turbulence_model(self, turbulence_model):
        """Sets the turbulence_model of this Compressible.

        Choose a turbulence model for your CFD analysis:<ul><li><strong>No turbulence</strong>: Laminar</li><li><strong>RANS</strong>: <a href='https://www.simscale.com/docs/simulation-setup/global-settings/k-epsilon/#standard-k-epsilon-model' target='_blank'>k-epsilon</a>, <a href='https://www.simscale.com/docs/simulation-setup/global-settings/k-epsilon/#realizable-k-epsilon-model' target='_blank'>Realizable k-epsilon</a>, <a href='https://www.simscale.com/docs/simulation-setup/global-settings/k-omega-sst/' target='_blank'>k-omega and k-omega SST</a></li><li><strong>LES</strong>: Smagorinsky, Spalart-Allmaras</li></ul><p><p><a href='https://www.simscale.com/blog/2017/12/turbulence-cfd-analysis/' target='_blank'>Learn more</a>.</p>  # noqa: E501

        :param turbulence_model: The turbulence_model of this Compressible.  # noqa: E501
        :type: str
        """
        allowed_values = ["SMAGORINSKY", "SPALARTALLMARAS", "NONE", "KEPSILON", "KOMEGASST"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and turbulence_model not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `turbulence_model` ({0}), must be one of {1}"  # noqa: E501
                .format(turbulence_model, allowed_values)
            )

        self._turbulence_model = turbulence_model

    @property
    def time_dependency(self):
        """Gets the time_dependency of this Compressible.  # noqa: E501


        :return: The time_dependency of this Compressible.  # noqa: E501
        :rtype: OneOfCompressibleTimeDependency
        """
        return self._time_dependency

    @time_dependency.setter
    def time_dependency(self, time_dependency):
        """Sets the time_dependency of this Compressible.


        :param time_dependency: The time_dependency of this Compressible.  # noqa: E501
        :type: OneOfCompressibleTimeDependency
        """

        self._time_dependency = time_dependency

    @property
    def model(self):
        """Gets the model of this Compressible.  # noqa: E501


        :return: The model of this Compressible.  # noqa: E501
        :rtype: FluidModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Compressible.


        :param model: The model of this Compressible.  # noqa: E501
        :type: FluidModel
        """

        self._model = model

    @property
    def materials(self):
        """Gets the materials of this Compressible.  # noqa: E501


        :return: The materials of this Compressible.  # noqa: E501
        :rtype: CompressibleFluidMaterials
        """
        return self._materials

    @materials.setter
    def materials(self, materials):
        """Sets the materials of this Compressible.


        :param materials: The materials of this Compressible.  # noqa: E501
        :type: CompressibleFluidMaterials
        """

        self._materials = materials

    @property
    def initial_conditions(self):
        """Gets the initial_conditions of this Compressible.  # noqa: E501


        :return: The initial_conditions of this Compressible.  # noqa: E501
        :rtype: FluidInitialConditions
        """
        return self._initial_conditions

    @initial_conditions.setter
    def initial_conditions(self, initial_conditions):
        """Sets the initial_conditions of this Compressible.


        :param initial_conditions: The initial_conditions of this Compressible.  # noqa: E501
        :type: FluidInitialConditions
        """

        self._initial_conditions = initial_conditions

    @property
    def boundary_conditions(self):
        """Gets the boundary_conditions of this Compressible.  # noqa: E501


        :return: The boundary_conditions of this Compressible.  # noqa: E501
        :rtype: list[OneOfCompressibleBoundaryConditions]
        """
        return self._boundary_conditions

    @boundary_conditions.setter
    def boundary_conditions(self, boundary_conditions):
        """Sets the boundary_conditions of this Compressible.


        :param boundary_conditions: The boundary_conditions of this Compressible.  # noqa: E501
        :type: list[OneOfCompressibleBoundaryConditions]
        """

        self._boundary_conditions = boundary_conditions

    @property
    def advanced_concepts(self):
        """Gets the advanced_concepts of this Compressible.  # noqa: E501


        :return: The advanced_concepts of this Compressible.  # noqa: E501
        :rtype: AdvancedConcepts
        """
        return self._advanced_concepts

    @advanced_concepts.setter
    def advanced_concepts(self, advanced_concepts):
        """Sets the advanced_concepts of this Compressible.


        :param advanced_concepts: The advanced_concepts of this Compressible.  # noqa: E501
        :type: AdvancedConcepts
        """

        self._advanced_concepts = advanced_concepts

    @property
    def numerics(self):
        """Gets the numerics of this Compressible.  # noqa: E501


        :return: The numerics of this Compressible.  # noqa: E501
        :rtype: FluidNumerics
        """
        return self._numerics

    @numerics.setter
    def numerics(self, numerics):
        """Sets the numerics of this Compressible.


        :param numerics: The numerics of this Compressible.  # noqa: E501
        :type: FluidNumerics
        """

        self._numerics = numerics

    @property
    def simulation_control(self):
        """Gets the simulation_control of this Compressible.  # noqa: E501


        :return: The simulation_control of this Compressible.  # noqa: E501
        :rtype: FluidSimulationControl
        """
        return self._simulation_control

    @simulation_control.setter
    def simulation_control(self, simulation_control):
        """Sets the simulation_control of this Compressible.


        :param simulation_control: The simulation_control of this Compressible.  # noqa: E501
        :type: FluidSimulationControl
        """

        self._simulation_control = simulation_control

    @property
    def result_control(self):
        """Gets the result_control of this Compressible.  # noqa: E501


        :return: The result_control of this Compressible.  # noqa: E501
        :rtype: FluidResultControls
        """
        return self._result_control

    @result_control.setter
    def result_control(self, result_control):
        """Sets the result_control of this Compressible.


        :param result_control: The result_control of this Compressible.  # noqa: E501
        :type: FluidResultControls
        """

        self._result_control = result_control

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
        if not isinstance(other, Compressible):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Compressible):
            return True

        return self.to_dict() != other.to_dict()
