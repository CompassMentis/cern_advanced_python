"""
Step 3 - convert words to sets - once
"""

# TODO:
# Before running this code,
# from https://github.com/dwyl/english-words
# download words_alpha.txt
# and store it in code09_optimising/data

import word_list
import timeit

def plus_next_available_word(words_as_set, words_found_so_far, characters_found_so_far):
    if len(words_found_so_far) == 5:
        return words_found_so_far

    for word in words_as_set:
        if not words_found_so_far or not word & characters_found_so_far:
            try:
                return plus_next_available_word(words_as_set, words_found_so_far + [word], word | characters_found_so_far)
            except ValueError:
                pass

    raise ValueError('No valid sequence found')


def main():
    words = word_list.load()

    print(f'Checking {len(words)} words')

    words = [word for word in words if len(word) == len(set(word)) == 5]
    words_as_set = [set(word) for word in words]

    try:
        result = plus_next_available_word(words_as_set, [], set())
    except KeyboardInterrupt:
        print('Interrupted - aborted')
        return
    except ValueError:
        print('No results found')
        return

    # Sanity check: 5 x 5 letter words, 25 unique characters
    assert len(set(''.join(result))) == 25 and all(len(word) == 5 for word in result)

    # TODO: Turn words_as_set back into actual words, by scanning through the list of words
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

Step 2
1,000 words: 0.17355
5,000 words: 1.2637
10,000 words: 12.584

Step 3
1,000 words: 0.17723
5,000 words: 0.46175
10,000 words: 3.342
20,000 words: 39.573
"""
