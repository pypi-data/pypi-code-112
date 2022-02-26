# coding: utf-8

"""
    printnanny-api-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from printnanny_api_client.configuration import Configuration


class TelemetryEventPolymorphicRequest(object):
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
        'ts': 'float',
        'event_type': 'OctoPrintNannyEvent',
        'octoprint_environment': 'OctoprintEnvironmentRequest',
        'octoprint_printer_data': 'OctoprintPrinterDataRequest',
        'event_data': 'dict(str, object)',
        'temperature': 'dict(str, object)',
        'print_nanny_plugin_version': 'str',
        'print_nanny_client_version': 'str',
        'print_nanny_beta_client_version': 'str',
        'octoprint_version': 'str',
        'octoprint_device': 'int',
        'print_session': 'int',
        'printer_state': 'OctoPrinterEvent'
    }

    attribute_map = {
        'ts': 'ts',
        'event_type': 'event_type',
        'octoprint_environment': 'octoprint_environment',
        'octoprint_printer_data': 'octoprint_printer_data',
        'event_data': 'event_data',
        'temperature': 'temperature',
        'print_nanny_plugin_version': 'print_nanny_plugin_version',
        'print_nanny_client_version': 'print_nanny_client_version',
        'print_nanny_beta_client_version': 'print_nanny_beta_client_version',
        'octoprint_version': 'octoprint_version',
        'octoprint_device': 'octoprint_device',
        'print_session': 'print_session',
        'printer_state': 'printer_state'
    }

    discriminator_value_class_map = {
    }

    def __init__(self, ts=None, event_type=None, octoprint_environment=None, octoprint_printer_data=None, event_data=None, temperature=None, print_nanny_plugin_version=None, print_nanny_client_version=None, print_nanny_beta_client_version=None, octoprint_version=None, octoprint_device=None, print_session=None, printer_state=None, local_vars_configuration=None):  # noqa: E501
        """TelemetryEventPolymorphicRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._ts = None
        self._event_type = None
        self._octoprint_environment = None
        self._octoprint_printer_data = None
        self._event_data = None
        self._temperature = None
        self._print_nanny_plugin_version = None
        self._print_nanny_client_version = None
        self._print_nanny_beta_client_version = None
        self._octoprint_version = None
        self._octoprint_device = None
        self._print_session = None
        self._printer_state = None
        self.discriminator = 'resourcetype'

        if ts is not None:
            self.ts = ts
        self.event_type = event_type
        self.octoprint_environment = octoprint_environment
        self.octoprint_printer_data = octoprint_printer_data
        self.event_data = event_data
        if temperature is not None:
            self.temperature = temperature
        self.print_nanny_plugin_version = print_nanny_plugin_version
        self.print_nanny_client_version = print_nanny_client_version
        self.print_nanny_beta_client_version = print_nanny_beta_client_version
        self.octoprint_version = octoprint_version
        self.octoprint_device = octoprint_device
        self.print_session = print_session
        if printer_state is not None:
            self.printer_state = printer_state

    @property
    def ts(self):
        """Gets the ts of this TelemetryEventPolymorphicRequest.  # noqa: E501


        :return: The ts of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :rtype: float
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this TelemetryEventPolymorphicRequest.


        :param ts: The ts of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :type ts: float
        """

        self._ts = ts

    @property
    def event_type(self):
        """Gets the event_type of this TelemetryEventPolymorphicRequest.  # noqa: E501


        :return: The event_type of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :rtype: OctoPrintNannyEvent
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this TelemetryEventPolymorphicRequest.


        :param event_type: The event_type of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :type event_type: OctoPrintNannyEvent
        """

        self._event_type = event_type

    @property
    def octoprint_environment(self):
        """Gets the octoprint_environment of this TelemetryEventPolymorphicRequest.  # noqa: E501


        :return: The octoprint_environment of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :rtype: OctoprintEnvironmentRequest
        """
        return self._octoprint_environment

    @octoprint_environment.setter
    def octoprint_environment(self, octoprint_environment):
        """Sets the octoprint_environment of this TelemetryEventPolymorphicRequest.


        :param octoprint_environment: The octoprint_environment of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :type octoprint_environment: OctoprintEnvironmentRequest
        """
        if self.local_vars_configuration.client_side_validation and octoprint_environment is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_environment`, must not be `None`")  # noqa: E501

        self._octoprint_environment = octoprint_environment

    @property
    def octoprint_printer_data(self):
        """Gets the octoprint_printer_data of this TelemetryEventPolymorphicRequest.  # noqa: E501


        :return: The octoprint_printer_data of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :rtype: OctoprintPrinterDataRequest
        """
        return self._octoprint_printer_data

    @octoprint_printer_data.setter
    def octoprint_printer_data(self, octoprint_printer_data):
        """Sets the octoprint_printer_data of this TelemetryEventPolymorphicRequest.


        :param octoprint_printer_data: The octoprint_printer_data of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :type octoprint_printer_data: OctoprintPrinterDataRequest
        """
        if self.local_vars_configuration.client_side_validation and octoprint_printer_data is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_printer_data`, must not be `None`")  # noqa: E501

        self._octoprint_printer_data = octoprint_printer_data

    @property
    def event_data(self):
        """Gets the event_data of this TelemetryEventPolymorphicRequest.  # noqa: E501


        :return: The event_data of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._event_data

    @event_data.setter
    def event_data(self, event_data):
        """Sets the event_data of this TelemetryEventPolymorphicRequest.


        :param event_data: The event_data of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :type event_data: dict(str, object)
        """

        self._event_data = event_data

    @property
    def temperature(self):
        """Gets the temperature of this TelemetryEventPolymorphicRequest.  # noqa: E501


        :return: The temperature of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this TelemetryEventPolymorphicRequest.


        :param temperature: The temperature of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :type temperature: dict(str, object)
        """

        self._temperature = temperature

    @property
    def print_nanny_plugin_version(self):
        """Gets the print_nanny_plugin_version of this TelemetryEventPolymorphicRequest.  # noqa: E501


        :return: The print_nanny_plugin_version of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :rtype: str
        """
        return self._print_nanny_plugin_version

    @print_nanny_plugin_version.setter
    def print_nanny_plugin_version(self, print_nanny_plugin_version):
        """Sets the print_nanny_plugin_version of this TelemetryEventPolymorphicRequest.


        :param print_nanny_plugin_version: The print_nanny_plugin_version of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :type print_nanny_plugin_version: str
        """
        if self.local_vars_configuration.client_side_validation and print_nanny_plugin_version is None:  # noqa: E501
            raise ValueError("Invalid value for `print_nanny_plugin_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                print_nanny_plugin_version is not None and len(print_nanny_plugin_version) > 60):
            raise ValueError("Invalid value for `print_nanny_plugin_version`, length must be less than or equal to `60`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                print_nanny_plugin_version is not None and len(print_nanny_plugin_version) < 1):
            raise ValueError("Invalid value for `print_nanny_plugin_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._print_nanny_plugin_version = print_nanny_plugin_version

    @property
    def print_nanny_client_version(self):
        """Gets the print_nanny_client_version of this TelemetryEventPolymorphicRequest.  # noqa: E501


        :return: The print_nanny_client_version of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :rtype: str
        """
        return self._print_nanny_client_version

    @print_nanny_client_version.setter
    def print_nanny_client_version(self, print_nanny_client_version):
        """Sets the print_nanny_client_version of this TelemetryEventPolymorphicRequest.


        :param print_nanny_client_version: The print_nanny_client_version of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :type print_nanny_client_version: str
        """
        if self.local_vars_configuration.client_side_validation and print_nanny_client_version is None:  # noqa: E501
            raise ValueError("Invalid value for `print_nanny_client_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                print_nanny_client_version is not None and len(print_nanny_client_version) > 60):
            raise ValueError("Invalid value for `print_nanny_client_version`, length must be less than or equal to `60`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                print_nanny_client_version is not None and len(print_nanny_client_version) < 1):
            raise ValueError("Invalid value for `print_nanny_client_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._print_nanny_client_version = print_nanny_client_version

    @property
    def print_nanny_beta_client_version(self):
        """Gets the print_nanny_beta_client_version of this TelemetryEventPolymorphicRequest.  # noqa: E501


        :return: The print_nanny_beta_client_version of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :rtype: str
        """
        return self._print_nanny_beta_client_version

    @print_nanny_beta_client_version.setter
    def print_nanny_beta_client_version(self, print_nanny_beta_client_version):
        """Sets the print_nanny_beta_client_version of this TelemetryEventPolymorphicRequest.


        :param print_nanny_beta_client_version: The print_nanny_beta_client_version of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :type print_nanny_beta_client_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                print_nanny_beta_client_version is not None and len(print_nanny_beta_client_version) > 60):
            raise ValueError("Invalid value for `print_nanny_beta_client_version`, length must be less than or equal to `60`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                print_nanny_beta_client_version is not None and len(print_nanny_beta_client_version) < 1):
            raise ValueError("Invalid value for `print_nanny_beta_client_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._print_nanny_beta_client_version = print_nanny_beta_client_version

    @property
    def octoprint_version(self):
        """Gets the octoprint_version of this TelemetryEventPolymorphicRequest.  # noqa: E501


        :return: The octoprint_version of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :rtype: str
        """
        return self._octoprint_version

    @octoprint_version.setter
    def octoprint_version(self, octoprint_version):
        """Sets the octoprint_version of this TelemetryEventPolymorphicRequest.


        :param octoprint_version: The octoprint_version of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :type octoprint_version: str
        """
        if self.local_vars_configuration.client_side_validation and octoprint_version is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                octoprint_version is not None and len(octoprint_version) > 36):
            raise ValueError("Invalid value for `octoprint_version`, length must be less than or equal to `36`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                octoprint_version is not None and len(octoprint_version) < 1):
            raise ValueError("Invalid value for `octoprint_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._octoprint_version = octoprint_version

    @property
    def octoprint_device(self):
        """Gets the octoprint_device of this TelemetryEventPolymorphicRequest.  # noqa: E501


        :return: The octoprint_device of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :rtype: int
        """
        return self._octoprint_device

    @octoprint_device.setter
    def octoprint_device(self, octoprint_device):
        """Sets the octoprint_device of this TelemetryEventPolymorphicRequest.


        :param octoprint_device: The octoprint_device of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :type octoprint_device: int
        """
        if self.local_vars_configuration.client_side_validation and octoprint_device is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_device`, must not be `None`")  # noqa: E501

        self._octoprint_device = octoprint_device

    @property
    def print_session(self):
        """Gets the print_session of this TelemetryEventPolymorphicRequest.  # noqa: E501


        :return: The print_session of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :rtype: int
        """
        return self._print_session

    @print_session.setter
    def print_session(self, print_session):
        """Sets the print_session of this TelemetryEventPolymorphicRequest.


        :param print_session: The print_session of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :type print_session: int
        """

        self._print_session = print_session

    @property
    def printer_state(self):
        """Gets the printer_state of this TelemetryEventPolymorphicRequest.  # noqa: E501


        :return: The printer_state of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :rtype: OctoPrinterEvent
        """
        return self._printer_state

    @printer_state.setter
    def printer_state(self, printer_state):
        """Sets the printer_state of this TelemetryEventPolymorphicRequest.


        :param printer_state: The printer_state of this TelemetryEventPolymorphicRequest.  # noqa: E501
        :type printer_state: OctoPrinterEvent
        """

        self._printer_state = printer_state

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TelemetryEventPolymorphicRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TelemetryEventPolymorphicRequest):
            return True

        return self.to_dict() != other.to_dict()
