import os
import platform
def speak(text):
    sysname=platform.system()
    if sysname=='Windows':
       command = (
          'powershell.exe -Command "'
          'Add-Type -AssemblyName System.Speech; '
           f'$synthesizer = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
           f'$synthesizer.Speak(\'{text}\')"'
       )
    elif sysname=='Linux':
         command = f"espeak '{text}'"
    elif sysname=='Darwin':
         command = f"say '{text}'"
    else:
         print(f"Unknown OS: {sysname}")
         return     
         
    os.system(command)



