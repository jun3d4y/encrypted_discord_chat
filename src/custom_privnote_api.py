import pyPrivnote as pn


def upload_text(text) :
    return pn.create_note(text)

def retrieve_text(link) :
    return pn.read_note(link)
