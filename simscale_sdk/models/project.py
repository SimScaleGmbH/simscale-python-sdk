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


class Project(object):
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
        'project_id': 'str',
        'space_id': 'str',
        'parent_folder_id': 'str',
        'created_at': 'datetime',
        'name': 'str',
        'description': 'str',
        'measurement_system': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'project_id': 'projectId',
        'space_id': 'spaceId',
        'parent_folder_id': 'parentFolderId',
        'created_at': 'createdAt',
        'name': 'name',
        'description': 'description',
        'measurement_system': 'measurementSystem',
        'tags': 'tags'
    }

    def __init__(self, project_id=None, space_id=None, parent_folder_id=None, created_at=None, name=None, description=None, measurement_system='SI', tags=None, local_vars_configuration=None):  # noqa: E501
        """Project - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._project_id = None
        self._space_id = None
        self._parent_folder_id = None
        self._created_at = None
        self._name = None
        self._description = None
        self._measurement_system = None
        self._tags = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if space_id is not None:
            self.space_id = space_id
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id
        if created_at is not None:
            self.created_at = created_at
        self.name = name
        self.description = description
        self.measurement_system = measurement_system
        if tags is not None:
            self.tags = tags

    @property
    def project_id(self):
        """Gets the project_id of this Project.  # noqa: E501


        :return: The project_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Project.


        :param project_id: The project_id of this Project.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def space_id(self):
        """Gets the space_id of this Project.  # noqa: E501

        Always returned by the backend. Optional at project creation. If missing, the project will be created in the Personal Space of the user.  # noqa: E501

        :return: The space_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this Project.

        Always returned by the backend. Optional at project creation. If missing, the project will be created in the Personal Space of the user.  # noqa: E501

        :param space_id: The space_id of this Project.  # noqa: E501
        :type: str
        """

        self._space_id = space_id

    @property
    def parent_folder_id(self):
        """Gets the parent_folder_id of this Project.  # noqa: E501

        If missing, the project is located at the root level of the Space.  # noqa: E501

        :return: The parent_folder_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, parent_folder_id):
        """Sets the parent_folder_id of this Project.

        If missing, the project is located at the root level of the Space.  # noqa: E501

        :param parent_folder_id: The parent_folder_id of this Project.  # noqa: E501
        :type: str
        """

        self._parent_folder_id = parent_folder_id

    @property
    def created_at(self):
        """Gets the created_at of this Project.  # noqa: E501


        :return: The created_at of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Project.


        :param created_at: The created_at of this Project.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501

        The project title should contain the application you want to analyze as well as the simulation method you want to use, e.g. 'Heat exchanger - CHT simulation'.   # noqa: E501

        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.

        The project title should contain the application you want to analyze as well as the simulation method you want to use, e.g. 'Heat exchanger - CHT simulation'.   # noqa: E501

        :param name: The name of this Project.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 250):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `250`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Project.  # noqa: E501

        A meaningful description of the project.  # noqa: E501

        :return: The description of this Project.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Project.

        A meaningful description of the project.  # noqa: E501

        :param description: The description of this Project.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 2000):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `2000`")  # noqa: E501

        self._description = description

    @property
    def measurement_system(self):
        """Gets the measurement_system of this Project.  # noqa: E501

        The measurement system of the project. Can't be modified.  # noqa: E501

        :return: The measurement_system of this Project.  # noqa: E501
        :rtype: str
        """
        return self._measurement_system

    @measurement_system.setter
    def measurement_system(self, measurement_system):
        """Sets the measurement_system of this Project.

        The measurement system of the project. Can't be modified.  # noqa: E501

        :param measurement_system: The measurement_system of this Project.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and measurement_system is None:  # noqa: E501
            raise ValueError("Invalid value for `measurement_system`, must not be `None`")  # noqa: E501
        allowed_values = ["SI", "US_CUSTOMARY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and measurement_system not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `measurement_system` ({0}), must be one of {1}"  # noqa: E501
                .format(measurement_system, allowed_values)
            )

        self._measurement_system = measurement_system

    @property
    def tags(self):
        """Gets the tags of this Project.  # noqa: E501


        :return: The tags of this Project.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Project.


        :param tags: The tags of this Project.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, Project):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Project):
            return True

        return self.to_dict() != other.to_dict()
