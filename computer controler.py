import webbrowser
import time
print ("controller 1.0 test")
print ("presse r to run. just is open the story of joha with arabic")
if input()=="r":
    url="https://www.google.com/?hl=fr"
    webbrowser.open_new_tab(url)
time.sleep(1)
url="https://www.youtube.com/"
webbrowser.open_new(url)
time.sleep(3)
url="https://www.youtube.com/@Sada9isas"
webbrowser.open(url)
time.sleep(3)
url="https://www.youtube.com/watch?v=1jfw9XQ9JnY"
webbrowser.open (url)