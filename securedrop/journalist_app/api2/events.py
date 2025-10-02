from db import db
from journalist_app.api import get_or_404
from journalist_app.api2.types import (
    Event,
    EventResult,
    EventStatusCode,
    EventType,
    ItemTarget,
    SourceTarget,
)
from journalist_app.utils import save_reply
from models import Source


class EventHandler:
    @classmethod
    def process(cls, event_dict: dict) -> EventResult:
        try:
            event = Event(**event_dict)
            event.event_type = EventType(event.type)
            if "source_uuid" in event.target:
                event.target = SourceTarget(**event.target)
            elif "item_uuid" in event.target:
                event.target = ItemTarget(**event.target)
            else:
                raise TypeError("invalid event target")

        except (TypeError, ValueError):
            return EventResult(
                event_id=event.id,
                status=EventStatusCode.BadRequest,
            )

        try:
            handler = getattr(cls, f"handle_{event.type}")
        except AttributeError:
            return EventResult(
                event_id=event.id,
                status=EventStatusCode.NotImplemented,
            )

        return handler(event)

    @staticmethod
    def handle_reply_sent(event: Event) -> EventResult:
        source = get_or_404(Source, event.target.source_uuid, column=Source.uuid)
        reply = save_reply(source, event.data)
        db.session.refresh(source)

        return EventResult(
            event_id=event.id,
            status=EventStatusCode.OK,
            sources={source.uuid: source},
            items={reply.uuid: reply},
        )
