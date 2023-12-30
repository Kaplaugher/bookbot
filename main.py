

def generate_report(book_title, word_count, character_count):
    report = f"""Book title: {book_title}
    Word count: {word_count} found the document
    Character count: {character_count}
    """
    print(report)
    return report

def count_characters(text):
    string_dict = {}
    string_list = []
    # convert string_dict to a list and sort
    characters = text.lower()

    for character in characters:
        if character.isalpha():
            if character in string_dict:
                string_dict[character] += 1
            else:
                string_dict[character] = 1

    # for key, value in string_dict.items():
    #     temp = [key,value]
    #     string_list.append(temp)
    return string_dict

def count_words(text):
    words = text.split()
    return len(words)

with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    generate_report('Frankenstein', count_words(file_contents), count_characters(file_contents))
    