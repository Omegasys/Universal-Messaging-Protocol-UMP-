"""
UMP Packet Trace

Records the lifecycle of packets during debugging.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class TraceEvent:

    event: str
    timestamp: str
    packet: dict

    def to_dict(self) -> dict:

        return {
            "event": self.event,
            "timestamp": self.timestamp,
            "packet": self.packet
        }


class PacketTrace:

    def __init__(self):

        self.events = []

    def record(
        self,
        event: str,
        packet: dict
    ) -> TraceEvent:

        trace_event = TraceEvent(
            event=event,
            timestamp=datetime.utcnow().isoformat(),
            packet=packet
        )

        self.events.append(
            trace_event
        )

        return trace_event

    def to_list(self) -> list:

        return [
            event.to_dict()
            for event in self.events
        ]

    def clear(self):

        self.events.clear()

    def count(self) -> int:

        return len(
            self.events
        )
