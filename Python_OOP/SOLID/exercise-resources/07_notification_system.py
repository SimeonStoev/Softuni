from abc import ABC, abstractmethod


class UnderMaintenanceException(Exception):
    pass


class NotificationSender(ABC):
    def __init__(self):
        self.is_under_maintenance = False

    @abstractmethod
    def send(self, message: str):
        pass

    def is_under_maintenance_validation(self):
        if self.is_under_maintenance:
            raise UnderMaintenanceException("This service is currently under maintenance.")


class EmailSender(NotificationSender):
    def send(self, message: str):
        self.is_under_maintenance_validation()
        print(f"Sending email with message: {message}")


class SMSSender(NotificationSender):
    def send(self, message: str):
        self.is_under_maintenance_validation()
        print(f"Sending SMS with message: {message}")


class PushSender(NotificationSender):
    def __init__(self):
        super().__init__()
        self.is_under_maintenance = True

    def send(self, message: str):
        self.is_under_maintenance_validation()
        print(f"Sending push notification with message: {message}")


class TVSender(NotificationSender):
    def send(self, message: str):
        self.is_under_maintenance_validation()
        print(f"Sending TV with message: {message}")


class NotificationService:
    def __init__(self, sender):
        self.sender = sender

    def notify(self, message: str):
        self.sender.send(message)


try:
    email_service = NotificationService(EmailSender())
    email_service.notify("Hello via email!")

    sms_service = NotificationService(SMSSender())
    sms_service.notify("Hello via SMS!")

    tv_service = NotificationService(TVSender())
    tv_service.notify("Hello via TV!")

    push_service = NotificationService(PushSender())
    push_service.notify("Hello via Push!")


except UnderMaintenanceException as ex:
    print(ex)
