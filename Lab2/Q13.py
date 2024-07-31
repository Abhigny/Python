def geometric_sequence(start, ratio, terms):
    sequence = []
    for i in range(terms):
        sequence.append(start * (ratio ** i))
    return sequence
start = 2
ratio = 3
terms = 6
sequence = geometric_sequence(start, ratio, terms)
print(f"The first {terms} terms of the geometric sequence are: {sequence}")
