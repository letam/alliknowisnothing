from django.conf import settings
import os, json



def get_entry_file_names(reverse=False):
    ''' Return a list of file names containing blog entries.
        The file names are of the format: YYYY-MM-DD_Name-Of-Entry.json
    '''
    entries_dir = settings.BLOG_ENTRIES_DIR
    file_list = os.listdir(entries_dir)
    if reverse:
        file_list.sort(reverse=True)
    return file_list


def get_entry_names_with_file_names():
    entries = get_entry_file_names()
    entry_data = { entry[11:-5].lower(): entry  for entry in entries }
    return entry_data



## for HTML Views ##

def get_entries():
    entries = get_entry_file_names(reverse=True)
    entry_data = [ {'name' : entry[11:-5].replace('-', ' '),
                    'date': entry[:10],
                    'url': '/blog/{}/'.format(entry[11:-5]),
                } for entry in entries ]
    return entry_data


def read_entry_file(file_name):
    file = open(os.path.join(settings.BLOG_ENTRIES_DIR, file_name), 'r')
    data = file.read()
    file.close()
    contents = json.loads(data)
    return contents


def get_entry_contents(entry=''):
    ''' If an entry is provided, look for it and returns its contents as a dict.
        If an entry is not provided, look for the latest entry and return its contents as a dict.
        If the entry requested is not found, return an empty dict.
    '''
    contents = {}
    if entry:
        entry = entry.lower()
        entries = get_entry_names_with_file_names()
        if entry in entries:
            file_name = entries[entry]
            contents = read_entry_file(file_name)
    else:
        entries = get_entry_file_names(reverse=True)
        if entries:
            file_name = entries[0]
            contents = read_entry_file(file_name)

    return contents


## for API ##


def get_entry_url(entry=''):
    url = ''
    if entry:
        entry = entry.lower()
        entries = get_entry_names_with_file_names()
        if entry in entries:
            file_name = entries[entry]
            url = (settings.BLOG_ENTRIES_URL + file_name)
    return url


def get_entries_ajax():
    entries = get_entry_file_names(reverse=True)
    entry_data = [ {'name' : entry[11:-5].replace('-', ' '),
                    'date': entry[:10],
                } for entry in entries ]
    return entry_data