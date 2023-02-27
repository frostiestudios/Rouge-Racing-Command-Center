import ac
import acsys
from third_party.sim_info import *




appName = "rrtimer"
width, height = 400 , 200 # width and height of the app's window
simInfo = SimInfo()



def acMain(ac_version):#----------------------------- App window Init

    # Don't forget to put anything you'll need to update later as a global variables
    global appWindow # <- you'll need to update your window in other functions.

    appWindow = ac.newApp(appName)
    ac.setTitle(appWindow, appName)
    ac.setSize(appWindow, width, height)
    
    ac.addLabel("Hello","hllow")
    
    
    ac.addRenderCallback(appWindow, appGL) # -> links this app's window to an OpenGL render function

    return appName





def appGL(deltaT):#-------------------------------- OpenGL UPDATE
    """
    This is where you redraw your openGL graphics
    if you need to use them .
    """
    pass # -> Delete this line if you do something here !




def acUpdate(deltaT):#-------------------------------- AC UPDATE
    """
    This is where you update your app window ( != OpenGL graphics )
    such as : labels , listener , ect ...
    """
    pass # -> Delete this line if you do something here !
