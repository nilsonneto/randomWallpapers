import os
import random

# Constants
numFiles = 100
basDir = 'C:\\Users\\nilso\\Dropbox\\Camera Uploads\\Wallpapers\\'
arcDir = basDir + 'Archive'
selDir = basDir + 'Selected'
oldDir = basDir + 'Old'

# List files in directories
arcFiles = os.listdir(arcDir)
selFiles = os.listdir(selDir)
# oldFiles = os.listdir(oldDir)

# Based on number of files in archive, select 100 random
arcRandIndex = random.sample(range(len(arcFiles)), numFiles)

# Move all wallpapers in Selected to Old
if len(selFiles) > 0:
    for selFile in selFiles:
        os.rename(selDir + "\\" + selFile, oldDir + "\\" + selFile)

# Create list of filenames based on random list created above
selected = []
for index in arcRandIndex:
    selected.append(arcFiles[index])

# Move random files from Archive to Selected
for arcFile in selected:
    os.rename(arcDir + "\\" + arcFile, selDir + "\\" + arcFile)
