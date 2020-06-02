import csv
import powerfactory
from pfsim import PowerFactorySim

FOLDER_NAME = ''
PROJECT_NAME = 'Wind Farm(1)'
STUDY_CASE_NAME = '06.2 LVRT Simulation 30% Un'
# MONITORED_VARIABLES = {'G1.ElmSym':['s:phi' , 's;speed' , 's:fe'],'*ElmTerm': ['m:I:_LOCALBUS:A' , 'm:I:_LOCALBUS:B','m:I:_LOCALBUS:C']}
MONITORED_VARIABLES = {'*.ElmGenstat': ['m:u1:bus1' , 'm:I1P:bus1','m:I1Q:bus1'],'Busbar.ElmTerm':['m:u1'],
                        'PQ PCC.StaPqmea':['s:p', 's:q']}


#active project and study case
sim = PowerFactorySim(folder_name=FOLDER_NAME, project_name=PROJECT_NAME, study_case_name=STUDY_CASE_NAME)
sim.prepare_loadflow(ldf_mode='balanced')
sim.run_load_flow()
#prepare EMT simulation
sim.prepare_dynamic_sim(monitored_variables=MONITORED_VARIABLES,sim_type='ins', start_time=0.0, step_size=0.0001, end_time=0.02)
#run EMT simulation
sim.run_dynamic_sim()
#retrieve line-to-line volages from one bus 
t,ulW = sim.get_dynamic_results('WTG 2.4.ElmGenstat', 'm:u1:bus1')
_,ulB = sim.get_dynamic_results('Busbar.ElmTerm', 'm:u1')
_,PCC_P = sim.get_dynamic_results('PQ PCC.StaPqmea', 's:p')
_,PCC_Q = sim.get_dynamic_results('PQ PCC.StaPqmea', 's:q')
#store line-to-line volages in csv files
with open('res_emt.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['t', 'ulW', 'ulB', 'PCC_P', 'PCC_Q'])
    for row in zip(t, ulW, ulB, PCC_P, PCC_Q):
        csvwriter.writerow(row)
input()