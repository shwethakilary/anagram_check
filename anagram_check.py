first_word = input("Enter the first word: ").replace(" ", "").lower()
second_word = input("Enter the second word: ").replace(" ", "").lower()

if sorted(first_word) == sorted(second_word):
    print("The words are anagrams.")
else:    
    print("The words are not anagrams.")