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


class ManualSimericsMeshSettings(object):
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
        'refinements': 'list[RegionRefinementSimerics]',
        'cell_size_specification': 'OneOfManualSimericsMeshSettingsCellSizeSpecification',
        'enable_cad_surface_merging': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'refinements': 'refinements',
        'cell_size_specification': 'cellSizeSpecification',
        'enable_cad_surface_merging': 'enableCADSurfaceMerging'
    }

    def __init__(self, type='MANUAL_SETTINGS', refinements=None, cell_size_specification=None, enable_cad_surface_merging=None, local_vars_configuration=None):  # noqa: E501
        """ManualSimericsMeshSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._refinements = None
        self._cell_size_specification = None
        self._enable_cad_surface_merging = None
        self.discriminator = None

        self.type = type
        if refinements is not None:
            self.refinements = refinements
        if cell_size_specification is not None:
            self.cell_size_specification = cell_size_specification
        if enable_cad_surface_merging is not None:
            self.enable_cad_surface_merging = enable_cad_surface_merging

    @property
    def type(self):
        """Gets the type of this ManualSimericsMeshSettings.  # noqa: E501

        Schema name: ManualSimericsMeshSettings  # noqa: E501

        :return: The type of this ManualSimericsMeshSettings.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ManualSimericsMeshSettings.

        Schema name: ManualSimericsMeshSettings  # noqa: E501

        :param type: The type of this ManualSimericsMeshSettings.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def refinements(self):
        """Gets the refinements of this ManualSimericsMeshSettings.  # noqa: E501


        :return: The refinements of this ManualSimericsMeshSettings.  # noqa: E501
        :rtype: list[RegionRefinementSimerics]
        """
        return self._refinements

    @refinements.setter
    def refinements(self, refinements):
        """Sets the refinements of this ManualSimericsMeshSettings.


        :param refinements: The refinements of this ManualSimericsMeshSettings.  # noqa: E501
        :type: list[RegionRefinementSimerics]
        """

        self._refinements = refinements

    @property
    def cell_size_specification(self):
        """Gets the cell_size_specification of this ManualSimericsMeshSettings.  # noqa: E501


        :return: The cell_size_specification of this ManualSimericsMeshSettings.  # noqa: E501
        :rtype: OneOfManualSimericsMeshSettingsCellSizeSpecification
        """
        return self._cell_size_specification

    @cell_size_specification.setter
    def cell_size_specification(self, cell_size_specification):
        """Sets the cell_size_specification of this ManualSimericsMeshSettings.


        :param cell_size_specification: The cell_size_specification of this ManualSimericsMeshSettings.  # noqa: E501
        :type: OneOfManualSimericsMeshSettingsCellSizeSpecification
        """

        self._cell_size_specification = cell_size_specification

    @property
    def enable_cad_surface_merging(self):
        """Gets the enable_cad_surface_merging of this ManualSimericsMeshSettings.  # noqa: E501

        <b>Merge CAD surfaces</b> combines all surfaces of the CAD model that are <i>not</i> assigned a boundary condition or result control. With this turned on, the probability of successful mesh generation for more complicated geometries significantly increases. If you need to inspect unassigned surfaces separately, turn it off. For more information, please contact Support.  # noqa: E501

        :return: The enable_cad_surface_merging of this ManualSimericsMeshSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_cad_surface_merging

    @enable_cad_surface_merging.setter
    def enable_cad_surface_merging(self, enable_cad_surface_merging):
        """Sets the enable_cad_surface_merging of this ManualSimericsMeshSettings.

        <b>Merge CAD surfaces</b> combines all surfaces of the CAD model that are <i>not</i> assigned a boundary condition or result control. With this turned on, the probability of successful mesh generation for more complicated geometries significantly increases. If you need to inspect unassigned surfaces separately, turn it off. For more information, please contact Support.  # noqa: E501

        :param enable_cad_surface_merging: The enable_cad_surface_merging of this ManualSimericsMeshSettings.  # noqa: E501
        :type: bool
        """

        self._enable_cad_surface_merging = enable_cad_surface_merging

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
        if not isinstance(other, ManualSimericsMeshSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ManualSimericsMeshSettings):
            return True

        return self.to_dict() != other.to_dict()