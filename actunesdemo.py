from appJar import gui
import sqlite3
import json

print("Loading Config")
with open("actunes.json","w") as f:
    print("Loaded config.json")
    
def musiccontrols(btn):
    if btn == "Prev":
        print("prev")
    if btn == "Play/Pause":
        print("p/p")
    if btn == "Next":
        print("Next")       
print("Loading App")
app=gui("ACTunes","400x200")

song=app.addLabel("Song","Song",1,1)

album=app.addLabel("Album","Album",2,1)

artist=app.addLabel("Artist","Song",3,1)

controls=app.addButtons(["Prev","Play/Pause","Next"],musiccontrols,4,1)
app.go()