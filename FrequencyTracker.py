class FrequencyTracker:

    def __init__(self):
        self.numbers = defaultdict(int)
        self.freq = defaultdict(int)
    def add(self, number: int) -> None:
        prev = self.numbers[number]
        if self.numbers[number] > 0:
            self.freq[prev] -= 1
        self.numbers[number] += 1
        self.freq[prev + 1] += 1

    def deleteOne(self, number: int) -> None:
        if self.numbers[number] > 0:
            prev = self.numbers[number]
            self.freq[prev] -= 1
            self.numbers[number] -= 1
            if self.numbers[number] > 0:
                self.freq[prev - 1] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0
