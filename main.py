from typing import List


paragraph = [
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away."
]


def word_frequency(string: List[str]) -> dict:
    """
    Counts the frequency of each word in a list of 
    strings and returns a dictionary.
    """
    items = ' '.join(string).lower().replace(',', ' ').replace('.', ' ').split()

    return {item: items.count(item) for item in items}


print(word_frequency(paragraph))

