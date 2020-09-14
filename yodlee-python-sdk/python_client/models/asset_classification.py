# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs, using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. You can generate a client SDK for Python, Java, javascript, PHP or other languages according to your development needs. For more details about our APIs themselves, please refer to https://developer.yodlee.com/Yodlee_API/.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AssetClassification(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'allocation': 'float',
        'classification_type': 'str',
        'classification_value': 'str'
    }

    attribute_map = {
        'allocation': 'allocation',
        'classification_type': 'classificationType',
        'classification_value': 'classificationValue'
    }

    def __init__(self, allocation=None, classification_type=None, classification_value=None):  # noqa: E501
        """AssetClassification - a model defined in Swagger"""  # noqa: E501

        self._allocation = None
        self._classification_type = None
        self._classification_value = None
        self.discriminator = None

        if allocation is not None:
            self.allocation = allocation
        if classification_type is not None:
            self.classification_type = classification_type
        if classification_value is not None:
            self.classification_value = classification_value

    @property
    def allocation(self):
        """Gets the allocation of this AssetClassification.  # noqa: E501

        The allocation percentage of the holding.<br><br><b>Required Feature Enablement</b>: Asset classification feature<br><br><b>Applicable containers</b>: investment<br>  # noqa: E501

        :return: The allocation of this AssetClassification.  # noqa: E501
        :rtype: float
        """
        return self._allocation

    @allocation.setter
    def allocation(self, allocation):
        """Sets the allocation of this AssetClassification.

        The allocation percentage of the holding.<br><br><b>Required Feature Enablement</b>: Asset classification feature<br><br><b>Applicable containers</b>: investment<br>  # noqa: E501

        :param allocation: The allocation of this AssetClassification.  # noqa: E501
        :type: float
        """

        self._allocation = allocation

    @property
    def classification_type(self):
        """Gets the classification_type of this AssetClassification.  # noqa: E501

        The type of classification to which the investment belongs (assetClass, country, sector, and style).<br><b>Required Feature Enablement</b>: Asset classification feature<br><br><b>Applicable containers</b>: investment<br>  # noqa: E501

        :return: The classification_type of this AssetClassification.  # noqa: E501
        :rtype: str
        """
        return self._classification_type

    @classification_type.setter
    def classification_type(self, classification_type):
        """Sets the classification_type of this AssetClassification.

        The type of classification to which the investment belongs (assetClass, country, sector, and style).<br><b>Required Feature Enablement</b>: Asset classification feature<br><br><b>Applicable containers</b>: investment<br>  # noqa: E501

        :param classification_type: The classification_type of this AssetClassification.  # noqa: E501
        :type: str
        """

        self._classification_type = classification_type

    @property
    def classification_value(self):
        """Gets the classification_value of this AssetClassification.  # noqa: E501

        The value for each classificationType.<br><b>Required Feature Enablement</b>: Asset classification feature<br><br><b>Applicable containers</b>: investment<br>  # noqa: E501

        :return: The classification_value of this AssetClassification.  # noqa: E501
        :rtype: str
        """
        return self._classification_value

    @classification_value.setter
    def classification_value(self, classification_value):
        """Sets the classification_value of this AssetClassification.

        The value for each classificationType.<br><b>Required Feature Enablement</b>: Asset classification feature<br><br><b>Applicable containers</b>: investment<br>  # noqa: E501

        :param classification_value: The classification_value of this AssetClassification.  # noqa: E501
        :type: str
        """

        self._classification_value = classification_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(AssetClassification, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AssetClassification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
