def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count =get_num_words(text)
    print(f"{word_count} words found in text.\n ")
    

def get_text(book_path):
    with open(book_path) as f:
        text = f.read()
        return text
    #opens text, then sets file_contents to the full output

def get_num_words(text):
    word_count = len(text.split())
    return word_count
    #uses list to count total words
    
    
    
    
if __name__ == "__main__":
    main()