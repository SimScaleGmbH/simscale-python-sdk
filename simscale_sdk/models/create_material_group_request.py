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


class CreateMaterialGroupRequest(object):
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
        'name': 'str',
        'metadata': 'object',
        'public': 'bool',
        'owner_group_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'metadata': 'metadata',
        'public': 'public',
        'owner_group_id': 'ownerGroupId'
    }

    def __init__(self, name=None, metadata=None, public=None, owner_group_id=None, local_vars_configuration=None):  # noqa: E501
        """CreateMaterialGroupRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._metadata = None
        self._public = None
        self._owner_group_id = None
        self.discriminator = None

        self.name = name
        if metadata is not None:
            self.metadata = metadata
        if public is not None:
            self.public = public
        if owner_group_id is not None:
            self.owner_group_id = owner_group_id

    @property
    def name(self):
        """Gets the name of this CreateMaterialGroupRequest.  # noqa: E501

        The name of the material group.  # noqa: E501

        :return: The name of this CreateMaterialGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateMaterialGroupRequest.

        The name of the material group.  # noqa: E501

        :param name: The name of this CreateMaterialGroupRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 40):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def metadata(self):
        """Gets the metadata of this CreateMaterialGroupRequest.  # noqa: E501


        :return: The metadata of this CreateMaterialGroupRequest.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateMaterialGroupRequest.


        :param metadata: The metadata of this CreateMaterialGroupRequest.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def public(self):
        """Gets the public of this CreateMaterialGroupRequest.  # noqa: E501


        :return: The public of this CreateMaterialGroupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this CreateMaterialGroupRequest.


        :param public: The public of this CreateMaterialGroupRequest.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def owner_group_id(self):
        """Gets the owner_group_id of this CreateMaterialGroupRequest.  # noqa: E501

        The material group will be assigned to this owner group. This field can only be used by support group members.  # noqa: E501

        :return: The owner_group_id of this CreateMaterialGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._owner_group_id

    @owner_group_id.setter
    def owner_group_id(self, owner_group_id):
        """Sets the owner_group_id of this CreateMaterialGroupRequest.

        The material group will be assigned to this owner group. This field can only be used by support group members.  # noqa: E501

        :param owner_group_id: The owner_group_id of this CreateMaterialGroupRequest.  # noqa: E501
        :type: int
        """

        self._owner_group_id = owner_group_id

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
        if not isinstance(other, CreateMaterialGroupRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateMaterialGroupRequest):
            return True

        return self.to_dict() != other.to_dict()
