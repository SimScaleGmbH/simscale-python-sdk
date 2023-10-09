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


class OneOfOgdenHyperElasticModelOrder(object):
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
        'mu1': 'DimensionalPressure',
        'alpha1': 'float',
        'mu2': 'DimensionalPressure',
        'alpha2': 'float',
        'mu3': 'DimensionalPressure',
        'alpha3': 'float'
    }

    attribute_map = {
        'type': 'type',
        'mu1': 'mu1',
        'alpha1': 'alpha1',
        'mu2': 'mu2',
        'alpha2': 'alpha2',
        'mu3': 'mu3',
        'alpha3': 'alpha3'
    }

    discriminator_value_class_map = {
        'FIRST_ORDER_OGDEN': 'FirstOrderOgden',
        'SECOND_ORDER_OGDEN': 'SecondOrderOgden',
        'THIRD_ORDER_OGDEN': 'ThirdOrderOgden'
    }

    def __init__(self, type='THIRD_ORDER_OGDEN', mu1=None, alpha1=None, mu2=None, alpha2=None, mu3=None, alpha3=None, local_vars_configuration=None):  # noqa: E501
        """OneOfOgdenHyperElasticModelOrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._mu1 = None
        self._alpha1 = None
        self._mu2 = None
        self._alpha2 = None
        self._mu3 = None
        self._alpha3 = None
        self.discriminator = 'type'

        self.type = type
        if mu1 is not None:
            self.mu1 = mu1
        if alpha1 is not None:
            self.alpha1 = alpha1
        if mu2 is not None:
            self.mu2 = mu2
        if alpha2 is not None:
            self.alpha2 = alpha2
        if mu3 is not None:
            self.mu3 = mu3
        if alpha3 is not None:
            self.alpha3 = alpha3

    @property
    def type(self):
        """Gets the type of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501

        Schema name: ThirdOrderOgden  # noqa: E501

        :return: The type of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfOgdenHyperElasticModelOrder.

        Schema name: ThirdOrderOgden  # noqa: E501

        :param type: The type of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def mu1(self):
        """Gets the mu1 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501


        :return: The mu1 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501
        :rtype: DimensionalPressure
        """
        return self._mu1

    @mu1.setter
    def mu1(self, mu1):
        """Sets the mu1 of this OneOfOgdenHyperElasticModelOrder.


        :param mu1: The mu1 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501
        :type: DimensionalPressure
        """

        self._mu1 = mu1

    @property
    def alpha1(self):
        """Gets the alpha1 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501

        <p>Provide a parameter value for the Ogden coefficient <b>&alpha;<sub>1</sub></b>. </p>  # noqa: E501

        :return: The alpha1 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501
        :rtype: float
        """
        return self._alpha1

    @alpha1.setter
    def alpha1(self, alpha1):
        """Sets the alpha1 of this OneOfOgdenHyperElasticModelOrder.

        <p>Provide a parameter value for the Ogden coefficient <b>&alpha;<sub>1</sub></b>. </p>  # noqa: E501

        :param alpha1: The alpha1 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501
        :type: float
        """

        self._alpha1 = alpha1

    @property
    def mu2(self):
        """Gets the mu2 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501


        :return: The mu2 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501
        :rtype: DimensionalPressure
        """
        return self._mu2

    @mu2.setter
    def mu2(self, mu2):
        """Sets the mu2 of this OneOfOgdenHyperElasticModelOrder.


        :param mu2: The mu2 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501
        :type: DimensionalPressure
        """

        self._mu2 = mu2

    @property
    def alpha2(self):
        """Gets the alpha2 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501

        <p>Provide a parameter value for the Ogden coefficient <b>&alpha;<sub>2</sub></b>. </p>  # noqa: E501

        :return: The alpha2 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501
        :rtype: float
        """
        return self._alpha2

    @alpha2.setter
    def alpha2(self, alpha2):
        """Sets the alpha2 of this OneOfOgdenHyperElasticModelOrder.

        <p>Provide a parameter value for the Ogden coefficient <b>&alpha;<sub>2</sub></b>. </p>  # noqa: E501

        :param alpha2: The alpha2 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501
        :type: float
        """

        self._alpha2 = alpha2

    @property
    def mu3(self):
        """Gets the mu3 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501


        :return: The mu3 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501
        :rtype: DimensionalPressure
        """
        return self._mu3

    @mu3.setter
    def mu3(self, mu3):
        """Sets the mu3 of this OneOfOgdenHyperElasticModelOrder.


        :param mu3: The mu3 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501
        :type: DimensionalPressure
        """

        self._mu3 = mu3

    @property
    def alpha3(self):
        """Gets the alpha3 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501

        <p>Provide a parameter value for the Ogden coefficient <b>&alpha;<sub>3</sub></b>. </p>  # noqa: E501

        :return: The alpha3 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501
        :rtype: float
        """
        return self._alpha3

    @alpha3.setter
    def alpha3(self, alpha3):
        """Sets the alpha3 of this OneOfOgdenHyperElasticModelOrder.

        <p>Provide a parameter value for the Ogden coefficient <b>&alpha;<sub>3</sub></b>. </p>  # noqa: E501

        :param alpha3: The alpha3 of this OneOfOgdenHyperElasticModelOrder.  # noqa: E501
        :type: float
        """

        self._alpha3 = alpha3

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
        if not isinstance(other, OneOfOgdenHyperElasticModelOrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfOgdenHyperElasticModelOrder):
            return True

        return self.to_dict() != other.to_dict()
