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


class Mesh(object):
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
        'mesh_id': 'str',
        'name': 'str',
        'created_at': 'datetime',
        'number_of_cells': 'int',
        'number_of_nodes': 'int'
    }

    attribute_map = {
        'mesh_id': 'meshId',
        'name': 'name',
        'created_at': 'createdAt',
        'number_of_cells': 'numberOfCells',
        'number_of_nodes': 'numberOfNodes'
    }

    def __init__(self, mesh_id=None, name=None, created_at=None, number_of_cells=None, number_of_nodes=None, local_vars_configuration=None):  # noqa: E501
        """Mesh - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mesh_id = None
        self._name = None
        self._created_at = None
        self._number_of_cells = None
        self._number_of_nodes = None
        self.discriminator = None

        if mesh_id is not None:
            self.mesh_id = mesh_id
        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if number_of_cells is not None:
            self.number_of_cells = number_of_cells
        if number_of_nodes is not None:
            self.number_of_nodes = number_of_nodes

    @property
    def mesh_id(self):
        """Gets the mesh_id of this Mesh.  # noqa: E501

        The ID of the mesh.  # noqa: E501

        :return: The mesh_id of this Mesh.  # noqa: E501
        :rtype: str
        """
        return self._mesh_id

    @mesh_id.setter
    def mesh_id(self, mesh_id):
        """Sets the mesh_id of this Mesh.

        The ID of the mesh.  # noqa: E501

        :param mesh_id: The mesh_id of this Mesh.  # noqa: E501
        :type: str
        """

        self._mesh_id = mesh_id

    @property
    def name(self):
        """Gets the name of this Mesh.  # noqa: E501

        The name of the mesh.  # noqa: E501

        :return: The name of this Mesh.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Mesh.

        The name of the mesh.  # noqa: E501

        :param name: The name of this Mesh.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this Mesh.  # noqa: E501

        The time when the mesh was imported.  # noqa: E501

        :return: The created_at of this Mesh.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Mesh.

        The time when the mesh was imported.  # noqa: E501

        :param created_at: The created_at of this Mesh.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def number_of_cells(self):
        """Gets the number_of_cells of this Mesh.  # noqa: E501

        Number of cells of the mesh.  # noqa: E501

        :return: The number_of_cells of this Mesh.  # noqa: E501
        :rtype: int
        """
        return self._number_of_cells

    @number_of_cells.setter
    def number_of_cells(self, number_of_cells):
        """Sets the number_of_cells of this Mesh.

        Number of cells of the mesh.  # noqa: E501

        :param number_of_cells: The number_of_cells of this Mesh.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                number_of_cells is not None and number_of_cells < 0):  # noqa: E501
            raise ValueError("Invalid value for `number_of_cells`, must be a value greater than or equal to `0`")  # noqa: E501

        self._number_of_cells = number_of_cells

    @property
    def number_of_nodes(self):
        """Gets the number_of_nodes of this Mesh.  # noqa: E501

        Number of nodes of the mesh.  # noqa: E501

        :return: The number_of_nodes of this Mesh.  # noqa: E501
        :rtype: int
        """
        return self._number_of_nodes

    @number_of_nodes.setter
    def number_of_nodes(self, number_of_nodes):
        """Sets the number_of_nodes of this Mesh.

        Number of nodes of the mesh.  # noqa: E501

        :param number_of_nodes: The number_of_nodes of this Mesh.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                number_of_nodes is not None and number_of_nodes < 0):  # noqa: E501
            raise ValueError("Invalid value for `number_of_nodes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._number_of_nodes = number_of_nodes

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
        if not isinstance(other, Mesh):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Mesh):
            return True

        return self.to_dict() != other.to_dict()
