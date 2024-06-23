

from data_operations import AbstractDataOperations
from domain_event import raise_domain_event, event_dispatcher
from message_producer import AbstractMessageProducer


class EventDrivenRepository:

    def __init__(self, db_ops: AbstractDataOperations = None, message_producer: AbstractMessageProducer = None):
        super().__init__()
        self.db_operations = db_ops
        self.message_producer = message_producer
        event_dispatcher.register("record_upserted", self.message_producer.emit)

    @raise_domain_event("record_upserted")
    def upsert(self, *args, **kwargs):
        return self.db_operations.upsert(*args, **kwargs)

