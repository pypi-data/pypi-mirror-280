import re

from nltk import download
from nltk.corpus import words
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

download("wordnet")
download("words")
download("punkt")

lemmatizer = WordNetLemmatizer()
common_words = set(w.lower() for w in words.words())


def is_common_word(token: str) -> bool:
    return lemmatizer.lemmatize(token.lower()) in common_words


def is_hex_digit(c: str) -> bool:
    return c in "0123456789abcdefABCDEF"


def is_hex_string(token: str) -> bool:
    return all(is_hex_digit(c) for c in token)


def is_digit_string(token: str) -> bool:
    return all(c.isdigit() for c in token)


def is_base64_string(token: str) -> bool:
    return all(c.isalnum() or c in "+/=" for c in token)


def is_uncommon_word(token: str) -> bool:
    return not is_common_word(token)


def is_random_string(token: str) -> bool:
    if (
        (re.search(r"\d", token) and len(token) > 2)
        or re.search(r"\W", token)
        or len(token) > 15
    ):
        return True
    return False


def need_mask(token: str) -> bool:
    if is_common_word(token):
        return False
    if is_hex_string(token):
        return True
    if is_digit_string(token):
        return True
    if is_base64_string(token):
        return True
    if is_random_string(token):
        return True
    return False


def mask_word(word: str) -> str:
    mask = "MASKED"
    return mask if is_random_string(word) else word


def mask_sentence(sentence: str) -> str:
    return " ".join([mask_word(word) for word in word_tokenize(sentence)])
