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


class UserRequestPreferences(object):
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
        'date_format': 'str',
        'time_zone': 'str',
        'currency': 'str',
        'locale': 'str'
    }

    attribute_map = {
        'date_format': 'dateFormat',
        'time_zone': 'timeZone',
        'currency': 'currency',
        'locale': 'locale'
    }

    def __init__(self, date_format=None, time_zone=None, currency=None, locale=None):  # noqa: E501
        """UserRequestPreferences - a model defined in Swagger"""  # noqa: E501

        self._date_format = None
        self._time_zone = None
        self._currency = None
        self._locale = None
        self.discriminator = None

        if date_format is not None:
            self.date_format = date_format
        if time_zone is not None:
            self.time_zone = time_zone
        if currency is not None:
            self.currency = currency
        if locale is not None:
            self.locale = locale

    @property
    def date_format(self):
        """Gets the date_format of this UserRequestPreferences.  # noqa: E501

        The dateformat of the user.This attribute is just a place holder and has no impact on any other API services.  # noqa: E501

        :return: The date_format of this UserRequestPreferences.  # noqa: E501
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this UserRequestPreferences.

        The dateformat of the user.This attribute is just a place holder and has no impact on any other API services.  # noqa: E501

        :param date_format: The date_format of this UserRequestPreferences.  # noqa: E501
        :type: str
        """
        if date_format is not None and len(date_format) > 2147483647:
            raise ValueError("Invalid value for `date_format`, length must be less than or equal to `2147483647`")  # noqa: E501
        if date_format is not None and len(date_format) < 1:
            raise ValueError("Invalid value for `date_format`, length must be greater than or equal to `1`")  # noqa: E501

        self._date_format = date_format

    @property
    def time_zone(self):
        """Gets the time_zone of this UserRequestPreferences.  # noqa: E501

        The timezone of the user. This attribute is just a place holder and has no impact on any other API services.  # noqa: E501

        :return: The time_zone of this UserRequestPreferences.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this UserRequestPreferences.

        The timezone of the user. This attribute is just a place holder and has no impact on any other API services.  # noqa: E501

        :param time_zone: The time_zone of this UserRequestPreferences.  # noqa: E501
        :type: str
        """
        if time_zone is not None and len(time_zone) > 2147483647:
            raise ValueError("Invalid value for `time_zone`, length must be less than or equal to `2147483647`")  # noqa: E501
        if time_zone is not None and len(time_zone) < 1:
            raise ValueError("Invalid value for `time_zone`, length must be greater than or equal to `1`")  # noqa: E501

        self._time_zone = time_zone

    @property
    def currency(self):
        """Gets the currency of this UserRequestPreferences.  # noqa: E501

        The currency of the user. This currency will be respected while providing the response for derived API services.<br><b>Applicable Values</b><br>  # noqa: E501

        :return: The currency of this UserRequestPreferences.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this UserRequestPreferences.

        The currency of the user. This currency will be respected while providing the response for derived API services.<br><b>Applicable Values</b><br>  # noqa: E501

        :param currency: The currency of this UserRequestPreferences.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUD", "BRL", "CAD", "EUR", "GBP", "HKD", "IDR", "INR", "JPY", "NZD", "SGD", "USD", "ZAR", "CNY", "VND"]  # noqa: E501
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"  # noqa: E501
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def locale(self):
        """Gets the locale of this UserRequestPreferences.  # noqa: E501

        The locale of the user. This locale will be considered for localization features like providing the provider information in the supported locale or providing category names in the transaction related services.<br><b>Applicable Values</b><br>  # noqa: E501

        :return: The locale of this UserRequestPreferences.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this UserRequestPreferences.

        The locale of the user. This locale will be considered for localization features like providing the provider information in the supported locale or providing category names in the transaction related services.<br><b>Applicable Values</b><br>  # noqa: E501

        :param locale: The locale of this UserRequestPreferences.  # noqa: E501
        :type: str
        """
        allowed_values = ["en_US", "en_ES", "fr_CA", "zh_CN"]  # noqa: E501
        if locale not in allowed_values:
            raise ValueError(
                "Invalid value for `locale` ({0}), must be one of {1}"  # noqa: E501
                .format(locale, allowed_values)
            )

        self._locale = locale

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
        if issubclass(UserRequestPreferences, dict):
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
        if not isinstance(other, UserRequestPreferences):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other