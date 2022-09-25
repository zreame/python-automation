# subprocess lib allows py script to interact with command line or shell
# subprocess lib contains many functions
# check call function runs executable in terminal and waits until process has finished before continuing our script
# each element in check_call represents an arg in the command
# from docs, check_call is older fn, can use subprocess.run()
import subprocess

for i in range(0,5) :
    subprocess.check_call(["python3", "terminal_dummy.py"])


