# Writing classes that produce callable instances can be pretty useful in a few 
# situations. For example, you can take advantage of callable instances when you need to:

# Retain state between calls
# Cache values that result from previous computations
# Implement straightforward and convenient APIs

# Writing Stateful Callables
def cumulative_average():
    data = []
    def average(new_value):
        data.append(new_value)
        return sum(data) / len(data)
    return average

stream_average = cumulative_average()

print(stream_average(12))
print(stream_average(13))
print(stream_average(11))
print(stream_average(10))

class CumulativeAverager:
    def __init__(self):
        self.data = []
    def __call__(self, new_value):
        self.data.append(new_value)
        return sum(self.data) / len(self.data)

stream_average = CumulativeAverager()
print(stream_average(12))
print(stream_average(13))
print(stream_average(11))
print(stream_average(10))
print(stream_average.data)
