
import os, string

inputfile = input("\n" + "Drag & drop the codec dump" + "\n").strip()


wanttocheckfile = input("\n" + "Do you want to check the file?" + "\n")
if wanttocheckfile in ['Yes', 'yes', "Y", 'y']:
    checkfile = os.path.isfile(inputfile)
    print("\n" + "checking the file...please wait" + "\n")
    if checkfile == 1:
        print("found the file")
    if checkfile == 0:
        print("cound't find the file")    

else:
    print("sorry for asking... stopping script")


