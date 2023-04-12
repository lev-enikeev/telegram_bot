import wikipedia
wikipedia.set_lang('ru')


def search_wiki(word):
    return wikipedia.search(word)
