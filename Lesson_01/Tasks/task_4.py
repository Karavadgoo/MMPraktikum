def get_new_dictionary(input_dict_name, output_dict_name):
    with open(input_dict_name, 'r') as input_file, \
         open(output_dict_name, 'w') as output_file:
        dict = {}
        for elem in [line.strip() for line in input_file][1:]:
            human_word = elem.split(' - ')[0]
            dragon_words_list = elem.split(' - ')[1].split(', ')
            for dragon_word in dragon_words_list:
                dict[dragon_word] = dict.get(dragon_word, []) + [human_word]
        output_file.write(str(len(dict)) + '\n')
        for id in sorted(dict):
            output_file.write(id + ' - ' + ', '.join(sorted(dict[id])) + '\n')
        return


# get_new_dictionary('input.txt', 'output.txt')
# print()
# with open('input.txt') as file:
    # for line in file:
        # print(line)
# print()
# with open('output.txt') as file:
    # for line in file:
        # print(line)
