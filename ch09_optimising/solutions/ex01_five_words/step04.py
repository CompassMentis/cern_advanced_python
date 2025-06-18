"""
Step 4
- Tried using numba: runs very fast but never returns valid results
    not even with a very short word list with a known set of correct words
"""

# TODO:
# Before running this code,
# from https://github.com/dwyl/english-words
# download words_alpha.txt
# and store it in code09_optimising/data

import word_list
import timeit
import collections
import string


class NoneFoundError(ValueError):
    ...

def plus_next_available_word(grouped_words_as_set, words_found_so_far, characters_found_so_far):
    if len(words_found_so_far) == 5:
        return words_found_so_far

    for first_missing_character in string.ascii_lowercase:
         if first_missing_character not in characters_found_so_far:
             break

    for word in grouped_words_as_set[first_missing_character]:
        if not word & characters_found_so_far:
            try:
                return plus_next_available_word(grouped_words_as_set, words_found_so_far + [word], word | characters_found_so_far)
            except NoneFoundError:
                pass

    raise NoneFoundError('No valid sequence found')


def word_as_sets_back_to_words(words, words_as_sets):
    result = []
    for word_as_set in words_as_sets:
        for word in words:
            if word_as_set == set(word):
                result.append(word)
                break
    return result


def main():
    words = word_list.load()

    print(f'Checking {len(words)} words')

    words = [word for word in words if len(word) == len(set(word)) == 5]
    # words_as_set = [set(word) for word in words]
    grouped_words_as_set = collections.defaultdict(list)
    for word in words:
        word_as_set = set(word)
        lowest_character = min(word_as_set)
        grouped_words_as_set[lowest_character].append(word_as_set)

    try:
        result = plus_next_available_word(grouped_words_as_set, [], set())
    except KeyboardInterrupt:
        print('Interrupted - aborted')
        return
    except ValueError:
        print('No results found')
        return

    result = word_as_sets_back_to_words(words, result)

    print(result)
    # Sanity check: 5 x 5 letter words, 25 unique characters
    assert len(set(''.join(result))) == 25 and all(len(word) == 5 for word in result)


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

Step 4
10,000 words: 0.19047
100,000 words: 18.429
125,000 words: 30.996 - ['vangs', 'chimb', 'fjord', 'expwy', 'klutz']
150,000 words: 50.783 - ['vangs', 'chimb', 'fjord', 'expwy', 'klutz']
200,000 words: 113.49 - ['vangs', 'chimb', 'fjord', 'expwy', 'klutz']
All (370,105) words: 2.5049 - ['wacks', 'minbu', 'fldxt', 'vejoz', 'gryph']
"""
