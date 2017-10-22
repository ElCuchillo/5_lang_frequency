import sys
import re
import collections

# The constant indicates quantity of the most common words to be outputed
HOW_MANY_WORDS = 10


def load_data(file_path):
    try:
        with open(file_path, 'r') as data:
            word_pattern = re.compile('\w+', re.IGNORECASE)
            parsed_text = word_pattern.findall(data.read())

    except FileNotFoundError:
        return None

    else:
        return parsed_text


def get_most_frequent_words(parsed_text, words_qty):

    return collections.Counter(parsed_text).most_common(words_qty)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        parsed_text = load_data(sys.argv[1])

        if not parsed_text:
            print("File or direcory {} not found".format(sys.argv[1]))
        else:
            top_10_words = get_most_frequent_words(parsed_text, HOW_MANY_WORDS)
            print("{} most сommon words in the {} are (word, qty):"
                  .format(HOW_MANY_WORDS, sys.argv[1]))
            for word, qty in top_10_words:
                print('{:.<20}{:<3}'.format(word, qty))

    else:
        print("Using: python3 lang_frequency.py <path_to_file>")
