def remove_non_vowels(input_string):
    vowels = "aeiou"
    return [char for char in input_string if char in vowels]

for test in range(int(input())):
    vowel_string = remove_non_vowels(input())
    sorted_string = sorted(vowel_string)
    if vowel_string==sorted_string:
        print("Easy")
    elif vowel_string==sorted_string[::-1]:
        print("Medium")
    else:
        print("Hard")