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


class OneOfDynamicAnalysisBoundaryConditions(object):
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
        'rotation': 'AngularRotation',
        'rotation_origin': 'DimensionalVectorFunctionLength',
        'rotation_axis': 'DimensionalVectorFunctionLength',
        'omega': 'DimensionalFunctionAngle',
        'enable_heat_transfer': 'str',
        'axis_origin': 'DimensionalVectorLength',
        'axis_direction': 'DimensionalVectorLength',
        'sector_angle': 'DimensionalAngle',
        'master_topological_reference': 'TopologicalReference',
        'slave_topological_reference': 'TopologicalReference',
        'pressure': 'DimensionalFunctionPressure',
        'force': 'DimensionalVectorFunctionForce',
        'scaling': 'DimensionalFunctionDimensionless',
        'phase_angle': 'DimensionalAngle',
        'moment': 'DimensionalVectorFunctionTorque',
        'remote_point': 'DimensionalVectorLength',
        'load': 'DimensionalVectorFunctionVolumeForce',
        'axis_definition': 'OneOfHingeConstraintBCAxisDefinition'
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
        'rotation': 'rotation',
        'rotation_origin': 'rotationOrigin',
        'rotation_axis': 'rotationAxis',
        'omega': 'omega',
        'enable_heat_transfer': 'enableHeatTransfer',
        'axis_origin': 'axisOrigin',
        'axis_direction': 'axisDirection',
        'sector_angle': 'sectorAngle',
        'master_topological_reference': 'masterTopologicalReference',
        'slave_topological_reference': 'slaveTopologicalReference',
        'pressure': 'pressure',
        'force': 'force',
        'scaling': 'scaling',
        'phase_angle': 'phaseAngle',
        'moment': 'moment',
        'remote_point': 'remotePoint',
        'load': 'load',
        'axis_definition': 'axisDefinition'
    }

    discriminator_value_class_map = {
        'BOLT_PRELOAD': 'BoltPreloadBC',
        'ELASTIC_SUPPORT': 'ElasticSupportBC',
        'FIXED_SUPPORT': 'FixedSupportBC',
        'FIXED_VALUE': 'FixedValueBC',
        'POINT_MASS': 'PointMassBC',
        'REMOTE_DISPLACEMENT_LOAD': 'RemoteDisplacementLoadBC',
        'ROTATING_MOTION': 'RotatingMotionBC',
        'SYMMETRY_PLANE': 'SymmetryPlaneBC',
        'CYCLIC_SYMMETRY': 'CyclicSymmetryBC',
        'CENTRIFUGAL_FORCE': 'CentrifugalForceBC',
        'FOLLOWER_PRESSURE': 'FollowerPressureBC',
        'FORCE_LOAD': 'ForceLoadBC',
        'NODAL_LOAD': 'NodalLoadBC',
        'PRESSURE': 'PressureBC',
        'REMOTE_FORCE_LOAD': 'RemoteForceLoadBC',
        'SURFACE_LOAD': 'SurfaceLoadBC',
        'VOLUME_LOAD': 'VolumeLoadBC',
        'HINGE_CONSTRAINT': 'HingeConstraintBC'
    }

    def __init__(self, type='HINGE_CONSTRAINT', name=None, preload=None, topological_reference=None, spring_stiffness=None, displacement=None, mass=None, mass_moment_of_inertia=None, external_point=None, deformation_behavior=None, enable_search_radius=None, search_radius=None, rotation=None, rotation_origin=None, rotation_axis=None, omega=None, enable_heat_transfer=None, axis_origin=None, axis_direction=None, sector_angle=None, master_topological_reference=None, slave_topological_reference=None, pressure=None, force=None, scaling=None, phase_angle=None, moment=None, remote_point=None, load=None, axis_definition=None, local_vars_configuration=None):  # noqa: E501
        """OneOfDynamicAnalysisBoundaryConditions - a model defined in OpenAPI"""  # noqa: E501
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
        self._rotation_origin = None
        self._rotation_axis = None
        self._omega = None
        self._enable_heat_transfer = None
        self._axis_origin = None
        self._axis_direction = None
        self._sector_angle = None
        self._master_topological_reference = None
        self._slave_topological_reference = None
        self._pressure = None
        self._force = None
        self._scaling = None
        self._phase_angle = None
        self._moment = None
        self._remote_point = None
        self._load = None
        self._axis_definition = None
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
        if rotation_origin is not None:
            self.rotation_origin = rotation_origin
        if rotation_axis is not None:
            self.rotation_axis = rotation_axis
        if omega is not None:
            self.omega = omega
        if enable_heat_transfer is not None:
            self.enable_heat_transfer = enable_heat_transfer
        if axis_origin is not None:
            self.axis_origin = axis_origin
        if axis_direction is not None:
            self.axis_direction = axis_direction
        if sector_angle is not None:
            self.sector_angle = sector_angle
        if master_topological_reference is not None:
            self.master_topological_reference = master_topological_reference
        if slave_topological_reference is not None:
            self.slave_topological_reference = slave_topological_reference
        if pressure is not None:
            self.pressure = pressure
        if force is not None:
            self.force = force
        if scaling is not None:
            self.scaling = scaling
        if phase_angle is not None:
            self.phase_angle = phase_angle
        if moment is not None:
            self.moment = moment
        if remote_point is not None:
            self.remote_point = remote_point
        if load is not None:
            self.load = load
        if axis_definition is not None:
            self.axis_definition = axis_definition

    @property
    def type(self):
        """Gets the type of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501

        Replicate the behaviour of a freely rotating hinge fixed to the ground. Note that only a single face assignment is allowed. The assigned surface is constrained such that only rotational motion around the hinge axis is free. SimScale can automatically detect the axis of the hinge based on an assigned cylindrical surface, but the boundary condition also allows for a user-defined input.  Schema name: HingeConstraintBC  # noqa: E501

        :return: The type of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfDynamicAnalysisBoundaryConditions.

        Replicate the behaviour of a freely rotating hinge fixed to the ground. Note that only a single face assignment is allowed. The assigned surface is constrained such that only rotational motion around the hinge axis is free. SimScale can automatically detect the axis of the hinge based on an assigned cylindrical surface, but the boundary condition also allows for a user-defined input.  Schema name: HingeConstraintBC  # noqa: E501

        :param type: The type of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The name of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfDynamicAnalysisBoundaryConditions.


        :param name: The name of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def preload(self):
        """Gets the preload of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The preload of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: ForcePreload
        """
        return self._preload

    @preload.setter
    def preload(self, preload):
        """Sets the preload of this OneOfDynamicAnalysisBoundaryConditions.


        :param preload: The preload of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: ForcePreload
        """

        self._preload = preload

    @property
    def topological_reference(self):
        """Gets the topological_reference of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The topological_reference of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this OneOfDynamicAnalysisBoundaryConditions.


        :param topological_reference: The topological_reference of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def spring_stiffness(self):
        """Gets the spring_stiffness of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The spring_stiffness of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: OneOfElasticSupportBCSpringStiffness
        """
        return self._spring_stiffness

    @spring_stiffness.setter
    def spring_stiffness(self, spring_stiffness):
        """Sets the spring_stiffness of this OneOfDynamicAnalysisBoundaryConditions.


        :param spring_stiffness: The spring_stiffness of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: OneOfElasticSupportBCSpringStiffness
        """

        self._spring_stiffness = spring_stiffness

    @property
    def displacement(self):
        """Gets the displacement of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The displacement of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalPartialVectorFunctionLength
        """
        return self._displacement

    @displacement.setter
    def displacement(self, displacement):
        """Sets the displacement of this OneOfDynamicAnalysisBoundaryConditions.


        :param displacement: The displacement of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalPartialVectorFunctionLength
        """

        self._displacement = displacement

    @property
    def mass(self):
        """Gets the mass of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The mass of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalMass
        """
        return self._mass

    @mass.setter
    def mass(self, mass):
        """Sets the mass of this OneOfDynamicAnalysisBoundaryConditions.


        :param mass: The mass of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalMass
        """

        self._mass = mass

    @property
    def mass_moment_of_inertia(self):
        """Gets the mass_moment_of_inertia of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The mass_moment_of_inertia of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalVectorMomentOfInertia
        """
        return self._mass_moment_of_inertia

    @mass_moment_of_inertia.setter
    def mass_moment_of_inertia(self, mass_moment_of_inertia):
        """Sets the mass_moment_of_inertia of this OneOfDynamicAnalysisBoundaryConditions.


        :param mass_moment_of_inertia: The mass_moment_of_inertia of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalVectorMomentOfInertia
        """

        self._mass_moment_of_inertia = mass_moment_of_inertia

    @property
    def external_point(self):
        """Gets the external_point of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The external_point of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._external_point

    @external_point.setter
    def external_point(self, external_point):
        """Sets the external_point of this OneOfDynamicAnalysisBoundaryConditions.


        :param external_point: The external_point of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._external_point = external_point

    @property
    def deformation_behavior(self):
        """Gets the deformation_behavior of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501

        <p>Choose the deformation behavior of the assigned entity. If <b>deformable</b> is selected, the entitiy is allowed to deform without applying additional stiffness, selecting <b>undeformable</b> leads to a rigid entity.</p>  # noqa: E501

        :return: The deformation_behavior of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: str
        """
        return self._deformation_behavior

    @deformation_behavior.setter
    def deformation_behavior(self, deformation_behavior):
        """Sets the deformation_behavior of this OneOfDynamicAnalysisBoundaryConditions.

        <p>Choose the deformation behavior of the assigned entity. If <b>deformable</b> is selected, the entitiy is allowed to deform without applying additional stiffness, selecting <b>undeformable</b> leads to a rigid entity.</p>  # noqa: E501

        :param deformation_behavior: The deformation_behavior of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
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
        """Gets the enable_search_radius of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The enable_search_radius of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: bool
        """
        return self._enable_search_radius

    @enable_search_radius.setter
    def enable_search_radius(self, enable_search_radius):
        """Sets the enable_search_radius of this OneOfDynamicAnalysisBoundaryConditions.


        :param enable_search_radius: The enable_search_radius of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: bool
        """

        self._enable_search_radius = enable_search_radius

    @property
    def search_radius(self):
        """Gets the search_radius of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The search_radius of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._search_radius

    @search_radius.setter
    def search_radius(self, search_radius):
        """Sets the search_radius of this OneOfDynamicAnalysisBoundaryConditions.


        :param search_radius: The search_radius of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalLength
        """

        self._search_radius = search_radius

    @property
    def rotation(self):
        """Gets the rotation of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The rotation of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: AngularRotation
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this OneOfDynamicAnalysisBoundaryConditions.


        :param rotation: The rotation of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: AngularRotation
        """

        self._rotation = rotation

    @property
    def rotation_origin(self):
        """Gets the rotation_origin of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The rotation_origin of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalVectorFunctionLength
        """
        return self._rotation_origin

    @rotation_origin.setter
    def rotation_origin(self, rotation_origin):
        """Sets the rotation_origin of this OneOfDynamicAnalysisBoundaryConditions.


        :param rotation_origin: The rotation_origin of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalVectorFunctionLength
        """

        self._rotation_origin = rotation_origin

    @property
    def rotation_axis(self):
        """Gets the rotation_axis of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The rotation_axis of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalVectorFunctionLength
        """
        return self._rotation_axis

    @rotation_axis.setter
    def rotation_axis(self, rotation_axis):
        """Sets the rotation_axis of this OneOfDynamicAnalysisBoundaryConditions.


        :param rotation_axis: The rotation_axis of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalVectorFunctionLength
        """

        self._rotation_axis = rotation_axis

    @property
    def omega(self):
        """Gets the omega of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The omega of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalFunctionAngle
        """
        return self._omega

    @omega.setter
    def omega(self, omega):
        """Sets the omega of this OneOfDynamicAnalysisBoundaryConditions.


        :param omega: The omega of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalFunctionAngle
        """

        self._omega = omega

    @property
    def enable_heat_transfer(self):
        """Gets the enable_heat_transfer of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501

        <p>Define if heat transfer should be allowed across the contact. If <b>yes</b> is chosen a perfectly bonded heat contact is assumed whereas if <b>no</b> is selected no heat transfer across the contact is allowed. Mechanical contact stays with both options active. With the selection of <b>heat transfer only</b> no mechanical contact is activated but only a bonded heat contact.</p>  # noqa: E501

        :return: The enable_heat_transfer of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: str
        """
        return self._enable_heat_transfer

    @enable_heat_transfer.setter
    def enable_heat_transfer(self, enable_heat_transfer):
        """Sets the enable_heat_transfer of this OneOfDynamicAnalysisBoundaryConditions.

        <p>Define if heat transfer should be allowed across the contact. If <b>yes</b> is chosen a perfectly bonded heat contact is assumed whereas if <b>no</b> is selected no heat transfer across the contact is allowed. Mechanical contact stays with both options active. With the selection of <b>heat transfer only</b> no mechanical contact is activated but only a bonded heat contact.</p>  # noqa: E501

        :param enable_heat_transfer: The enable_heat_transfer of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: str
        """
        allowed_values = ["YES", "NO", "HEAT_TRANSFER_ONLY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and enable_heat_transfer not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `enable_heat_transfer` ({0}), must be one of {1}"  # noqa: E501
                .format(enable_heat_transfer, allowed_values)
            )

        self._enable_heat_transfer = enable_heat_transfer

    @property
    def axis_origin(self):
        """Gets the axis_origin of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The axis_origin of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._axis_origin

    @axis_origin.setter
    def axis_origin(self, axis_origin):
        """Sets the axis_origin of this OneOfDynamicAnalysisBoundaryConditions.


        :param axis_origin: The axis_origin of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._axis_origin = axis_origin

    @property
    def axis_direction(self):
        """Gets the axis_direction of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The axis_direction of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._axis_direction

    @axis_direction.setter
    def axis_direction(self, axis_direction):
        """Sets the axis_direction of this OneOfDynamicAnalysisBoundaryConditions.


        :param axis_direction: The axis_direction of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._axis_direction = axis_direction

    @property
    def sector_angle(self):
        """Gets the sector_angle of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The sector_angle of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._sector_angle

    @sector_angle.setter
    def sector_angle(self, sector_angle):
        """Sets the sector_angle of this OneOfDynamicAnalysisBoundaryConditions.


        :param sector_angle: The sector_angle of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalAngle
        """

        self._sector_angle = sector_angle

    @property
    def master_topological_reference(self):
        """Gets the master_topological_reference of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The master_topological_reference of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._master_topological_reference

    @master_topological_reference.setter
    def master_topological_reference(self, master_topological_reference):
        """Sets the master_topological_reference of this OneOfDynamicAnalysisBoundaryConditions.


        :param master_topological_reference: The master_topological_reference of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: TopologicalReference
        """

        self._master_topological_reference = master_topological_reference

    @property
    def slave_topological_reference(self):
        """Gets the slave_topological_reference of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The slave_topological_reference of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._slave_topological_reference

    @slave_topological_reference.setter
    def slave_topological_reference(self, slave_topological_reference):
        """Sets the slave_topological_reference of this OneOfDynamicAnalysisBoundaryConditions.


        :param slave_topological_reference: The slave_topological_reference of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: TopologicalReference
        """

        self._slave_topological_reference = slave_topological_reference

    @property
    def pressure(self):
        """Gets the pressure of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The pressure of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._pressure

    @pressure.setter
    def pressure(self, pressure):
        """Sets the pressure of this OneOfDynamicAnalysisBoundaryConditions.


        :param pressure: The pressure of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._pressure = pressure

    @property
    def force(self):
        """Gets the force of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The force of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalVectorFunctionForce
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this OneOfDynamicAnalysisBoundaryConditions.


        :param force: The force of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalVectorFunctionForce
        """

        self._force = force

    @property
    def scaling(self):
        """Gets the scaling of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The scaling of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalFunctionDimensionless
        """
        return self._scaling

    @scaling.setter
    def scaling(self, scaling):
        """Sets the scaling of this OneOfDynamicAnalysisBoundaryConditions.


        :param scaling: The scaling of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalFunctionDimensionless
        """

        self._scaling = scaling

    @property
    def phase_angle(self):
        """Gets the phase_angle of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The phase_angle of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._phase_angle

    @phase_angle.setter
    def phase_angle(self, phase_angle):
        """Sets the phase_angle of this OneOfDynamicAnalysisBoundaryConditions.


        :param phase_angle: The phase_angle of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalAngle
        """

        self._phase_angle = phase_angle

    @property
    def moment(self):
        """Gets the moment of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The moment of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalVectorFunctionTorque
        """
        return self._moment

    @moment.setter
    def moment(self, moment):
        """Sets the moment of this OneOfDynamicAnalysisBoundaryConditions.


        :param moment: The moment of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalVectorFunctionTorque
        """

        self._moment = moment

    @property
    def remote_point(self):
        """Gets the remote_point of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The remote_point of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._remote_point

    @remote_point.setter
    def remote_point(self, remote_point):
        """Sets the remote_point of this OneOfDynamicAnalysisBoundaryConditions.


        :param remote_point: The remote_point of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._remote_point = remote_point

    @property
    def load(self):
        """Gets the load of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The load of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: DimensionalVectorFunctionVolumeForce
        """
        return self._load

    @load.setter
    def load(self, load):
        """Sets the load of this OneOfDynamicAnalysisBoundaryConditions.


        :param load: The load of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: DimensionalVectorFunctionVolumeForce
        """

        self._load = load

    @property
    def axis_definition(self):
        """Gets the axis_definition of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501


        :return: The axis_definition of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :rtype: OneOfHingeConstraintBCAxisDefinition
        """
        return self._axis_definition

    @axis_definition.setter
    def axis_definition(self, axis_definition):
        """Sets the axis_definition of this OneOfDynamicAnalysisBoundaryConditions.


        :param axis_definition: The axis_definition of this OneOfDynamicAnalysisBoundaryConditions.  # noqa: E501
        :type: OneOfHingeConstraintBCAxisDefinition
        """

        self._axis_definition = axis_definition

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
        if not isinstance(other, OneOfDynamicAnalysisBoundaryConditions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfDynamicAnalysisBoundaryConditions):
            return True

        return self.to_dict() != other.to_dict()
