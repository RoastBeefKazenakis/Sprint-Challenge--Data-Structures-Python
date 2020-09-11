class RingBuffer:
    def __init__(self, capacity):
        self.contents = []
        self.capacity = capacity
        self.oldest_ext_ind = 0

    def append(self, item):
        if len(self.contents) < self.capacity:
            self.contents.append(item)

        elif len(self.contents) == self.capacity:
            self.contents[self.oldest_ext_ind] = item
            self.oldest_ext_ind = (self.oldest_ext_ind + 1) % self.capacity

    def get(self):
        return self.contents