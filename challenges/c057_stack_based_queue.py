from common.stack import Stack


class Queue:
    def __init__(self):
        self._inbox = Stack()
        self._outbox = Stack()

    def enqueue(self, elem):
        self._inbox.push(elem)

    def dequeue(self):
        if self.is_empty():
            raise QueueIsEmptyException()
        self._transfer_inbox_to_outbox()
        return self._outbox.pop()

    def peek(self):
        if self.is_empty():
            raise QueueIsEmptyException()
        self._transfer_inbox_to_outbox()
        return self._outbox.peek()

    def is_empty(self):
        return self._inbox.is_empty() and self._outbox.is_empty()

    def _transfer_inbox_to_outbox(self):
        if self._outbox.is_empty():
            while not self._inbox.is_empty():
                self._outbox.push(self._inbox.pop())


class QueueIsEmptyException(Exception):
    pass


def main():
    waiting_persons = Queue()

    waiting_persons.enqueue("Marcello")
    waiting_persons.enqueue("Michael")
    waiting_persons.enqueue("Karthi")

    while not waiting_persons.is_empty():
        if waiting_persons.peek() == "Michael":
            waiting_persons.enqueue("Michael again")
            waiting_persons.enqueue("Last Man")
        next_person = waiting_persons.dequeue()
        print("Processing " + next_person)


if __name__ == "__main__":
    main()
