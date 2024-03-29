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


class SurfaceLoadBC(object):
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
        'load': 'DimensionalVectorFunctionPressure',
        'scaling': 'DimensionalFunctionDimensionless',
        'phase_angle': 'DimensionalAngle',
        'topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'load': 'load',
        'scaling': 'scaling',
        'phase_angle': 'phaseAngle',
        'topological_reference': 'topologicalReference'
    }

    def __init__(self, type='SURFACE_LOAD', name=None, load=None, scaling=None, phase_angle=None, topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """SurfaceLoadBC - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._load = None
        self._scaling = None
        self._phase_angle = None
        self._topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if load is not None:
            self.load = load
        if scaling is not None:
            self.scaling = scaling
        if phase_angle is not None:
            self.phase_angle = phase_angle
        if topological_reference is not None:
            self.topological_reference = topological_reference

    @property
    def type(self):
        """Gets the type of this SurfaceLoadBC.  # noqa: E501

        This is a <b>surface load</b> boundary condition representing a distributed load on the selection. It is applied as surface traction in the global coordinate system.<br /><br />Important remarks: <br /><ul><li>The applied total force depends on the surface area of the selection</li></ul><a href= https://www.simscale.com/docs/simulation-setup/boundary-conditions/surface-load/' target='_blank'>Learn more</a>.  Schema name: SurfaceLoadBC  # noqa: E501

        :return: The type of this SurfaceLoadBC.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SurfaceLoadBC.

        This is a <b>surface load</b> boundary condition representing a distributed load on the selection. It is applied as surface traction in the global coordinate system.<br /><br />Important remarks: <br /><ul><li>The applied total force depends on the surface area of the selection</li></ul><a href= https://www.simscale.com/docs/simulation-setup/boundary-conditions/surface-load/' target='_blank'>Learn more</a>.  Schema name: SurfaceLoadBC  # noqa: E501

        :param type: The type of this SurfaceLoadBC.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this SurfaceLoadBC.  # noqa: E501


        :return: The name of this SurfaceLoadBC.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SurfaceLoadBC.


        :param name: The name of this SurfaceLoadBC.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def load(self):
        """Gets the load of this SurfaceLoadBC.  # noqa: E501


        :return: The load of this SurfaceLoadBC.  # noqa: E501
        :rtype: DimensionalVectorFunctionPressure
        """
        return self._load

    @load.setter
    def load(self, load):
        """Sets the load of this SurfaceLoadBC.


        :param load: The load of this SurfaceLoadBC.  # noqa: E501
        :type: DimensionalVectorFunctionPressure
        """

        self._load = load

    @property
    def scaling(self):
        """Gets the scaling of this SurfaceLoadBC.  # noqa: E501


        :return: The scaling of this SurfaceLoadBC.  # noqa: E501
        :rtype: DimensionalFunctionDimensionless
        """
        return self._scaling

    @scaling.setter
    def scaling(self, scaling):
        """Sets the scaling of this SurfaceLoadBC.


        :param scaling: The scaling of this SurfaceLoadBC.  # noqa: E501
        :type: DimensionalFunctionDimensionless
        """

        self._scaling = scaling

    @property
    def phase_angle(self):
        """Gets the phase_angle of this SurfaceLoadBC.  # noqa: E501


        :return: The phase_angle of this SurfaceLoadBC.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._phase_angle

    @phase_angle.setter
    def phase_angle(self, phase_angle):
        """Sets the phase_angle of this SurfaceLoadBC.


        :param phase_angle: The phase_angle of this SurfaceLoadBC.  # noqa: E501
        :type: DimensionalAngle
        """

        self._phase_angle = phase_angle

    @property
    def topological_reference(self):
        """Gets the topological_reference of this SurfaceLoadBC.  # noqa: E501


        :return: The topological_reference of this SurfaceLoadBC.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this SurfaceLoadBC.


        :param topological_reference: The topological_reference of this SurfaceLoadBC.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

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
        if not isinstance(other, SurfaceLoadBC):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SurfaceLoadBC):
            return True

        return self.to_dict() != other.to_dict()
