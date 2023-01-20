from unicodedata import normalize


def normalize_txt(txt):
    return normalize('NFKD', txt)