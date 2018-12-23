def find_max_substring_occurrence(input_string):
    divisors = [x for x in range(1, len(input_string) + 1)
                if len(input_string) % x == 0]
    for divisor in divisors:
        if input_string[:divisor] * \
           (len(input_string) // divisor) == input_string:
            return len(input_string) // divisor


# print()
# input_string = 'abab'
# print(input_string)
# print(find_max_substring_occurrence(input_string))
# print()
# input_string = 'ttttttttttt'
# print(input_string)
# print(find_max_substring_occurrence(input_string))
# print()
# input_string = 'молоко'
# print(input_string)
# print(find_max_substring_occurrence(input_string))
# print()
# input_string = 'qwertyuiopqwertyuiop'
# print(input_string)
# print(find_max_substring_occurrence(input_string))

# В оригинале было:
# def find_max_substring_occurrence(input_string):
    # divisors = [x for x in range(1, len(input_string) + 1) if len(input_string) % x == 0]
    # for divisor in divisors:
        # if input_string[:divisor] * (len(input_string) // divisor) == input_string:
            # return len(input_string) // divisor
            # break

# И я очень страдаю от того, что длина строк выходит за 79 и надо строки резать
