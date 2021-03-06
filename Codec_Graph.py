#!/usr/bin/python3
#
# Helper Script to generate graphviz graphs from HDA-Intel codec information
#
# by Stijn Rombouts <stijnrombouts@outlook.com>
#
# Copyright (c) 2021,2022 Stijn Rombouts <stijnrombouts@outlook.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

import os, time, datetime,subprocess, webbrowser, shutil

debug = 0

# heading
terminalwith = os.get_terminal_size().columns
print("\033[1;31m")
os.system('clear')
print(("# Welcome to Codec Graph - Script to generate graphviz graphs from HDA-Intel codec information #").center(terminalwith))
print(("# © Core i99 2021 - Brought you by Core i99 and Helllabs #").center(terminalwith))

# normal text color
print("\033[0;30m")
print("\n \n \n" )

# debug mode
setdebug = input('Would you like to enable debug mode? (default = no) '+ "Options: Y or N \n" )
if setdebug in ['yes', 'Yes', 'Y', 'y']:
  debug = 1
  print("\n" + "Enabled debug mode")
else:
  debug = 0

if debug == 1:
  print("\n" + "Checking if Graphviz is installed... please wait (a sec)")
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
        webbrowser.open("https://github.com/Core-i99/Codec-Graph/blob/main/Graphviz%20Instructions.md")
        if debug == 1:
          print("Opened webbrowser")
          print("script will now exit")
        exit()
      countdown(10)
      
if checkGraphviz.returncode != 1:
  if debug ==1:
      print("Found graphviz")

# working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
working_dir = os.getcwd()
if debug == 1:
  print("\n" + "Current working directory: {0}".format(working_dir) + "\n")


# input file
inputfile = input("Drag & drop the codec dump: " + "\n").strip()
fixedinputfile = inputfile.replace("\\",  '')  #Remove the backslashes from the inputfile string. Otherwise checkinputfile will return false.
checkinputfile = os.path.isfile (fixedinputfile)
if debug == 1:
  print("\n" + "Checking the input file...please wait" + "\n")
  if checkinputfile == 1:
    print("Found the input file")
if checkinputfile == 0:
  print("Couldn't find the file")
  print("Script will now exit")
  exit()  



# outputfilename
setoutputfilename = input("\n" + 'Would you like to set a output file name? (default = no) Options: Y or N \n')
if setoutputfilename in ['yes', 'Yes', 'Y', 'y']:
  print("\n" + "Great!" + "\n")
  outputname = input("Choose the output file name: " + "\n")
  if debug == 1:
    printoutputfilename = print("\n" + "The output file name is set to: " + outputname + "\n")
  
else:
  if debug == 1:
    print ("You choose to skip the custom output file name"+ "\n")
  outputname = "codecdump"

#create folders

createtemp = 'tmp'
if os.path.exists(createtemp):
    shutil.rmtree(createtemp)
    if debug == 1:
      print("Found an existing tmp directory")
os.makedirs(createtemp)
if debug == 1:
      print("Created tmp directory")

createoutput = 'output'
if os.path.exists(createoutput):
    shutil.rmtree(createoutput)
    if debug == 1:
      print("Found an existing output directory")
os.makedirs(createoutput)
if debug == 1:
      print("Created output directory")

open = os.system("python3 " + working_dir + "/scripts/codecgraph.py " + inputfile +  " > " + "tmp/dotfile.txt")
if open != 0:
  print("Couldn't found /scripts/codecgraph.py. Please check permissions")
  exit()
if debug ==1:
  if open!= 1:
    print("The main script was found")

outputfilename = outputname + ".svg"

# running graphviz
# usage of graphviz (dot): dot -T$extention -o$outfile.$extention $inputfile
rungraphviz = os.system("dot -Tsvg -o./output/" + outputfilename +  " tmp/dotfile.txt")
if debug ==1:
  if rungraphviz!= 1:
    print("Running Graphviz succeed") 

if rungraphviz != 0:
  print("Running graphviz failed. The script wil now exit")
  exit()

# removing the temp folder
removedotfile = os.system("rm -r ./tmp/ ")
if removedotfile != 0:
  print("Removing the temp folder failed.")
if debug == 1: 
  if removedotfile != 1:
    print("Removing the temp folder succeed")

# create decimal dump
makedecimal = os.system("./scripts/hex2dec.rb ./output/" + outputfilename + " > ./output/" + outputname + "dec.svg")
if makedecimal != 0:
  print("Making the decimal dump failed. Please check permissions")
  if debug == 1:
    print('Command used to make the decimal dump: ' + makedecimal)
if debug == 1:
  if open != 1:
    print("Making the decimal dump succeed")

#end of script
os.system('clear')
print("The output file has been placed in the output directory \n")
print("Thanks for using Codec Graph\n")
print("Written By Core i99 - © Stijn Rombouts 2021\n")
print("Check out my GitHub:\n")
print("https://github.com/Core-i99/\n\n")

hr = datetime.datetime.now().time().hour
if hr > 3 and hr < 12:
    print("Have a nice morning!\n\n")
elif hr >= 12 and hr < 17:
    print("Have a nice afternoon!\n\n")
elif hr >= 17 and hr < 21:
    print("Have a nice evening!\n\n")
else:
    print("Have a nice night! (And don't forget to sleep!)\n\n")
