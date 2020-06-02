import sys
import powerfactory as pf

app = pf.GetApplication()
app.ResetCalculation()

def setupSimultation(comInc, comSim):
  comInc.iopt_sim = "rms"
  comInc.iopt_show = 0
  comInc.iopt_adapt = 0
  comInc.dtgrd = 0.01
  comInc.start = -0.1
  
  comSim.tstop = 5


def runSimulation(comInc, comSim):
  app.EchoOff()
  comInc.Execute()
  app.EchoOn()
  comSim.Execute()
  
  
def clearSimEvents():
  faultFolder = app.GetFromStudyCase("Simulation Events/Fault.IntEvt")
  cont = faultFolder.GetContents()
  for obj in cont:
    obj.Delete()
  
def addShcEvent(obj, sec, faultType):
  faultFolder = app.GetFromStudyCase("Simulation Events/Fault.IntEvt")
  event = faultFolder.CreateObject("EvtShc", obj.loc_name)
  event.p_target = obj
  event.time = sec
  event.i_shc = faultType

def addRecordedResult(elmRes, obj, param):
  if type(obj) is str:
    for elm in app.GetCalcRelevantObjects(obj):
      elmRes.AddVariable(elm, param)
  elif type(obj) is list:
    for elm in obj:
      elmRes.AddVariable(elm, param)
  else:
    elmRes.AddVariable(obj, param)
  
def enableShcOnLine(shcLine):
  if shcLine.ishclne == 0:
    shcLine.ishclne = 1

shcLine = app.GetCalcRelevantObjects("Line 02 - 03.ElmLne")[0]
time = 0 # event time = 0 sec
clearTime = 0.23
faultType = 0 # 3ph shc
faulClear = 4  #Fault type 4 is fault clearing

comInc = app.GetFromStudyCase("ComInc")
comSim = app.GetFromStudyCase("ComSim")
comInc.Execute()
elmRes = comInc.p_resvar

clearSimEvents()
setupSimultation(comInc, comSim)
enableShcOnLine(shcLine)
addShcEvent(shcLine, time, faultType)
addShcEvent(shcLine, clearTime, faulClear)

addRecordedResult(elmRes, shcLine, "m:Psum:bus1")
addRecordedResult(elmRes, shcLine, "m:Psum:bus2")
addRecordedResult(elmRes, shcLine, "m:Qsum:bus1")
addRecordedResult(elmRes, shcLine, "m:Qsum:bus2")
addRecordedResult(elmRes, "ElmSym", "s:xspeed")

runSimulation(comInc, comSim)

setDesktop=app.GetGraphicsBoard()
viPage = setDesktop.GetPage('Simulations_Plot',1)
oVi = viPage.GetVI('LinePower','VisPlot',1)

oVi.AddVars(shcLine, "m:Psum:bus1")
oVi.AddVars(shcLine, "m:Qsum:bus1")

oVi = viPage.GetVI('GenSpeed','VisPlot',1)
oVi.AddVars(app.GetCalcRelevantObjects("ElmSym")[0], "s:xspeed")

viPage.DoAutoScaleX()
viPage.DoAutoScaleY()