def remove_highlights(highlights, article_text):
    return list(filter(lambda x: x not in highlights, article_text))