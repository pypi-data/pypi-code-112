import warnings

from winsdk.windows.data.xml.dom import XmlDocument
from winsdk.windows.ui.notifications import ToastActivatedEventArgs, ToastNotification, ToastNotificationManager

from .toast_document import ToastDocument
from .toast_types import ToastDuration


class BaseWindowsToaster:
    def __init__(self, applicationText):
        """
        Wrapper to simplify WinRT's ToastNotificationManager

        :param applicationText: Text to display the application as
        :type applicationText: str
        """
        self.applicationText = applicationText
        self.toastNotifier = None

    def setup_toast(self, toast):
        """
        Setup toast to send. Should only be used internally

        :return: XML built from a template of the supplied toast type
        :rtype: XmlDocument
        """
        toastContent = ToastDocument(ToastNotificationManager.get_template_content(toast.ToastType))
        if toast.HasImage and toast.imagePath is not None:
            toastContent.SetImageField(str(toast.imagePath))

        for i, fieldContent in enumerate(toast.textFields):
            toastContent.SetTextField(fieldContent, i)

        if toast.duration != ToastDuration.Default:
            toastContent.AddDuration(toast.duration.value)

        if toast.timestamp is not None:
            toastContent.SetCustomTimestamp(toast.timestamp)

        if toast.audio is not None:
            toastContent.SetAudioAttributes(toast.audio)

        toastContent.SetAttributionText(self.applicationText)
        return toastContent

    def show_toast(self, toast):
        """
        Displays the passed notification toast
        """
        notificationToSend = ToastNotification(self.setup_toast(toast).xmlDocument)
        if toast.on_activated is not None:
            # For some reason on_activated's type is generic, so cast it
            # noinspection PyProtectedMember
            notificationToSend.add_activated(
                lambda _, eventArgs: toast.on_activated(ToastActivatedEventArgs._from(eventArgs))
            )

        if toast.on_dismissed is not None:
            notificationToSend.add_dismissed(lambda _, eventArgs: toast.on_dismissed(eventArgs))

        if toast.on_failed is not None:
            notificationToSend.add_failed(lambda _, eventArgs: toast.on_failed(eventArgs))

        self.toastNotifier.show(notificationToSend)


class WindowsToaster(BaseWindowsToaster):
    def __init__(self, applicationText):
        super().__init__(applicationText)
        self.toastNotifier = ToastNotificationManager.create_toast_notifier(applicationText)

    def show_toast(self, toast):
        if len(toast.actions) > 0:
            warnings.warn(
                "Actions are not supported in WindowsToaster. If you'd like to use "
                "actions, instantiate a InteractableWindowsToaster class instead"
            )

        super().show_toast(toast)


class InteractableWindowsToaster(BaseWindowsToaster):
    def __init__(self, applicationText, notifierAUMI="{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\\cmd.exe"):
        """
        WindowsToaster, but uses an AUMI to support actions. Actions require a recognised AUMI to trigger on_activated,
        otherwise it triggers on_dismissed with no arguments

        :param applicationText: Text to display the application as
        :type applicationText: str
        :param notifierAUMI: AUMI to use. Defaults to Command Prompt. To use a custom AUMI, see one of the scripts
        """
        super().__init__(applicationText)
        self.toastNotifier = ToastNotificationManager.create_toast_notifier(notifierAUMI)

    def setup_toast(self, toast):
        toastContent = super().setup_toast(toast)

        for customAction in toast.actions:
            toastContent.AddAction(customAction[0], customAction[1])

        return toastContent
