def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_character_dict(text)
    char_list_of_dict = dict_to_list(num_chars)
    char_list_of_dict.sort(reverse=True, key=sort_on)
    create_report(book_path,num_words,char_list_of_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_dict(text):
    char_dict = {}
    for char in text:
        if char.lower() not in char_dict:
            char_dict[char.lower()] = 1
        else:
            char_dict[char.lower()] += 1
    return char_dict

def dict_to_list(dict):
    char_list = []
    for c in dict:
        if c.isalpha():
            new_dict = {"character": c, "number": dict[c]}
            char_list.append(new_dict)
    return char_list

def sort_on(dict):
    return dict["number"]

def create_report(path,wordcount,sorted_list):
    print(f"--- Begin report of {path} ---")
    print(f"{wordcount} words found in the document\n")
    for c in sorted_list:
        current_char = c["character"]
        current_count = c["number"]
        print(f"The '{current_char}' character was found {current_count} times")
    print("--- End report ---")
main()