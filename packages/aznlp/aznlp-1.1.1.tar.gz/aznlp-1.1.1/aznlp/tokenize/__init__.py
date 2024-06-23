"""
AZNLP: Tokenizers

This package provides tokenizers for processing Azerbaijani text.
"""

import re

def word_tokenize(text):
    """
    Tokenizes a given text into words.

    :param text: str, input text
    :return: list of str, tokenized words
    """
    word_token_pattern = re.compile(r'\w+|[^\w\s]', re.UNICODE)
    return word_token_pattern.findall(text)

def sentence_tokenize(text):
    """
    Tokenizes a given text into sentences.

    :param text: str, input text
    :return: list of str, tokenized sentences
    """
    sentence_token_pattern = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s')
    return sentence_token_pattern.split(text)