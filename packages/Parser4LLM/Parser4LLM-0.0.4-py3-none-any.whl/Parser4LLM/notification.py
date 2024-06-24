from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def notify(self, message):
        pass
    
class DefaultNotification(Notification):
    
    def notify(self, message):
        print(message)