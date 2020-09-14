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

from python_client.models.derived_transactions_links import DerivedTransactionsLinks  # noqa: F401,E501
from python_client.models.derived_transactions_summary import DerivedTransactionsSummary  # noqa: F401,E501


class DerivedTransactionSummaryResponse(object):
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
        'links': 'DerivedTransactionsLinks',
        'transaction_summary': 'list[DerivedTransactionsSummary]'
    }

    attribute_map = {
        'links': 'links',
        'transaction_summary': 'transactionSummary'
    }

    def __init__(self, links=None, transaction_summary=None):  # noqa: E501
        """DerivedTransactionSummaryResponse - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._transaction_summary = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if transaction_summary is not None:
            self.transaction_summary = transaction_summary

    @property
    def links(self):
        """Gets the links of this DerivedTransactionSummaryResponse.  # noqa: E501


        :return: The links of this DerivedTransactionSummaryResponse.  # noqa: E501
        :rtype: DerivedTransactionsLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DerivedTransactionSummaryResponse.


        :param links: The links of this DerivedTransactionSummaryResponse.  # noqa: E501
        :type: DerivedTransactionsLinks
        """

        self._links = links

    @property
    def transaction_summary(self):
        """Gets the transaction_summary of this DerivedTransactionSummaryResponse.  # noqa: E501


        :return: The transaction_summary of this DerivedTransactionSummaryResponse.  # noqa: E501
        :rtype: list[DerivedTransactionsSummary]
        """
        return self._transaction_summary

    @transaction_summary.setter
    def transaction_summary(self, transaction_summary):
        """Sets the transaction_summary of this DerivedTransactionSummaryResponse.


        :param transaction_summary: The transaction_summary of this DerivedTransactionSummaryResponse.  # noqa: E501
        :type: list[DerivedTransactionsSummary]
        """

        self._transaction_summary = transaction_summary

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
        if issubclass(DerivedTransactionSummaryResponse, dict):
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
        if not isinstance(other, DerivedTransactionSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
