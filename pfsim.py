# coding=<utf-8>
import string
import math
import sys
import os
import powerfactory as pf

class PowerFactorySim(object):
    def __init__(self,folder_name, project_name,study_case_name):
        #start PowerFactory 
        self.app = pf.GetApplication()
        self.app.Show()
        #active PowerFactory 
        self.project = self.app.ActivateProject(os.path.join(folder_name,project_name))
        #active study case
        study_case_folder = self.app.GetProjectFolder('study')
        study_case = study_case_folder.GetContents(study_case_name+'.IntCase')[0]
        self.study_case = study_case[0]
        self.study_case.Activate()
        # self.app.GetFromStudyCase(study_case_name)
    
    def prepare_loadflow(self , ldf_mode):
        #translate load flow mode keyword to its int equivalent
        modes = {'balanced':0, 'unbalanced':1 , 'dc':2}
        #retrieve load-flow object
        self.ldf = self.app.GetFromStudyCase('ComLdf')
        #set load flow mode 
        self.ldf.iopt_net = modes[ldf_mode]

    def run_load_flow(self):
        return bool(self.ldf.Execute())

    def get_bus_voltages(self):
        voltages = {}
        #collect all bus elements 
        buses = self.app.GetCalcRelevantObjects('*.ElmTerm')
        #store voltages of each bus in a dictionary
        for bus in buses:
            voltages[bus.loc_name] = bus.GetAttribute('m:u')

        return voltages
    
    def prepare_dynamic_sim(self , monitored_variables, sim_type,start_time,step_size,end_time):
        #get result file 
        self.res = self.app.GetFromStudyCase('*.Elmres')
        #select results variables to monitor  
        for elm_name, var_names in monitored_variables.items():
            #get all network elements that match 'elm_name'
            elements = self.app.GetCalcRelevantObjects(elm_name)
            #select variables to monitor for each element
            for element in elements:
                self.res.AddVars(element, *var_names)
        #retrieve initial conditions and domain sim.objects
        self.inc = self.app.GetFromStudyCase('ComInc')
        self.sim = self.app.GetFromStudyCase('ComSim')
        #set simulation type: 'rms' or 'ins'(for EMT)
        self.inc.iopt_sim = sim_type
        #set start time ,step size and end time 
        self.inc.tstart = start_time
        self.inc.dtgrd = step_size
        self.sim.tstop = end_time
        #set initial conditions 
        self.inc.Execute()

    def run_dynamic_sim(self):
        return bool(self.sim.Execute())

    def get_dynamic_results(self, elm_name, var_name):
        #get network element of interest 
        element = self.app.GetCalcRelevantObjects(elm_name)[0]
        #load results from files
        self.app.ResLoadData(self.res)
        # self.ElmRes.Load()
        col_index = self.app.ResGetIndex(self.res, element, var_name)
        # get number of rows(points in time) in the results file 
        n_rows = self.app.ResGetValueCount(self.res, 0 )
        # read results and time and store them in lists 
        time = []
        var_values = []
        for i in range(n_rows):
            time.append(self.app.ResGetData(self.res, i,-1)[1])
            var_values.append(self.app.ResGetData(self.res, i ,col_index)[1])

        return time , var_values
    


    

    # 设置仿真初始条件
    def setupSimultation(comInc, comSim):
        comInc.iopt_sim = "rms"
        comInc.iopt_show = 0
        comInc.iopt_adapt = 0
        comInc.dtgrd = 0.01
        comInc.start = -0.1
        comSim.tstop = 5

    #执行仿真
    def runSimulation(comInc, comSim):
        app.EchoOff()
        comInc.Execute()
        app.EchoOn()
        comSim.Execute()

    #清除故障事件
    def clearSimEvents():
        faultFolder = app.GetFromStudyCase("Simulation Events/Fault.IntEvt")
        cont = faultFolder.GetContents()
        for obj in cont:
            obj.Delete()

    #添加短路事件
    def addShcEvent(obj, sec, faultType):
        faultFolder = app.GetFromStudyCase("Simulation Events/Fault.IntEvt")
        event = faultFolder.CreateObject("EvtShc", obj.loc_name)
        event.p_target = obj
        event.time = sec
        event.i_shc = faultType
    #添加记录结果
    def addRecordedResult(elmRes, obj, param):
        if type(obj) is str:
            for elm in app.GetCalcRelevantObjects(obj):
                elmRes.AddVariable(elm, param)
        elif type(obj) is list:
            for elm in obj:
                elmRes.AddVariable(elm, param)
        else:
            elmRes.AddVariable(obj, param)

    #启用
    def enableShcOnLine(shcLine):
        if shcLine.ishclne == 0:
            shcLine.ishclne = 1