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


class ElectromagneticAnalysis(object):
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
        'dominant_field': 'str',
        'time_dependency': 'StationaryTimeDependency',
        'materials': 'list[ElectromagneticMaterial]',
        'coils': 'list[Coil]',
        'boundary_conditions': 'list[OneOfElectromagneticAnalysisBoundaryConditions]',
        'result_control': 'ElectromagneticResultControl',
        'numerics': 'ElectromagneticNumerics',
        'simulation_control': 'ElectromagneticSimulationControl'
    }

    attribute_map = {
        'type': 'type',
        'dominant_field': 'dominantField',
        'time_dependency': 'timeDependency',
        'materials': 'materials',
        'coils': 'coils',
        'boundary_conditions': 'boundaryConditions',
        'result_control': 'resultControl',
        'numerics': 'numerics',
        'simulation_control': 'simulationControl'
    }

    def __init__(self, type='ELECTROMAGNETIC_ANALYSIS', dominant_field=None, time_dependency=None, materials=None, coils=None, boundary_conditions=None, result_control=None, numerics=None, simulation_control=None, local_vars_configuration=None):  # noqa: E501
        """ElectromagneticAnalysis - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._dominant_field = None
        self._time_dependency = None
        self._materials = None
        self._coils = None
        self._boundary_conditions = None
        self._result_control = None
        self._numerics = None
        self._simulation_control = None
        self.discriminator = None

        self.type = type
        if dominant_field is not None:
            self.dominant_field = dominant_field
        if time_dependency is not None:
            self.time_dependency = time_dependency
        if materials is not None:
            self.materials = materials
        if coils is not None:
            self.coils = coils
        if boundary_conditions is not None:
            self.boundary_conditions = boundary_conditions
        if result_control is not None:
            self.result_control = result_control
        if numerics is not None:
            self.numerics = numerics
        if simulation_control is not None:
            self.simulation_control = simulation_control

    @property
    def type(self):
        """Gets the type of this ElectromagneticAnalysis.  # noqa: E501

        Schema name: ElectromagneticAnalysis  # noqa: E501

        :return: The type of this ElectromagneticAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ElectromagneticAnalysis.

        Schema name: ElectromagneticAnalysis  # noqa: E501

        :param type: The type of this ElectromagneticAnalysis.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def dominant_field(self):
        """Gets the dominant_field of this ElectromagneticAnalysis.  # noqa: E501


        :return: The dominant_field of this ElectromagneticAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._dominant_field

    @dominant_field.setter
    def dominant_field(self, dominant_field):
        """Sets the dominant_field of this ElectromagneticAnalysis.


        :param dominant_field: The dominant_field of this ElectromagneticAnalysis.  # noqa: E501
        :type: str
        """
        allowed_values = ["MAGNETIC"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and dominant_field not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `dominant_field` ({0}), must be one of {1}"  # noqa: E501
                .format(dominant_field, allowed_values)
            )

        self._dominant_field = dominant_field

    @property
    def time_dependency(self):
        """Gets the time_dependency of this ElectromagneticAnalysis.  # noqa: E501


        :return: The time_dependency of this ElectromagneticAnalysis.  # noqa: E501
        :rtype: StationaryTimeDependency
        """
        return self._time_dependency

    @time_dependency.setter
    def time_dependency(self, time_dependency):
        """Sets the time_dependency of this ElectromagneticAnalysis.


        :param time_dependency: The time_dependency of this ElectromagneticAnalysis.  # noqa: E501
        :type: StationaryTimeDependency
        """

        self._time_dependency = time_dependency

    @property
    def materials(self):
        """Gets the materials of this ElectromagneticAnalysis.  # noqa: E501


        :return: The materials of this ElectromagneticAnalysis.  # noqa: E501
        :rtype: list[ElectromagneticMaterial]
        """
        return self._materials

    @materials.setter
    def materials(self, materials):
        """Sets the materials of this ElectromagneticAnalysis.


        :param materials: The materials of this ElectromagneticAnalysis.  # noqa: E501
        :type: list[ElectromagneticMaterial]
        """

        self._materials = materials

    @property
    def coils(self):
        """Gets the coils of this ElectromagneticAnalysis.  # noqa: E501


        :return: The coils of this ElectromagneticAnalysis.  # noqa: E501
        :rtype: list[Coil]
        """
        return self._coils

    @coils.setter
    def coils(self, coils):
        """Sets the coils of this ElectromagneticAnalysis.


        :param coils: The coils of this ElectromagneticAnalysis.  # noqa: E501
        :type: list[Coil]
        """

        self._coils = coils

    @property
    def boundary_conditions(self):
        """Gets the boundary_conditions of this ElectromagneticAnalysis.  # noqa: E501


        :return: The boundary_conditions of this ElectromagneticAnalysis.  # noqa: E501
        :rtype: list[OneOfElectromagneticAnalysisBoundaryConditions]
        """
        return self._boundary_conditions

    @boundary_conditions.setter
    def boundary_conditions(self, boundary_conditions):
        """Sets the boundary_conditions of this ElectromagneticAnalysis.


        :param boundary_conditions: The boundary_conditions of this ElectromagneticAnalysis.  # noqa: E501
        :type: list[OneOfElectromagneticAnalysisBoundaryConditions]
        """

        self._boundary_conditions = boundary_conditions

    @property
    def result_control(self):
        """Gets the result_control of this ElectromagneticAnalysis.  # noqa: E501


        :return: The result_control of this ElectromagneticAnalysis.  # noqa: E501
        :rtype: ElectromagneticResultControl
        """
        return self._result_control

    @result_control.setter
    def result_control(self, result_control):
        """Sets the result_control of this ElectromagneticAnalysis.


        :param result_control: The result_control of this ElectromagneticAnalysis.  # noqa: E501
        :type: ElectromagneticResultControl
        """

        self._result_control = result_control

    @property
    def numerics(self):
        """Gets the numerics of this ElectromagneticAnalysis.  # noqa: E501


        :return: The numerics of this ElectromagneticAnalysis.  # noqa: E501
        :rtype: ElectromagneticNumerics
        """
        return self._numerics

    @numerics.setter
    def numerics(self, numerics):
        """Sets the numerics of this ElectromagneticAnalysis.


        :param numerics: The numerics of this ElectromagneticAnalysis.  # noqa: E501
        :type: ElectromagneticNumerics
        """

        self._numerics = numerics

    @property
    def simulation_control(self):
        """Gets the simulation_control of this ElectromagneticAnalysis.  # noqa: E501


        :return: The simulation_control of this ElectromagneticAnalysis.  # noqa: E501
        :rtype: ElectromagneticSimulationControl
        """
        return self._simulation_control

    @simulation_control.setter
    def simulation_control(self, simulation_control):
        """Sets the simulation_control of this ElectromagneticAnalysis.


        :param simulation_control: The simulation_control of this ElectromagneticAnalysis.  # noqa: E501
        :type: ElectromagneticSimulationControl
        """

        self._simulation_control = simulation_control

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
        if not isinstance(other, ElectromagneticAnalysis):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElectromagneticAnalysis):
            return True

        return self.to_dict() != other.to_dict()
