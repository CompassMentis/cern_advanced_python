"""
Step 1
Tidied up the code
Only load the list of words once
"""

# TODO:
# Before running this code,
# from https://github.com/dwyl/english-words
# download words_alpha.txt
# and store it in code09_optimising/data

import word_list
import timeit


def plus_next_available_word(all_words, words_found_so_far):
    if len(words_found_so_far) == 5:
        return words_found_so_far

    for word in all_words:
        if len(word) != 5:
            continue
        if len(word) != len(set(word)):
            continue
        if not words_found_so_far or not set(word) & set(''.join(words_found_so_far)):
            try:
                return plus_next_available_word(all_words, words_found_so_far + [word])
            except ValueError:
                pass

    raise ValueError('No valid sequence found')


def main():
    words = word_list.load()
    print(f'Checking {len(words)} words')

    try:
        result = plus_next_available_word(words, [])
    except KeyboardInterrupt:
        print('Interrupted - aborted')
        return
    except ValueError:
        print('No results found')
        return

    # Sanity check: 5 x 5 letter words, 25 unique characters
    assert len(set(''.join(result))) == 25 and all(len(word) == 5 for word in result)

    print(len(words), 'words')
    print(result)


duration = timeit.timeit(stmt='main()', globals=globals(), number=1)
print(f'{word_list.WORDS_TO_CHECK:,} words: {duration:.5}')

# Timings
"""
Step 0
100 words: 0.71723
500 words: 6.9294
1,000 words: 25.355

Step 1
100 words: 0.17413
500 words: 0.17702
1,000 words: 0.18012
2,000 words: 0.23995
5,000 words: 2.9581
10,000 words: 33.034
"""
