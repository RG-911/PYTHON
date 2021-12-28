class Queue(object):
    def __init__(self):
        self.instack = []
        self.oustack = []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):
        if not self.oustack:
            while self.instack:
                self.oustack.append(self.instack.pop())
        return self.oustack.pop()

q = Queue()
for i in range(11):
    q.enqueue(i)
for i in range(11):
    print(q.dequeue())