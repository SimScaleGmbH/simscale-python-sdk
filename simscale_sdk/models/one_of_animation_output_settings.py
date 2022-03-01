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


class OneOfAnimationOutputSettings(object):
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
        'frame_rate': 'int',
        'show_legend': 'bool',
        'show_cube': 'bool',
        'background_color': 'Color',
        'type': 'str',
        'from_frame_index': 'int',
        'to_frame_index': 'int',
        'skip_frames': 'int',
        'frame_index': 'int',
        'steps': 'int',
        'range': 'str'
    }

    attribute_map = {
        'name': 'name',
        'format': 'format',
        'resolution': 'resolution',
        'frame_rate': 'frameRate',
        'show_legend': 'showLegend',
        'show_cube': 'showCube',
        'background_color': 'backgroundColor',
        'type': 'type',
        'from_frame_index': 'fromFrameIndex',
        'to_frame_index': 'toFrameIndex',
        'skip_frames': 'skipFrames',
        'frame_index': 'frameIndex',
        'steps': 'steps',
        'range': 'range'
    }

    discriminator_value_class_map = {
        'TIME_STEP': 'TimeStepAnimationOutputSettings',
        'PARTICLE_TRACE': 'ParticleTraceAnimationOutputSettings',
        'SHAPE': 'ShapeAnimationOutputSettings'
    }

    def __init__(self, name=None, format='GIF', resolution=None, frame_rate=20, show_legend=True, show_cube=True, background_color=None, type='SHAPE', from_frame_index=0, to_frame_index=None, skip_frames=0, frame_index=None, steps=30, range='FULL', local_vars_configuration=None):  # noqa: E501
        """OneOfAnimationOutputSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._format = None
        self._resolution = None
        self._frame_rate = None
        self._show_legend = None
        self._show_cube = None
        self._background_color = None
        self._type = None
        self._from_frame_index = None
        self._to_frame_index = None
        self._skip_frames = None
        self._frame_index = None
        self._steps = None
        self._range = None
        self.discriminator = 'type'

        self.name = name
        self.format = format
        self.resolution = resolution
        self.frame_rate = frame_rate
        self.show_legend = show_legend
        self.show_cube = show_cube
        if background_color is not None:
            self.background_color = background_color
        self.type = type
        self.from_frame_index = from_frame_index
        self.to_frame_index = to_frame_index
        self.skip_frames = skip_frames
        if frame_index is not None:
            self.frame_index = frame_index
        self.steps = steps
        self.range = range

    @property
    def name(self):
        """Gets the name of this OneOfAnimationOutputSettings.  # noqa: E501


        :return: The name of this OneOfAnimationOutputSettings.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfAnimationOutputSettings.


        :param name: The name of this OneOfAnimationOutputSettings.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def format(self):
        """Gets the format of this OneOfAnimationOutputSettings.  # noqa: E501


        :return: The format of this OneOfAnimationOutputSettings.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this OneOfAnimationOutputSettings.


        :param format: The format of this OneOfAnimationOutputSettings.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and format is None:  # noqa: E501
            raise ValueError("Invalid value for `format`, must not be `None`")  # noqa: E501
        allowed_values = ["GIF", "MP4"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and format not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def resolution(self):
        """Gets the resolution of this OneOfAnimationOutputSettings.  # noqa: E501


        :return: The resolution of this OneOfAnimationOutputSettings.  # noqa: E501
        :rtype: ResolutionInfo
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this OneOfAnimationOutputSettings.


        :param resolution: The resolution of this OneOfAnimationOutputSettings.  # noqa: E501
        :type: ResolutionInfo
        """
        if self.local_vars_configuration.client_side_validation and resolution is None:  # noqa: E501
            raise ValueError("Invalid value for `resolution`, must not be `None`")  # noqa: E501

        self._resolution = resolution

    @property
    def frame_rate(self):
        """Gets the frame_rate of this OneOfAnimationOutputSettings.  # noqa: E501


        :return: The frame_rate of this OneOfAnimationOutputSettings.  # noqa: E501
        :rtype: int
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this OneOfAnimationOutputSettings.


        :param frame_rate: The frame_rate of this OneOfAnimationOutputSettings.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and frame_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `frame_rate`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                frame_rate is not None and frame_rate > 60):  # noqa: E501
            raise ValueError("Invalid value for `frame_rate`, must be a value less than or equal to `60`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                frame_rate is not None and frame_rate < 1):  # noqa: E501
            raise ValueError("Invalid value for `frame_rate`, must be a value greater than or equal to `1`")  # noqa: E501

        self._frame_rate = frame_rate

    @property
    def show_legend(self):
        """Gets the show_legend of this OneOfAnimationOutputSettings.  # noqa: E501


        :return: The show_legend of this OneOfAnimationOutputSettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_legend

    @show_legend.setter
    def show_legend(self, show_legend):
        """Sets the show_legend of this OneOfAnimationOutputSettings.


        :param show_legend: The show_legend of this OneOfAnimationOutputSettings.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and show_legend is None:  # noqa: E501
            raise ValueError("Invalid value for `show_legend`, must not be `None`")  # noqa: E501

        self._show_legend = show_legend

    @property
    def show_cube(self):
        """Gets the show_cube of this OneOfAnimationOutputSettings.  # noqa: E501


        :return: The show_cube of this OneOfAnimationOutputSettings.  # noqa: E501
        :rtype: bool
        """
        return self._show_cube

    @show_cube.setter
    def show_cube(self, show_cube):
        """Sets the show_cube of this OneOfAnimationOutputSettings.


        :param show_cube: The show_cube of this OneOfAnimationOutputSettings.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and show_cube is None:  # noqa: E501
            raise ValueError("Invalid value for `show_cube`, must not be `None`")  # noqa: E501

        self._show_cube = show_cube

    @property
    def background_color(self):
        """Gets the background_color of this OneOfAnimationOutputSettings.  # noqa: E501


        :return: The background_color of this OneOfAnimationOutputSettings.  # noqa: E501
        :rtype: Color
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this OneOfAnimationOutputSettings.


        :param background_color: The background_color of this OneOfAnimationOutputSettings.  # noqa: E501
        :type: Color
        """

        self._background_color = background_color

    @property
    def type(self):
        """Gets the type of this OneOfAnimationOutputSettings.  # noqa: E501


        :return: The type of this OneOfAnimationOutputSettings.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfAnimationOutputSettings.


        :param type: The type of this OneOfAnimationOutputSettings.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def from_frame_index(self):
        """Gets the from_frame_index of this OneOfAnimationOutputSettings.  # noqa: E501


        :return: The from_frame_index of this OneOfAnimationOutputSettings.  # noqa: E501
        :rtype: int
        """
        return self._from_frame_index

    @from_frame_index.setter
    def from_frame_index(self, from_frame_index):
        """Sets the from_frame_index of this OneOfAnimationOutputSettings.


        :param from_frame_index: The from_frame_index of this OneOfAnimationOutputSettings.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and from_frame_index is None:  # noqa: E501
            raise ValueError("Invalid value for `from_frame_index`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                from_frame_index is not None and from_frame_index < 0):  # noqa: E501
            raise ValueError("Invalid value for `from_frame_index`, must be a value greater than or equal to `0`")  # noqa: E501

        self._from_frame_index = from_frame_index

    @property
    def to_frame_index(self):
        """Gets the to_frame_index of this OneOfAnimationOutputSettings.  # noqa: E501


        :return: The to_frame_index of this OneOfAnimationOutputSettings.  # noqa: E501
        :rtype: int
        """
        return self._to_frame_index

    @to_frame_index.setter
    def to_frame_index(self, to_frame_index):
        """Sets the to_frame_index of this OneOfAnimationOutputSettings.


        :param to_frame_index: The to_frame_index of this OneOfAnimationOutputSettings.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and to_frame_index is None:  # noqa: E501
            raise ValueError("Invalid value for `to_frame_index`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                to_frame_index is not None and to_frame_index < 0):  # noqa: E501
            raise ValueError("Invalid value for `to_frame_index`, must be a value greater than or equal to `0`")  # noqa: E501

        self._to_frame_index = to_frame_index

    @property
    def skip_frames(self):
        """Gets the skip_frames of this OneOfAnimationOutputSettings.  # noqa: E501


        :return: The skip_frames of this OneOfAnimationOutputSettings.  # noqa: E501
        :rtype: int
        """
        return self._skip_frames

    @skip_frames.setter
    def skip_frames(self, skip_frames):
        """Sets the skip_frames of this OneOfAnimationOutputSettings.


        :param skip_frames: The skip_frames of this OneOfAnimationOutputSettings.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and skip_frames is None:  # noqa: E501
            raise ValueError("Invalid value for `skip_frames`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                skip_frames is not None and skip_frames < 0):  # noqa: E501
            raise ValueError("Invalid value for `skip_frames`, must be a value greater than or equal to `0`")  # noqa: E501

        self._skip_frames = skip_frames

    @property
    def frame_index(self):
        """Gets the frame_index of this OneOfAnimationOutputSettings.  # noqa: E501

        Frame (or frequency) for which to create a mode shape animation.Default is the last frame in the result.  # noqa: E501

        :return: The frame_index of this OneOfAnimationOutputSettings.  # noqa: E501
        :rtype: int
        """
        return self._frame_index

    @frame_index.setter
    def frame_index(self, frame_index):
        """Sets the frame_index of this OneOfAnimationOutputSettings.

        Frame (or frequency) for which to create a mode shape animation.Default is the last frame in the result.  # noqa: E501

        :param frame_index: The frame_index of this OneOfAnimationOutputSettings.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                frame_index is not None and frame_index < 0):  # noqa: E501
            raise ValueError("Invalid value for `frame_index`, must be a value greater than or equal to `0`")  # noqa: E501

        self._frame_index = frame_index

    @property
    def steps(self):
        """Gets the steps of this OneOfAnimationOutputSettings.  # noqa: E501

        The number of steps to generate for the shape animation  # noqa: E501

        :return: The steps of this OneOfAnimationOutputSettings.  # noqa: E501
        :rtype: int
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this OneOfAnimationOutputSettings.

        The number of steps to generate for the shape animation  # noqa: E501

        :param steps: The steps of this OneOfAnimationOutputSettings.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and steps is None:  # noqa: E501
            raise ValueError("Invalid value for `steps`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                steps is not None and steps > 100):  # noqa: E501
            raise ValueError("Invalid value for `steps`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                steps is not None and steps < 1):  # noqa: E501
            raise ValueError("Invalid value for `steps`, must be a value greater than or equal to `1`")  # noqa: E501

        self._steps = steps

    @property
    def range(self):
        """Gets the range of this OneOfAnimationOutputSettings.  # noqa: E501

        How to deform the model for the animation. FULL implies animating from the original, undeformed shape to the maximum displaced position, then back to original shape; do the same for the negative maximum deformation, then back (x_0 -> +x_max -> x_0 -> -x_max -> x_0). HALF implies animating from the original, undeformed shape to the maximum displaced position, then back to original shape (x_0 -> +x_max -> x_0). QUARTER implies animating from the original, undeformed shape to the maxiumum displaced position (x_0 -> +x_max)  # noqa: E501

        :return: The range of this OneOfAnimationOutputSettings.  # noqa: E501
        :rtype: str
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this OneOfAnimationOutputSettings.

        How to deform the model for the animation. FULL implies animating from the original, undeformed shape to the maximum displaced position, then back to original shape; do the same for the negative maximum deformation, then back (x_0 -> +x_max -> x_0 -> -x_max -> x_0). HALF implies animating from the original, undeformed shape to the maximum displaced position, then back to original shape (x_0 -> +x_max -> x_0). QUARTER implies animating from the original, undeformed shape to the maxiumum displaced position (x_0 -> +x_max)  # noqa: E501

        :param range: The range of this OneOfAnimationOutputSettings.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and range is None:  # noqa: E501
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501
        allowed_values = ["FULL", "HALF", "QUARTER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and range not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `range` ({0}), must be one of {1}"  # noqa: E501
                .format(range, allowed_values)
            )

        self._range = range

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
        if not isinstance(other, OneOfAnimationOutputSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfAnimationOutputSettings):
            return True

        return self.to_dict() != other.to_dict()