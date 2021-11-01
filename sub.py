# checking the returncode of a shell command
# Copyright Easy Hackintoshing 2021
# By TheHackGuy

import subprocess

checkGraphviz = subprocess.run(['test', '-e' '/Users/stijnrombDocuments/GitHub/Codec-Graph/dump.txt'], 
    #block the output
    stdout= subprocess.DEVNULL)


if checkGraphviz.returncode != 0:
    print("Couldn't find Graphviz. Do you have Graphviz installed?")
if checkGraphviz.returncode != 1:
    print("Found graphviz")
