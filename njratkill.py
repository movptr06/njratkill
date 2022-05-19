'''
njratkill.py
* If only one file appears to have been erased, it is not a bug.
'''
import ctypes
import winreg
import os

def njratkill():
    print("\n[+] Trying remove njrat.")
    print("\n[+] Trying connect registry")
    kill = []
    pwd = "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    pwd2 = "SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run"
    cmd = "cd %AppData%\Microsoft\Windows\Start Menu\Programs\Startup"
    key = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    key2 = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    sub = winreg.OpenKey(key, pwd, 0, winreg.KEY_ALL_ACCESS)
    sub2 = winreg.OpenKey(key2, pwd2, 0, winreg.KEY_ALL_ACCESS)
    get = []
    i = 0
    print("[+] Trying get value by registry")
    while True:
        try:
            get.append(winreg.EnumValue(sub, i))
        except:
            break
        i += 1
    print("[+] Trying find malignity registry")
    for i in get:
        if len(i[0]) == 32:
            os.system("del " + i[1])
            winreg.DeleteValue(sub, i[0])
            try:
                winreg.DeleteValue(sub2, i[0])
            except:
                pass
            kill.append(i[1])
    before = len(kill)
    if not before:
        print("[!] Warning: malignity registry not found")
    else:
        print("[+] Found", before, "and remove")
    print("\n[+] Examine startup folder")
    get = os.popen(cmd + " && dir /b").read().split()
    for i in get:
        if len(i) == 36:
            os.system(cmd + "&& del " + i)
            kill.append(i)
    if len(kill) == before:
        print("[!] Warning: malignity file not found")
    else:
        print("[+] Found", len(kill) - before, "and remove")
    return kill

if __name__ == "__main__":
    print("\n[+] njratkill 1.0.0")
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("\n[-] Error: this program need admin permission.")
        exit(0)
    result = njratkill()
    if result:
        print("\n[+] Remove complete.")
        print("[*] Info: if it didn't work, see this list.\n")
        for i in result:
            print("[+]", i)
        print()
    else:
        print("\n[-] Error: can't find njrat.")
    print("[+] Program ended.")
    
