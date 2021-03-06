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


class SubmeshRefinement(object):
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
        'name': 'str',
        'sizing': 'OneOfSubmeshRefinementSizing',
        'allow_quadrangles': 'bool',
        'topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'sizing': 'sizing',
        'allow_quadrangles': 'allowQuadrangles',
        'topological_reference': 'topologicalReference'
    }

    def __init__(self, type='SUBMESH', name=None, sizing=None, allow_quadrangles=None, topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """SubmeshRefinement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._sizing = None
        self._allow_quadrangles = None
        self._topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if sizing is not None:
            self.sizing = sizing
        if allow_quadrangles is not None:
            self.allow_quadrangles = allow_quadrangles
        if topological_reference is not None:
            self.topological_reference = topological_reference

    @property
    def type(self):
        """Gets the type of this SubmeshRefinement.  # noqa: E501

        <p>The refinement type <a href='https://www.simscale.com/docs/simulation-setup/meshing/tet-dominant/#local-element-size' target='_blank'><b>local element size</b></a> allows the definition of local mesh sizings on particular faces or solids. This can be used to increase the mesh efficiency by using smaller elements only where needed, for example on contact surfaces, fillets or other regions with potentially large stress gradients.</p><p><img src=\"/spec/resources/help/imgs/local_element_size.png\" class=\"helpPopupImage\"/> The figure shows a mesh of a bolted connection with local refinements on the contact surfaces.</p>  Schema name: SubmeshRefinement  # noqa: E501

        :return: The type of this SubmeshRefinement.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SubmeshRefinement.

        <p>The refinement type <a href='https://www.simscale.com/docs/simulation-setup/meshing/tet-dominant/#local-element-size' target='_blank'><b>local element size</b></a> allows the definition of local mesh sizings on particular faces or solids. This can be used to increase the mesh efficiency by using smaller elements only where needed, for example on contact surfaces, fillets or other regions with potentially large stress gradients.</p><p><img src=\"/spec/resources/help/imgs/local_element_size.png\" class=\"helpPopupImage\"/> The figure shows a mesh of a bolted connection with local refinements on the contact surfaces.</p>  Schema name: SubmeshRefinement  # noqa: E501

        :param type: The type of this SubmeshRefinement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this SubmeshRefinement.  # noqa: E501


        :return: The name of this SubmeshRefinement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubmeshRefinement.


        :param name: The name of this SubmeshRefinement.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sizing(self):
        """Gets the sizing of this SubmeshRefinement.  # noqa: E501


        :return: The sizing of this SubmeshRefinement.  # noqa: E501
        :rtype: OneOfSubmeshRefinementSizing
        """
        return self._sizing

    @sizing.setter
    def sizing(self, sizing):
        """Sets the sizing of this SubmeshRefinement.


        :param sizing: The sizing of this SubmeshRefinement.  # noqa: E501
        :type: OneOfSubmeshRefinementSizing
        """

        self._sizing = sizing

    @property
    def allow_quadrangles(self):
        """Gets the allow_quadrangles of this SubmeshRefinement.  # noqa: E501

        <p>This parameter determines if <a href='https://www.simscale.com/docs/simulation-setup/meshing/tet-dominant/#quadrangles' target='_blank'><b>quadrangular surface elements</b></a> shall be allowed. When disabled, only triangles will be used. Meshing with triangles only is usually more robust while quadrangular elements may lead to better results.</p><p><img src=\"/spec/resources/help/imgs/allow_quads_comparison.png\" class=\"helpPopupImage\"/> The figure shows sample meshes with quadrangular surface elements disallowed (left) and allowed (right).</p>  # noqa: E501

        :return: The allow_quadrangles of this SubmeshRefinement.  # noqa: E501
        :rtype: bool
        """
        return self._allow_quadrangles

    @allow_quadrangles.setter
    def allow_quadrangles(self, allow_quadrangles):
        """Sets the allow_quadrangles of this SubmeshRefinement.

        <p>This parameter determines if <a href='https://www.simscale.com/docs/simulation-setup/meshing/tet-dominant/#quadrangles' target='_blank'><b>quadrangular surface elements</b></a> shall be allowed. When disabled, only triangles will be used. Meshing with triangles only is usually more robust while quadrangular elements may lead to better results.</p><p><img src=\"/spec/resources/help/imgs/allow_quads_comparison.png\" class=\"helpPopupImage\"/> The figure shows sample meshes with quadrangular surface elements disallowed (left) and allowed (right).</p>  # noqa: E501

        :param allow_quadrangles: The allow_quadrangles of this SubmeshRefinement.  # noqa: E501
        :type: bool
        """

        self._allow_quadrangles = allow_quadrangles

    @property
    def topological_reference(self):
        """Gets the topological_reference of this SubmeshRefinement.  # noqa: E501


        :return: The topological_reference of this SubmeshRefinement.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this SubmeshRefinement.


        :param topological_reference: The topological_reference of this SubmeshRefinement.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

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
        if not isinstance(other, SubmeshRefinement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubmeshRefinement):
            return True

        return self.to_dict() != other.to_dict()
