def count_characters(s):
    char_count = {}
    for char in s:
        char_count[char] += 1
    return char_count

def is_anagram(a, b):
    count_a = count_characters(a)
    count_b = count_characters(b)
    
    return count_a == count_b

a = input("Enter: ")
b = input("Enter: ")

if is_anagram(a, b):
    print("Anagram")
else:
    print("Not an anagram")
