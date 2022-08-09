class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # self.queue.append(item)
        self.queue.insert(0,item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        # return self.queue.pop(0)
        return self.queue.pop()

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

