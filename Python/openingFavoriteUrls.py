# -*- coding: utf-8 -*-

import os
import json
import webbrowser
from pathlib import PureWindowsPath

folder_name = "eseo"
urls = []

def get_chrome_bookmarks():
    # Working with Windows 10
    local_app_data_path = PureWindowsPath(os.getenv("LOCALAPPDATA"))
    chrome_bookmarks_path = local_app_data_path / 'Google' / 'Chrome' / 'User Data' / 'Default' / 'Bookmarks'

    with open(chrome_bookmarks_path, encoding="utf8") as f:
        data = json.load(f)

    for children in data["roots"]["bookmark_bar"]["children"] :
        try:
            if children["name"] == folder_name :
                for bookmark in children["children"] :
                    urls.append(bookmark["url"])
        except:
            pass
            

def open_urls():
    for url in urls :
        webbrowser.open(url)

if __name__ == "__main__":
    get_chrome_bookmarks()
    open_urls()
