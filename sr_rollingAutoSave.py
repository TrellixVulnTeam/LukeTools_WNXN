import nuke
import glob
import time
import os

def onAutoSave(filename):

  ## ignore untitled autosave
    if nuke.root().name() == 'Root':
        return filename

    fileNo = 0
    files = getAutoSaveFiles(filename)
    filename = addIncrementalFolder(filename)
    if len(files) > 0 :
        lastFile = files[-1]
    # get the last file number
        if len(lastFile) > 0:
            try:
                fileNo = int(lastFile[-1:])
            except:
                pass

            fileNo = fileNo + 1

    if ( fileNo > 5 ):
        fileNo = 0

    if ( fileNo != 0 ):
        filename = filename + str(fileNo)

    return filename


def onAutoSaveRestore(filename):

    files = getAutoSaveFiles(filename)

    if len(files) > 0:
        filename = files[-1]

    return filename

def onAutoSaveDelete(filename):

  ## only delete untiled autosave
    if nuke.root().name() == 'Root':
      return filename
  # return None here to not delete auto save file
    return None

  
def getAutoSaveFiles(filename):
  
    filename = addIncrementalFolder(filename)
    date_file_list = []
    files = glob.glob(filename + '[1-9]')
    files.extend( glob.glob(filename) )

    for file in files:
        # retrieves the stats for the current file as a tuple
        # (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
        # the tuple element mtime at index 8 is the last-modified-date
        stats = os.stat(file)
        # create tuple (year yyyy, month(1-12), day(1-31), hour(0-23), minute(0-59), second(0-59),
        # weekday(0-6, 0 is monday), Julian day(1-366), daylight flag(-1,0 or 1)) from seconds since epoch
        # note:  this tuple can be sorted properly by date and time
        lastmod_date = time.localtime(stats[8])
        #print image_file, lastmod_date   # test
        # create list of tuples ready for sorting by date
        date_file_tuple = lastmod_date, file
        date_file_list.append(date_file_tuple)
   
    date_file_list.sort()
    return [ filename for _, filename in date_file_list ]

def addIncrementalFolder(filename):
	
    fileList = list(os.path.split(filename))
    fileList.insert(1,'.nukeAutoSave')
    filename = os.path.join(*fileList)
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
    except OSError as e:
            nuke.tprint(e)
    return filename