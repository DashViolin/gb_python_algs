class MinStack:
    def __init__(self):
        self.items = []
        self.mins = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)

    def pop(self) -> None:
        if self.items:
            item = self.items.pop()
            if item in self.mins:
                self.mins.remove(item)
        if not self.mins and self.items:
            self.mins.append(min(self.items))

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.mins[-1]
