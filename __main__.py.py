"""
Created on Mon Apr 16 21:09:46 2018

@author: Dell inspiron
"""

import glob
import os
from STAGE1 import first
from STAGE3 import program_flow
from datetime import datetime 
from Tkinter import *
#PATH='C:\\Users\\Dell inspiron\\Desktop\\AntiPlagiarism\\AntiPlagiarism'
PATH=""
def show():
    global PATH
    PATH=e1.get();
bind_score=list();
walkthrough_simulation=list();
LIST_FILE=list();
GENUINE_CLUSTERS=list();
#Creating necessary files and writing to the files
def generate_report():
    os.chdir(PATH+"\\testData")
    f=open('LOG_REPORT.txt', 'w+')
    f.write('DATED:')
    f.write(str(datetime.now()))
    f.write('\n\n')
    f.write('STARTING THE PROCESS....\n\n')
    f.write('LOOKING FOR EXCEPTIONS....\n\n')
    f.write('IMPORTING DISUTILS.....\n\n')
    f.write('WORKING WITH DLL\'s......\n\n')
    f.write('STARTING STAGE 1....\n\n')
    f.write('COMPUTING BIND SCORE FOR FILES....\n\n')
    f.write('STATUS AFTER COMPUTING BIND SCORE.....\n\n')
    f.write('STAGE 1 ANALYSIS....\n\n')
    f.write('FILENAME\tBIND SCORE\n\n')
    a=len(bind_score)
    for i in range(a):
        f.write(LIST_FILE[i]+'\t\t'+str(bind_score[i])+"\n")
    f.write('\n')
    f.write('FORMING CLUSTERS.....\n\n')
    f.write('CLUSTERS FORMED....\n\n')
    f.write('FILES UNDER SCANNER....\n\n')
    f.write('FILENAME1\tFILENAME2\tCLUSTER NUMBER\n\n')
    a=len(GENUINE_CLUSTERS)
    for i in range(a):
        f.write(LIST_FILE[GENUINE_CLUSTERS[i][0]]+'\t\t'+LIST_FILE[GENUINE_CLUSTERS[i][1]]+'\t\t'+str(GENUINE_CLUSTERS[i])+'\n')
    f.write('\n')
    f.write('EXECUTING WALKTHROUGH SIMULATION FOR CLUSTERS.....\n\n')
    f.write('GENERATED SEQUENCES\n\n')
    f.write('FILENAME\tWALKTHROUGH SILMUATION\n\n')
    for i in range(a):
        f.write(LIST_FILE[GENUINE_CLUSTERS[i][0]]+'\t'+str(walkthrough_simulation[i])+'\n')
        f.write(LIST_FILE[GENUINE_CLUSTERS[i][1]]+'\t'+str(walkthrough_simulation[i+1])+'\n')
    f.write('\n\n')
    f.write('CALCULATING OUTCOMES...\n\n')
    f.write('FINAL OUTCOME.......\n\n')
    f.write('FILENAME1\tFILENAME2\tCERTAINITY OF PLAGIARISM\tSTATUS\n\n')
    result=calculate();
    for i in range(a):
        f.write(LIST_FILE[GENUINE_CLUSTERS[i][0]]+'\t\t'+LIST_FILE[GENUINE_CLUSTERS[i][1]]+'\t\t\t'+str(result[i])+"%"+'\t\t\t'+status(result[i])+'\n')
    p=open('FINAL REPORT.txt', 'w+')
    p.write('FINAL OUTCOME.......\n\n')
    p.write('FILENAME1\tFILENAME2\tCERTAINITY OF PLAGIARISM\tSTATUS\n\n')
    result=calculate();
    for i in range(a):
        p.write(LIST_FILE[GENUINE_CLUSTERS[i][0]]+'\t\t'+LIST_FILE[GENUINE_CLUSTERS[i][1]]+'\t\t\t'+str(result[i])+"%"+'\t\t\t'+status(result[i])+'\n')
        
    f.close();
    p.close();

#Deciding whether a number is plagiarized or not
def status(number):
    if number>90:
        return("PLAGIARIZED")
    elif number>=80 and number<=90:
        return("PROBABLY PLAGIARZIED- ASK QUESTIONS ON PROGRAM LOGIC TO ASCERTAIN")
    elif number>=70 and number<80:
        return("PROBABLY NOT PLAGIARZIED- ASK QUESTIONS ON PROGRAM LOGIC TO ASCERTAIN")
    else:
        return("NOT PLAGIARIZED")
        
    
#Computing clusters from the bind score generated
def find_clusters(array):
    clusters=list();
    x=len(array)
    for i in range(x):
        temp=array[i]
        for j in range(x):
            d=list();
            d.append(i)
            if abs(temp-array[j])<=6 and i!=j:
            #print(array[j])
                d.append(j)
            #print(d)
            clusters.append(d)
        del d;
    new=list();
    for i in range(len(clusters)):
        p=len(clusters[i])
        if p>1:
            new.append(clusters[i])
        
    for elem in new:
        for other in new:
            if other[0]==elem[1] or other[1]==elem[0]:
                new.remove(other)
    return new
#Comaring walktrhoguh simulation data
def calculate():
    x=len(walkthrough_simulation)
    cluster_wise=list();
    for i in range(0,x-1,2):
        s=list();
        p=len(walkthrough_simulation[i])
        for j in range(p):
            m=walkthrough_simulation[i][j][1]
            n=walkthrough_simulation[i+1][j][1]
            s.append(abs(m-n))
        cluster_wise.append(s)
        del s
    each_cluster=list();
    c=len(cluster_wise)
    for i in range(c):
        s=sum(cluster_wise[i])
        if s>100:
            each_cluster.append(0)
        else:
            each_cluster.append(100-s)
    return each_cluster


    
    
def main():
    global bind_score
    global walkthrough_simulation
    global LIST_FILE
    global GENUINE_CLUSTERS
    os.chdir(PATH+"\\testData")
    LIST_FILE=glob.glob('*') #List of all the files in the test data
    a=len(LIST_FILE)
    for i in range(a):
        os.chdir(PATH+"\\testData")
        FILENAME=LIST_FILE[i]
        file_pointer=open(FILENAME)
        #Compute first stage
        os.chdir(PATH)
        obj=first(file_pointer)
        bind_score.append(obj.compute_bind())
    #computing clusters from the bind score
    GENUINE_CLUSTERS=find_clusters(bind_score)
    len_genuine_cluster=len(GENUINE_CLUSTERS)
    for i in range(len_genuine_cluster):
        #Getting file name from one file in cluster
        FILENAME=LIST_FILE[GENUINE_CLUSTERS[i][0]]
        os.chdir(PATH+"\\testData")
        file_pointer=open(FILENAME)
        os.chdir(PATH)
        obj=program_flow(file_pointer)
        #Creating walkthrough simulation
        walkthrough_simulation.append(obj.create_walkthrough_simulation_data())
        #Accessing the second file in the cluster
        FILENAME=LIST_FILE[GENUINE_CLUSTERS[i][1]]
        os.chdir(PATH+"\\testData")
        file_pointer=open(FILENAME)
        os.chdir(PATH)
        obj=program_flow(file_pointer)
        #Repating steps
        walkthrough_simulation.append(obj.create_walkthrough_simulation_data())
    #generating report
    generate_report();

#UI development. Standard Tkinter library is used. Self explanatory        
master=Tk()
Label(master, text='Enter Path').grid(row=0)
e1=Entry(master)
e1.grid(row=0, column=1)
Button(master, text='Generate Report', command=show).grid(row=1, column=0, sticky=W, pady=4)

mainloop()

if __name__=='__main__':
    main();

    