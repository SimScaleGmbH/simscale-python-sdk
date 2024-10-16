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


class OneOfFrequencyAnalysisBoundaryConditions(object):
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
        'preload': 'ForcePreload',
        'topological_reference': 'TopologicalReference',
        'spring_stiffness': 'OneOfElasticSupportBCSpringStiffness',
        'displacement': 'DimensionalPartialVectorFunctionLength',
        'mass': 'DimensionalMass',
        'mass_moment_of_inertia': 'DimensionalVectorMomentOfInertia',
        'external_point': 'DimensionalVectorLength',
        'deformation_behavior': 'str',
        'enable_search_radius': 'bool',
        'search_radius': 'DimensionalLength',
        'rotation': 'AngularRotation'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'preload': 'preload',
        'topological_reference': 'topologicalReference',
        'spring_stiffness': 'springStiffness',
        'displacement': 'displacement',
        'mass': 'mass',
        'mass_moment_of_inertia': 'massMomentOfInertia',
        'external_point': 'externalPoint',
        'deformation_behavior': 'deformationBehavior',
        'enable_search_radius': 'enableSearchRadius',
        'search_radius': 'searchRadius',
        'rotation': 'rotation'
    }

    discriminator_value_class_map = {
        'BOLT_PRELOAD': 'BoltPreloadBC',
        'ELASTIC_SUPPORT': 'ElasticSupportBC',
        'FIXED_SUPPORT': 'FixedSupportBC',
        'FIXED_VALUE': 'FixedValueBC',
        'POINT_MASS': 'PointMassBC',
        'REMOTE_DISPLACEMENT_LOAD': 'RemoteDisplacementLoadBC',
        'SYMMETRY_PLANE': 'SymmetryPlaneBC',
        'CENTRIFUGAL_FORCE': 'CentrifugalForceBC'
    }

    def __init__(self, type='CENTRIFUGAL_FORCE', name=None, preload=None, topological_reference=None, spring_stiffness=None, displacement=None, mass=None, mass_moment_of_inertia=None, external_point=None, deformation_behavior=None, enable_search_radius=None, search_radius=None, rotation=None, local_vars_configuration=None):  # noqa: E501
        """OneOfFrequencyAnalysisBoundaryConditions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._preload = None
        self._topological_reference = None
        self._spring_stiffness = None
        self._displacement = None
        self._mass = None
        self._mass_moment_of_inertia = None
        self._external_point = None
        self._deformation_behavior = None
        self._enable_search_radius = None
        self._search_radius = None
        self._rotation = None
        self.discriminator = 'type'

        self.type = type
        if name is not None:
            self.name = name
        if preload is not None:
            self.preload = preload
        if topological_reference is not None:
            self.topological_reference = topological_reference
        if spring_stiffness is not None:
            self.spring_stiffness = spring_stiffness
        if displacement is not None:
            self.displacement = displacement
        if mass is not None:
            self.mass = mass
        if mass_moment_of_inertia is not None:
            self.mass_moment_of_inertia = mass_moment_of_inertia
        if external_point is not None:
            self.external_point = external_point
        if deformation_behavior is not None:
            self.deformation_behavior = deformation_behavior
        if enable_search_radius is not None:
            self.enable_search_radius = enable_search_radius
        if search_radius is not None:
            self.search_radius = search_radius
        if rotation is not None:
            self.rotation = rotation

    @property
    def type(self):
        """Gets the type of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501

        <p>This is a <b>centrifugal force</b> boundary condition. Each volume element of the selection is loaded with a centrifugal force which is calculated depending on its volume, the density of the assigned material, its distance from the axis of rotation and the defined rotational velocity.<br /><a href= https://www.simscale.com/docs/simulation-setup/boundary-conditions/centrifugal-force/' target='_blank'>Learn more</a>.</p>  Schema name: CentrifugalForceBC  # noqa: E501

        :return: The type of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfFrequencyAnalysisBoundaryConditions.

        <p>This is a <b>centrifugal force</b> boundary condition. Each volume element of the selection is loaded with a centrifugal force which is calculated depending on its volume, the density of the assigned material, its distance from the axis of rotation and the defined rotational velocity.<br /><a href= https://www.simscale.com/docs/simulation-setup/boundary-conditions/centrifugal-force/' target='_blank'>Learn more</a>.</p>  Schema name: CentrifugalForceBC  # noqa: E501

        :param type: The type of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501


        :return: The name of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfFrequencyAnalysisBoundaryConditions.


        :param name: The name of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def preload(self):
        """Gets the preload of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501


        :return: The preload of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :rtype: ForcePreload
        """
        return self._preload

    @preload.setter
    def preload(self, preload):
        """Sets the preload of this OneOfFrequencyAnalysisBoundaryConditions.


        :param preload: The preload of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :type: ForcePreload
        """

        self._preload = preload

    @property
    def topological_reference(self):
        """Gets the topological_reference of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501


        :return: The topological_reference of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this OneOfFrequencyAnalysisBoundaryConditions.


        :param topological_reference: The topological_reference of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def spring_stiffness(self):
        """Gets the spring_stiffness of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501


        :return: The spring_stiffness of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :rtype: OneOfElasticSupportBCSpringStiffness
        """
        return self._spring_stiffness

    @spring_stiffness.setter
    def spring_stiffness(self, spring_stiffness):
        """Sets the spring_stiffness of this OneOfFrequencyAnalysisBoundaryConditions.


        :param spring_stiffness: The spring_stiffness of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :type: OneOfElasticSupportBCSpringStiffness
        """

        self._spring_stiffness = spring_stiffness

    @property
    def displacement(self):
        """Gets the displacement of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501


        :return: The displacement of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalPartialVectorFunctionLength
        """
        return self._displacement

    @displacement.setter
    def displacement(self, displacement):
        """Sets the displacement of this OneOfFrequencyAnalysisBoundaryConditions.


        :param displacement: The displacement of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalPartialVectorFunctionLength
        """

        self._displacement = displacement

    @property
    def mass(self):
        """Gets the mass of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501


        :return: The mass of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalMass
        """
        return self._mass

    @mass.setter
    def mass(self, mass):
        """Sets the mass of this OneOfFrequencyAnalysisBoundaryConditions.


        :param mass: The mass of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalMass
        """

        self._mass = mass

    @property
    def mass_moment_of_inertia(self):
        """Gets the mass_moment_of_inertia of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501


        :return: The mass_moment_of_inertia of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalVectorMomentOfInertia
        """
        return self._mass_moment_of_inertia

    @mass_moment_of_inertia.setter
    def mass_moment_of_inertia(self, mass_moment_of_inertia):
        """Sets the mass_moment_of_inertia of this OneOfFrequencyAnalysisBoundaryConditions.


        :param mass_moment_of_inertia: The mass_moment_of_inertia of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalVectorMomentOfInertia
        """

        self._mass_moment_of_inertia = mass_moment_of_inertia

    @property
    def external_point(self):
        """Gets the external_point of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501


        :return: The external_point of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._external_point

    @external_point.setter
    def external_point(self, external_point):
        """Sets the external_point of this OneOfFrequencyAnalysisBoundaryConditions.


        :param external_point: The external_point of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._external_point = external_point

    @property
    def deformation_behavior(self):
        """Gets the deformation_behavior of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501

        <p>Choose the deformation behavior of the assigned entity. If <b>deformable</b> is selected, the entity is allowed to deform, selecting <b>undeformable</b> leads to a rigid entity.</p>  # noqa: E501

        :return: The deformation_behavior of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :rtype: str
        """
        return self._deformation_behavior

    @deformation_behavior.setter
    def deformation_behavior(self, deformation_behavior):
        """Sets the deformation_behavior of this OneOfFrequencyAnalysisBoundaryConditions.

        <p>Choose the deformation behavior of the assigned entity. If <b>deformable</b> is selected, the entity is allowed to deform, selecting <b>undeformable</b> leads to a rigid entity.</p>  # noqa: E501

        :param deformation_behavior: The deformation_behavior of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEFORMABLE", "UNDEFORMABLE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and deformation_behavior not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `deformation_behavior` ({0}), must be one of {1}"  # noqa: E501
                .format(deformation_behavior, allowed_values)
            )

        self._deformation_behavior = deformation_behavior

    @property
    def enable_search_radius(self):
        """Gets the enable_search_radius of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501


        :return: The enable_search_radius of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :rtype: bool
        """
        return self._enable_search_radius

    @enable_search_radius.setter
    def enable_search_radius(self, enable_search_radius):
        """Sets the enable_search_radius of this OneOfFrequencyAnalysisBoundaryConditions.


        :param enable_search_radius: The enable_search_radius of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :type: bool
        """

        self._enable_search_radius = enable_search_radius

    @property
    def search_radius(self):
        """Gets the search_radius of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501


        :return: The search_radius of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._search_radius

    @search_radius.setter
    def search_radius(self, search_radius):
        """Sets the search_radius of this OneOfFrequencyAnalysisBoundaryConditions.


        :param search_radius: The search_radius of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalLength
        """

        self._search_radius = search_radius

    @property
    def rotation(self):
        """Gets the rotation of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501


        :return: The rotation of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :rtype: AngularRotation
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this OneOfFrequencyAnalysisBoundaryConditions.


        :param rotation: The rotation of this OneOfFrequencyAnalysisBoundaryConditions.  # noqa: E501
        :type: AngularRotation
        """

        self._rotation = rotation

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
        if not isinstance(other, OneOfFrequencyAnalysisBoundaryConditions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfFrequencyAnalysisBoundaryConditions):
            return True

        return self.to_dict() != other.to_dict()
