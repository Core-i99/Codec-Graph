# Codec Graph
# Copyright Easy Hackintoshing 2021
# By TheHackGuy

import os, time, datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))
working_dir = os.getcwd()
print("\n" + "Current working directory: {0}".format(working_dir) + "\n")


inputfile = input("Select codec dump: " + "\n")

setoutputfilename = input("\n" + 'Would you like to set a output file name? (default = no)' + "\n")
if setoutputfilename in ['yes', 'Yes', 'Y', 'y']:
  print("\n" + "Great!" + "\n")
  outputname = input("Select output file name: " + "\n")
  printoutputfilename = print("\n" + "The output file name is set to: " + outputname + "\n")
  open = os.system(working_dir + "/1-codecgraph/codecgraph" + " -o " + outputname + " " + inputfile)

else:
  print ("Sorry for asking... Script will now continue"+ "\n")
  open = os.system(working_dir+ "/1-codecgraph/codecgraph" + " " + inputfile) 







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