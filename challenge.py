"""Functions to correctly transform words with either a prefix or suffix."""

def add_prefix_un(word: str) -> str:
    """Adds the prefix 'un' to a given word."""
    return f"un{word}"

def make_word_groups(words: list) -> str:
    """Adds a prefix to all words in a list. Words list will be in the following format.
    [<prefix>, <word_1>, <word_2> .... <word_n>]"""
    prefix = words[0]
    result_list = []

    for count, word in enumerate(words):
        if count == 0:
            result_list.append(word)
        else:
            result_list.append(f"{prefix}{word}")

    return " :: ".join(result_list)

def remove_suffix_ness(word: str) -> str:
    """Take a word and remove the suffix 'ness'. Amends the end of the new string as required."""
    without_ness = word.removesuffix("ness")

    if without_ness[-1] == "i":
        without_ness = without_ness[:-1] + "y" 

    return without_ness
