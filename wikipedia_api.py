import wikipedia
wikipedia.set_lang('ru')

def search_wiki(word):
    return wikipedia.search(word)


def get_page_info(title):
    page = wikipedia.page(title)
    # page.title
    # page.url
    # page.content
    return page