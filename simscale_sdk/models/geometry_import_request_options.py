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


class GeometryImportRequestOptions(object):
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
        'facet_split': 'bool',
        'sewing': 'bool',
        'improve': 'bool',
        'optimize_for_lbm_solver': 'bool'
    }

    attribute_map = {
        'facet_split': 'facetSplit',
        'sewing': 'sewing',
        'improve': 'improve',
        'optimize_for_lbm_solver': 'optimizeForLBMSolver'
    }

    def __init__(self, facet_split=False, sewing=False, improve=True, optimize_for_lbm_solver=False, local_vars_configuration=None):  # noqa: E501
        """GeometryImportRequestOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._facet_split = None
        self._sewing = None
        self._improve = None
        self._optimize_for_lbm_solver = None
        self.discriminator = None

        self.facet_split = facet_split
        self.sewing = sewing
        self.improve = improve
        self.optimize_for_lbm_solver = optimize_for_lbm_solver

    @property
    def facet_split(self):
        """Gets the facet_split of this GeometryImportRequestOptions.  # noqa: E501

        _Facet Split_ tries to split the faceted parts of a model. This means it can create new faces from original faces. In this case it's not possible to use the original faces to make assignments.   # noqa: E501

        :return: The facet_split of this GeometryImportRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._facet_split

    @facet_split.setter
    def facet_split(self, facet_split):
        """Sets the facet_split of this GeometryImportRequestOptions.

        _Facet Split_ tries to split the faceted parts of a model. This means it can create new faces from original faces. In this case it's not possible to use the original faces to make assignments.   # noqa: E501

        :param facet_split: The facet_split of this GeometryImportRequestOptions.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and facet_split is None:  # noqa: E501
            raise ValueError("Invalid value for `facet_split`, must not be `None`")  # noqa: E501

        self._facet_split = facet_split

    @property
    def sewing(self):
        """Gets the sewing of this GeometryImportRequestOptions.  # noqa: E501

        _Automatic Sewing_ is sewing faces or sheet bodies together. This means that it can create one new face from two (or more) original faces, as well as one solid body from two (or more) original sheet bodies. In this case, if the entities have the same ID, it will be inherited by the newly created entity. However if the original entities do not share the same ID, only one of these will be mapped to the new entity. This might not be desirable if one would like to make assignments on the original entities and not on the new (sewn) entities.   # noqa: E501

        :return: The sewing of this GeometryImportRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._sewing

    @sewing.setter
    def sewing(self, sewing):
        """Sets the sewing of this GeometryImportRequestOptions.

        _Automatic Sewing_ is sewing faces or sheet bodies together. This means that it can create one new face from two (or more) original faces, as well as one solid body from two (or more) original sheet bodies. In this case, if the entities have the same ID, it will be inherited by the newly created entity. However if the original entities do not share the same ID, only one of these will be mapped to the new entity. This might not be desirable if one would like to make assignments on the original entities and not on the new (sewn) entities.   # noqa: E501

        :param sewing: The sewing of this GeometryImportRequestOptions.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and sewing is None:  # noqa: E501
            raise ValueError("Invalid value for `sewing`, must not be `None`")  # noqa: E501

        self._sewing = sewing

    @property
    def improve(self):
        """Gets the improve of this GeometryImportRequestOptions.  # noqa: E501

        This option tries to improve the topology (e.g. edges, vertices) and geometry of the model by adjusting tolerances, simplifying entities, etc. As this option should improve CAD operations and data handling for all downstream applications it is recommended to use it on import. For very complex models it can take a considerable amount of time though, therefore you can also opt-out and reconsider in case you face issues in geometry handling or meshing.   # noqa: E501

        :return: The improve of this GeometryImportRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._improve

    @improve.setter
    def improve(self, improve):
        """Sets the improve of this GeometryImportRequestOptions.

        This option tries to improve the topology (e.g. edges, vertices) and geometry of the model by adjusting tolerances, simplifying entities, etc. As this option should improve CAD operations and data handling for all downstream applications it is recommended to use it on import. For very complex models it can take a considerable amount of time though, therefore you can also opt-out and reconsider in case you face issues in geometry handling or meshing.   # noqa: E501

        :param improve: The improve of this GeometryImportRequestOptions.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and improve is None:  # noqa: E501
            raise ValueError("Invalid value for `improve`, must not be `None`")  # noqa: E501

        self._improve = improve

    @property
    def optimize_for_lbm_solver(self):
        """Gets the optimize_for_lbm_solver of this GeometryImportRequestOptions.  # noqa: E501

        This option allows you to import a *.stl file that is optimized for the Incompressible LBM and Wind Comfort analysis types. It leaves out complex import steps like sewing and cleanup that are not required by the LBM solver and therefore also allows to import big and complex models fast.   # noqa: E501

        :return: The optimize_for_lbm_solver of this GeometryImportRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._optimize_for_lbm_solver

    @optimize_for_lbm_solver.setter
    def optimize_for_lbm_solver(self, optimize_for_lbm_solver):
        """Sets the optimize_for_lbm_solver of this GeometryImportRequestOptions.

        This option allows you to import a *.stl file that is optimized for the Incompressible LBM and Wind Comfort analysis types. It leaves out complex import steps like sewing and cleanup that are not required by the LBM solver and therefore also allows to import big and complex models fast.   # noqa: E501

        :param optimize_for_lbm_solver: The optimize_for_lbm_solver of this GeometryImportRequestOptions.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and optimize_for_lbm_solver is None:  # noqa: E501
            raise ValueError("Invalid value for `optimize_for_lbm_solver`, must not be `None`")  # noqa: E501

        self._optimize_for_lbm_solver = optimize_for_lbm_solver

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
        if not isinstance(other, GeometryImportRequestOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeometryImportRequestOptions):
            return True

        return self.to_dict() != other.to_dict()