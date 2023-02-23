l_lapcount=0
lapcount=0

def acMain(ac_version):
   global l_lapcount

   appWindow = ac.newApp("appName")
   ac.setSize(appWindow, 200, 200)

   ac.log("Hello, Assetto Corsa application world!")
   ac.console("Hello, Assetto Corsa console!")

   l_lapcount = ac.addLabel(appWindow, "Laps: 0");
   ac.setPosition(l_lapcount, 3, 30)
   return "appName"

def acUpdate(deltaT):
   global l_lapcount, lapcount
   laps = ac.getCarState(0, acsys.CS.LapCount)
   if laps > lapcount:
      lapcount = laps
      ac.setText(l_lapcount, "Laps: {}".format(lapcount))
