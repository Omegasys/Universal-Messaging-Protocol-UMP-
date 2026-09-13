"""
UMP Offline Queue

Stores messages until a suitable transport becomes available.
"""


class OfflineQueue:

    def __init__(self):

        self.queue = []

    def enqueue(
        self,
        message
    ):

        self.queue.append(message)

    def dequeue(self):

        if not self.queue:
            return None

        return self.queue.pop(0)

    def peek(self):

        if not self.queue:
            return None

        return self.queue[0]

    def size(self) -> int:

        return len(self.queue)

    def clear(self):

        self.queue.clear()

    def is_empty(self) -> bool:

        return not self.queue
