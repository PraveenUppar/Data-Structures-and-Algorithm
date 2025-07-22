def count_vowels_consonants(text):

    # Define the vowels in both upper and lower letter bcz we will not convert the char to all small makes it easier to declare
    vowels = "aeiouAEIOU"

    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha(): # Check if the character is an alphabet
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return {vowel_count,consonant_count}

# Test cases
print(f"Counts in 'Hello World': {count_vowels_consonants('Hello World')}")
print(f"Counts in 'Python': {count_vowels_consonants('Python')}")
