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


class SimericsAnalysis(object):
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
        'model': 'FluidModel',
        'materials': 'SimericsFluidMaterials',
        'is_compressible': 'bool',
        'is_multiphase': 'bool',
        'cavitation_model': 'str',
        'turbulence_model': 'str',
        'time_dependency': 'OneOfSimericsAnalysisTimeDependency',
        'boundary_conditions': 'list[OneOfSimericsAnalysisBoundaryConditions]',
        'advanced_concepts': 'AdvancedConcepts',
        'numerics': 'FluidNumerics',
        'simulation_control': 'FluidSimulationControl',
        'result_control': 'FluidResultControls',
        'mesh_settings': 'OneOfSimericsAnalysisMeshSettings'
    }

    attribute_map = {
        'type': 'type',
        'model': 'model',
        'materials': 'materials',
        'is_compressible': 'isCompressible',
        'is_multiphase': 'isMultiphase',
        'cavitation_model': 'cavitationModel',
        'turbulence_model': 'turbulenceModel',
        'time_dependency': 'timeDependency',
        'boundary_conditions': 'boundaryConditions',
        'advanced_concepts': 'advancedConcepts',
        'numerics': 'numerics',
        'simulation_control': 'simulationControl',
        'result_control': 'resultControl',
        'mesh_settings': 'meshSettings'
    }

    def __init__(self, type='SIMERICS_ANALYSIS', model=None, materials=None, is_compressible=None, is_multiphase=None, cavitation_model=None, turbulence_model=None, time_dependency=None, boundary_conditions=None, advanced_concepts=None, numerics=None, simulation_control=None, result_control=None, mesh_settings=None, local_vars_configuration=None):  # noqa: E501
        """SimericsAnalysis - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._model = None
        self._materials = None
        self._is_compressible = None
        self._is_multiphase = None
        self._cavitation_model = None
        self._turbulence_model = None
        self._time_dependency = None
        self._boundary_conditions = None
        self._advanced_concepts = None
        self._numerics = None
        self._simulation_control = None
        self._result_control = None
        self._mesh_settings = None
        self.discriminator = None

        self.type = type
        if model is not None:
            self.model = model
        if materials is not None:
            self.materials = materials
        if is_compressible is not None:
            self.is_compressible = is_compressible
        if is_multiphase is not None:
            self.is_multiphase = is_multiphase
        if cavitation_model is not None:
            self.cavitation_model = cavitation_model
        if turbulence_model is not None:
            self.turbulence_model = turbulence_model
        if time_dependency is not None:
            self.time_dependency = time_dependency
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
        if mesh_settings is not None:
            self.mesh_settings = mesh_settings

    @property
    def type(self):
        """Gets the type of this SimericsAnalysis.  # noqa: E501

        Schema name: SimericsAnalysis  # noqa: E501

        :return: The type of this SimericsAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SimericsAnalysis.

        Schema name: SimericsAnalysis  # noqa: E501

        :param type: The type of this SimericsAnalysis.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def model(self):
        """Gets the model of this SimericsAnalysis.  # noqa: E501


        :return: The model of this SimericsAnalysis.  # noqa: E501
        :rtype: FluidModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this SimericsAnalysis.


        :param model: The model of this SimericsAnalysis.  # noqa: E501
        :type: FluidModel
        """

        self._model = model

    @property
    def materials(self):
        """Gets the materials of this SimericsAnalysis.  # noqa: E501


        :return: The materials of this SimericsAnalysis.  # noqa: E501
        :rtype: SimericsFluidMaterials
        """
        return self._materials

    @materials.setter
    def materials(self, materials):
        """Sets the materials of this SimericsAnalysis.


        :param materials: The materials of this SimericsAnalysis.  # noqa: E501
        :type: SimericsFluidMaterials
        """

        self._materials = materials

    @property
    def is_compressible(self):
        """Gets the is_compressible of this SimericsAnalysis.  # noqa: E501


        :return: The is_compressible of this SimericsAnalysis.  # noqa: E501
        :rtype: bool
        """
        return self._is_compressible

    @is_compressible.setter
    def is_compressible(self, is_compressible):
        """Sets the is_compressible of this SimericsAnalysis.


        :param is_compressible: The is_compressible of this SimericsAnalysis.  # noqa: E501
        :type: bool
        """

        self._is_compressible = is_compressible

    @property
    def is_multiphase(self):
        """Gets the is_multiphase of this SimericsAnalysis.  # noqa: E501


        :return: The is_multiphase of this SimericsAnalysis.  # noqa: E501
        :rtype: bool
        """
        return self._is_multiphase

    @is_multiphase.setter
    def is_multiphase(self, is_multiphase):
        """Sets the is_multiphase of this SimericsAnalysis.


        :param is_multiphase: The is_multiphase of this SimericsAnalysis.  # noqa: E501
        :type: bool
        """

        self._is_multiphase = is_multiphase

    @property
    def cavitation_model(self):
        """Gets the cavitation_model of this SimericsAnalysis.  # noqa: E501


        :return: The cavitation_model of this SimericsAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._cavitation_model

    @cavitation_model.setter
    def cavitation_model(self, cavitation_model):
        """Sets the cavitation_model of this SimericsAnalysis.


        :param cavitation_model: The cavitation_model of this SimericsAnalysis.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONSTANT_GAS_MASS_FRACTION", "NONE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and cavitation_model not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `cavitation_model` ({0}), must be one of {1}"  # noqa: E501
                .format(cavitation_model, allowed_values)
            )

        self._cavitation_model = cavitation_model

    @property
    def turbulence_model(self):
        """Gets the turbulence_model of this SimericsAnalysis.  # noqa: E501

        Choose a turbulence model for your CFD analysis:<ul><li><strong>No turbulence</strong>: Laminar</li><li><strong>RANS</strong>: <a href='https://www.simscale.com/docs/simulation-setup/global-settings/k-epsilon/' target='_blank'>k-epsilon</a></ul><p><p><a href='https://www.simscale.com/blog/2017/12/turbulence-cfd-analysis/' target='_blank'>Learn more</a>.</p>  # noqa: E501

        :return: The turbulence_model of this SimericsAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._turbulence_model

    @turbulence_model.setter
    def turbulence_model(self, turbulence_model):
        """Sets the turbulence_model of this SimericsAnalysis.

        Choose a turbulence model for your CFD analysis:<ul><li><strong>No turbulence</strong>: Laminar</li><li><strong>RANS</strong>: <a href='https://www.simscale.com/docs/simulation-setup/global-settings/k-epsilon/' target='_blank'>k-epsilon</a></ul><p><p><a href='https://www.simscale.com/blog/2017/12/turbulence-cfd-analysis/' target='_blank'>Learn more</a>.</p>  # noqa: E501

        :param turbulence_model: The turbulence_model of this SimericsAnalysis.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "KEPSILON"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and turbulence_model not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `turbulence_model` ({0}), must be one of {1}"  # noqa: E501
                .format(turbulence_model, allowed_values)
            )

        self._turbulence_model = turbulence_model

    @property
    def time_dependency(self):
        """Gets the time_dependency of this SimericsAnalysis.  # noqa: E501


        :return: The time_dependency of this SimericsAnalysis.  # noqa: E501
        :rtype: OneOfSimericsAnalysisTimeDependency
        """
        return self._time_dependency

    @time_dependency.setter
    def time_dependency(self, time_dependency):
        """Sets the time_dependency of this SimericsAnalysis.


        :param time_dependency: The time_dependency of this SimericsAnalysis.  # noqa: E501
        :type: OneOfSimericsAnalysisTimeDependency
        """

        self._time_dependency = time_dependency

    @property
    def boundary_conditions(self):
        """Gets the boundary_conditions of this SimericsAnalysis.  # noqa: E501


        :return: The boundary_conditions of this SimericsAnalysis.  # noqa: E501
        :rtype: list[OneOfSimericsAnalysisBoundaryConditions]
        """
        return self._boundary_conditions

    @boundary_conditions.setter
    def boundary_conditions(self, boundary_conditions):
        """Sets the boundary_conditions of this SimericsAnalysis.


        :param boundary_conditions: The boundary_conditions of this SimericsAnalysis.  # noqa: E501
        :type: list[OneOfSimericsAnalysisBoundaryConditions]
        """

        self._boundary_conditions = boundary_conditions

    @property
    def advanced_concepts(self):
        """Gets the advanced_concepts of this SimericsAnalysis.  # noqa: E501


        :return: The advanced_concepts of this SimericsAnalysis.  # noqa: E501
        :rtype: AdvancedConcepts
        """
        return self._advanced_concepts

    @advanced_concepts.setter
    def advanced_concepts(self, advanced_concepts):
        """Sets the advanced_concepts of this SimericsAnalysis.


        :param advanced_concepts: The advanced_concepts of this SimericsAnalysis.  # noqa: E501
        :type: AdvancedConcepts
        """

        self._advanced_concepts = advanced_concepts

    @property
    def numerics(self):
        """Gets the numerics of this SimericsAnalysis.  # noqa: E501


        :return: The numerics of this SimericsAnalysis.  # noqa: E501
        :rtype: FluidNumerics
        """
        return self._numerics

    @numerics.setter
    def numerics(self, numerics):
        """Sets the numerics of this SimericsAnalysis.


        :param numerics: The numerics of this SimericsAnalysis.  # noqa: E501
        :type: FluidNumerics
        """

        self._numerics = numerics

    @property
    def simulation_control(self):
        """Gets the simulation_control of this SimericsAnalysis.  # noqa: E501


        :return: The simulation_control of this SimericsAnalysis.  # noqa: E501
        :rtype: FluidSimulationControl
        """
        return self._simulation_control

    @simulation_control.setter
    def simulation_control(self, simulation_control):
        """Sets the simulation_control of this SimericsAnalysis.


        :param simulation_control: The simulation_control of this SimericsAnalysis.  # noqa: E501
        :type: FluidSimulationControl
        """

        self._simulation_control = simulation_control

    @property
    def result_control(self):
        """Gets the result_control of this SimericsAnalysis.  # noqa: E501


        :return: The result_control of this SimericsAnalysis.  # noqa: E501
        :rtype: FluidResultControls
        """
        return self._result_control

    @result_control.setter
    def result_control(self, result_control):
        """Sets the result_control of this SimericsAnalysis.


        :param result_control: The result_control of this SimericsAnalysis.  # noqa: E501
        :type: FluidResultControls
        """

        self._result_control = result_control

    @property
    def mesh_settings(self):
        """Gets the mesh_settings of this SimericsAnalysis.  # noqa: E501


        :return: The mesh_settings of this SimericsAnalysis.  # noqa: E501
        :rtype: OneOfSimericsAnalysisMeshSettings
        """
        return self._mesh_settings

    @mesh_settings.setter
    def mesh_settings(self, mesh_settings):
        """Sets the mesh_settings of this SimericsAnalysis.


        :param mesh_settings: The mesh_settings of this SimericsAnalysis.  # noqa: E501
        :type: OneOfSimericsAnalysisMeshSettings
        """

        self._mesh_settings = mesh_settings

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
        if not isinstance(other, SimericsAnalysis):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimericsAnalysis):
            return True

        return self.to_dict() != other.to_dict()
