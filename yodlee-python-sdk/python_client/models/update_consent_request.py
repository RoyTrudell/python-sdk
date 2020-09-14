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


class UpdateConsentRequest(object):
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
        'scope_id': 'list[str]'
    }

    attribute_map = {
        'scope_id': 'scopeId'
    }

    def __init__(self, scope_id=None):  # noqa: E501
        """UpdateConsentRequest - a model defined in Swagger"""  # noqa: E501

        self._scope_id = None
        self.discriminator = None

        if scope_id is not None:
            self.scope_id = scope_id

    @property
    def scope_id(self):
        """Gets the scope_id of this UpdateConsentRequest.  # noqa: E501

        Applicable Open Banking data cluster values.<br><br><b>Endpoints</b>:<ul><li>PUT Consent</li></ul>  # noqa: E501

        :return: The scope_id of this UpdateConsentRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        """Sets the scope_id of this UpdateConsentRequest.

        Applicable Open Banking data cluster values.<br><br><b>Endpoints</b>:<ul><li>PUT Consent</li></ul>  # noqa: E501

        :param scope_id: The scope_id of this UpdateConsentRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ACCOUNT_DETAILS", "TRANSACTION_DETAILS", "STATEMENT_DETAILS", "CONTACT_DETAILS"]  # noqa: E501
        if not set(scope_id).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `scope_id` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(scope_id) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._scope_id = scope_id

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
        if issubclass(UpdateConsentRequest, dict):
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
        if not isinstance(other, UpdateConsentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
