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

from python_client.models.field import Field  # noqa: F401,E501
from python_client.models.provider_account_preferences import ProviderAccountPreferences  # noqa: F401,E501
from python_client.models.providers_dataset import ProvidersDataset  # noqa: F401,E501


class ProviderAccountRequest(object):
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
        'consent_id': 'int',
        'preferences': 'ProviderAccountPreferences',
        'aggregation_source': 'str',
        'field': 'list[Field]',
        'dataset_name': 'list[str]',
        'dataset': 'list[ProvidersDataset]'
    }

    attribute_map = {
        'consent_id': 'consentId',
        'preferences': 'preferences',
        'aggregation_source': 'aggregationSource',
        'field': 'field',
        'dataset_name': 'datasetName',
        'dataset': 'dataset'
    }

    def __init__(self, consent_id=None, preferences=None, aggregation_source=None, field=None, dataset_name=None, dataset=None):  # noqa: E501
        """ProviderAccountRequest - a model defined in Swagger"""  # noqa: E501

        self._consent_id = None
        self._preferences = None
        self._aggregation_source = None
        self._field = None
        self._dataset_name = None
        self._dataset = None
        self.discriminator = None

        if consent_id is not None:
            self.consent_id = consent_id
        if preferences is not None:
            self.preferences = preferences
        if aggregation_source is not None:
            self.aggregation_source = aggregation_source
        self.field = field
        if dataset_name is not None:
            self.dataset_name = dataset_name
        if dataset is not None:
            self.dataset = dataset

    @property
    def consent_id(self):
        """Gets the consent_id of this ProviderAccountRequest.  # noqa: E501

        Consent Id generated for the request through POST Consent.<br><br><b>Endpoints</b>:<ul><li>POST Provider Account</li><li>PUT Provider Account</li></ul>  # noqa: E501

        :return: The consent_id of this ProviderAccountRequest.  # noqa: E501
        :rtype: int
        """
        return self._consent_id

    @consent_id.setter
    def consent_id(self, consent_id):
        """Sets the consent_id of this ProviderAccountRequest.

        Consent Id generated for the request through POST Consent.<br><br><b>Endpoints</b>:<ul><li>POST Provider Account</li><li>PUT Provider Account</li></ul>  # noqa: E501

        :param consent_id: The consent_id of this ProviderAccountRequest.  # noqa: E501
        :type: int
        """

        self._consent_id = consent_id

    @property
    def preferences(self):
        """Gets the preferences of this ProviderAccountRequest.  # noqa: E501


        :return: The preferences of this ProviderAccountRequest.  # noqa: E501
        :rtype: ProviderAccountPreferences
        """
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        """Sets the preferences of this ProviderAccountRequest.


        :param preferences: The preferences of this ProviderAccountRequest.  # noqa: E501
        :type: ProviderAccountPreferences
        """

        self._preferences = preferences

    @property
    def aggregation_source(self):
        """Gets the aggregation_source of this ProviderAccountRequest.  # noqa: E501


        :return: The aggregation_source of this ProviderAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_source

    @aggregation_source.setter
    def aggregation_source(self, aggregation_source):
        """Sets the aggregation_source of this ProviderAccountRequest.


        :param aggregation_source: The aggregation_source of this ProviderAccountRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["SYSTEM", "USER"]  # noqa: E501
        if aggregation_source not in allowed_values:
            raise ValueError(
                "Invalid value for `aggregation_source` ({0}), must be one of {1}"  # noqa: E501
                .format(aggregation_source, allowed_values)
            )

        self._aggregation_source = aggregation_source

    @property
    def field(self):
        """Gets the field of this ProviderAccountRequest.  # noqa: E501


        :return: The field of this ProviderAccountRequest.  # noqa: E501
        :rtype: list[Field]
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this ProviderAccountRequest.


        :param field: The field of this ProviderAccountRequest.  # noqa: E501
        :type: list[Field]
        """
        if field is None:
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field

    @property
    def dataset_name(self):
        """Gets the dataset_name of this ProviderAccountRequest.  # noqa: E501


        :return: The dataset_name of this ProviderAccountRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        """Sets the dataset_name of this ProviderAccountRequest.


        :param dataset_name: The dataset_name of this ProviderAccountRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["BASIC_AGG_DATA", "ADVANCE_AGG_DATA", "ACCT_PROFILE", "DOCUMENT"]  # noqa: E501
        if not set(dataset_name).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `dataset_name` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(dataset_name) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._dataset_name = dataset_name

    @property
    def dataset(self):
        """Gets the dataset of this ProviderAccountRequest.  # noqa: E501


        :return: The dataset of this ProviderAccountRequest.  # noqa: E501
        :rtype: list[ProvidersDataset]
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this ProviderAccountRequest.


        :param dataset: The dataset of this ProviderAccountRequest.  # noqa: E501
        :type: list[ProvidersDataset]
        """

        self._dataset = dataset

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
        if issubclass(ProviderAccountRequest, dict):
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
        if not isinstance(other, ProviderAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
