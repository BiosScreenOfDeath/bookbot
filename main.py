def character_count(provided_text):
    character_dictionary = {}

    provided_text_words = provided_text.lower()
    for word in provided_text_words:
        for character in word:
            if character not in character_dictionary:
                character_dictionary[character] = 1
            else:
                character_dictionary[character] += 1

    return character_dictionary

def word_count(provided_text):
    return len(provided_text.split())

def report(provided_text):
    provided_data = character_count(provided_text)
    word_counter = word_count(provided_text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_counter} were found in the document\n")

    provided_data = dict(sorted(provided_data.items(), key=lambda item: item[1], reverse=True))

    for character, times in provided_data.items():
        if(character in "abcdefghijklmnopqrstuvwxyz"):
            print(f"The '{character}' was found {times} times")

def main():
    
    with open("books/frankenstein.txt") as file_handle:
        file_contents = file_handle.read()
        #print(file_contents)
        #print(word_count(file_contents))
        #print(character_count(file_contents))
        report(file_contents)

main()