def main():
    # print("hello world")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # print(file_contents)
    # print(count_words(file_contents))
    # print(count_chars(file_contents))

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")

    main_count = count_chars(file_contents)
    
    for item in main_count:
        print(f"The character '{item['character']}' was found in {item['num']} times")

    print("--- End Report ---")
def count_words(text):
    words = text.split()
    # print(words)
    return len(words)

def count_chars(text):
    dict = {}
    lower_text = text.lower()

    for c in lower_text:
        if c in dict:
            dict[c] += 1
        elif c not in dict and c.isalpha(): 
            dict[c] = 1

    char_list = []
    for char, count in dict.items():
        char_list.append({"character": char, "num": count})

    char_list.sort(reverse=True, key=sort_on)
    return char_list

# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

main()