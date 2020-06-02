# os.environ["PATH"] = r"C:\Program Files\DIgSILENT\PowerFactory 15.2;"+ os.environ["PATH"]
# os.environ["PATH"] = r"F:\software\Digsilentchinese;"+ os.environ["PATH"]
# PYDpath = "‪‪F:\\software\\Digsilentchinese\\Python\\3.4"
# sys.path.append(PYDpath)
#import PowerFactory module
import powerfactory
#start PowerFactory in engine mode
app = powerfactory.GetApplication()
#run Python code below
app.Show()
app.PrintInfo("Python Script started..")
#active project
prj = app.ActivateProject("Nine-bus System(1)")
#get active project
# prj = app.GetActiveProject()     #可以加入可视化弹窗
if prj is 1:
    raise Exception("No project activated. Python Script stopped.")
ldf = app.GetFromStudyCase("ComLdf")
#force balanced load flow
ldf.iopt_net = 0
ldf.iopt_lim = 1
ldf.Execute()
input()
#retrieve load-flow object
# ldf = app.GetFromStudyCase("ComLdf")

# #force balanced load flow
# ldf.iopt_net = 0

# #collect all relevant terminals
# app.PrintInfo("Collecting all calculation relevant terminals..")
# terminals = app.GetCalcRelevantObjects("*.ElmTerm")
# if not terminals:
#     raise Exception("No calculation relevant terminals found")
# app.PrintPlain("Number of terminals found: %d" % len(terminals))

# for terminal in terminals:
#     voltage = terminal.GetAttribute("m:u")
# app.PrintPlain("Voltage at terminal %s is %f p.u." % (terminal , voltage))
# #print to PowerFactory output window
# app.PrintInfo("Python Script ended.")


#考虑无功限制
#    app.PrintInfo(ldf.iopt_lim)

#    ldf.iopt_pq = 1
#execute load flow

# outputWindow = app.GetOutputWindow()
# outputWindow.clear()
# outputWindow.Print(powerfactory.OutputWindow.MessageType.Plain, "Hello World!")
# def main()