# coding: utf-8

"""
    Zuora API Reference

    REST API reference for the Zuora Billing, Payments, and Central Platform! Check out the [REST API Overview](https://www.zuora.com/developer/api-references/api/overview/).  # noqa: E501

    OpenAPI spec version: 2023-10-24
    Contact: docs@zuora.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PutServiceProviderRequest(object):
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
        'name': 'str',
        'test': 'bool',
        'provider': 'str',
        'company_identifier': 'str',
        'api_key': 'str',
        'secret_key': 'str',
        'client_certificate': 'str',
        'client_certificate_type': 'str',
        'client_certificate_password': 'str'
    }

    attribute_map = {
        'name': 'name',
        'test': 'test',
        'provider': 'provider',
        'company_identifier': 'companyIdentifier',
        'api_key': 'apiKey',
        'secret_key': 'secretKey',
        'client_certificate': 'clientCertificate',
        'client_certificate_type': 'clientCertificateType',
        'client_certificate_password': 'clientCertificatePassword'
    }

    def __init__(self, name=None, test=None, provider=None, company_identifier=None, api_key=None, secret_key=None, client_certificate=None, client_certificate_type=None, client_certificate_password=None):  # noqa: E501
        """PutServiceProviderRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._test = None
        self._provider = None
        self._company_identifier = None
        self._api_key = None
        self._secret_key = None
        self._client_certificate = None
        self._client_certificate_type = None
        self._client_certificate_password = None
        self.discriminator = None
        self.name = name
        if test is not None:
            self.test = test
        self.provider = provider
        if company_identifier is not None:
            self.company_identifier = company_identifier
        if api_key is not None:
            self.api_key = api_key
        if secret_key is not None:
            self.secret_key = secret_key
        if client_certificate is not None:
            self.client_certificate = client_certificate
        if client_certificate_type is not None:
            self.client_certificate_type = client_certificate_type
        if client_certificate_password is not None:
            self.client_certificate_password = client_certificate_password

    @property
    def name(self):
        """Gets the name of this PutServiceProviderRequest.  # noqa: E501

        The name of the e-invoicing service provider.   # noqa: E501

        :return: The name of this PutServiceProviderRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutServiceProviderRequest.

        The name of the e-invoicing service provider.   # noqa: E501

        :param name: The name of this PutServiceProviderRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def test(self):
        """Gets the test of this PutServiceProviderRequest.  # noqa: E501

        Whether the e-invoicing service provider's configuration is intended for testing.   - If you set this field to `true`, requests are directed to the testing integration endpoints. If you set this field to `false`, requests are directed to the production integration endpoints.   # noqa: E501

        :return: The test of this PutServiceProviderRequest.  # noqa: E501
        :rtype: bool
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this PutServiceProviderRequest.

        Whether the e-invoicing service provider's configuration is intended for testing.   - If you set this field to `true`, requests are directed to the testing integration endpoints. If you set this field to `false`, requests are directed to the production integration endpoints.   # noqa: E501

        :param test: The test of this PutServiceProviderRequest.  # noqa: E501
        :type: bool
        """

        self._test = test

    @property
    def provider(self):
        """Gets the provider of this PutServiceProviderRequest.  # noqa: E501

        The name of the e-invoicing service provider that can help you generate e-invoice files for billing documents.   # noqa: E501

        :return: The provider of this PutServiceProviderRequest.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this PutServiceProviderRequest.

        The name of the e-invoicing service provider that can help you generate e-invoice files for billing documents.   # noqa: E501

        :param provider: The provider of this PutServiceProviderRequest.  # noqa: E501
        :type: str
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501
        allowed_values = ["Sovos"]  # noqa: E501
        if provider not in allowed_values:
            raise ValueError(
                "Invalid value for `provider` ({0}), must be one of {1}"  # noqa: E501
                .format(provider, allowed_values)
            )

        self._provider = provider

    @property
    def company_identifier(self):
        """Gets the company_identifier of this PutServiceProviderRequest.  # noqa: E501

        The Company Identifier is used to create a SenderSystemId, which serves to identify the system from which the transactions are sent.   # noqa: E501

        :return: The company_identifier of this PutServiceProviderRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_identifier

    @company_identifier.setter
    def company_identifier(self, company_identifier):
        """Sets the company_identifier of this PutServiceProviderRequest.

        The Company Identifier is used to create a SenderSystemId, which serves to identify the system from which the transactions are sent.   # noqa: E501

        :param company_identifier: The company_identifier of this PutServiceProviderRequest.  # noqa: E501
        :type: str
        """

        self._company_identifier = company_identifier

    @property
    def api_key(self):
        """Gets the api_key of this PutServiceProviderRequest.  # noqa: E501

        The API key is used to authenticate the e-invoicing service provider's requests.   # noqa: E501

        :return: The api_key of this PutServiceProviderRequest.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this PutServiceProviderRequest.

        The API key is used to authenticate the e-invoicing service provider's requests.   # noqa: E501

        :param api_key: The api_key of this PutServiceProviderRequest.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def secret_key(self):
        """Gets the secret_key of this PutServiceProviderRequest.  # noqa: E501

        The Secret Key is used to authenticate the e-invoicing service provider's requests.   # noqa: E501

        :return: The secret_key of this PutServiceProviderRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this PutServiceProviderRequest.

        The Secret Key is used to authenticate the e-invoicing service provider's requests.   # noqa: E501

        :param secret_key: The secret_key of this PutServiceProviderRequest.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def client_certificate(self):
        """Gets the client_certificate of this PutServiceProviderRequest.  # noqa: E501

        The client certificate is used to authenticate the e-invoicing service provider's requests, which should be in base64 encoded format.   # noqa: E501

        :return: The client_certificate of this PutServiceProviderRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_certificate

    @client_certificate.setter
    def client_certificate(self, client_certificate):
        """Sets the client_certificate of this PutServiceProviderRequest.

        The client certificate is used to authenticate the e-invoicing service provider's requests, which should be in base64 encoded format.   # noqa: E501

        :param client_certificate: The client_certificate of this PutServiceProviderRequest.  # noqa: E501
        :type: str
        """

        self._client_certificate = client_certificate

    @property
    def client_certificate_type(self):
        """Gets the client_certificate_type of this PutServiceProviderRequest.  # noqa: E501

        The client certificate type is used to specify the type of the client certificate. The default value is `PKCS12`.   # noqa: E501

        :return: The client_certificate_type of this PutServiceProviderRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_certificate_type

    @client_certificate_type.setter
    def client_certificate_type(self, client_certificate_type):
        """Sets the client_certificate_type of this PutServiceProviderRequest.

        The client certificate type is used to specify the type of the client certificate. The default value is `PKCS12`.   # noqa: E501

        :param client_certificate_type: The client_certificate_type of this PutServiceProviderRequest.  # noqa: E501
        :type: str
        """

        self._client_certificate_type = client_certificate_type

    @property
    def client_certificate_password(self):
        """Gets the client_certificate_password of this PutServiceProviderRequest.  # noqa: E501

        The client certificate password is the password to protect the client certificate.   # noqa: E501

        :return: The client_certificate_password of this PutServiceProviderRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_certificate_password

    @client_certificate_password.setter
    def client_certificate_password(self, client_certificate_password):
        """Sets the client_certificate_password of this PutServiceProviderRequest.

        The client certificate password is the password to protect the client certificate.   # noqa: E501

        :param client_certificate_password: The client_certificate_password of this PutServiceProviderRequest.  # noqa: E501
        :type: str
        """

        self._client_certificate_password = client_certificate_password

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
        if issubclass(PutServiceProviderRequest, dict):
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
        if not isinstance(other, PutServiceProviderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
