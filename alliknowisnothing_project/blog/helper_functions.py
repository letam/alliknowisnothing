from django.conf import settings
import os, datetime



def get_blog_entry_file_names():
    entries_dir = settings.BLOG_ENTRIES_DIR
    file_list = os.listdir(entries_dir)
    return file_list


def get_blog_entry_names_with_file_names():
    file_list = get_blog_entry_file_names()
    entries = { file[11:-5].lower(): file  for file in file_list }
    return entries


def get_blog_entries_v1():
    file_list = get_blog_entry_file_names()
    file_list.sort(reverse=True)
    entries = [ {   'article' : file[11:-5].replace('-', ' '),
                    'date': file[:10],
                } for file in file_list ]
    return entries


def get_blog_entries():
    entries = get_blog_entry_file_names()
    entries.sort(reverse=True)
    return entries


