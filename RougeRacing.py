from appJar import gui
import os
import webbrowser
import subprocess
def rouge(btn):
    if btn=="XAMPP":
        print("opening XAMPP")
        os.startfile("C:/XAMPP/xampp-control.exe")
        subprocess.call(['C:/XAMPP/xampp-control.exe', 'startapache', 'startmysql'])
        app.infoBox("Success", "Apache and MySQL servers started!")
    if btn=="Lounge Control":
        print("Lounge Control Is Running")
        os.startfile("C:/LoungeControl/LoungeControl-Server/LoungeControl-Server.exe")
    if btn=="Remote Launcher":
        print("Starting Remote Launcher")
        webbrowser.open_new_tab("https://192.168.1.12:6001/ACLauncherControl")
        print("https://192.168.1.12:6001/ACLauncherControl")
    if btn=="MultiServer":
        os.open("C:\LoungeControl\LoungeControl-ACMultiServer\LC-AC-MultiServer.exe")
    if btn=="Leaderboard Control":
        webbrowser.open_new_tab("https://192.168.1.12:6001/RemoteViewSettings")
        print("https://192.168.1.12:6001/RemoteViewSettings")
def xampp(btn):
    if btn=="Start":
        print("opening XAMPP")
        os.startfile("C:/XAMPP/xampp-control.exe")
        subprocess.call(['C:/XAMPP/xampp-control.exe', 'startapache', 'startmysql'])
        app.infoBox("Success", "Apache and MySQL servers started!")

app = gui("Command Center")
app.addButtons(["XAMPP","Lounge Control","MultiServer"],rouge)
app.addButtons(["Remote Launcher","Leaderboard Control"],rouge)

app.startLabelFrame("Step 1")
app.addButtons(["Start","Stop"],xampp)
app.stopLabelFrame()
app.go()