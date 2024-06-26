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


class AdvancedConnectorSettings(object):
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
        'assigned_face_behavior': 'str'
    }

    attribute_map = {
        'assigned_face_behavior': 'assignedFaceBehavior'
    }

    def __init__(self, assigned_face_behavior=None, local_vars_configuration=None):  # noqa: E501
        """AdvancedConnectorSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._assigned_face_behavior = None
        self.discriminator = None

        if assigned_face_behavior is not None:
            self.assigned_face_behavior = assigned_face_behavior

    @property
    def assigned_face_behavior(self):
        """Gets the assigned_face_behavior of this AdvancedConnectorSettings.  # noqa: E501

        <p>Choose the deformation behavior of the assigned entity. If <b>deformable</b> is selected, the entity is allowed to deform without applying additional stiffness, selecting <b>undeformable</b> leads to a rigid entity. <a href='https://www.simscale.com/docs/simulation-setup/boundary-conditions/remote-displacement/#deformation-behavior' target='_blank'>Learn more</a></p>  # noqa: E501

        :return: The assigned_face_behavior of this AdvancedConnectorSettings.  # noqa: E501
        :rtype: str
        """
        return self._assigned_face_behavior

    @assigned_face_behavior.setter
    def assigned_face_behavior(self, assigned_face_behavior):
        """Sets the assigned_face_behavior of this AdvancedConnectorSettings.

        <p>Choose the deformation behavior of the assigned entity. If <b>deformable</b> is selected, the entity is allowed to deform without applying additional stiffness, selecting <b>undeformable</b> leads to a rigid entity. <a href='https://www.simscale.com/docs/simulation-setup/boundary-conditions/remote-displacement/#deformation-behavior' target='_blank'>Learn more</a></p>  # noqa: E501

        :param assigned_face_behavior: The assigned_face_behavior of this AdvancedConnectorSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEFORMABLE", "UNDEFORMABLE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and assigned_face_behavior not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `assigned_face_behavior` ({0}), must be one of {1}"  # noqa: E501
                .format(assigned_face_behavior, allowed_values)
            )

        self._assigned_face_behavior = assigned_face_behavior

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
        if not isinstance(other, AdvancedConnectorSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdvancedConnectorSettings):
            return True

        return self.to_dict() != other.to_dict()
