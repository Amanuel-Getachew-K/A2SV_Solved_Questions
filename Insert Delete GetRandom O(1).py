class RandomizedSet:

    def __init__(self):
        self.random = []
        self.freq = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.freq:
            return False
        self.freq[val] = len(self.random)
        self.random.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.freq:
            return False
        idx = self.freq[val]
        last_element = self.random[-1] 
        self.random[idx] = last_element
        self.freq[last_element] = idx
        self.random.pop()
        del self.freq[val] 
        return True

    def getRandom(self) -> int:
        if not self.random:
            return None
        return random.choice(self.random)
