def get_number_of_words(file_contents):
    num_words = len(file_contents.split())
    return num_words

def get_number_of_characters(file_contents):
    character_dict = {}
    character_list = []
    for letter in file_contents:
        if letter.isupper():
            letter = letter.lower()
        if letter not in character_dict:
            character_dict[letter] = 1
        else:
            character_dict[letter] += 1
    for key in character_dict:
        character_list.append({'letter' :key, 'num':character_dict[key]})
    return character_list

def sort_on_values(dict):
    return dict['num']

def get_sorted_dictionary(character_list):
    character_list.sort(reverse=True, key=sort_on_values)
    return character_list
