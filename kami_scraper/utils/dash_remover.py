def clean(sentence):
    if sentence.startswith("-"):
        return sentence[1::]
    
    return sentence