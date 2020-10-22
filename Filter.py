from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from utils import FolderAssigner
from configparser import ConfigParser
import os
import json
import time

dot = "."
slash = "/"

# Get/validate the path, if inserted in the config-ini, if not assign it by default
def validateInsertedDirectory():
    try:
        parser = ConfigParser()
        parser.read('config.ini')
        customDirectoryPath = parser.get('custom', 'custom.filter.directory')
    except:
        pass
    if customDirectoryPath == None or customDirectoryPath == "":
        print("empty")
        return os.path.expanduser("~") + "/Downloads"
    else:
        try:
            if os.path.exists(customDirectoryPath) == False or os.path.isdir(customDirectoryPath) == False:
                raise Exception("The inserted path is not a directory")
            else:
                return customDirectoryPath
        except:
            raise Exception("The inserted path was invalid")

# Class for the listener
class CustomFileHandler(FileSystemEventHandler):

    def on_modified(self, event):
        for self.filename in os.listdir(folderToFilter):
            if dot in self.filename:
                splittedFilename = self.filename.split(dot)
                self.extension = splittedFilename[len(splittedFilename) - 1]
                getFolderNameByExtesnsion(self)
                moveFile(self)

        deleteFoldersIfEmpty()

# Gets from folder name from the dictionary, using the extension as key
def getFolderNameByExtesnsion(self):
    self.folderAssigned = FolderAssigner.folderDictionary.get(
        self.extension, None)

def moveFile(self):
    src = folderToFilter + slash + self.filename
    if self.folderAssigned != None:
        dest = folderToFilter + slash + self.folderAssigned
        if self.folderAssigned not in os.listdir(folderToFilter):
            os.mkdir(dest)
            print("CREATE folder: " + dest)
        dest += slash + self.filename
        counter = 0
        if os.stat(src).st_size == 0 & counter <= 3:
            print("The file size is zero, sleep in case is downloading")
            time.sleep(30)
            counter += 1
        os.rename(src, dest)
        print("MOVE The archive: " + self.filename +
              " was moved to the folder: " + dest)


def deleteFoldersIfEmpty():
    for folder in os.listdir(folderToFilter):
        if not dot in folder:
            folderDir = folderToFilter + slash + folder
            if len(os.listdir(folderDir)) == 0:
                os.rmdir(folderDir)
                print("DELETED folder: " + folderDir)


folderToFilter = validateInsertedDirectory()
print(folderToFilter)
file_handler = CustomFileHandler()
observer = Observer()
observer.schedule(file_handler, folderToFilter, recursive=True)
observer.start()

try:
    while observer.isAlive:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
    observer.join()
