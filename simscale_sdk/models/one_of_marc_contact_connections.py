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


class OneOfMarcContactConnections(object):
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
        'contact_bodies': 'TopologicalReference',
        'friction_coefficient': 'float',
        'interference_fit': 'InterferenceFit',
        'touching_faces': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'contact_bodies': 'contactBodies',
        'friction_coefficient': 'frictionCoefficient',
        'interference_fit': 'interferenceFit',
        'touching_faces': 'touchingFaces'
    }

    discriminator_value_class_map = {
        'BONDED': 'MarcBondedContactConnection',
        'TOUCHING': 'MarcTouchingContactConnection',
        'BONDED_AND_TOUCHING': 'MarcBondedAndTouchingContactConnection'
    }

    def __init__(self, type='BONDED_AND_TOUCHING', name=None, contact_bodies=None, friction_coefficient=None, interference_fit=None, touching_faces=None, local_vars_configuration=None):  # noqa: E501
        """OneOfMarcContactConnections - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._contact_bodies = None
        self._friction_coefficient = None
        self._interference_fit = None
        self._touching_faces = None
        self.discriminator = 'type'

        self.type = type
        if name is not None:
            self.name = name
        if contact_bodies is not None:
            self.contact_bodies = contact_bodies
        if friction_coefficient is not None:
            self.friction_coefficient = friction_coefficient
        if interference_fit is not None:
            self.interference_fit = interference_fit
        if touching_faces is not None:
            self.touching_faces = touching_faces

    @property
    def type(self):
        """Gets the type of this OneOfMarcContactConnections.  # noqa: E501

        Schema name: MarcBondedAndTouchingContactConnection  # noqa: E501

        :return: The type of this OneOfMarcContactConnections.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfMarcContactConnections.

        Schema name: MarcBondedAndTouchingContactConnection  # noqa: E501

        :param type: The type of this OneOfMarcContactConnections.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this OneOfMarcContactConnections.  # noqa: E501


        :return: The name of this OneOfMarcContactConnections.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfMarcContactConnections.


        :param name: The name of this OneOfMarcContactConnections.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def contact_bodies(self):
        """Gets the contact_bodies of this OneOfMarcContactConnections.  # noqa: E501


        :return: The contact_bodies of this OneOfMarcContactConnections.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._contact_bodies

    @contact_bodies.setter
    def contact_bodies(self, contact_bodies):
        """Sets the contact_bodies of this OneOfMarcContactConnections.


        :param contact_bodies: The contact_bodies of this OneOfMarcContactConnections.  # noqa: E501
        :type: TopologicalReference
        """

        self._contact_bodies = contact_bodies

    @property
    def friction_coefficient(self):
        """Gets the friction_coefficient of this OneOfMarcContactConnections.  # noqa: E501


        :return: The friction_coefficient of this OneOfMarcContactConnections.  # noqa: E501
        :rtype: float
        """
        return self._friction_coefficient

    @friction_coefficient.setter
    def friction_coefficient(self, friction_coefficient):
        """Sets the friction_coefficient of this OneOfMarcContactConnections.


        :param friction_coefficient: The friction_coefficient of this OneOfMarcContactConnections.  # noqa: E501
        :type: float
        """

        self._friction_coefficient = friction_coefficient

    @property
    def interference_fit(self):
        """Gets the interference_fit of this OneOfMarcContactConnections.  # noqa: E501


        :return: The interference_fit of this OneOfMarcContactConnections.  # noqa: E501
        :rtype: InterferenceFit
        """
        return self._interference_fit

    @interference_fit.setter
    def interference_fit(self, interference_fit):
        """Sets the interference_fit of this OneOfMarcContactConnections.


        :param interference_fit: The interference_fit of this OneOfMarcContactConnections.  # noqa: E501
        :type: InterferenceFit
        """

        self._interference_fit = interference_fit

    @property
    def touching_faces(self):
        """Gets the touching_faces of this OneOfMarcContactConnections.  # noqa: E501


        :return: The touching_faces of this OneOfMarcContactConnections.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._touching_faces

    @touching_faces.setter
    def touching_faces(self, touching_faces):
        """Sets the touching_faces of this OneOfMarcContactConnections.


        :param touching_faces: The touching_faces of this OneOfMarcContactConnections.  # noqa: E501
        :type: TopologicalReference
        """

        self._touching_faces = touching_faces

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
        if not isinstance(other, OneOfMarcContactConnections):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfMarcContactConnections):
            return True

        return self.to_dict() != other.to_dict()
