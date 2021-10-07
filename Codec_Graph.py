# Codec Graph
# Copyright Easy Hackintoshing 2021
# By TheHackGuy

import os, time, datetime

dir = input('Drag & Drop The CodecGraph Directory: ')
print("The dir is set to: " + dir + "\n")
inputfile = input("Select codec dump: " + "\n")

setoutputfilename = input('Would you like to set a output file name? (default = no)')
if setoutputfilename in ['yes', 'Yes', 'Y', 'y']:
  print("Great," + '!')
  outputname = input("Select output file name: " + "\n")
  open = os.system(dir+"/1-codecgraph/codecgraph" + " -o " + outputname + " " + inputfile)
else:
  print ("Sorry for asking... Script will now continue")
  open = os.system(dir+"/1-codecgraph/codecgraph" + " " + inputfile)


#end of script
print("\n" + "By TheHackGuy" + "\n" + "© Easy Hackintoshing 2021\n")
print("Thanks for using CodecGraph\n")
print("Check out my GitHub:\n")
print("https://github.com/TheHackGuy\n")

hr = datetime.datetime.now().time().hour
if hr > 3 and hr < 12:
    print("Have a nice morning!\n\n")
elif hr >= 12 and hr < 17:
    print("Have a nice afternoon!\n\n")
elif hr >= 17 and hr < 21:
    print("Have a nice evening!\n\n")
else:
    print("Have a nice night! And don't forget to sleep!\n\n")