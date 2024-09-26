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


class BilinearElastoPlasticModel(object):
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
        'youngs_modulus': 'DimensionalFunctionPressure',
        'poissons_ratio': 'OneOfBilinearElastoPlasticModelPoissonsRatio',
        'hardening_model': 'OneOfBilinearElastoPlasticModelHardeningModel'
    }

    attribute_map = {
        'type': 'type',
        'youngs_modulus': 'youngsModulus',
        'poissons_ratio': 'poissonsRatio',
        'hardening_model': 'hardeningModel'
    }

    def __init__(self, type='BILINEAR', youngs_modulus=None, poissons_ratio=None, hardening_model=None, local_vars_configuration=None):  # noqa: E501
        """BilinearElastoPlasticModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._youngs_modulus = None
        self._poissons_ratio = None
        self._hardening_model = None
        self.discriminator = None

        self.type = type
        if youngs_modulus is not None:
            self.youngs_modulus = youngs_modulus
        if poissons_ratio is not None:
            self.poissons_ratio = poissons_ratio
        if hardening_model is not None:
            self.hardening_model = hardening_model

    @property
    def type(self):
        """Gets the type of this BilinearElastoPlasticModel.  # noqa: E501

        Schema name: BilinearElastoPlasticModel  # noqa: E501

        :return: The type of this BilinearElastoPlasticModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BilinearElastoPlasticModel.

        Schema name: BilinearElastoPlasticModel  # noqa: E501

        :param type: The type of this BilinearElastoPlasticModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def youngs_modulus(self):
        """Gets the youngs_modulus of this BilinearElastoPlasticModel.  # noqa: E501


        :return: The youngs_modulus of this BilinearElastoPlasticModel.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._youngs_modulus

    @youngs_modulus.setter
    def youngs_modulus(self, youngs_modulus):
        """Sets the youngs_modulus of this BilinearElastoPlasticModel.


        :param youngs_modulus: The youngs_modulus of this BilinearElastoPlasticModel.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._youngs_modulus = youngs_modulus

    @property
    def poissons_ratio(self):
        """Gets the poissons_ratio of this BilinearElastoPlasticModel.  # noqa: E501


        :return: The poissons_ratio of this BilinearElastoPlasticModel.  # noqa: E501
        :rtype: OneOfBilinearElastoPlasticModelPoissonsRatio
        """
        return self._poissons_ratio

    @poissons_ratio.setter
    def poissons_ratio(self, poissons_ratio):
        """Sets the poissons_ratio of this BilinearElastoPlasticModel.


        :param poissons_ratio: The poissons_ratio of this BilinearElastoPlasticModel.  # noqa: E501
        :type: OneOfBilinearElastoPlasticModelPoissonsRatio
        """

        self._poissons_ratio = poissons_ratio

    @property
    def hardening_model(self):
        """Gets the hardening_model of this BilinearElastoPlasticModel.  # noqa: E501


        :return: The hardening_model of this BilinearElastoPlasticModel.  # noqa: E501
        :rtype: OneOfBilinearElastoPlasticModelHardeningModel
        """
        return self._hardening_model

    @hardening_model.setter
    def hardening_model(self, hardening_model):
        """Sets the hardening_model of this BilinearElastoPlasticModel.


        :param hardening_model: The hardening_model of this BilinearElastoPlasticModel.  # noqa: E501
        :type: OneOfBilinearElastoPlasticModelHardeningModel
        """

        self._hardening_model = hardening_model

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
        if not isinstance(other, BilinearElastoPlasticModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BilinearElastoPlasticModel):
            return True

        return self.to_dict() != other.to_dict()