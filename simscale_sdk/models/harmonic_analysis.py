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


class HarmonicAnalysis(object):
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
        'connection_groups': 'list[Contact]',
        'connectors': 'list[PinConnector]',
        'element_technology': 'SolidElementTechnology',
        'model': 'SolidModel',
        'materials': 'list[SolidMaterial]',
        'initial_conditions': 'SolidInitialConditions',
        'boundary_conditions': 'list[OneOfHarmonicAnalysisBoundaryConditions]',
        'numerics': 'SolidNumerics',
        'simulation_control': 'SolidSimulationControl',
        'result_control': 'SolidResultControl',
        'mesh_order': 'str'
    }

    attribute_map = {
        'type': 'type',
        'connection_groups': 'connectionGroups',
        'connectors': 'connectors',
        'element_technology': 'elementTechnology',
        'model': 'model',
        'materials': 'materials',
        'initial_conditions': 'initialConditions',
        'boundary_conditions': 'boundaryConditions',
        'numerics': 'numerics',
        'simulation_control': 'simulationControl',
        'result_control': 'resultControl',
        'mesh_order': 'meshOrder'
    }

    def __init__(self, type='HARMONIC_ANALYSIS', connection_groups=None, connectors=None, element_technology=None, model=None, materials=None, initial_conditions=None, boundary_conditions=None, numerics=None, simulation_control=None, result_control=None, mesh_order=None, local_vars_configuration=None):  # noqa: E501
        """HarmonicAnalysis - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._connection_groups = None
        self._connectors = None
        self._element_technology = None
        self._model = None
        self._materials = None
        self._initial_conditions = None
        self._boundary_conditions = None
        self._numerics = None
        self._simulation_control = None
        self._result_control = None
        self._mesh_order = None
        self.discriminator = None

        self.type = type
        if connection_groups is not None:
            self.connection_groups = connection_groups
        if connectors is not None:
            self.connectors = connectors
        if element_technology is not None:
            self.element_technology = element_technology
        if model is not None:
            self.model = model
        if materials is not None:
            self.materials = materials
        if initial_conditions is not None:
            self.initial_conditions = initial_conditions
        if boundary_conditions is not None:
            self.boundary_conditions = boundary_conditions
        if numerics is not None:
            self.numerics = numerics
        if simulation_control is not None:
            self.simulation_control = simulation_control
        if result_control is not None:
            self.result_control = result_control
        if mesh_order is not None:
            self.mesh_order = mesh_order

    @property
    def type(self):
        """Gets the type of this HarmonicAnalysis.  # noqa: E501

        Schema name: HarmonicAnalysis  # noqa: E501

        :return: The type of this HarmonicAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HarmonicAnalysis.

        Schema name: HarmonicAnalysis  # noqa: E501

        :param type: The type of this HarmonicAnalysis.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def connection_groups(self):
        """Gets the connection_groups of this HarmonicAnalysis.  # noqa: E501


        :return: The connection_groups of this HarmonicAnalysis.  # noqa: E501
        :rtype: list[Contact]
        """
        return self._connection_groups

    @connection_groups.setter
    def connection_groups(self, connection_groups):
        """Sets the connection_groups of this HarmonicAnalysis.


        :param connection_groups: The connection_groups of this HarmonicAnalysis.  # noqa: E501
        :type: list[Contact]
        """

        self._connection_groups = connection_groups

    @property
    def connectors(self):
        """Gets the connectors of this HarmonicAnalysis.  # noqa: E501


        :return: The connectors of this HarmonicAnalysis.  # noqa: E501
        :rtype: list[PinConnector]
        """
        return self._connectors

    @connectors.setter
    def connectors(self, connectors):
        """Sets the connectors of this HarmonicAnalysis.


        :param connectors: The connectors of this HarmonicAnalysis.  # noqa: E501
        :type: list[PinConnector]
        """

        self._connectors = connectors

    @property
    def element_technology(self):
        """Gets the element_technology of this HarmonicAnalysis.  # noqa: E501


        :return: The element_technology of this HarmonicAnalysis.  # noqa: E501
        :rtype: SolidElementTechnology
        """
        return self._element_technology

    @element_technology.setter
    def element_technology(self, element_technology):
        """Sets the element_technology of this HarmonicAnalysis.


        :param element_technology: The element_technology of this HarmonicAnalysis.  # noqa: E501
        :type: SolidElementTechnology
        """

        self._element_technology = element_technology

    @property
    def model(self):
        """Gets the model of this HarmonicAnalysis.  # noqa: E501


        :return: The model of this HarmonicAnalysis.  # noqa: E501
        :rtype: SolidModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this HarmonicAnalysis.


        :param model: The model of this HarmonicAnalysis.  # noqa: E501
        :type: SolidModel
        """

        self._model = model

    @property
    def materials(self):
        """Gets the materials of this HarmonicAnalysis.  # noqa: E501


        :return: The materials of this HarmonicAnalysis.  # noqa: E501
        :rtype: list[SolidMaterial]
        """
        return self._materials

    @materials.setter
    def materials(self, materials):
        """Sets the materials of this HarmonicAnalysis.


        :param materials: The materials of this HarmonicAnalysis.  # noqa: E501
        :type: list[SolidMaterial]
        """

        self._materials = materials

    @property
    def initial_conditions(self):
        """Gets the initial_conditions of this HarmonicAnalysis.  # noqa: E501


        :return: The initial_conditions of this HarmonicAnalysis.  # noqa: E501
        :rtype: SolidInitialConditions
        """
        return self._initial_conditions

    @initial_conditions.setter
    def initial_conditions(self, initial_conditions):
        """Sets the initial_conditions of this HarmonicAnalysis.


        :param initial_conditions: The initial_conditions of this HarmonicAnalysis.  # noqa: E501
        :type: SolidInitialConditions
        """

        self._initial_conditions = initial_conditions

    @property
    def boundary_conditions(self):
        """Gets the boundary_conditions of this HarmonicAnalysis.  # noqa: E501


        :return: The boundary_conditions of this HarmonicAnalysis.  # noqa: E501
        :rtype: list[OneOfHarmonicAnalysisBoundaryConditions]
        """
        return self._boundary_conditions

    @boundary_conditions.setter
    def boundary_conditions(self, boundary_conditions):
        """Sets the boundary_conditions of this HarmonicAnalysis.


        :param boundary_conditions: The boundary_conditions of this HarmonicAnalysis.  # noqa: E501
        :type: list[OneOfHarmonicAnalysisBoundaryConditions]
        """

        self._boundary_conditions = boundary_conditions

    @property
    def numerics(self):
        """Gets the numerics of this HarmonicAnalysis.  # noqa: E501


        :return: The numerics of this HarmonicAnalysis.  # noqa: E501
        :rtype: SolidNumerics
        """
        return self._numerics

    @numerics.setter
    def numerics(self, numerics):
        """Sets the numerics of this HarmonicAnalysis.


        :param numerics: The numerics of this HarmonicAnalysis.  # noqa: E501
        :type: SolidNumerics
        """

        self._numerics = numerics

    @property
    def simulation_control(self):
        """Gets the simulation_control of this HarmonicAnalysis.  # noqa: E501


        :return: The simulation_control of this HarmonicAnalysis.  # noqa: E501
        :rtype: SolidSimulationControl
        """
        return self._simulation_control

    @simulation_control.setter
    def simulation_control(self, simulation_control):
        """Sets the simulation_control of this HarmonicAnalysis.


        :param simulation_control: The simulation_control of this HarmonicAnalysis.  # noqa: E501
        :type: SolidSimulationControl
        """

        self._simulation_control = simulation_control

    @property
    def result_control(self):
        """Gets the result_control of this HarmonicAnalysis.  # noqa: E501


        :return: The result_control of this HarmonicAnalysis.  # noqa: E501
        :rtype: SolidResultControl
        """
        return self._result_control

    @result_control.setter
    def result_control(self, result_control):
        """Sets the result_control of this HarmonicAnalysis.


        :param result_control: The result_control of this HarmonicAnalysis.  # noqa: E501
        :type: SolidResultControl
        """

        self._result_control = result_control

    @property
    def mesh_order(self):
        """Gets the mesh_order of this HarmonicAnalysis.  # noqa: E501


        :return: The mesh_order of this HarmonicAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._mesh_order

    @mesh_order.setter
    def mesh_order(self, mesh_order):
        """Sets the mesh_order of this HarmonicAnalysis.


        :param mesh_order: The mesh_order of this HarmonicAnalysis.  # noqa: E501
        :type: str
        """
        allowed_values = ["FIRST", "SECOND", "NONE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mesh_order not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mesh_order` ({0}), must be one of {1}"  # noqa: E501
                .format(mesh_order, allowed_values)
            )

        self._mesh_order = mesh_order

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
        if not isinstance(other, HarmonicAnalysis):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HarmonicAnalysis):
            return True

        return self.to_dict() != other.to_dict()
