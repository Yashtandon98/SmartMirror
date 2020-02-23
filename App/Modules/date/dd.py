from datetime import date

def day():
    cdate = date.today()
    data = {'datee': None, 'wday': None}
    d = cdate.strftime('%B %d %Y')
    wd = cdate.strftime('%A')
    data.update(datee = d)
    data.update(wday = wd)
    return data
