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


class SimulationRunResultDownload(object):
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
        'format': 'str',
        'uncompressed_size_in_bytes': 'int',
        'url': 'str',
        'compression': 'str',
        'can_export': 'bool',
        'available_export_formats': 'list[str]'
    }

    attribute_map = {
        'format': 'format',
        'uncompressed_size_in_bytes': 'uncompressedSizeInBytes',
        'url': 'url',
        'compression': 'compression',
        'can_export': 'canExport',
        'available_export_formats': 'availableExportFormats'
    }

    def __init__(self, format=None, uncompressed_size_in_bytes=None, url=None, compression=None, can_export=None, available_export_formats=None, local_vars_configuration=None):  # noqa: E501
        """SimulationRunResultDownload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._format = None
        self._uncompressed_size_in_bytes = None
        self._url = None
        self._compression = None
        self._can_export = None
        self._available_export_formats = None
        self.discriminator = None

        if format is not None:
            self.format = format
        if uncompressed_size_in_bytes is not None:
            self.uncompressed_size_in_bytes = uncompressed_size_in_bytes
        if url is not None:
            self.url = url
        if compression is not None:
            self.compression = compression
        if can_export is not None:
            self.can_export = can_export
        if available_export_formats is not None:
            self.available_export_formats = available_export_formats

    @property
    def format(self):
        """Gets the format of this SimulationRunResultDownload.  # noqa: E501

        The result format. Valid values include `OPEN_FOAM`, `ENSIGHT_GOLD`, `PVD`, `VTM`, `CSV`.   # noqa: E501

        :return: The format of this SimulationRunResultDownload.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this SimulationRunResultDownload.

        The result format. Valid values include `OPEN_FOAM`, `ENSIGHT_GOLD`, `PVD`, `VTM`, `CSV`.   # noqa: E501

        :param format: The format of this SimulationRunResultDownload.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def uncompressed_size_in_bytes(self):
        """Gets the uncompressed_size_in_bytes of this SimulationRunResultDownload.  # noqa: E501

        The uncompressed size of the result content.  # noqa: E501

        :return: The uncompressed_size_in_bytes of this SimulationRunResultDownload.  # noqa: E501
        :rtype: int
        """
        return self._uncompressed_size_in_bytes

    @uncompressed_size_in_bytes.setter
    def uncompressed_size_in_bytes(self, uncompressed_size_in_bytes):
        """Sets the uncompressed_size_in_bytes of this SimulationRunResultDownload.

        The uncompressed size of the result content.  # noqa: E501

        :param uncompressed_size_in_bytes: The uncompressed_size_in_bytes of this SimulationRunResultDownload.  # noqa: E501
        :type: int
        """

        self._uncompressed_size_in_bytes = uncompressed_size_in_bytes

    @property
    def url(self):
        """Gets the url of this SimulationRunResultDownload.  # noqa: E501

        URL for downloading the result content.  # noqa: E501

        :return: The url of this SimulationRunResultDownload.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SimulationRunResultDownload.

        URL for downloading the result content.  # noqa: E501

        :param url: The url of this SimulationRunResultDownload.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def compression(self):
        """Gets the compression of this SimulationRunResultDownload.  # noqa: E501

        The compression used for the result download archive.  # noqa: E501

        :return: The compression of this SimulationRunResultDownload.  # noqa: E501
        :rtype: str
        """
        return self._compression

    @compression.setter
    def compression(self, compression):
        """Sets the compression of this SimulationRunResultDownload.

        The compression used for the result download archive.  # noqa: E501

        :param compression: The compression of this SimulationRunResultDownload.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "ZIP64"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and compression not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `compression` ({0}), must be one of {1}"  # noqa: E501
                .format(compression, allowed_values)
            )

        self._compression = compression

    @property
    def can_export(self):
        """Gets the can_export of this SimulationRunResultDownload.  # noqa: E501

        Can this result be exported and downloaded  # noqa: E501

        :return: The can_export of this SimulationRunResultDownload.  # noqa: E501
        :rtype: bool
        """
        return self._can_export

    @can_export.setter
    def can_export(self, can_export):
        """Sets the can_export of this SimulationRunResultDownload.

        Can this result be exported and downloaded  # noqa: E501

        :param can_export: The can_export of this SimulationRunResultDownload.  # noqa: E501
        :type: bool
        """

        self._can_export = can_export

    @property
    def available_export_formats(self):
        """Gets the available_export_formats of this SimulationRunResultDownload.  # noqa: E501

        Supported export format for this result.  # noqa: E501

        :return: The available_export_formats of this SimulationRunResultDownload.  # noqa: E501
        :rtype: list[str]
        """
        return self._available_export_formats

    @available_export_formats.setter
    def available_export_formats(self, available_export_formats):
        """Sets the available_export_formats of this SimulationRunResultDownload.

        Supported export format for this result.  # noqa: E501

        :param available_export_formats: The available_export_formats of this SimulationRunResultDownload.  # noqa: E501
        :type: list[str]
        """

        self._available_export_formats = available_export_formats

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
        if not isinstance(other, SimulationRunResultDownload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimulationRunResultDownload):
            return True

        return self.to_dict() != other.to_dict()
