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

from python_client.models.providers_dataset import ProvidersDataset  # noqa: F401,E501


class CreateConsentRequest(object):
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
        'provider_id': 'int',
        'dataset': 'list[ProvidersDataset]',
        'application_name': 'str'
    }

    attribute_map = {
        'provider_id': 'providerId',
        'dataset': 'dataset',
        'application_name': 'applicationName'
    }

    def __init__(self, provider_id=None, dataset=None, application_name=None):  # noqa: E501
        """CreateConsentRequest - a model defined in Swagger"""  # noqa: E501

        self._provider_id = None
        self._dataset = None
        self._application_name = None
        self.discriminator = None

        if provider_id is not None:
            self.provider_id = provider_id
        if dataset is not None:
            self.dataset = dataset
        if application_name is not None:
            self.application_name = application_name

    @property
    def provider_id(self):
        """Gets the provider_id of this CreateConsentRequest.  # noqa: E501

        Unique identifier for the provider site.(e.g., financial institution sites, biller sites, lender sites, etc.).<br><br><b>Endpoints</b>:<ul><li>POST Consent</li></ul>  # noqa: E501

        :return: The provider_id of this CreateConsentRequest.  # noqa: E501
        :rtype: int
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this CreateConsentRequest.

        Unique identifier for the provider site.(e.g., financial institution sites, biller sites, lender sites, etc.).<br><br><b>Endpoints</b>:<ul><li>POST Consent</li></ul>  # noqa: E501

        :param provider_id: The provider_id of this CreateConsentRequest.  # noqa: E501
        :type: int
        """

        self._provider_id = provider_id

    @property
    def dataset(self):
        """Gets the dataset of this CreateConsentRequest.  # noqa: E501

        The name of the dataset attribute supported by the provider.If no dataset value is provided, the datasets that are configured for the customer will be considered.The configured dataset can be overridden by providing the dataset as an input.<br><br><b>Endpoints</b>:<ul><li>POST Consent</li></ul>  # noqa: E501

        :return: The dataset of this CreateConsentRequest.  # noqa: E501
        :rtype: list[ProvidersDataset]
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this CreateConsentRequest.

        The name of the dataset attribute supported by the provider.If no dataset value is provided, the datasets that are configured for the customer will be considered.The configured dataset can be overridden by providing the dataset as an input.<br><br><b>Endpoints</b>:<ul><li>POST Consent</li></ul>  # noqa: E501

        :param dataset: The dataset of this CreateConsentRequest.  # noqa: E501
        :type: list[ProvidersDataset]
        """

        self._dataset = dataset

    @property
    def application_name(self):
        """Gets the application_name of this CreateConsentRequest.  # noqa: E501

        The name of the application.If no applicationName is provided in the input, the default applicationName will be considered<br><br><b>Endpoints</b>:<ul><li>POST Consent</li></ul>  # noqa: E501

        :return: The application_name of this CreateConsentRequest.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this CreateConsentRequest.

        The name of the application.If no applicationName is provided in the input, the default applicationName will be considered<br><br><b>Endpoints</b>:<ul><li>POST Consent</li></ul>  # noqa: E501

        :param application_name: The application_name of this CreateConsentRequest.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

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
        if issubclass(CreateConsentRequest, dict):
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
        if not isinstance(other, CreateConsentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
