def bubble_sort_word(word):
    char_list = list(word)
    n = len(char_list)

    for i in range(n):
        for j in range(n - i - 1):
            if char_list[j] > char_list[j + 1]:
                char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]
    return ''.join(char_list)  
sorted_word = bubble_sort_word("word")
print("Sorted word:", sorted_word)
