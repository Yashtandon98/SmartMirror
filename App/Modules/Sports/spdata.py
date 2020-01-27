import sports

def sp(text):
    if 'cricket' in text:
        cmatches()
    elif 'basketball' in text:
        bkmatch()
    elif 'tennis' in text:
        tmatch()
    elif 'hockey' in text:
        hmatch()
    elif 'soccer' in text:
        smatch()

def cmatches():
    try:
        matches = sports.get_sport(sports.CRICKET)
        cdata = matches
    except Exception as exc:
        cdata = None

    return cdata

def bkmatch():
    try:
        matches = sports.get_sport(sports.BASKETBALL)
        bdata = matches
    except Exception as exc:
        bdata = None

    return bdata

def tmatch():
    try:
        matches = sports.get_sport(sports.TENNIS)
        tdata = matches
    except Exception as exc:
        tdata = None

    return tdata

def hmatch():
    try:
        matches = sports.get_sport(sports.HOCKEY)
        hdata = matches
    except Exception as exc:
        hdata = None

    return hdata

def smatch():
    try:
        matches = sports.get_sport(sports.SOCCER)
        sdata = matches
    except Exception as exc:
        sdata = None

    return sdata
