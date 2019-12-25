import os
import sys
import subprocess
import json

if getattr(sys, 'frozen', False):
    current_dir = os.path.dirname(sys.executable)
elif __file__:
    current_dir = os.path.dirname(os.path.abspath(__file__))

with open(current_dir + "\\config.json",'r') as f_config:
    config_info = json.load(f_config)
    cmder = config_info['cmder']

def main(argv):
    process = subprocess.Popen('cat ' + cmder + '\\config\\.history',shell=True,stdout=subprocess.PIPE) 
    out,err = process.communicate() 
    keyword = argv[0]
    i = 1
    count = 0
    lines = out.splitlines()
    for line in lines:
        count+=1
        if keyword in line and count != len(lines):
            print "  " + str(i) + ". " + line
            i+=1

if __name__ == "__main__":
    main(sys.argv[1:])