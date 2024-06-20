
class MaxSizeReached(Exception):
    def __init__(self, message="Queue max size was exceeded"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

class QueueEmpty(Exception):
    def __init__(self, message="No element retrieved, queue is empty"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message