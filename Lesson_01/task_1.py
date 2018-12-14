def subreverse_sequence(sequence):
    return tuple(sequence[-2 + len(sequence) % 2::-2] + sequence[1::2])


# print()
# sequence = [0, 1, 2, 3, 4, 5, 6]
# print(sequence)
# print(subreverse_sequence(sequence))
# print()
# sequence = list('молоко')
# print(sequence)
# print(subreverse_sequence(sequence))
# print()
# sequence = [[j, j + 1] for j in range(5)]
# print(sequence)
# print(subreverse_sequence(sequence))
