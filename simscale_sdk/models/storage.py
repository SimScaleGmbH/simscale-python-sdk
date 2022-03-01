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


class Storage(object):
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
        'url': 'str',
        'storage_id': 'str',
        'expires_at': 'datetime'
    }

    attribute_map = {
        'url': 'url',
        'storage_id': 'storageId',
        'expires_at': 'expiresAt'
    }

    def __init__(self, url=None, storage_id=None, expires_at=None, local_vars_configuration=None):  # noqa: E501
        """Storage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._storage_id = None
        self._expires_at = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if storage_id is not None:
            self.storage_id = storage_id
        if expires_at is not None:
            self.expires_at = expires_at

    @property
    def url(self):
        """Gets the url of this Storage.  # noqa: E501

        The URL of the temporary storage location.  # noqa: E501

        :return: The url of this Storage.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Storage.

        The URL of the temporary storage location.  # noqa: E501

        :param url: The url of this Storage.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def storage_id(self):
        """Gets the storage_id of this Storage.  # noqa: E501

        The storage ID.  # noqa: E501

        :return: The storage_id of this Storage.  # noqa: E501
        :rtype: str
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        """Sets the storage_id of this Storage.

        The storage ID.  # noqa: E501

        :param storage_id: The storage_id of this Storage.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                storage_id is not None and len(storage_id) < 1):
            raise ValueError("Invalid value for `storage_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._storage_id = storage_id

    @property
    def expires_at(self):
        """Gets the expires_at of this Storage.  # noqa: E501

        The expiration time.  # noqa: E501

        :return: The expires_at of this Storage.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this Storage.

        The expiration time.  # noqa: E501

        :param expires_at: The expires_at of this Storage.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

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
        if not isinstance(other, Storage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Storage):
            return True

        return self.to_dict() != other.to_dict()