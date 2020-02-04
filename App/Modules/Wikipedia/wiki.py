import wikipediaapi

def getwiki(select):
    wikidata = {'titlee': None, 'summaryy': None}
    title = None
    summary = None
    wiki = wikipediaapi.Wikipedia('en')
    page = wiki.page(select)
    status = page.exists()
    if status == True:
        wikidata.update(titlee = page.title)
        wikidata.update(summaryy = page.summary)

        return wikidata
    else:
        error = 'The could not be found.'
        return error
