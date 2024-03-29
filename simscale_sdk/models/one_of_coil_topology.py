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


class OneOfCoilTopology(object):
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
        'bodies': 'TopologicalReference',
        'entry_port': 'TopologicalReference',
        'exit_port': 'TopologicalReference',
        'internal_port': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'bodies': 'bodies',
        'entry_port': 'entryPort',
        'exit_port': 'exitPort',
        'internal_port': 'internalPort'
    }

    discriminator_value_class_map = {
        'OPEN_COIL': 'OpenCoil',
        'CLOSED_COIL': 'ClosedCoil'
    }

    def __init__(self, type='CLOSED_COIL', bodies=None, entry_port=None, exit_port=None, internal_port=None, local_vars_configuration=None):  # noqa: E501
        """OneOfCoilTopology - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._bodies = None
        self._entry_port = None
        self._exit_port = None
        self._internal_port = None
        self.discriminator = 'type'

        self.type = type
        if bodies is not None:
            self.bodies = bodies
        if entry_port is not None:
            self.entry_port = entry_port
        if exit_port is not None:
            self.exit_port = exit_port
        if internal_port is not None:
            self.internal_port = internal_port

    @property
    def type(self):
        """Gets the type of this OneOfCoilTopology.  # noqa: E501

        Schema name: ClosedCoil  # noqa: E501

        :return: The type of this OneOfCoilTopology.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfCoilTopology.

        Schema name: ClosedCoil  # noqa: E501

        :param type: The type of this OneOfCoilTopology.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def bodies(self):
        """Gets the bodies of this OneOfCoilTopology.  # noqa: E501


        :return: The bodies of this OneOfCoilTopology.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._bodies

    @bodies.setter
    def bodies(self, bodies):
        """Sets the bodies of this OneOfCoilTopology.


        :param bodies: The bodies of this OneOfCoilTopology.  # noqa: E501
        :type: TopologicalReference
        """

        self._bodies = bodies

    @property
    def entry_port(self):
        """Gets the entry_port of this OneOfCoilTopology.  # noqa: E501


        :return: The entry_port of this OneOfCoilTopology.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._entry_port

    @entry_port.setter
    def entry_port(self, entry_port):
        """Sets the entry_port of this OneOfCoilTopology.


        :param entry_port: The entry_port of this OneOfCoilTopology.  # noqa: E501
        :type: TopologicalReference
        """

        self._entry_port = entry_port

    @property
    def exit_port(self):
        """Gets the exit_port of this OneOfCoilTopology.  # noqa: E501


        :return: The exit_port of this OneOfCoilTopology.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._exit_port

    @exit_port.setter
    def exit_port(self, exit_port):
        """Sets the exit_port of this OneOfCoilTopology.


        :param exit_port: The exit_port of this OneOfCoilTopology.  # noqa: E501
        :type: TopologicalReference
        """

        self._exit_port = exit_port

    @property
    def internal_port(self):
        """Gets the internal_port of this OneOfCoilTopology.  # noqa: E501


        :return: The internal_port of this OneOfCoilTopology.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._internal_port

    @internal_port.setter
    def internal_port(self, internal_port):
        """Sets the internal_port of this OneOfCoilTopology.


        :param internal_port: The internal_port of this OneOfCoilTopology.  # noqa: E501
        :type: TopologicalReference
        """

        self._internal_port = internal_port

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
        if not isinstance(other, OneOfCoilTopology):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfCoilTopology):
            return True

        return self.to_dict() != other.to_dict()
