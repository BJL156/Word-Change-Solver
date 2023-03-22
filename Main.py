import enchant

dict = enchant.Dict("en_US")
english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
input_word = str(input("Enter the last word in the puzzle: "))

potential_solutions = []

word_test = list(input_word)
for index in range(len(word_test)):
    for letter in english_alphabet:
        word_test[index] = letter

        join_string = str()
        join_string = join_string.join(word_test)

        if dict.check(join_string) and (join_string in potential_solutions) == False and input_word != join_string:
            potential_solutions.append(join_string)
        print(f"Testing: {word_test} ({dict.check(join_string)})")

    word_test = list(input_word)

print("Potential solutions:")
for word in potential_solutions:
    print(word)
input()