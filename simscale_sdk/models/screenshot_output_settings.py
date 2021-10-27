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


class ScreenshotOutputSettings(object):
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
        'format': 'str',
        'resolution': 'ResolutionInfo',
        'frame_index': 'int',
        'show_legend': 'bool',
        'show_cube': 'bool',
        'background_color': 'Color'
    }

    attribute_map = {
        'name': 'name',
        'format': 'format',
        'resolution': 'resolution',
        'frame_index': 'frameIndex',
        'show_legend': 'showLegend',
        'show_cube': 'showCube',
        'background_color': 'backgroundColor'
    }

    def __init__(self, name=None, format='PNG', resolution=None, frame_index=None, show_legend=True, show_cube=True, background_color=None, local_vars_configuration=None):  # noqa: E501
        """ScreenshotOutputSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._format = None
        self._resolution = None
        self._frame_index = None
        self._show_legend = None
        self._show_cube = None
        self._background_color = None
        self.discriminator = None

        self.name = name
        self.format = format
        self.resolution = resolution
        if frame_index is not None:
            self.frame_index = frame_index
        self.show_legend = show_legend
        self.show_cube = show_cube
        if background_color is not None:
            self.background_color = background_color

    @property
    def name(self):
        """Gets the name of this ScreenshotOutputSettings.  # noqa: E501


        :return: The name of this ScreenshotOutputSettings.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScreenshotOutputSettings.


        :param name: The name of this ScreenshotOutputSettings.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def format(self):
        """Gets the format of this ScreenshotOutputSettings.  # noqa: E501


        :return: The format of this ScreenshotOutputSettings.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ScreenshotOutputSettings.


        :param format: The format of this ScreenshotOutputSettings.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and format is None:  # noqa: E501
            raise ValueError("Invalid value for `format`, must not be `None`")  # noqa: E501
        allowed_values = ["PNG"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and format not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def resolution(self):
        """Gets the resolution of this ScreenshotOutputSettings.  # noqa: E501


        :return: The resolution of this ScreenshotOutputSettings.  # noqa: E501
        :rtype: ResolutionInfo
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this ScreenshotOutputSettings.


        :param resolution: The resolution of this ScreenshotOutputSettings.  # noqa: E501
        :type: ResolutionInfo
        """
        if self.local_vars_configuration.client_side_validation and resolution is None:  # noqa: E501
            raise ValueError("Invalid value for `resolution`, must not be `None`")  # noqa: E501

        self._resolution = resolution

    @property
    def frame_index(self):
        """Gets the frame_index of this ScreenshotOutputSettings.  # noqa: E501

        Default to the last timestep or frame in the result.  # noqa: E501

        :return: The frame_index of this ScreenshotOutputSettings.  # noqa: E501
        :rtype: int
        """
        return self._frame_index

    @frame_index.setter
    def frame_index(self, frame_index):
        """Sets the frame_index of this ScreenshotOutputSettings.

        Default to the last timestep or frame in the result.  # noqa: E501

        :param frame_index: The frame_index of this ScreenshotOutputSettings.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                frame_index is not None and frame_index < 0):  # noqa: E501
            raise ValueError("Invalid value for `frame_index`, must be a value greater than or equal to `0`")  # noqa: E501

        self._frame_index = frame_index

    @property
    def show_legend(self):
        """Gets the show_legend of this ScreenshotOutputSettings.  # noqa: E501


        :return: The show_legend of this ScreenshotOutputSettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_legend

    @show_legend.setter
    def show_legend(self, show_legend):
        """Sets the show_legend of this ScreenshotOutputSettings.


        :param show_legend: The show_legend of this ScreenshotOutputSettings.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and show_legend is None:  # noqa: E501
            raise ValueError("Invalid value for `show_legend`, must not be `None`")  # noqa: E501

        self._show_legend = show_legend

    @property
    def show_cube(self):
        """Gets the show_cube of this ScreenshotOutputSettings.  # noqa: E501


        :return: The show_cube of this ScreenshotOutputSettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_cube

    @show_cube.setter
    def show_cube(self, show_cube):
        """Sets the show_cube of this ScreenshotOutputSettings.


        :param show_cube: The show_cube of this ScreenshotOutputSettings.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and show_cube is None:  # noqa: E501
            raise ValueError("Invalid value for `show_cube`, must not be `None`")  # noqa: E501

        self._show_cube = show_cube

    @property
    def background_color(self):
        """Gets the background_color of this ScreenshotOutputSettings.  # noqa: E501


        :return: The background_color of this ScreenshotOutputSettings.  # noqa: E501
        :rtype: Color
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this ScreenshotOutputSettings.


        :param background_color: The background_color of this ScreenshotOutputSettings.  # noqa: E501
        :type: Color
        """

        self._background_color = background_color

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
        if not isinstance(other, ScreenshotOutputSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScreenshotOutputSettings):
            return True

        return self.to_dict() != other.to_dict()
