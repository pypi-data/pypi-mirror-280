from dataclasses import dataclass
from functools import wraps


@dataclass
class DomainEvent:
    name: str
    payload: str


class EventDispatcher:
    def __init__(self):
        self.listeners = {}

    def register(self, event_name, listener):
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(listener)

    def dispatch(self, event):
        if event.name in self.listeners:
            for listener in self.listeners[event.name]:
                listener(event)


def raise_domain_event(event_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result['result']['result'] == 'created':
                document = kwargs.get('document')
                event = DomainEvent(event_name, document)
                event_dispatcher.dispatch(event)
            return result

        return wrapper

    return decorator


# Singleton event dispatcher
event_dispatcher = EventDispatcher()
