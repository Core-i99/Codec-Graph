# Script to generate graphviz graphs from HDA-Intel codec information
# Copyright Easy Hackintoshing 2021
# By TheHackGuy

import os, time, datetime,subprocess

debug = 0

terminalwith = os.get_terminal_size().columns
print("\033[1;31m")
os.system('clear')
print(("# Welcome to Codec Graph - Script to generate graphviz graphs from HDA-Intel codec information #").center(terminalwith))
print(("# © Copyright Easy Hackintoshing 2021 - Brought you by TheHackGuy and Hellabs #").center(terminalwith))


#welcome = print("# Welcome to Codec Graph #"+ "\n" 
# "# Script to generate graphviz graphs from HDA-Intel codec information #" + "\n" + "# 
# Based on existing code from hellabs #" + "\n" + "# 
# Copyright Easy Hackintoshing 2021 #" + "\n" + "# 
# Brought you by TheHackGuy and Hellabs #" + "\n")

print("\033[0;30m")
print("\n \n \n \n " )
print(('Would you like to enable debug mode? (default = no)').center(terminalwith))
setdebug = input('\n')
if setdebug in ['yes', 'Yes', 'Y', 'y']:
  debug = 1
  print("\n" + "Enabled debug mode")

else:
  debug = 0
  print("The script will continue with debug mode disabled.")



if debug == 1:
  print("\n" + "checking if Graphviz is installed... please wait (a sec)")
checkGraphviz = subprocess.run(['which', 'dot'], stdout= subprocess.DEVNULL)
if checkGraphviz.returncode != 0:
      print("Couldn't find Graphviz. Do you have Graphviz installed?")
if checkGraphviz.returncode != 1:
  if debug ==1:
      print("Found graphviz")


os.chdir(os.path.dirname(os.path.abspath(__file__)))
working_dir = os.getcwd()
print("\n" + "Current working directory: {0}".format(working_dir) + "\n")



inputfile = input("Select codec dump: " + "\n").strip()
checkinputfile = os.path.isfile(inputfile)
if debug == 1:
  print("\n" + "checking the file...please wait" + "\n")
  if checkinputfile == 1:
    print("Found the input file")
if checkinputfile == 0:
  print("Couldn't find the file")  

setoutputfilename = input("\n" + 'Would you like to set a output file name? (default = no)' + "\n")
if setoutputfilename in ['yes', 'Yes', 'Y', 'y']:
  print("\n" + "Great!" + "\n")
  outputname = input("Select output file name: " + "\n")
  printoutputfilename = print("\n" + "The output file name is set to: " + outputname + "\n")
  open = os.system(working_dir + "/1-codecgraph/codecgraph" + " -o " + outputname + " " + inputfile)

else:
  print ("Sorry for asking... Script will now continue"+ "\n")
  open = os.system(working_dir+ "/1-codecgraph/codecgraph" + " " + inputfile) 


os.system('clear')
#end of script
print("Thanks for Using Codec Graph" + "\n")
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