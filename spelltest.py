import string
adj_file = open('adjacent_keys.txt')
ADJ_LETTER_DICT = {line.split()[0]: line.split()[1:] for line in adj_file}
adj_file.close()
eng_dict = open("english_dict.txt")
ENG_SET = {line.strip() for line in eng_dict}
eng_dict.close()
word_file = open('words.txt')
words = [[word for word in line.split()] for line in word_file]
possible_words = set()
for line in words:
    for word in line:
        if word not in ENG_SET:
            omitted, extra, adjacent = set(word[:i] + lower_letter + word[i:] for i, letter in enumerate(word) for lower_letter in string.ascii_lowercase), set(word[:i] + word[i + 1:] for i in range(len(word))), set(word[:i] + ADJ_LETTER_DICT[word[i]][j] + word[i + 1:] for i in range(len(word)) if word[i] in string.ascii_lowercase for j in range(len(ADJ_LETTER_DICT[word[i]])))
            possible_words = possible_words.union(set(list(filter(lambda word: word if word in ENG_SET else None, omitted)) + list(filter(lambda word: word if word in ENG_SET else None, extra)) + list(filter(lambda word: word if word in ENG_SET else None, adjacent))))
[print(word) for word in possible_words]