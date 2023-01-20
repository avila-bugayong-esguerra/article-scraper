def clean(txt):
    try:
        idx = txt.index('—')
        txt = txt[idx+1::].strip()
    except:
        pass
    return txt