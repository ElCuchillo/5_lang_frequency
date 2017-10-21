import re
import sys
import collections


def load_data(file_path):
    try:
        with open(file_path, 'r') as f:
            word_pattern = re.compile('\w+', re.IGNORECASE)
            parsed_text = word_pattern.findall(f.read())
    except FileNotFoundError:
        return None, 1
    else:
        return parsed_text, None


def get_most_frequent_words(parsed_text):
    top_10_words = collections.Counter(parsed_text).most_common(10)
    # print(top_10_words)
    words_list = []
    for word, frequency in top_10_words:
        words_list.append(word)
    return words_list


if __name__ == '__main__':
    if len(sys.argv) > 1:
        parsed_text, load_error = load_data(sys.argv[1])
        if load_error:
            print('No such file or directory: ', sys.argv[1])
        else:
            print("The 10 most frequently used words in the {} are: {}".format(sys.argv[1], \
                                                                               get_most_frequent_words(parsed_text)))
    else:
        print("Using: python3 lang_frequency.py <path to file>")
