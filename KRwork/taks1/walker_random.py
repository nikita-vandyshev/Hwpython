import random


class WalkerRandom:
    def __init__(self, events):
        if not events:
            raise ValueError("Events list is empty")

        self.events = []
        probs = []

        total = 0.0
        for event, p in events:
            if p <= 0:
                raise ValueError("Probability must be positive")
            self.events.append(event)
            probs.append(float(p))
            total += float(p)

        if abs(total - 1.0) > 0.000001:
            raise ValueError("Sum of probabilities must be 1")

        n = len(self.events)
        scaled = [p * n for p in probs]

        self.prob = [0.0] * n
        self.alias = [0] * n

        small = []
        large = []

        for i in range(n):
            if scaled[i] < 1.0:
                small.append(i)
            else:
                large.append(i)

        while small and large:
            s = small.pop()
            l = large.pop()

            self.prob[s] = scaled[s]
            self.alias[s] = l

            scaled[l] = scaled[l] - (1.0 - scaled[s])

            if scaled[l] < 1.0:
                small.append(l)
            else:
                large.append(l)

        for i in small + large:
            self.prob[i] = 1.0
            self.alias[i] = i

    def get_random(self):
        i = random.randint(0, len(self.events) - 1)
        r = random.random()

        if r < self.prob[i]:
            return self.events[i]
        return self.events[self.alias[i]]


if __name__ == "__main__":
    events = [
        ("A", 0.5),
        ("B", 0.3),
        ("C", 0.2),
    ]

    chooser = WalkerRandom(events)
    print(chooser.get_random())
