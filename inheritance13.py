# Notification System (Multiple Inheritance)
class EmailNotifier:
    def notify(self):
        print("Sending email...")

class SMSNotifier:
    def notify(self):
        print("Sending SMS...")

class AppNotifier(EmailNotifier, SMSNotifier):
    def notify_all(self):
        EmailNotifier.notify(self)
        SMSNotifier.notify(self)

n = AppNotifier()
n.notify_all()
