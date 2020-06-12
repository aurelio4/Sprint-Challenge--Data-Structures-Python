class RingBuffer:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity
        self.index = 0
    
    def incrementIndex(self):
        self.index = (self.index + 1) % self.capacity

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            self.data[self.index] = item

        self.incrementIndex()

    def get(self):
        return self.data