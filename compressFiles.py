import shutil
import os

REP_DATA = "Data"
baseFolder = os.getcwd()

for directory in os.listdir(REP_DATA):
    if not directory[0] == '.':
        print(directory)
        dir = os.path.join(baseFolder, REP_DATA, directory)
        os.chdir(dir)
        print(os.getcwd())

        # Get all the file in the dir_day repository
        list_elt = [dir_day for dir_day in os.listdir(os.getcwd())]
        # Filter to keep only the directories
        list_elt = list(filter(lambda elt: os.path.isdir(elt), list_elt))
        # Remove the most recent one (the one with the maximum number)
        list_elt.remove(str(max(list(map(int, list_elt)))))
        # print(list_elt)

        # For each folder (but the most recent one), 1) compress it, 2) remove the folder.
        for dir in list_elt:
            print(dir)
            shutil.make_archive(os.path.join(os.getcwd(),dir), 'zip', os.path.join(os.getcwd(),dir))
            shutil.rmtree(os.path.join(os.getcwd(),dir))
