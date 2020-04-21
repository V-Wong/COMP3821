class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __len__(self):
        return self.end - self.start

    def is_intersect(self, other) -> bool:
        if self.start < other.start:
            return self.end < other.start
        else:
            return other.end < self.start