import os
import webbrowser
import subprocess


def execute_task(intent):
    #It open Browser
    if intent == "open browser":
        subprocess.run(["brave"])
    
    #it open vs code
    elif intent=="open code":
        subprocess.Popen(["/snap/bin/code"])
    
    #it shutdown the system
    elif intent == "shutdown":
        os.system("shutdown now")
    
    #it open instagram
    elif intent=="Instagram":
        webbrowser.open('https://www.Instagram.com/')
    
    #it open reddit
    elif intent=="reddit":
        webbrowser.open("https://www.reddit.com/")
    
    else:
        print("Friday doesn't know this command yet.")
