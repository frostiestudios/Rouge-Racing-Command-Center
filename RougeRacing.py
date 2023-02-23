from appJar import gui
import os
import webbrowser
import subprocess
import threading
def xampp(btn):
    if btn=="Start":
        print("opening XAMPP")
        os.startfile("C:/XAMPP/xampp-control.exe")
        threading.Thread(target=xampp).start() 
        subprocess.call(['C:/XAMPP/xampp-control.exe', 'startapache', 'startmysql'])
        app.infoBox("Success", "Apache and MySQL servers started!")
def lc(btn):
    print("Lounge Control")
    if btn=="LCOpen":
        print("Lounge Control Is Running")
        os.startfile("C:/LoungeControl/LoungeControl-Server/LoungeControl-Server.exe")
    if btn=="LCStop":
        print("Lounge Control Is Closed")
        os.stopfile("C:/LoungeControl/LoungeControl-Server/LoungeControl-Server.exe")
    
def ms(btn):    
    print("MultiServer")
    if btn=="MSOpen":
        os.open("C:\LoungeControl\LoungeControl-ACMultiServer\LC-AC-MultiServer.exe")
app = gui("Command Center")

app.startLabelFrame("XAMPP",1,1)
app.addButtons(["XAMPPStart","XAMPPStop"],xampp)
app.stopLabelFrame()

app.startLabelFrame("Lounge Control",1,2)
app.addButtons(["LCOpen","LCStop"],lc)
app.stopLabelFrame()

app.startLabelFrame("MultiServer",1,3)
app.addButtons(["MSOpen","MSStop"],ms)
app.stopLabelFrame()

app.startLabelFrame("Lounge Control Settigns",2,1,3)
app.stopLabelFrame()
app.go()