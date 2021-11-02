# Script to generate graphviz graphs from HDA-Intel codec information
# Copyright Easy Hackintoshing 2021
# By TheHackGuy

import os, time, datetime,subprocess, webbrowser

debug = 0

#heading
terminalwith = os.get_terminal_size().columns
print("\033[1;31m")
os.system('clear')
print(("# Welcome to Codec Graph - Script to generate graphviz graphs from HDA-Intel codec information #").center(terminalwith))
print(("# © Copyright Easy Hackintoshing 2021 - Brought you by TheHackGuy and Helllabs #").center(terminalwith))

#normal text color
print("\033[0;30m")
print("\n \n \n" )

#debug mode
setdebug = input('Would you like to enable debug mode? (default = no)')
if setdebug in ['yes', 'Yes', 'Y', 'y']:
  debug = 1
  print("\n" + "Enabled debug mode")
else:
  debug = 0
  print("The script will continue with debug mode disabled.\n")



if debug == 1:
  print("\n" + "checking if Graphviz is installed... please wait (a sec)")
checkGraphviz = subprocess.run(['which', 'dot'], stdout= subprocess.DEVNULL)
if checkGraphviz.returncode != 0:
      print("\n" + "Couldn't find Graphviz.")
      print("Please follow the instructions to install Graphviz")
      print("Instructions will open in:")
      def countdown(time_sec):
        while time_sec:
          secs = time_sec
          timeformat = '{:02d}'.format(secs)
          print(timeformat, end='\r')
          time.sleep(1)
          time_sec -= 1  
        webbrowser.open("https://github.com/TheHackGuy/Codec-Graph/blob/main/Graphviz%20Instructions.pdf")
        if debug == 1:
          print("Opened webbrowser")
          print("script will now exit")
        exit()
      countdown(10)
      
if checkGraphviz.returncode != 1:
  if debug ==1:
      print("Found graphviz")

#working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
working_dir = os.getcwd()
if debug == 1:
  print("\n" + "Current working directory: {0}".format(working_dir) + "\n")

#input file
inputfile = input("Drag & drop the codec dump: " + "\n").strip()
checkinputfile = os.path.isfile(inputfile)
if debug == 1:
  print("\n" + "Checking the input file...please wait" + "\n")
  if checkinputfile == 1:
    print("Found the input file")
if checkinputfile == 0:
  print("Couldn't find the file")
  print("Script will now exit")
  exit()  

#outputfilename
setoutputfilename = input("\n" + 'Would you like to set a output file name? (default = no)' + "\n")
if setoutputfilename in ['yes', 'Yes', 'Y', 'y']:
  print("\n" + "Great!" + "\n")
  outputname = input("Select output file name: " + "\n")
  if debug ==1:
    printoutputfilename = print("\n" + "The output file name is set to: " + outputname + "\n")
  open = os.system(working_dir + "/1-codecgraph/codecgraph" + " -o " + outputname + " " + inputfile)
  if open != 0:
    print("The script failed. Please check permissions")
    if debug ==1:
      print(open)
    exit()
  if debug ==1:
    if open != 1:
      print(open)
      print("Script has been successfully executed")

else:
  if debug == 1:
    print ("You choose to skip the custom output file name"+ "\n")
  open = os.system(working_dir+ "/1-codecgraph/codecgraph" + " " + inputfile) 
  if open != 0:
    print("The script failed. Please check permissions")
    exit()
  if debug ==1:
    if open!= 1:
      print("Script has been successfully executed")

#end of script
os.system('clear')
print("The output file has been placed in the Codec Graph directory \n")
print("Thanks for Using Codec Graph Written By TheHackGuy - © Copytight Easy Hackintoshing 2021\n")
print("Check out my GitHub:\n")
print("https://github.com/TheHackGuy\n\n")

hr = datetime.datetime.now().time().hour
if hr > 3 and hr < 12:
    print("Have a nice morning!\n\n")
elif hr >= 12 and hr < 17:
    print("Have a nice afternoon!\n\n")
elif hr >= 17 and hr < 21:
    print("Have a nice evening!\n\n")
else:
    print("Have a nice night! And don't forget to sleep!\n\n")