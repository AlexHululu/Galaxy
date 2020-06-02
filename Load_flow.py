# coding=<utf-8>

import string
import math
import sys
import os

import powerfactory
#start PowerFactory in engine mode
app = powerfactory.GetApplication()
def load_flow():
    global app
    #run Python code below
    app.Show()
    app.PrintInfo("Python Script started..")
    #active project
    prj = app.ActivateProject("NeiMeng+Unipolar DC")
    if prj is 1:
        raise Exception("No project activated. Python Script stopped.")
    ldf = app.GetFromStudyCase("ComLdf")                 # 检索潮流目标
    ldf.iopt_net = 0                                     # force balanced load flow
    ldf.iopt_lim = 1
    app.PrintInfo(ldf.iopt_lim)                          #是否考虑无功限制
    ldf.Execute()                                        #计算潮流
    # input()
# load_flow()