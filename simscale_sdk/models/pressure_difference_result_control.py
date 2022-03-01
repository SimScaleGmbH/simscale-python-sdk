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


class PressureDifferenceResultControl(object):
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
        'inlet_face_topological_reference': 'TopologicalReference',
        'outlet_face_topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'inlet_face_topological_reference': 'inletFaceTopologicalReference',
        'outlet_face_topological_reference': 'outletFaceTopologicalReference'
    }

    def __init__(self, type='PRESSURE_DIFFERENCE', name=None, inlet_face_topological_reference=None, outlet_face_topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """PressureDifferenceResultControl - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._inlet_face_topological_reference = None
        self._outlet_face_topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if inlet_face_topological_reference is not None:
            self.inlet_face_topological_reference = inlet_face_topological_reference
        if outlet_face_topological_reference is not None:
            self.outlet_face_topological_reference = outlet_face_topological_reference

    @property
    def type(self):
        """Gets the type of this PressureDifferenceResultControl.  # noqa: E501

        Schema name: PressureDifferenceResultControl  # noqa: E501

        :return: The type of this PressureDifferenceResultControl.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PressureDifferenceResultControl.

        Schema name: PressureDifferenceResultControl  # noqa: E501

        :param type: The type of this PressureDifferenceResultControl.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this PressureDifferenceResultControl.  # noqa: E501


        :return: The name of this PressureDifferenceResultControl.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PressureDifferenceResultControl.


        :param name: The name of this PressureDifferenceResultControl.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[A-Za-z()][-+0-9a-zA-Z_()\h]{0,199}$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[A-Za-z()][-+0-9a-zA-Z_()\h]{0,199}$/`")  # noqa: E501

        self._name = name

    @property
    def inlet_face_topological_reference(self):
        """Gets the inlet_face_topological_reference of this PressureDifferenceResultControl.  # noqa: E501


        :return: The inlet_face_topological_reference of this PressureDifferenceResultControl.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._inlet_face_topological_reference

    @inlet_face_topological_reference.setter
    def inlet_face_topological_reference(self, inlet_face_topological_reference):
        """Sets the inlet_face_topological_reference of this PressureDifferenceResultControl.


        :param inlet_face_topological_reference: The inlet_face_topological_reference of this PressureDifferenceResultControl.  # noqa: E501
        :type: TopologicalReference
        """

        self._inlet_face_topological_reference = inlet_face_topological_reference

    @property
    def outlet_face_topological_reference(self):
        """Gets the outlet_face_topological_reference of this PressureDifferenceResultControl.  # noqa: E501


        :return: The outlet_face_topological_reference of this PressureDifferenceResultControl.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._outlet_face_topological_reference

    @outlet_face_topological_reference.setter
    def outlet_face_topological_reference(self, outlet_face_topological_reference):
        """Sets the outlet_face_topological_reference of this PressureDifferenceResultControl.


        :param outlet_face_topological_reference: The outlet_face_topological_reference of this PressureDifferenceResultControl.  # noqa: E501
        :type: TopologicalReference
        """

        self._outlet_face_topological_reference = outlet_face_topological_reference

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
        if not isinstance(other, PressureDifferenceResultControl):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PressureDifferenceResultControl):
            return True

        return self.to_dict() != other.to_dict()