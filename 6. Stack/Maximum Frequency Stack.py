class FreqStack:

    def __init__(self):
        self.hashmap = defaultdict(int)
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.hashmap[val] += 1

    def pop(self) -> int:
        max_count = max(self.hashmap.values())
        i = len(self.stack) - 1
        while self.hashmap[self.stack[i]] != max_count:
            i -= 1
        self.hashmap[self.stack[i]] -= 1
        return self.stack.pop(i)


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()