home_dir1 = 'G:/My Drive/B1 NMCI Project/Documentation/Brem/Cutover/Phase 2/Pre-Post Collection Scripts/Pre/data/'
home_dir2 = 'G:/My Drive/B1 NMCI Project/Documentation/Brem/Cutover/Phase 2/Pre-Post Collection Scripts/Post/data/'

Pre_IR_01 = home_dir1 + 'brem-u00-ir-01-pre-data-collection-data.txt'
Post_IR_01 = home_dir2 + 'IR-01-Post-Data-Collection-Results.txt'
file_name = 'Difference_File'

def compare(File1, File2):
    with open(File1, 'r') as f:
        d=set(f.readlines())
    
    with open(File2, 'r') as f:
        e=set(f.readlines())
    
    open(f'{file_name}.txt', 'w').close() # Create new file.

    with open(f'{file_name}.txt', 'a') as f:
        for line in list(d-e):
            f.write(line + '\n')

compare(Pre_IR_01, Post_IR_01)