import os
import glob
import shutil


save_dir = "C:\python\TXT"
if not os.path.isdir(save_dir):
    res = os.mkdir(save_dir)
    if res == OSError:
        print("cant create directory "+save_dir)
        raise SystemExit(1)

save_dir2 = "C:\python\TXT2"
if not os.path.isdir(save_dir2):
    res = os.mkdir(save_dir2)
    if res == OSError:
        print("cant create directory "+save_dir2)
        raise SystemExit(1)


#shutil.copy(os.path.abspath(filename), save_dir)

all_filenames = glob.glob('../**/*f*.txt', recursive=True)
for filename in all_filenames:
    if os.path.isfile(os.path.abspath(filename)):
        dir_name = os.path.dirname(os.path.abspath(filename))
        if not os.path.samefile(save_dir, dir_name):           
            fname = os.path.basename(filename)
            if 'r' in fname:
#                os.replace(os.path.join(save_dir, fname), os.path.join(save_dir2, fname))
                shutil.copy(os.path.abspath(filename), save_dir2)
            else:
                shutil.copy(os.path.abspath(filename), save_dir)
            
    
#os.path.abspath(filename)