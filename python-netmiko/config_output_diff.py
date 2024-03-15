from difflib import Differ
import os

home_dir1 = 'G:/My Drive/B1 NMCI Project/Documentation/Brem/Cutover/Phase 2/Pre-Post Collection Scripts/Pre/data/'
home_dir2 = 'G:/My Drive/B1 NMCI Project/Documentation/Brem/Cutover/Phase 2/Pre-Post Collection Scripts/Post/data/'

with open(home_dir1 + 'brem-u00-ir-01-pre-data-collection-data.txt') as file_1, open(home_dir2 + 'IR-01-Post-Data-Collection-Results.txt') as file_2:
    differ = Differ()

    for line in differ.compare(file_1.readlines(), file_2.readlines()):
        print(line)

file_1.close()
file_2.close()