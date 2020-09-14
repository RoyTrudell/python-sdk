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

from python_client.models.transaction import Transaction  # noqa: F401,E501


class TransactionResponse(object):
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
        'transaction': 'list[Transaction]'
    }

    attribute_map = {
        'transaction': 'transaction'
    }

    def __init__(self, transaction=None):  # noqa: E501
        """TransactionResponse - a model defined in Swagger"""  # noqa: E501

        self._transaction = None
        self.discriminator = None

        if transaction is not None:
            self.transaction = transaction

    @property
    def transaction(self):
        """Gets the transaction of this TransactionResponse.  # noqa: E501


        :return: The transaction of this TransactionResponse.  # noqa: E501
        :rtype: list[Transaction]
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this TransactionResponse.


        :param transaction: The transaction of this TransactionResponse.  # noqa: E501
        :type: list[Transaction]
        """

        self._transaction = transaction

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
        if issubclass(TransactionResponse, dict):
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
        if not isinstance(other, TransactionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
