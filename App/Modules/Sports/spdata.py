import sports

def sp(sport):
    if sport == 'cricket':
        cmatches()
    elif sport == 'basketball':
        bkmatch()
    elif sport == 'tennis':
        tmatch()
    elif sport == 'hockey':
        hmatch()
    elif sport == 'soccer':
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
