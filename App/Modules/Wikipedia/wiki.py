import wikipediaapi

def getwiki(select):
    wikidata = {'title': None, 'summary': None}
    title = None
    summary = None
    wiki = wikipediaapi.Wikipedia('en')
    page = wiki.page(select)
    status = page.exists()
    if status == True:
        wikidata.update(title = page.title)
        wikidata.update(summary = page.summary)

        return wikidata
    else:
        error = 'The could not be found.'
        return error
