# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 06:44:24 2022

@author: DenyCB
"""

"""------------------------------ List of all atoms position on Aromatics on core-------------------------------------------------"""


import os


path='C:/CodeCore/PDBs/'#/ent/
pdbInfo='C:/CodeCore/Aromatics/PDBfiles.txt'


    
for CurrentPdbFile in os.listdir(path):
    
    CurrentPdbName=CurrentPdbFile[:4]#[3:][:4]
    with open(path+CurrentPdbFile , 'r') as f1:
      
       with open('C:/CodeCore/Aromatics/PDBfiles.txt' , 'r') as f3:
          for j in f3: 
              PDBinfo=f3.readline(4)
              space=f3.readline(12)
              S1in=f3.readline(4)
              space=f3.readline(31)
              endS4=f3.readline(4)
              
              
        
              for i in f1:
             
                header=f1.readline(4)
                chainCG="A"
                chain="A"
                if(header=="ATOM" and chainCG==chain):
                    
                    space= f1.readline(9)
                    atomtype=f1.readline(3)
                    space= f1.readline(1)
                    resname=f1.readline(3)
                    space= f1.readline(1)
                    chain=f1.readline(1)
                    resid=f1.readline(4)
                    # print(CurrentPdbName)
                    # if (int(resid)>int(endS4)):
                    #     # print(endS4)
                    #     break
                    # if(int(resid)>int(S1in)):
                    with open('C:/CodeCore/Aromatics/DistComparator.txt' , 'r') as f2:  
                        
                        for i in f2:
                            
                            PDB=f2.readline(4)
                            # print(PDB," ",CurrentPdbName," ",resid)
                            if (PDB.lower()==CurrentPdbName.lower()):
                                space=f2.readline(1)
                                chainCG=f2.readline(1)
                                space=f2.readline(1)
                                resnameCG=f2.readline(3)
                                space=f2.readline(1)
                                residCG=f2.readline(4)
                                space=f2.readline(1)
                                frontResID=f2.readline(4)
                                space=f2.readline(29)
                                # print(PDB," ",CurrentPdbName)
                                
                                if(chain==chainCG and resid==residCG):
                                    print(PDB," ",CurrentPdbName," ",resid)
                               
                                    space=f1.readline(4)
                                    coorx=f1.readline(8)
                                    # space=f1.readline(1)
                                    coory=f1.readline(8)
                                    # space=f1.readline(1)
                                    coorz=f1.readline(8)
                                    space= f1.readline()
                                    with open('C:/CodeCore/Aromatics/1AromaticPositions/'+PDB+'Positions.dcb','a') as w1:    
                                        
                                        w1.write(PDB+" "+chain+" "+resname+" "+resid+" "+atomtype+" "+coorx+" "+coory +" "+coorz+'\n')
                                        print(PDB," ",resid)
                             # else:
                                # f1.readline()
                    
                    
                    # print(CurrentPdbName)
                else:
                    nextline=f1.readline()
                  

"""------------------------------ List of all distances between pair of Aromatics on core (treshold of 15A)-------------------------------------------------"""

path='C:/CodeCore/Aromatics/1AromaticPositions/'


# with open('C:/b/Aromatics/AromaticDistancePares.txt','w') as w1:
with open('C:/CodeCore/Aromatics/DistComparator.txt', 'r') as f4:#f1
    
    for i in f4:
       PDBidA=f4.readline(4)
       space=f4.readline(1)
       chainA=f4.readline(1)
       space=f4.readline(1)
       resnameA=f4.readline(3)
       space=f4.readline(1)
       residA=f4.readline(4)
       # space=f4.readline(34)
       with open('C:/CodeCore/Aromatics/DistComparator.txt', 'r') as f5:#f2   
           for j in f5:
               PDBidB=f5.readline(4)
               space=f5.readline(1)
               chainB=f5.readline(1)
               space=f5.readline(1)
               resnameB=f5.readline(3)
               space=f5.readline(1)
               residB=f5.readline(4)
               # space=f5.readline(34)
               if(PDBidA.lower()==PDBidB.lower()):
                   if path+PDBidA+'Positions.dcb'=='C:/CodeCore/Aromatics/1AromaticPositions/Positions.dcb':
                       break
                   with open(path+PDBidA+'Positions.dcb', 'r') as f6:#f3
                   
                       
                    
                       for k in f6:
                          
                          PDBid1=f6.readline(4)
                          space=f6.readline(1)
                          chain1=f6.readline(1)
                          space=f6.readline(1)
                          resname1=f6.readline(3)
                          space=f6.readline(1)
                          resid1=f6.readline(4)
                          space=f6.readline(1)
                          atomtype1=f6.readline(3)
                          space=f6.readline(1)
                                                 
                          ca1x=f6.readline(8)
                          space=f6.readline(1)
                          ca1y=f6.readline(8)
                          space=f6.readline(1)
                          ca1z=f6.readline(8)
                          
                          if(PDBidA.lower()==PDBid1.lower() and residA==resid1):
                          
                              with open(path+PDBidA+'Positions.dcb', 'r') as f7: #f4
                                  for m in f7:
                                      
                                     
                                     
                                     PDBid2=f7.readline(4)
                                     space=f7.readline(1)
                                     chain2=f7.readline(1)
                                     space=f7.readline(1)
                                     resname2=f7.readline(3)
                                     space=f7.readline(1)
                                     resid2=f7.readline(4)
                                     space=f7.readline(1)
                                     atomtype2=f7.readline(3)
                                     space=f7.readline(1)
                                                            
                                     ca2x=f7.readline(8)
                                     space=f7.readline(1)
                                     ca2y=f7.readline(8)
                                     space=f7.readline(1)
                                     ca2z=f7.readline(8)
                              
                                     # if(PDBidB==PDBid2 and resid2==resid1 and atomtype1=="CA "):
                                     #     print(PDBid1," ",PDBid2," ",resid1," ",resid2," ",atomtype1," ",atomtype2)
                                     #     w1.write(PDBid1+" "+PDBid2+" "+resid1+" "+atomtype1+" "+resid2+" "+atomtype2+'\n')
                                     
                                     if(PDBidB.lower()==PDBid2.lower() and resid1!=resid2 and (atomtype1!="CA " and atomtype1!="C  " and atomtype1!="N  " and atomtype1!="O  " and atomtype1!="CB ") and (atomtype2!="CA " and atomtype2!="C  " and atomtype2!="N  " and atomtype2!="O  " and atomtype2!="CB ")):    
                                         
                                         
                                         dist2=((float(ca1x)-float(ca2x))**2+(float(ca1y)-float(ca2y))**2+(float(ca1z)-float(ca2z))**2)**(1/2)
                                         
                                         if(dist2<15):
                                             with open('C:/CodeCore/Aromatics/2AromaticDistancesPares/'+PDBid1+'distances.dcb','a') as w2:
                                                 print(PDBid1," ",PDBid2," ",resid1," ",resid2," ",atomtype1," ",atomtype2," ",str(dist2)[:8])
                                                 w2.write(PDBid1+" "+PDBid2+" "+resid1+" "+resid2+" "+resname1+" "+resname2+" "+atomtype1+" "+atomtype2+" "+str(dist2)[:8]+'\n')
                                      
"""------------------------------------------ List of minimal distances between atoms of pair of Aromatics on core -------------------------------------------------"""                   
 
 
path='C:/CodeCore/Aromatics/2AromaticDistancesPares/'
atomtypeA="   "
atomtypeB="   "
with open('C:/CodeCore/Aromatics/DistComparator.txt','r') as f8:#f1
    # with open('C:/b/Aromatics/MinDistancesAromatics.txt','w') as w1:    

        for i in f8:
    
            PDBidA=f8.readline(4)
            space=f8.readline(1)
            chainA=f8.readline(1)
            space=f8.readline(1)
            resnameA=f8.readline(3)
            space=f8.readline(1)
            residA=f8.readline(4)
            space=f8.readline(34)
            
            with open('C:/CodeCore/Aromatics/DistComparator.txt','r') as f9:#f3
                for i in f9:
                       
                    PDBidB=f9.readline(4)
                    space=f9.readline(1)
                    chainB=f9.readline(1)
                    space=f9.readline(1)
                    resnameB=f9.readline(3)
                    space=f9.readline(1)
                    residB=f9.readline(4)
                    space=f9.readline(34)
                    
                    if(PDBidA.lower()==PDBidB.lower() and residA!=residB):
                        
                        dist2=1000
                      
                        with open(path+PDBidA+'distances.dcb','r') as f10: #f2
                            for j in f10:
                              
                              PDBid1=f10.readline(4)
                              space=f10.readline(1)
                              PDBid2=f10.readline(4)
                              space=f10.readline(1)
                              resid1=f10.readline(4)
                              space=f10.readline(1)
                              resid2=f10.readline(4)
                              space=f10.readline(1)
                              resname1=f10.readline(3)
                              space=f10.readline(1)
                              resname2=f10.readline(3)
                              space=f10.readline(1)
                              atomtype1=f10.readline(3)
                              space=f10.readline(1)
                              atomtype2=f10.readline(3)
                              space=f10.readline(1)
                              dist1=f10.readline(8)
                              #space=f10.readline()
                              
                              if(resid1==residA and resid2==residB):
                                  
                                  if(float(dist2)>float(dist1)):
                                      dist2=dist1
                                      atomtypeA=atomtype1
                                      atomtypeB=atomtype2
                                  
                                  # print(PDBidA," ",PDBidB," ",residA," ",residB," ",dist1," ", dist2)
                        if(float(dist2)!=1000):   
                            with open('C:/CodeCore/Aromatics/minDist.dcb','a') as w3: 
                                print(PDBidA," ",PDBidB," ",residA," ",residB," ",dist1," ", dist2) 
                                w3.write(PDBidA+" "+PDBidB+" "+residA+" "+residB+" "+resnameA+" "+resnameB+" "+atomtypeA+" "+atomtypeB+" "+str(dist1)+" "+ str(dist2)+'\n')
                                

                                
                                