from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")
speak.speak("Engage in daring or risky activity")
