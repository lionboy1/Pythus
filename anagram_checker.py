def anagram_checker(my_input):
    my_input.lower()
    sorted_input = sorted(my_input)
    with open('words_list.txt', 'r') as file:
           for word in file:
                my_word = sorted(word)
                if len(sorted_input) == len(my_word):
                    print('Same length')
                    if sorted_input == my_word:
                        print('Yes!')
                        return my_input
                else:
                    print('Not same')
                    
anagram_checker('ih')
