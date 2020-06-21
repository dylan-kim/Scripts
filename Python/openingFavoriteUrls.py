# -*- coding: utf-8 -*-

import os
import json
import webbrowser
from pathlib import PureWindowsPath

folderName = "eseo"
urls = []

def getChromeBookmarks():
    # Working with Windows 10
    LocalAppDataPath = PureWindowsPath(os.getenv("LOCALAPPDATA"))
    ChromeBookmarksPath = LocalAppDataPath / 'Google' / 'Chrome' / 'User Data' / 'Default' / 'Bookmarks.bak'

    with open(ChromeBookmarksPath, encoding="utf8") as f:
        data = json.load(f)

    for children in data["roots"]["bookmark_bar"]["children"] :
        try:
            if children["name"] == folderName :
                for bookmark in children["children"] :
                    urls.append(bookmark["url"])
        except:
            pass

def openUrls():
    for url in urls :
        webbrowser.open(url)

if __name__ == "__main__":
    getChromeBookmarks()
    openUrls()
