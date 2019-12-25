#coding=utf-8
import os, sys
reload(sys)
sys.setdefaultencoding('gbk')
import json
import win32gui, win32con, win32api

if getattr(sys, 'frozen', False):
    current_dir = os.path.dirname(sys.executable)
elif __file__:
    current_dir = os.path.dirname(os.path.abspath(__file__))

def _callback(hwnd, extra):
    windows = extra
    temp=[]
    temp.append(hwnd)
    temp.append(win32gui.GetClassName(hwnd))
    temp.append(win32gui.GetWindowText(hwnd))
    windows[hwnd] = temp
  
def show(keyword):
    keyword = keyword.strip()
    windows = {}
    win32gui.EnumWindows(_callback, windows)
    find = False
    for item in windows:
        if keyword.strip() in windows[item][2]:
            win32gui.ShowWindow(windows[item][0], win32con.SW_NORMAL)
            win32gui.SetForegroundWindow(windows[item][0])
            find = True
    return find

def main(argv):
    if len(argv) != 1:
        print "You must specify a keyword"
        sys.exit()
    
    keyword = argv[0]

    with open(current_dir + "\\keyword.json",'r') as f_keyword:
        keyword_info = json.load(f_keyword)
        if keyword_info.has_key(keyword):
            target_keyword = keyword_info[keyword]
            search_keyword = target_keyword['search']
            if not show(search_keyword):
                if target_keyword.has_key('exe'):
                    target_exe = target_keyword['exe']
                    if target_exe is not None and target_exe != '':
                        os.startfile(target_exe)
        else:
            print "You need to configure '" + keyword + "' in the keyword file"

if __name__ == "__main__":
    main(sys.argv[1:])

