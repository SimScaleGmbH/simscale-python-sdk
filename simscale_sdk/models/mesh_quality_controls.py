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


class MeshQualityControls(object):
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
        'max_non_orthogonality': 'DimensionalAngle',
        'max_boundary_skewness': 'DimensionalAngle',
        'max_internal_skewness': 'DimensionalAngle',
        'max_concaveness': 'DimensionalAngle',
        'min_volume': 'DimensionalVolume',
        'min_tet_quality': 'float',
        'min_face_area': 'DimensionalArea',
        'min_face_twist': 'float',
        'min_determinant': 'float',
        'min_face_weight': 'float',
        'min_volume_ratio': 'float',
        'min_triangle_twist': 'float',
        'error_distribution_iterations': 'int',
        'error_reduction': 'float',
        'relaxed_max_non_orthogonality': 'DimensionalAngle',
        'merge_tolerance': 'float'
    }

    attribute_map = {
        'max_non_orthogonality': 'maxNonOrthogonality',
        'max_boundary_skewness': 'maxBoundarySkewness',
        'max_internal_skewness': 'maxInternalSkewness',
        'max_concaveness': 'maxConcaveness',
        'min_volume': 'minVolume',
        'min_tet_quality': 'minTetQuality',
        'min_face_area': 'minFaceArea',
        'min_face_twist': 'minFaceTwist',
        'min_determinant': 'minDeterminant',
        'min_face_weight': 'minFaceWeight',
        'min_volume_ratio': 'minVolumeRatio',
        'min_triangle_twist': 'minTriangleTwist',
        'error_distribution_iterations': 'errorDistributionIterations',
        'error_reduction': 'errorReduction',
        'relaxed_max_non_orthogonality': 'relaxedMaxNonOrthogonality',
        'merge_tolerance': 'mergeTolerance'
    }

    def __init__(self, max_non_orthogonality=None, max_boundary_skewness=None, max_internal_skewness=None, max_concaveness=None, min_volume=None, min_tet_quality=None, min_face_area=None, min_face_twist=None, min_determinant=None, min_face_weight=None, min_volume_ratio=None, min_triangle_twist=None, error_distribution_iterations=None, error_reduction=None, relaxed_max_non_orthogonality=None, merge_tolerance=None, local_vars_configuration=None):  # noqa: E501
        """MeshQualityControls - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._max_non_orthogonality = None
        self._max_boundary_skewness = None
        self._max_internal_skewness = None
        self._max_concaveness = None
        self._min_volume = None
        self._min_tet_quality = None
        self._min_face_area = None
        self._min_face_twist = None
        self._min_determinant = None
        self._min_face_weight = None
        self._min_volume_ratio = None
        self._min_triangle_twist = None
        self._error_distribution_iterations = None
        self._error_reduction = None
        self._relaxed_max_non_orthogonality = None
        self._merge_tolerance = None
        self.discriminator = None

        if max_non_orthogonality is not None:
            self.max_non_orthogonality = max_non_orthogonality
        if max_boundary_skewness is not None:
            self.max_boundary_skewness = max_boundary_skewness
        if max_internal_skewness is not None:
            self.max_internal_skewness = max_internal_skewness
        if max_concaveness is not None:
            self.max_concaveness = max_concaveness
        if min_volume is not None:
            self.min_volume = min_volume
        if min_tet_quality is not None:
            self.min_tet_quality = min_tet_quality
        if min_face_area is not None:
            self.min_face_area = min_face_area
        if min_face_twist is not None:
            self.min_face_twist = min_face_twist
        if min_determinant is not None:
            self.min_determinant = min_determinant
        if min_face_weight is not None:
            self.min_face_weight = min_face_weight
        if min_volume_ratio is not None:
            self.min_volume_ratio = min_volume_ratio
        if min_triangle_twist is not None:
            self.min_triangle_twist = min_triangle_twist
        if error_distribution_iterations is not None:
            self.error_distribution_iterations = error_distribution_iterations
        if error_reduction is not None:
            self.error_reduction = error_reduction
        if relaxed_max_non_orthogonality is not None:
            self.relaxed_max_non_orthogonality = relaxed_max_non_orthogonality
        if merge_tolerance is not None:
            self.merge_tolerance = merge_tolerance

    @property
    def max_non_orthogonality(self):
        """Gets the max_non_orthogonality of this MeshQualityControls.  # noqa: E501


        :return: The max_non_orthogonality of this MeshQualityControls.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._max_non_orthogonality

    @max_non_orthogonality.setter
    def max_non_orthogonality(self, max_non_orthogonality):
        """Sets the max_non_orthogonality of this MeshQualityControls.


        :param max_non_orthogonality: The max_non_orthogonality of this MeshQualityControls.  # noqa: E501
        :type: DimensionalAngle
        """

        self._max_non_orthogonality = max_non_orthogonality

    @property
    def max_boundary_skewness(self):
        """Gets the max_boundary_skewness of this MeshQualityControls.  # noqa: E501


        :return: The max_boundary_skewness of this MeshQualityControls.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._max_boundary_skewness

    @max_boundary_skewness.setter
    def max_boundary_skewness(self, max_boundary_skewness):
        """Sets the max_boundary_skewness of this MeshQualityControls.


        :param max_boundary_skewness: The max_boundary_skewness of this MeshQualityControls.  # noqa: E501
        :type: DimensionalAngle
        """

        self._max_boundary_skewness = max_boundary_skewness

    @property
    def max_internal_skewness(self):
        """Gets the max_internal_skewness of this MeshQualityControls.  # noqa: E501


        :return: The max_internal_skewness of this MeshQualityControls.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._max_internal_skewness

    @max_internal_skewness.setter
    def max_internal_skewness(self, max_internal_skewness):
        """Sets the max_internal_skewness of this MeshQualityControls.


        :param max_internal_skewness: The max_internal_skewness of this MeshQualityControls.  # noqa: E501
        :type: DimensionalAngle
        """

        self._max_internal_skewness = max_internal_skewness

    @property
    def max_concaveness(self):
        """Gets the max_concaveness of this MeshQualityControls.  # noqa: E501


        :return: The max_concaveness of this MeshQualityControls.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._max_concaveness

    @max_concaveness.setter
    def max_concaveness(self, max_concaveness):
        """Sets the max_concaveness of this MeshQualityControls.


        :param max_concaveness: The max_concaveness of this MeshQualityControls.  # noqa: E501
        :type: DimensionalAngle
        """

        self._max_concaveness = max_concaveness

    @property
    def min_volume(self):
        """Gets the min_volume of this MeshQualityControls.  # noqa: E501


        :return: The min_volume of this MeshQualityControls.  # noqa: E501
        :rtype: DimensionalVolume
        """
        return self._min_volume

    @min_volume.setter
    def min_volume(self, min_volume):
        """Sets the min_volume of this MeshQualityControls.


        :param min_volume: The min_volume of this MeshQualityControls.  # noqa: E501
        :type: DimensionalVolume
        """

        self._min_volume = min_volume

    @property
    def min_tet_quality(self):
        """Gets the min_tet_quality of this MeshQualityControls.  # noqa: E501

        <p>Define a minimum tetrahedron quality for cells (see documentation). Choose a low negative number to disable this check, e.g. -1e30.</p>  # noqa: E501

        :return: The min_tet_quality of this MeshQualityControls.  # noqa: E501
        :rtype: float
        """
        return self._min_tet_quality

    @min_tet_quality.setter
    def min_tet_quality(self, min_tet_quality):
        """Sets the min_tet_quality of this MeshQualityControls.

        <p>Define a minimum tetrahedron quality for cells (see documentation). Choose a low negative number to disable this check, e.g. -1e30.</p>  # noqa: E501

        :param min_tet_quality: The min_tet_quality of this MeshQualityControls.  # noqa: E501
        :type: float
        """

        self._min_tet_quality = min_tet_quality

    @property
    def min_face_area(self):
        """Gets the min_face_area of this MeshQualityControls.  # noqa: E501


        :return: The min_face_area of this MeshQualityControls.  # noqa: E501
        :rtype: DimensionalArea
        """
        return self._min_face_area

    @min_face_area.setter
    def min_face_area(self, min_face_area):
        """Sets the min_face_area of this MeshQualityControls.


        :param min_face_area: The min_face_area of this MeshQualityControls.  # noqa: E501
        :type: DimensionalArea
        """

        self._min_face_area = min_face_area

    @property
    def min_face_twist(self):
        """Gets the min_face_twist of this MeshQualityControls.  # noqa: E501

        <p>Define the minimum cosine of face twist allowed (see documentation). Set to a value smaller than -1 to disable. The value results from the dot product of the face normal and the face centre triangles normal.</p>  # noqa: E501

        :return: The min_face_twist of this MeshQualityControls.  # noqa: E501
        :rtype: float
        """
        return self._min_face_twist

    @min_face_twist.setter
    def min_face_twist(self, min_face_twist):
        """Sets the min_face_twist of this MeshQualityControls.

        <p>Define the minimum cosine of face twist allowed (see documentation). Set to a value smaller than -1 to disable. The value results from the dot product of the face normal and the face centre triangles normal.</p>  # noqa: E501

        :param min_face_twist: The min_face_twist of this MeshQualityControls.  # noqa: E501
        :type: float
        """

        self._min_face_twist = min_face_twist

    @property
    def min_determinant(self):
        """Gets the min_determinant of this MeshQualityControls.  # noqa: E501

        <p>Define the minimum normalised cell determinant. Choose a value between 0 and 1. Hex corresponds to 1.</p>  # noqa: E501

        :return: The min_determinant of this MeshQualityControls.  # noqa: E501
        :rtype: float
        """
        return self._min_determinant

    @min_determinant.setter
    def min_determinant(self, min_determinant):
        """Sets the min_determinant of this MeshQualityControls.

        <p>Define the minimum normalised cell determinant. Choose a value between 0 and 1. Hex corresponds to 1.</p>  # noqa: E501

        :param min_determinant: The min_determinant of this MeshQualityControls.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                min_determinant is not None and min_determinant > 1):  # noqa: E501
            raise ValueError("Invalid value for `min_determinant`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                min_determinant is not None and min_determinant < 0):  # noqa: E501
            raise ValueError("Invalid value for `min_determinant`, must be a value greater than or equal to `0`")  # noqa: E501

        self._min_determinant = min_determinant

    @property
    def min_face_weight(self):
        """Gets the min_face_weight of this MeshQualityControls.  # noqa: E501

        <p>The face weight specifies the distribution of a face's contribution to its two neighbouring cells. A very small face weight would mean that the neighbouring cells are disproportionately different in size. Choose a value between 0 and 0.5. 0.5 refers to a face with neighbouring cells of the same size.</p>  # noqa: E501

        :return: The min_face_weight of this MeshQualityControls.  # noqa: E501
        :rtype: float
        """
        return self._min_face_weight

    @min_face_weight.setter
    def min_face_weight(self, min_face_weight):
        """Sets the min_face_weight of this MeshQualityControls.

        <p>The face weight specifies the distribution of a face's contribution to its two neighbouring cells. A very small face weight would mean that the neighbouring cells are disproportionately different in size. Choose a value between 0 and 0.5. 0.5 refers to a face with neighbouring cells of the same size.</p>  # noqa: E501

        :param min_face_weight: The min_face_weight of this MeshQualityControls.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                min_face_weight is not None and min_face_weight > 0.5):  # noqa: E501
            raise ValueError("Invalid value for `min_face_weight`, must be a value less than or equal to `0.5`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                min_face_weight is not None and min_face_weight < 0):  # noqa: E501
            raise ValueError("Invalid value for `min_face_weight`, must be a value greater than or equal to `0`")  # noqa: E501

        self._min_face_weight = min_face_weight

    @property
    def min_volume_ratio(self):
        """Gets the min_volume_ratio of this MeshQualityControls.  # noqa: E501

        <p>This parameter specifies the minimum allowed volume ratio between two adjacent cells. Choose a value between 0 and 1. 1 means that the neighbouring cells have the same volume.</p>  # noqa: E501

        :return: The min_volume_ratio of this MeshQualityControls.  # noqa: E501
        :rtype: float
        """
        return self._min_volume_ratio

    @min_volume_ratio.setter
    def min_volume_ratio(self, min_volume_ratio):
        """Sets the min_volume_ratio of this MeshQualityControls.

        <p>This parameter specifies the minimum allowed volume ratio between two adjacent cells. Choose a value between 0 and 1. 1 means that the neighbouring cells have the same volume.</p>  # noqa: E501

        :param min_volume_ratio: The min_volume_ratio of this MeshQualityControls.  # noqa: E501
        :type: float
        """

        self._min_volume_ratio = min_volume_ratio

    @property
    def min_triangle_twist(self):
        """Gets the min_triangle_twist of this MeshQualityControls.  # noqa: E501

        <p>Same as Min Face Twist, but for adjacent triangular faces (see documentation). Choose a value below -1 to disable this feature.</p>  # noqa: E501

        :return: The min_triangle_twist of this MeshQualityControls.  # noqa: E501
        :rtype: float
        """
        return self._min_triangle_twist

    @min_triangle_twist.setter
    def min_triangle_twist(self, min_triangle_twist):
        """Sets the min_triangle_twist of this MeshQualityControls.

        <p>Same as Min Face Twist, but for adjacent triangular faces (see documentation). Choose a value below -1 to disable this feature.</p>  # noqa: E501

        :param min_triangle_twist: The min_triangle_twist of this MeshQualityControls.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                min_triangle_twist is not None and min_triangle_twist > 1):  # noqa: E501
            raise ValueError("Invalid value for `min_triangle_twist`, must be a value less than or equal to `1`")  # noqa: E501

        self._min_triangle_twist = min_triangle_twist

    @property
    def error_distribution_iterations(self):
        """Gets the error_distribution_iterations of this MeshQualityControls.  # noqa: E501

        <p>Define the number of error distribution iterations.</p>  # noqa: E501

        :return: The error_distribution_iterations of this MeshQualityControls.  # noqa: E501
        :rtype: int
        """
        return self._error_distribution_iterations

    @error_distribution_iterations.setter
    def error_distribution_iterations(self, error_distribution_iterations):
        """Sets the error_distribution_iterations of this MeshQualityControls.

        <p>Define the number of error distribution iterations.</p>  # noqa: E501

        :param error_distribution_iterations: The error_distribution_iterations of this MeshQualityControls.  # noqa: E501
        :type: int
        """

        self._error_distribution_iterations = error_distribution_iterations

    @property
    def error_reduction(self):
        """Gets the error_reduction of this MeshQualityControls.  # noqa: E501

        <p>This parameter specifies how much the displacement is scaled at error locations.</p>  # noqa: E501

        :return: The error_reduction of this MeshQualityControls.  # noqa: E501
        :rtype: float
        """
        return self._error_reduction

    @error_reduction.setter
    def error_reduction(self, error_reduction):
        """Sets the error_reduction of this MeshQualityControls.

        <p>This parameter specifies how much the displacement is scaled at error locations.</p>  # noqa: E501

        :param error_reduction: The error_reduction of this MeshQualityControls.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                error_reduction is not None and error_reduction < 0):  # noqa: E501
            raise ValueError("Invalid value for `error_reduction`, must be a value greater than or equal to `0`")  # noqa: E501

        self._error_reduction = error_reduction

    @property
    def relaxed_max_non_orthogonality(self):
        """Gets the relaxed_max_non_orthogonality of this MeshQualityControls.  # noqa: E501


        :return: The relaxed_max_non_orthogonality of this MeshQualityControls.  # noqa: E501
        :rtype: DimensionalAngle
        """
        return self._relaxed_max_non_orthogonality

    @relaxed_max_non_orthogonality.setter
    def relaxed_max_non_orthogonality(self, relaxed_max_non_orthogonality):
        """Sets the relaxed_max_non_orthogonality of this MeshQualityControls.


        :param relaxed_max_non_orthogonality: The relaxed_max_non_orthogonality of this MeshQualityControls.  # noqa: E501
        :type: DimensionalAngle
        """

        self._relaxed_max_non_orthogonality = relaxed_max_non_orthogonality

    @property
    def merge_tolerance(self):
        """Gets the merge_tolerance of this MeshQualityControls.  # noqa: E501

        <p>This parameters specifies the accuracy of face merging as a fraction of the initial bounding box.</p>  # noqa: E501

        :return: The merge_tolerance of this MeshQualityControls.  # noqa: E501
        :rtype: float
        """
        return self._merge_tolerance

    @merge_tolerance.setter
    def merge_tolerance(self, merge_tolerance):
        """Sets the merge_tolerance of this MeshQualityControls.

        <p>This parameters specifies the accuracy of face merging as a fraction of the initial bounding box.</p>  # noqa: E501

        :param merge_tolerance: The merge_tolerance of this MeshQualityControls.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                merge_tolerance is not None and merge_tolerance < 0):  # noqa: E501
            raise ValueError("Invalid value for `merge_tolerance`, must be a value greater than or equal to `0`")  # noqa: E501

        self._merge_tolerance = merge_tolerance

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
        if not isinstance(other, MeshQualityControls):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MeshQualityControls):
            return True

        return self.to_dict() != other.to_dict()
