import csv
import os
import shutil

workingDirectory = 'C:/Users/Student/Downloads/archive/Kaggle Dataset/sorted' #location files are being sorted into
folderList = ['gls', 'nclb', 'pls', 'cr', 'sr', 'healthy', 'other'] #list the name of the folders you want sorted into according to csv
originFolder = 'C:/Users/Student/Downloads/archive/Kaggle Dataset/leaf_images' #location of files to be sorted

with open('Database.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        name = row[1]
        classifications = row[2:-1]
        location = os.path.join(originFolder, name)
        for i in range(len(classifications)):
            if classifications[i] == '1':
                shutil.copy(location, (os.path.join(workingDirectory, folderList[i])))
            else:
                pass