def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #opens text, then sets file_contents to the full output

    print(file_contents)


if __name__ == "__main__":
    main()