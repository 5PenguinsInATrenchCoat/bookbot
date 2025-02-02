def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = get_num_words(text)
    char_count = get_char_count(text)
    print(f"{word_count} words found in text.\n")
    #print(f"Space count: {char_count.get(' ', 0)}")
    #for char in char_count:
    #    print(f"'{char}'" + ": " + f"{char_count[char]}") 
    print(char_count)

def get_text(book_path):
    with open(book_path) as f:
        text = f.read()
        return text
    #opens text, then sets file_contents to the full output

def get_num_words(text):
    word_count = len(text.split())
    return word_count
    #uses list to count total words
    
def get_char_count(text):
    lower_Text = text.lower()
    lines = lower_Text.splitlines()
    char_count = {}
    for char in lower_Text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
            

    
    
if __name__ == "__main__":
    main()