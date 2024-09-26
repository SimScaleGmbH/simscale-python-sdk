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


class OneOfLinearElasticMaterialBehaviorDirectionalDependency(object):
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
        'poissons_ratio': 'OneOfIsotropicDirectionalDependencyPoissonsRatio',
        'expansion_coefficient': 'DimensionalFunctionThermalExpansionRate',
        'reference_temperature': 'DimensionalTemperature',
        'youngs_modulus_x': 'DimensionalFunctionPressure',
        'youngs_modulus_y': 'DimensionalFunctionPressure',
        'youngs_modulus_z': 'DimensionalFunctionPressure',
        'poissons_ratio_xy': 'OneOfOrthotropicDirectionalDependencyPoissonsRatioXY',
        'poissons_ratio_yz': 'OneOfOrthotropicDirectionalDependencyPoissonsRatioYZ',
        'poissons_ratio_xz': 'OneOfOrthotropicDirectionalDependencyPoissonsRatioXZ',
        'shear_modulus_xy': 'DimensionalFunctionPressure',
        'shear_modulus_yz': 'DimensionalFunctionPressure',
        'shear_modulus_xz': 'DimensionalFunctionPressure',
        'expansion_coefficient_x': 'DimensionalFunctionThermalExpansionRate',
        'expansion_coefficient_y': 'DimensionalFunctionThermalExpansionRate',
        'expansion_coefficient_z': 'DimensionalFunctionThermalExpansionRate'
    }

    attribute_map = {
        'type': 'type',
        'youngs_modulus': 'youngsModulus',
        'poissons_ratio': 'poissonsRatio',
        'expansion_coefficient': 'expansionCoefficient',
        'reference_temperature': 'referenceTemperature',
        'youngs_modulus_x': 'youngsModulusX',
        'youngs_modulus_y': 'youngsModulusY',
        'youngs_modulus_z': 'youngsModulusZ',
        'poissons_ratio_xy': 'poissonsRatioXY',
        'poissons_ratio_yz': 'poissonsRatioYZ',
        'poissons_ratio_xz': 'poissonsRatioXZ',
        'shear_modulus_xy': 'shearModulusXY',
        'shear_modulus_yz': 'shearModulusYZ',
        'shear_modulus_xz': 'shearModulusXZ',
        'expansion_coefficient_x': 'expansionCoefficientX',
        'expansion_coefficient_y': 'expansionCoefficientY',
        'expansion_coefficient_z': 'expansionCoefficientZ'
    }

    discriminator_value_class_map = {
        'ISOTROPIC': 'IsotropicDirectionalDependency',
        'ORTHOTROPIC': 'OrthotropicDirectionalDependency'
    }

    def __init__(self, type='ORTHOTROPIC', youngs_modulus=None, poissons_ratio=None, expansion_coefficient=None, reference_temperature=None, youngs_modulus_x=None, youngs_modulus_y=None, youngs_modulus_z=None, poissons_ratio_xy=None, poissons_ratio_yz=None, poissons_ratio_xz=None, shear_modulus_xy=None, shear_modulus_yz=None, shear_modulus_xz=None, expansion_coefficient_x=None, expansion_coefficient_y=None, expansion_coefficient_z=None, local_vars_configuration=None):  # noqa: E501
        """OneOfLinearElasticMaterialBehaviorDirectionalDependency - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._youngs_modulus = None
        self._poissons_ratio = None
        self._expansion_coefficient = None
        self._reference_temperature = None
        self._youngs_modulus_x = None
        self._youngs_modulus_y = None
        self._youngs_modulus_z = None
        self._poissons_ratio_xy = None
        self._poissons_ratio_yz = None
        self._poissons_ratio_xz = None
        self._shear_modulus_xy = None
        self._shear_modulus_yz = None
        self._shear_modulus_xz = None
        self._expansion_coefficient_x = None
        self._expansion_coefficient_y = None
        self._expansion_coefficient_z = None
        self.discriminator = 'type'

        self.type = type
        if youngs_modulus is not None:
            self.youngs_modulus = youngs_modulus
        if poissons_ratio is not None:
            self.poissons_ratio = poissons_ratio
        if expansion_coefficient is not None:
            self.expansion_coefficient = expansion_coefficient
        if reference_temperature is not None:
            self.reference_temperature = reference_temperature
        if youngs_modulus_x is not None:
            self.youngs_modulus_x = youngs_modulus_x
        if youngs_modulus_y is not None:
            self.youngs_modulus_y = youngs_modulus_y
        if youngs_modulus_z is not None:
            self.youngs_modulus_z = youngs_modulus_z
        if poissons_ratio_xy is not None:
            self.poissons_ratio_xy = poissons_ratio_xy
        if poissons_ratio_yz is not None:
            self.poissons_ratio_yz = poissons_ratio_yz
        if poissons_ratio_xz is not None:
            self.poissons_ratio_xz = poissons_ratio_xz
        if shear_modulus_xy is not None:
            self.shear_modulus_xy = shear_modulus_xy
        if shear_modulus_yz is not None:
            self.shear_modulus_yz = shear_modulus_yz
        if shear_modulus_xz is not None:
            self.shear_modulus_xz = shear_modulus_xz
        if expansion_coefficient_x is not None:
            self.expansion_coefficient_x = expansion_coefficient_x
        if expansion_coefficient_y is not None:
            self.expansion_coefficient_y = expansion_coefficient_y
        if expansion_coefficient_z is not None:
            self.expansion_coefficient_z = expansion_coefficient_z

    @property
    def type(self):
        """Gets the type of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501

        Schema name: OrthotropicDirectionalDependency  # noqa: E501

        :return: The type of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.

        Schema name: OrthotropicDirectionalDependency  # noqa: E501

        :param type: The type of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def youngs_modulus(self):
        """Gets the youngs_modulus of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501


        :return: The youngs_modulus of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._youngs_modulus

    @youngs_modulus.setter
    def youngs_modulus(self, youngs_modulus):
        """Sets the youngs_modulus of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.


        :param youngs_modulus: The youngs_modulus of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._youngs_modulus = youngs_modulus

    @property
    def poissons_ratio(self):
        """Gets the poissons_ratio of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501


        :return: The poissons_ratio of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: OneOfIsotropicDirectionalDependencyPoissonsRatio
        """
        return self._poissons_ratio

    @poissons_ratio.setter
    def poissons_ratio(self, poissons_ratio):
        """Sets the poissons_ratio of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.


        :param poissons_ratio: The poissons_ratio of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: OneOfIsotropicDirectionalDependencyPoissonsRatio
        """

        self._poissons_ratio = poissons_ratio

    @property
    def expansion_coefficient(self):
        """Gets the expansion_coefficient of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501


        :return: The expansion_coefficient of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: DimensionalFunctionThermalExpansionRate
        """
        return self._expansion_coefficient

    @expansion_coefficient.setter
    def expansion_coefficient(self, expansion_coefficient):
        """Sets the expansion_coefficient of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.


        :param expansion_coefficient: The expansion_coefficient of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: DimensionalFunctionThermalExpansionRate
        """

        self._expansion_coefficient = expansion_coefficient

    @property
    def reference_temperature(self):
        """Gets the reference_temperature of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501


        :return: The reference_temperature of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: DimensionalTemperature
        """
        return self._reference_temperature

    @reference_temperature.setter
    def reference_temperature(self, reference_temperature):
        """Sets the reference_temperature of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.


        :param reference_temperature: The reference_temperature of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: DimensionalTemperature
        """

        self._reference_temperature = reference_temperature

    @property
    def youngs_modulus_x(self):
        """Gets the youngs_modulus_x of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501


        :return: The youngs_modulus_x of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._youngs_modulus_x

    @youngs_modulus_x.setter
    def youngs_modulus_x(self, youngs_modulus_x):
        """Sets the youngs_modulus_x of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.


        :param youngs_modulus_x: The youngs_modulus_x of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._youngs_modulus_x = youngs_modulus_x

    @property
    def youngs_modulus_y(self):
        """Gets the youngs_modulus_y of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501


        :return: The youngs_modulus_y of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._youngs_modulus_y

    @youngs_modulus_y.setter
    def youngs_modulus_y(self, youngs_modulus_y):
        """Sets the youngs_modulus_y of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.


        :param youngs_modulus_y: The youngs_modulus_y of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._youngs_modulus_y = youngs_modulus_y

    @property
    def youngs_modulus_z(self):
        """Gets the youngs_modulus_z of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501


        :return: The youngs_modulus_z of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._youngs_modulus_z

    @youngs_modulus_z.setter
    def youngs_modulus_z(self, youngs_modulus_z):
        """Sets the youngs_modulus_z of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.


        :param youngs_modulus_z: The youngs_modulus_z of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._youngs_modulus_z = youngs_modulus_z

    @property
    def poissons_ratio_xy(self):
        """Gets the poissons_ratio_xy of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501


        :return: The poissons_ratio_xy of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: OneOfOrthotropicDirectionalDependencyPoissonsRatioXY
        """
        return self._poissons_ratio_xy

    @poissons_ratio_xy.setter
    def poissons_ratio_xy(self, poissons_ratio_xy):
        """Sets the poissons_ratio_xy of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.


        :param poissons_ratio_xy: The poissons_ratio_xy of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: OneOfOrthotropicDirectionalDependencyPoissonsRatioXY
        """

        self._poissons_ratio_xy = poissons_ratio_xy

    @property
    def poissons_ratio_yz(self):
        """Gets the poissons_ratio_yz of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501


        :return: The poissons_ratio_yz of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: OneOfOrthotropicDirectionalDependencyPoissonsRatioYZ
        """
        return self._poissons_ratio_yz

    @poissons_ratio_yz.setter
    def poissons_ratio_yz(self, poissons_ratio_yz):
        """Sets the poissons_ratio_yz of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.


        :param poissons_ratio_yz: The poissons_ratio_yz of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: OneOfOrthotropicDirectionalDependencyPoissonsRatioYZ
        """

        self._poissons_ratio_yz = poissons_ratio_yz

    @property
    def poissons_ratio_xz(self):
        """Gets the poissons_ratio_xz of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501


        :return: The poissons_ratio_xz of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: OneOfOrthotropicDirectionalDependencyPoissonsRatioXZ
        """
        return self._poissons_ratio_xz

    @poissons_ratio_xz.setter
    def poissons_ratio_xz(self, poissons_ratio_xz):
        """Sets the poissons_ratio_xz of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.


        :param poissons_ratio_xz: The poissons_ratio_xz of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: OneOfOrthotropicDirectionalDependencyPoissonsRatioXZ
        """

        self._poissons_ratio_xz = poissons_ratio_xz

    @property
    def shear_modulus_xy(self):
        """Gets the shear_modulus_xy of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501


        :return: The shear_modulus_xy of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._shear_modulus_xy

    @shear_modulus_xy.setter
    def shear_modulus_xy(self, shear_modulus_xy):
        """Sets the shear_modulus_xy of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.


        :param shear_modulus_xy: The shear_modulus_xy of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._shear_modulus_xy = shear_modulus_xy

    @property
    def shear_modulus_yz(self):
        """Gets the shear_modulus_yz of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501


        :return: The shear_modulus_yz of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._shear_modulus_yz

    @shear_modulus_yz.setter
    def shear_modulus_yz(self, shear_modulus_yz):
        """Sets the shear_modulus_yz of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.


        :param shear_modulus_yz: The shear_modulus_yz of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._shear_modulus_yz = shear_modulus_yz

    @property
    def shear_modulus_xz(self):
        """Gets the shear_modulus_xz of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501


        :return: The shear_modulus_xz of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._shear_modulus_xz

    @shear_modulus_xz.setter
    def shear_modulus_xz(self, shear_modulus_xz):
        """Sets the shear_modulus_xz of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.


        :param shear_modulus_xz: The shear_modulus_xz of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._shear_modulus_xz = shear_modulus_xz

    @property
    def expansion_coefficient_x(self):
        """Gets the expansion_coefficient_x of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501


        :return: The expansion_coefficient_x of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: DimensionalFunctionThermalExpansionRate
        """
        return self._expansion_coefficient_x

    @expansion_coefficient_x.setter
    def expansion_coefficient_x(self, expansion_coefficient_x):
        """Sets the expansion_coefficient_x of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.


        :param expansion_coefficient_x: The expansion_coefficient_x of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: DimensionalFunctionThermalExpansionRate
        """

        self._expansion_coefficient_x = expansion_coefficient_x

    @property
    def expansion_coefficient_y(self):
        """Gets the expansion_coefficient_y of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501


        :return: The expansion_coefficient_y of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: DimensionalFunctionThermalExpansionRate
        """
        return self._expansion_coefficient_y

    @expansion_coefficient_y.setter
    def expansion_coefficient_y(self, expansion_coefficient_y):
        """Sets the expansion_coefficient_y of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.


        :param expansion_coefficient_y: The expansion_coefficient_y of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: DimensionalFunctionThermalExpansionRate
        """

        self._expansion_coefficient_y = expansion_coefficient_y

    @property
    def expansion_coefficient_z(self):
        """Gets the expansion_coefficient_z of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501


        :return: The expansion_coefficient_z of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :rtype: DimensionalFunctionThermalExpansionRate
        """
        return self._expansion_coefficient_z

    @expansion_coefficient_z.setter
    def expansion_coefficient_z(self, expansion_coefficient_z):
        """Sets the expansion_coefficient_z of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.


        :param expansion_coefficient_z: The expansion_coefficient_z of this OneOfLinearElasticMaterialBehaviorDirectionalDependency.  # noqa: E501
        :type: DimensionalFunctionThermalExpansionRate
        """

        self._expansion_coefficient_z = expansion_coefficient_z

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
        if not isinstance(other, OneOfLinearElasticMaterialBehaviorDirectionalDependency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfLinearElasticMaterialBehaviorDirectionalDependency):
            return True

        return self.to_dict() != other.to_dict()