#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 19:45:08 2021

@author: christianschoeberl
@file: dabp_final_project.py
"""

from gurobipy import *
import numpy as np
import pandas as pd
import csv 
import math
import os
import matplotlib.pyplot as plt 


#import/establish datasets 

#number of hospitals 
#index = j
#[0-28]
path= "hospitals_fix.csv"
data = np.genfromtxt(path, dtype=str, delimiter=',', encoding='utf-8-sig')
hospital_names = data.astype(np.str)

#number of beds per hospital 
#index = j
#[0-28]
path = "hospital_licensed_beds.csv"
data = pd.read_excel("hospital_licensed_beds.xlsx")
hospital_licensed_beds = [552, 190, 30, 62, 162, 44, 315, 124, 176, 341, 
                          63, 49, 80, 200, 35, 32, 124, 30, 32, 328, 315, 
                          155, 383, 222, 495, 423, 1577, 520, 248, 263, 
                          549, 317]

#number of high schools 
#index = j
#[0-46]
path = 'schools.csv'
data = np.genfromtxt(path, dtype=str, delimiter=',', encoding='utf-8-sig')
school_names = data.astype(np.str)

#number of students per high school 
#index = j
#[0-46]
path = 'school_populations.csv'
data = np.genfromtxt(path, dtype=str, delimiter=',', encoding='utf-8-sig')
school_population = data.astype(np.int)

#vary number of positive cases by simulation
#index = s 
#[0-999]
path = 'positive_percents.csv'
data = np.genfromtxt(path, dtype=str, delimiter=',', encoding='utf-8-sig')
positive_percents = data.astype(np.float)

#distances from each school to each hospital 
#29x47 matrix of distance from j -> i 
path = 'distances_store.csv'
data = np.genfromtxt(path, dtype=str, delimiter=',', encoding='utf-8-sig')
distance_store  = data.astype(np.float)

#bus cost 
bus_cost = 300 

#number of kits available at hospitals 
hospital_kits = [2857, 983, 155, 321, 838, 228, 1630, 642, 911, 1765, 326, 254, 
                 414, 1035,181, 166, 642, 155, 166, 1697, 1630, 802, 1982, 
                 1149, 2562, 2189, 8161, 2691, 1283, 1361, 2841, 1640]

#indices: 
hospitals = range(len(hospital_names)) 
schools = range(len(school_names))
simulation = range(len(positive_percents))

#setting up model object 
m = Model()

#add decision variables 
x = m.addVars(schools, hospitals, vtype = GRB.INTEGER, lb = 0.0)
y = m.addVars(schools, hospitals, vtype = GRB.INTEGER, lb = 0.0)

#adding objective 
#minimize total travel distance and transportation cost 
expr = LinExpr()
for j in schools: 
    for i in hospitals:
        expr += distance_store[j,i] * x[j,i] + y[j,i] * bus_cost
m.setObjective(expr)
m.modelSense = GRB.MINIMIZE

#constraints

#every student must get assigned to a hospital  
for j in schools:
    sum_sent = sum(x[j,i] for i in hospitals)
    m.addConstr(sum_sent == school_population[j])

#number of students recevied is less than kit capacity 
#number of infected students received is less than bed capacity 
for i in hospitals: 
    sum_received = sum(x[j,i] for j in schools)
    sum_received_positive = sum_received * 0.15
    m.addConstr(sum_received <= hospital_kits[i])
    m.addConstr(sum_received_positive <= hospital_licensed_beds[i])

#number of buses required is ceil(12) of number of students sent 
for j in schools:
    for i in hospitals: 
        ceiling = x[j,i]/12
        m.addConstr(y[j,i] >= ceiling)
        m.addConstr(y[j,i] <= ceiling + 0.999)


m.optimize()
print(m.objVal)



        
        
        
        
        
        
        
        