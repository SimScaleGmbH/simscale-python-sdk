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


class OneOfRegionRefinementWindComfortNewFineness(object):
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
        'minimum_cell_size': 'DimensionalLength'
    }

    attribute_map = {
        'type': 'type',
        'minimum_cell_size': 'minimumCellSize'
    }

    discriminator_value_class_map = {
        'VERY_COARSE': 'PacefishFinenessVeryCoarse',
        'COARSE': 'PacefishFinenessCoarse',
        'MODERATE': 'PacefishFinenessModerate',
        'FINE': 'PacefishFinenessFine',
        'VERY_FINE': 'PacefishFinenessVeryFine',
        'TARGET_SIZE': 'PacefishFinenessTargetSize'
    }

    def __init__(self, type='TARGET_SIZE', minimum_cell_size=None, local_vars_configuration=None):  # noqa: E501
        """OneOfRegionRefinementWindComfortNewFineness - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._minimum_cell_size = None
        self.discriminator = 'type'

        self.type = type
        if minimum_cell_size is not None:
            self.minimum_cell_size = minimum_cell_size

    @property
    def type(self):
        """Gets the type of this OneOfRegionRefinementWindComfortNewFineness.  # noqa: E501

        <p>This parameter determines the <b>fineness of the mesh</b> and affects the overall number of cells. It is recommended to start with the <i>coarse</i> setting. <a href='https://www.simscale.com/docs/analysis-types/pedestrian-wind-comfort-analysis/mesh-settings/' target='_blank'>Find out more.</a></p><p><b>Note:</b> This setting will impact the accuracy of your results as well as computing time and result size. A finer mesh will be more demanding in terms of machine size and memory but lead to more accurate results in most cases.</p>  Schema name: PacefishFinenessTargetSize  # noqa: E501

        :return: The type of this OneOfRegionRefinementWindComfortNewFineness.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfRegionRefinementWindComfortNewFineness.

        <p>This parameter determines the <b>fineness of the mesh</b> and affects the overall number of cells. It is recommended to start with the <i>coarse</i> setting. <a href='https://www.simscale.com/docs/analysis-types/pedestrian-wind-comfort-analysis/mesh-settings/' target='_blank'>Find out more.</a></p><p><b>Note:</b> This setting will impact the accuracy of your results as well as computing time and result size. A finer mesh will be more demanding in terms of machine size and memory but lead to more accurate results in most cases.</p>  Schema name: PacefishFinenessTargetSize  # noqa: E501

        :param type: The type of this OneOfRegionRefinementWindComfortNewFineness.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def minimum_cell_size(self):
        """Gets the minimum_cell_size of this OneOfRegionRefinementWindComfortNewFineness.  # noqa: E501


        :return: The minimum_cell_size of this OneOfRegionRefinementWindComfortNewFineness.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._minimum_cell_size

    @minimum_cell_size.setter
    def minimum_cell_size(self, minimum_cell_size):
        """Sets the minimum_cell_size of this OneOfRegionRefinementWindComfortNewFineness.


        :param minimum_cell_size: The minimum_cell_size of this OneOfRegionRefinementWindComfortNewFineness.  # noqa: E501
        :type: DimensionalLength
        """

        self._minimum_cell_size = minimum_cell_size

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
        if not isinstance(other, OneOfRegionRefinementWindComfortNewFineness):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfRegionRefinementWindComfortNewFineness):
            return True

        return self.to_dict() != other.to_dict()
