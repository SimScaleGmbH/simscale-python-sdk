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


class ForcesMomentsResultControl(object):
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
        'center_of_rotation': 'DimensionalVectorLength',
        'write_control': 'OneOfForcesMomentsResultControlWriteControl',
        'fraction_from_end': 'float',
        'export_statistics': 'bool',
        'group_assignments': 'bool',
        'topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'center_of_rotation': 'centerOfRotation',
        'write_control': 'writeControl',
        'fraction_from_end': 'fractionFromEnd',
        'export_statistics': 'exportStatistics',
        'group_assignments': 'groupAssignments',
        'topological_reference': 'topologicalReference'
    }

    def __init__(self, type='FORCES_AND_MOMENTS', name=None, center_of_rotation=None, write_control=None, fraction_from_end=None, export_statistics=None, group_assignments=None, topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """ForcesMomentsResultControl - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._center_of_rotation = None
        self._write_control = None
        self._fraction_from_end = None
        self._export_statistics = None
        self._group_assignments = None
        self._topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if center_of_rotation is not None:
            self.center_of_rotation = center_of_rotation
        if write_control is not None:
            self.write_control = write_control
        if fraction_from_end is not None:
            self.fraction_from_end = fraction_from_end
        if export_statistics is not None:
            self.export_statistics = export_statistics
        if group_assignments is not None:
            self.group_assignments = group_assignments
        if topological_reference is not None:
            self.topological_reference = topological_reference

    @property
    def type(self):
        """Gets the type of this ForcesMomentsResultControl.  # noqa: E501

        Schema name: ForcesMomentsResultControl  # noqa: E501

        :return: The type of this ForcesMomentsResultControl.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ForcesMomentsResultControl.

        Schema name: ForcesMomentsResultControl  # noqa: E501

        :param type: The type of this ForcesMomentsResultControl.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this ForcesMomentsResultControl.  # noqa: E501


        :return: The name of this ForcesMomentsResultControl.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ForcesMomentsResultControl.


        :param name: The name of this ForcesMomentsResultControl.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[A-Za-z()][-+0-9a-zA-Z_()\h]{0,199}$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[A-Za-z()][-+0-9a-zA-Z_()\h]{0,199}$/`")  # noqa: E501

        self._name = name

    @property
    def center_of_rotation(self):
        """Gets the center_of_rotation of this ForcesMomentsResultControl.  # noqa: E501


        :return: The center_of_rotation of this ForcesMomentsResultControl.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._center_of_rotation

    @center_of_rotation.setter
    def center_of_rotation(self, center_of_rotation):
        """Sets the center_of_rotation of this ForcesMomentsResultControl.


        :param center_of_rotation: The center_of_rotation of this ForcesMomentsResultControl.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._center_of_rotation = center_of_rotation

    @property
    def write_control(self):
        """Gets the write_control of this ForcesMomentsResultControl.  # noqa: E501


        :return: The write_control of this ForcesMomentsResultControl.  # noqa: E501
        :rtype: OneOfForcesMomentsResultControlWriteControl
        """
        return self._write_control

    @write_control.setter
    def write_control(self, write_control):
        """Sets the write_control of this ForcesMomentsResultControl.


        :param write_control: The write_control of this ForcesMomentsResultControl.  # noqa: E501
        :type: OneOfForcesMomentsResultControlWriteControl
        """

        self._write_control = write_control

    @property
    def fraction_from_end(self):
        """Gets the fraction_from_end of this ForcesMomentsResultControl.  # noqa: E501

        It defines the point in simulation where the result output data extraction starts. For instance, <i>Fraction from end</i> of 1 (100%) extracts all data from the beginning of the simulation while default 0.2 extracts 20% data from the end of the simulation.  # noqa: E501

        :return: The fraction_from_end of this ForcesMomentsResultControl.  # noqa: E501
        :rtype: float
        """
        return self._fraction_from_end

    @fraction_from_end.setter
    def fraction_from_end(self, fraction_from_end):
        """Sets the fraction_from_end of this ForcesMomentsResultControl.

        It defines the point in simulation where the result output data extraction starts. For instance, <i>Fraction from end</i> of 1 (100%) extracts all data from the beginning of the simulation while default 0.2 extracts 20% data from the end of the simulation.  # noqa: E501

        :param fraction_from_end: The fraction_from_end of this ForcesMomentsResultControl.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                fraction_from_end is not None and fraction_from_end > 1):  # noqa: E501
            raise ValueError("Invalid value for `fraction_from_end`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fraction_from_end is not None and fraction_from_end < 0):  # noqa: E501
            raise ValueError("Invalid value for `fraction_from_end`, must be a value greater than or equal to `0`")  # noqa: E501

        self._fraction_from_end = fraction_from_end

    @property
    def export_statistics(self):
        """Gets the export_statistics of this ForcesMomentsResultControl.  # noqa: E501

        <p>When this switch is activated, statistical data for the selected forces and moments will be exported:</p><ul> <li>Minimum (<strong>MIN</strong>)</li><li>Maximum (<strong>MAX</strong>)</li><li>Absolute minimum (<strong>MIN (Abs)</strong>)</li><li>Absolute maximum (<strong>MAX (Abs)</strong>)</li><li>Average (<strong>AVG</strong>)</li><li>Standard deviation (<strong>STDDEV</strong>)</li><li>Root mean square (<strong>RMS (fluctuation)</strong>)</li></ul>  # noqa: E501

        :return: The export_statistics of this ForcesMomentsResultControl.  # noqa: E501
        :rtype: bool
        """
        return self._export_statistics

    @export_statistics.setter
    def export_statistics(self, export_statistics):
        """Sets the export_statistics of this ForcesMomentsResultControl.

        <p>When this switch is activated, statistical data for the selected forces and moments will be exported:</p><ul> <li>Minimum (<strong>MIN</strong>)</li><li>Maximum (<strong>MAX</strong>)</li><li>Absolute minimum (<strong>MIN (Abs)</strong>)</li><li>Absolute maximum (<strong>MAX (Abs)</strong>)</li><li>Average (<strong>AVG</strong>)</li><li>Standard deviation (<strong>STDDEV</strong>)</li><li>Root mean square (<strong>RMS (fluctuation)</strong>)</li></ul>  # noqa: E501

        :param export_statistics: The export_statistics of this ForcesMomentsResultControl.  # noqa: E501
        :type: bool
        """

        self._export_statistics = export_statistics

    @property
    def group_assignments(self):
        """Gets the group_assignments of this ForcesMomentsResultControl.  # noqa: E501

        When this switch is activated, forces and moments will be calculated cumulatively on all assignments. When deactivated, they will be calculated individually for each assignment.  # noqa: E501

        :return: The group_assignments of this ForcesMomentsResultControl.  # noqa: E501
        :rtype: bool
        """
        return self._group_assignments

    @group_assignments.setter
    def group_assignments(self, group_assignments):
        """Sets the group_assignments of this ForcesMomentsResultControl.

        When this switch is activated, forces and moments will be calculated cumulatively on all assignments. When deactivated, they will be calculated individually for each assignment.  # noqa: E501

        :param group_assignments: The group_assignments of this ForcesMomentsResultControl.  # noqa: E501
        :type: bool
        """

        self._group_assignments = group_assignments

    @property
    def topological_reference(self):
        """Gets the topological_reference of this ForcesMomentsResultControl.  # noqa: E501


        :return: The topological_reference of this ForcesMomentsResultControl.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this ForcesMomentsResultControl.


        :param topological_reference: The topological_reference of this ForcesMomentsResultControl.  # noqa: E501
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
        if not isinstance(other, ForcesMomentsResultControl):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ForcesMomentsResultControl):
            return True

        return self.to_dict() != other.to_dict()
