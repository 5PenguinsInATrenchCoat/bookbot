def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = get_num_words(text)
    char_count = get_char_count(text)
    print(f"{word_count} words found in text.\n")
    for char in char_count:
        print(f"The '{char}' character was found {char_count[char]} times.") 
    print("--- End Report ---")


def get_text(book_path):
    with open(book_path) as f:
        text = f.read()
        return text
    # opens text, then sets file_contents to the full output

def get_num_words(text):
    word_count = len(text.split())
    return word_count
    # uses list to count total words
    
def get_char_count(text):
    char_count = {}
    lower_Text = text.lower()
    for char in lower_Text:
        if char.isalpha():
        # only if the character is alphabetical
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count
            

    
    
if __name__ == "__main__":
    main()