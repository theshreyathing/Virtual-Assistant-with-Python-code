import pyttsx3 
import os

pyttsx3 .speak("welcome in my tools")

while True:
    pyttsx3.speak("chat with me your requirement")
    print("chat with me your requirement : ", end='')
    p=input()
    if("dont" in p):
        print("cant open application")    
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("chrome" in p):
        pyttsx3.speak("yes, here is chrome")
        os.system("chrome")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("notepad" in p) or ("editor" in p)):
        pyttsx3.speak("yes, here is notepad")
        os.system("notepad")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("vlc" in p):
        pyttsx3.speak("yes, here is vlc")
        os.system("vlc")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("calendar" in p):
        pyttsx3.speak("yes, here is calendar")
        os.system("calendar")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("calculator" in p):
        pyttsx3.speak("yes, here is calculator")
        os.system("calculator")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("player" in p) or ("media" in p)):
        pyttsx3.speak("yes, here is wmplayer")
        os.system("wmplayer")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("powerpoint" in p):
        pyttsx3.speak("yes, here is PowerPoint")
        os.system("PowerPoint")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("Control Panel" in p):
        pyttsx3.speak("yes, here is Control Panel")
        os.system("Control Panel")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("Task Manager" in p):
        pyttsx3.speak("yes, here is Task Manager")
        os.system("Task Manager")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("Command Prompt" in p): 
        pyttsx3.speak("yes, here is Command Prompt")
        os.system("Command Prompt")
   elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("Discord" in p): 
        pyttsx3.speak("yes, here is Discord")
        os.system("Discord")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("Excel" in p): 
        pyttsx3.speak("yes, here is Excel")
        os.system("Excel")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and ("Word" in p): 
        pyttsx3.speak("yes, here is Word")
        os.system("Word")
    elif (("run" in p) or ("launch" in p) or ("open" in p) ) and (("paint" in p)):
        pyttsx3.speak("yes, here is paint")
        os.system("paint")
    elif ("exit" in p) or ("quit" in p):
        break
    else:
        print("dont support")
  