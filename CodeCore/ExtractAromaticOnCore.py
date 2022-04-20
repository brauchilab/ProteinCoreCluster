# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 05:50:53 2022

@author: DenyCB
"""

"""--------------------------Generating files with list of Alpha and Gamma Carbons atoms between specified limits--------------------------------"""

head=""
import os

#Working Folders

pdbFile='C:/CodeCore/Aromatics/PDBfiles.txt'
AromaticFolder='C:/CodeCore/Aromatics/Aromatics.txt'
CAlist='C:/CodeCore/Aromatics/CAlist.txt'
CAlist2='C:/CodeCore/Aromatics/CAlist2.txt'
CGlist='C:/CodeCore/Aromatics/CGlist.txt'

path='C:/CodeCore/PDBs/'


for CurrentPdbFile in os.listdir(path):
        CurrentPdbName=CurrentPdbFile[:4]#[3:][:4] depending of the naming of PDB files
        
        
        with open(pdbFile, 'r') as f1:
          with open(CAlist, 'a') as f3:
            with open(CAlist2, 'a') as f5:
              with open(CGlist, 'a') as f4:
                  f4.write("PDBid helix atomtype resname chain resid coordX coordY coordZ"+'\n')  
                  f5.write("PDBid helix atomtype resname chain resid coordX coordY coordZ"+'\n')  
                  for i in f1:     
                      
                   PDB= f1.readline(4)
                   space= f1.readline(12)
                   S1i= f1.readline(4)
                   space= f1.readline(1)
                   S1f= f1.readline(4)
                   space= f1.readline(1)
                   S2i= f1.readline(4)
                   space= f1.readline(1)
                   S2f= f1.readline(4)
                   space= f1.readline(1)
                   S3i= f1.readline(4)
                   space= f1.readline(1)
                   S3f= f1.readline(4)
                   space= f1.readline(1)
                   S4i= f1.readline(4)
                   space= f1.readline(1)
                   S4f= f1.readline(4)

                   
   
                   if(PDB.lower()==CurrentPdbName.lower()):

                       print(PDB," ",S1i," ",S1f," ",S2i," ",S2f," ",S3i," ",S3f," ",S4i," ",S4f)
                       
                     
                       with open(path+CurrentPdbFile, 'r') as f2:
                           
                             for j in f2:
                                 
                                 header=f2.readline(4)
                                 
                      
                                 if(PDB.lower()=="6agf"): #This is for exception where all the rest are the same, B chain
                                     chainID="A"
                                 else:
                                     chainID="B"
                                     
                                # print(chainID)

                                 if (header=="ATOM"):
                                     space= f2.readline(9)
                                     atomtype=f2.readline(3)
                                     repeatedAtomType= f2.readline(1)
                                     resname=f2.readline(3)
                                     space= f2.readline(1)
                                     chain=f2.readline(1)
                                     resid=f2.readline(4)
                                     if(chain==chainID and resid>S1i and resid<S1f and atomtype=="CA " and (repeatedAtomType==" " or repeatedAtomType=="A")):
                                       
                                          space=f2.readline(4)
                                          coorx=f2.readline(8)
                                          coory=f2.readline(8)
                                          coorz=f2.readline(8)
                                          f3.write(PDB+" "+"S1 "+atomtype+" "+resname+" "+chain+" "+resid+" "+coorx+" "+coory +" "+coorz+'\n')
                                          f5.write(PDB+" "+"S1 "+atomtype+" "+resname+" "+chain+" "+resid+" "+coorx+" "+coory +" "+coorz+'\n')
                                        
                                     elif(chain==chainID and resid>S1i and resid<S1f and atomtype=="CG " and (repeatedAtomType==" " or repeatedAtomType=="A")):
                                         
                                           space=f2.readline(4)
                                           coorx=f2.readline(8)
                                           coory=f2.readline(8)
                                           coorz=f2.readline(8)
                                           f4.write(PDB+" "+"S1 "+atomtype+" "+resname+" "+chain+" "+resid+" "+coorx+" "+coory +" "+coorz+'\n')
                                          
                                    
                                     elif(chain==chainID and resid>S2i and resid<S2f and atomtype=="CA " and (repeatedAtomType==" " or repeatedAtomType=="A")):
                                        
                                          space=f2.readline(4)
                                          coorx=f2.readline(8)
                                          coory=f2.readline(8)
                                          coorz=f2.readline(8)
                                          f3.write(PDB+" "+"S2 "+atomtype+" "+resname+" "+chain+" "+resid+" "+coorx+" "+coory +" "+coorz+'\n')
                                          f5.write(PDB+" "+"S2 "+atomtype+" "+resname+" "+chain+" "+resid+" "+coorx+" "+coory +" "+coorz+'\n')
                                        
                                     elif(chain==chainID and resid>S2i and resid<S2f and atomtype=="CG " and (repeatedAtomType==" " or repeatedAtomType=="A")):
                                         
                                          space=f2.readline(4)
                                          coorx=f2.readline(8)
                                          coory=f2.readline(8)
                                          coorz=f2.readline(8)
                                          f4.write(PDB+" "+"S2 "+atomtype+" "+resname+" "+chain+" "+resid+" "+coorx+" "+coory +" "+coorz+'\n')
                                           
                                         
                                   
                                     elif(chain==chainID and resid>S3i and resid<S3f and atomtype=="CA " and (repeatedAtomType==" " or repeatedAtomType=="A")):
                                               
                                          space=f2.readline(4)
                                          coorx=f2.readline(8)
                                          coory=f2.readline(8)
                                          coorz=f2.readline(8)
                                          f3.write(PDB+" "+"S3 "+atomtype+" "+resname+" "+chain+" "+resid+" "+coorx+" "+coory +" "+coorz+'\n')
                                          f5.write(PDB+" "+"S3 "+atomtype+" "+resname+" "+chain+" "+resid+" "+coorx+" "+coory +" "+coorz+'\n')
                                        
                                     elif(chain==chainID and resid>S3i and resid<S3f and atomtype=="CG " and (repeatedAtomType==" " or repeatedAtomType=="A")):
                                          
                                            space=f2.readline(4)
                                            coorx=f2.readline(8)
                                            coory=f2.readline(8)
                                            coorz=f2.readline(8)
                                            f4.write(PDB+" "+"S3 "+atomtype+" "+resname+" "+chain+" "+resid+" "+coorx+" "+coory +" "+coorz+'\n')
                                              
                                              
                                     elif(chain==chainID and resid>S4i and resid<S4f and atomtype=="CA " and (repeatedAtomType==" " or repeatedAtomType=="A")):
                                                   
                                          space=f2.readline(4)
                                          coorx=f2.readline(8)
                                          coory=f2.readline(8)
                                          coorz=f2.readline(8)
                                          f3.write(PDB+" "+"S4 "+atomtype+" "+resname+" "+chain+" "+resid+" "+coorx+" "+coory +" "+coorz+'\n')
                                          f5.write(PDB+" "+"S4 "+atomtype+" "+resname+" "+chain+" "+resid+" "+coorx+" "+coory +" "+coorz+'\n')
                                        
                                     elif(chain==chainID and resid>S4i and resid<S4f and atomtype=="CG " and (repeatedAtomType==" " or repeatedAtomType=="A")):
                                          
                                          space=f2.readline(4)
                                          coorx=f2.readline(8)
                                          coory=f2.readline(8)
                                          coorz=f2.readline(8)
                                          f4.write(PDB+" "+"S4 "+atomtype+" "+resname+" "+chain+" "+resid+" "+coorx+" "+coory +" "+coorz+'\n')
 
                                          
"""------------------------------ Geting distances between Alpha Carbons of residues on oposing helixes (TM1-TM3 and TM2-TM4 pairs)---------------------"""                  

i=0
j=0
ca4x=0.000
ca4z=0.000

with open('C:/CodeCore/Aromatics/CAlist.txt', 'r') as f6: #f6
  with open('C:/CodeCore/Aromatics/DistCAs.txt','w') as f7: #f3
     f7.write("PDB chain resid resname residFront distance"+'\n')
     for i in f6:
        PDBid1=f6.readline(4)
        space=f6.readline(1)
        helix1=f6.readline(2)
        space=f6.readline(5)
        resname1=f6.readline(3)
        space=f6.readline(1)
        chain1=f6.readline(1)
        space=f6.readline(1)
        resid1=f6.readline(4)
        space=f6.readline(1)
        if(helix1=="S1"):
        
            ca1x=float(f6.readline(8))
            space=f6.readline(1)
            ca1y=float(f6.readline(8))
            space=f6.readline(1)
            ca1z=float(f6.readline(8))
     
            dist1=1000
            
            with open('C:/CodeCore/Aromatics/CAlist2.txt', 'r') as f8: #f2
                for j in f8:
                    PDBid=f8.readline(4)
                    space=f8.readline(1)
                    helix=f8.readline(2)
                    space=f8.readline(5)
                    resname=f8.readline(3)
                    space=f8.readline(3)
                    resid2=f8.readline(4)
                    space=f8.readline(1)
                    if (PDBid==PDBid1 and helix=="S3"):
                        caS3ax=float(f8.readline(8))
                        space=f8.readline(1)
                        caS3ay=float(f8.readline(8))
                        space=f8.readline(1)
                        caS3az=float(f8.readline(8))
                        space=f8.readline()
                        
                        
                        dist2=((ca1x-caS3ax)**2+(ca1y-caS3ay)**2+(ca1z-caS3az)**2)**(1/2)
                        if(dist2<dist1):
                            resid2def=resid2
                            dist1=dist2      
                # print(resid1," ",resid2)
                print (resid1," ",resid2def," ",dist1)
                f7.write(PDBid1+" "+chain1+" "+resid1+" "+resname1+"  "+resid2def+" ")
                f7.write(str(dist1)[:8])
                f7.write('\n')
          
            
        elif(helix1=="S2"):
            # print("S2 vs S4")
            ca1x=float(f6.readline(8))
            space=f6.readline(1)
            ca1y=float(f6.readline(8))
            space=f6.readline(1)
            ca1z=float(f6.readline(8))
            dist1=1000
            
            with open('C:/CodeCore/Aromatics/CAlist2.txt', 'r') as f8:
                for j in f8:
                    PDBid=f8.readline(4)
                    space=f8.readline(1)
                    helix=f8.readline(2)
                    space=f8.readline(5)
                    resname=f8.readline(3)
                    space=f8.readline(3)
                    resid2=f8.readline(4)
                    space=f8.readline(1)
                    if (PDBid==PDBid1 and helix=="S4"):
                        caS3ax=float(f8.readline(8))
                        space=f8.readline(1)
                        caS3ay=float(f8.readline(8))
                        space=f8.readline(1)
                        caS3az=float(f8.readline(8))
                        space=f8.readline()
                        
                        
                        dist2=((ca1x-caS3ax)**2+(ca1y-caS3ay)**2+(ca1z-caS3az)**2)**(1/2)
                        if(dist2<dist1):
                            resid2def=resid2
                            dist1=dist2      
                # print(resid1," ",resid2)
                print (resid1," ",resid2def," ",dist1)
                f7.write(PDBid1+" "+chain1+" "+resid1+" "+resname1+"  "+resid2def+" ")
                f7.write(str(dist1)[:8])
                f7.write('\n')
                
      
        elif(helix1=="S3"):
            # print("S2 vs S4")
            ca1x=float(f6.readline(8))
            space=f6.readline(1)
            ca1y=float(f6.readline(8))
            space=f6.readline(1)
            ca1z=float(f6.readline(8))
            dist1=1000
            
            with open('C:/CodeCore/Aromatics/CAlist2.txt', 'r') as f8:
                for j in f8:
                    PDBid=f8.readline(4)
                    space=f8.readline(1)
                    helix=f8.readline(2)
                    space=f8.readline(5)
                    resname=f8.readline(3)
                    space=f8.readline(3)
                    resid2=f8.readline(4)
                    space=f8.readline(1)
                    if (PDBid==PDBid1 and helix=="S1"):
                        caS3ax=float(f8.readline(8))
                        space=f8.readline(1)
                        caS3ay=float(f8.readline(8))
                        space=f8.readline(1)
                        caS3az=float(f8.readline(8))
                        space=f8.readline()
                        
                        
                        dist2=((ca1x-caS3ax)**2+(ca1y-caS3ay)**2+(ca1z-caS3az)**2)**(1/2)
                        if(dist2<dist1):
                            resid2def=resid2
                            dist1=dist2      
                # print(resid1," ",resid2)
                print (resid1," ",resid2def," ",dist1)
                f7.write(PDBid1+" "+chain1+" "+resid1+" "+resname1+"  "+resid2def+" ")
                f7.write(str(dist1)[:8])
                f7.write('\n')
                

        elif(helix1=="S4"):
            # print("S2 vs S4")
            ca1x=float(f6.readline(8))
            space=f6.readline(1)
            ca1y=float(f6.readline(8))
            space=f6.readline(1)
            ca1z=float(f6.readline(8))
            dist1=1000
            
            with open('C:/CodeCore/Aromatics/CAlist2.txt', 'r') as f8:
                for j in f8:
                    PDBid=f8.readline(4)
                    space=f8.readline(1)
                    helix=f8.readline(2)
                    space=f8.readline(5)
                    resname=f8.readline(3)
                    space=f8.readline(3)
                    resid2=f8.readline(4)
                    space=f8.readline(1)
                    if (PDBid==PDBid1 and helix=="S2"):
                        caS3ax=float(f8.readline(8))
                        space=f8.readline(1)
                        caS3ay=float(f8.readline(8))
                        space=f8.readline(1)
                        caS3az=float(f8.readline(8))
                        space=f8.readline()
                        
                        
                        dist2=((ca1x-caS3ax)**2+(ca1y-caS3ay)**2+(ca1z-caS3az)**2)**(1/2)
                        if(dist2<dist1):
                            resid2def=resid2
                            dist1=dist2      
                # print(resid1," ",resid2)
                print (resid1," ",resid2def," ",dist1)
                f7.write(PDBid1+" "+chain1+" "+resid1+" "+resname1+"  "+resid2def+" ")
                f7.write(str(dist1)[:8])
                f7.write('\n')
    
 
"""-------------------- Geting distances between Alpha Carbons and Gamma Carbons of residues on oposing helixes (TM1-TM3 and TM2-TM4 pairs)-----------------------"""                  
   
 
i=0
j=0
ca4x=0.000
ca4z=0.000

with open('C:/CodeCore/Aromatics/CGlist.txt', 'r') as f9: #f1
  with open('C:/CodeCore/Aromatics/DistCGs.txt','w') as f10: #f10
     f10.write("PDB chain resid resname residFront distance"+'\n')
     for i in f9:
        PDBid1=f9.readline(4)
        space=f9.readline(1)
        helix1=f9.readline(2)
        space=f9.readline(5)
        resname1=f9.readline(3)
        space=f9.readline(1)
        chain1=f9.readline(1)
        space=f9.readline(1)
        resid1=f9.readline(4)
        space=f9.readline(1)
        if(helix1=="S1"):
            # print("S1 vs S3")
            ca1x=float(f9.readline(8))
            space=f9.readline(1)
            ca1y=float(f9.readline(8))
            space=f9.readline(1)
            ca1z=float(f9.readline(8))
            dist1=1000
            
            with open('C:/CodeCore/Aromatics/CAlist.txt', 'r') as f11: #2
                for j in f11:
                    PDBid=f11.readline(4)
                    space=f11.readline(1)
                    helix=f11.readline(2)
                    space=f11.readline(5)
                    resname=f11.readline(3)
                    space=f11.readline(3)
                    resid2=f11.readline(4)
                    space=f11.readline(1)
                    if (PDBid==PDBid1 and helix=="S3"):
                        caS3ax=float(f11.readline(8))
                        space=f11.readline(1)
                        caS3ay=float(f11.readline(8))
                        space=f11.readline(1)
                        caS3az=float(f11.readline(8))
                        space=f11.readline()
                        
                        
                        dist2=((ca1x-caS3ax)**2+(ca1y-caS3ay)**2+(ca1z-caS3az)**2)**(1/2)
                        if(dist2<dist1):
                            resid2def=resid2
                            dist1=dist2      
                # print(resid1," ",resid2)
                print (resid1," ",resid2def," ",dist1)
                f10.write(PDBid1+" "+chain1+" "+resid1+" "+resname1+"  "+resid2def+" ")
                f10.write(str(dist1)[:8])
                f10.write('\n')
          
            
        elif(helix1=="S2"):
            # print("S2 vs S4")
            ca1x=float(f9.readline(8))
            space=f9.readline(1)
            ca1y=float(f9.readline(8))
            space=f9.readline(1)
            ca1z=float(f9.readline(8))
            dist1=1000
            
            with open('C:/CodeCore/Aromatics/CAlist.txt', 'r') as f11:
                for j in f11:
                    PDBid=f11.readline(4)
                    space=f11.readline(1)
                    helix=f11.readline(2)
                    space=f11.readline(5)
                    resname=f11.readline(3)
                    space=f11.readline(3)
                    resid2=f11.readline(4)
                    space=f11.readline(1)
                    if (PDBid==PDBid1 and helix=="S4"):
                        caS3ax=float(f11.readline(8))
                        space=f11.readline(1)
                        caS3ay=float(f11.readline(8))
                        space=f11.readline(1)
                        caS3az=float(f11.readline(8))
                        space=f11.readline()
                        
                        
                        dist2=((ca1x-caS3ax)**2+(ca1y-caS3ay)**2+(ca1z-caS3az)**2)**(1/2)
                        if(dist2<dist1):
                            resid2def=resid2
                            dist1=dist2      
                # print(resid1," ",resid2)
                print (resid1," ",resid2def," ",dist1)
                f10.write(PDBid1+" "+chain1+" "+resid1+" "+resname1+"  "+resid2def+" ")
                f10.write(str(dist1)[:8])
                f10.write('\n')
                
      
        elif(helix1=="S3"):
            # print("S2 vs S4")
            ca1x=float(f9.readline(8))
            space=f9.readline(1)
            ca1y=float(f9.readline(8))
            space=f9.readline(1)
            ca1z=float(f9.readline(8))
            dist1=1000
            
            with open('C:/CodeCore/Aromatics/CAlist.txt', 'r') as f11:
                for j in f11:
                    PDBid=f11.readline(4)
                    space=f11.readline(1)
                    helix=f11.readline(2)
                    space=f11.readline(5)
                    resname=f11.readline(3)
                    space=f11.readline(3)
                    resid2=f11.readline(4)
                    space=f11.readline(1)
                    if (PDBid==PDBid1 and helix=="S1"):
                        caS3ax=float(f11.readline(8))
                        space=f11.readline(1)
                        caS3ay=float(f11.readline(8))
                        space=f11.readline(1)
                        caS3az=float(f11.readline(8))
                        space=f11.readline()
                        
                        
                        dist2=((ca1x-caS3ax)**2+(ca1y-caS3ay)**2+(ca1z-caS3az)**2)**(1/2)
                        if(dist2<dist1):
                            resid2def=resid2
                            dist1=dist2      
                # print(resid1," ",resid2)
                print (resid1," ",resid2def," ",dist1)
                f10.write(PDBid1+" "+chain1+" "+resid1+" "+resname1+"  "+resid2def+" ")
                f10.write(str(dist1)[:8])
                f10.write('\n')
                

        elif(helix1=="S4"):
            # print("S2 vs S4")
            ca1x=float(f9.readline(8))
            space=f9.readline(1)
            ca1y=float(f9.readline(8))
            space=f9.readline(1)
            ca1z=float(f9.readline(8))
            dist1=1000
            
            with open('C:/CodeCore/Aromatics/CAlist.txt', 'r') as f11:
                for j in f11:
                    PDBid=f11.readline(4)
                    space=f11.readline(1)
                    helix=f11.readline(2)
                    space=f11.readline(5)
                    resname=f11.readline(3)
                    space=f11.readline(3)
                    resid2=f11.readline(4)
                    space=f11.readline(1)
                    if (PDBid==PDBid1 and helix=="S2"):
                        caS3ax=float(f11.readline(8))
                        space=f11.readline(1)
                        caS3ay=float(f11.readline(8))
                        space=f11.readline(1)
                        caS3az=float(f11.readline(8))
                        space=f11.readline()
                        
                        
                        dist2=((ca1x-caS3ax)**2+(ca1y-caS3ay)**2+(ca1z-caS3az)**2)**(1/2)
                        if(dist2<dist1):
                            resid2def=resid2
                            dist1=dist2      
                # print(resid1," ",resid2)
                print (resid1," ",resid2def," ",dist1)
                f10.write(PDBid1+" "+chain1+" "+resid1+" "+resname1+"  "+resid2def+" ")
                f10.write(str(dist1)[:8])
                f10.write('\n')
                
                
                
"""------------------------------------------- Geting list of Aromatics with AG-AC closer than AC-AC-------------------------------------------------------"""

with open('C:/CodeCore/Aromatics/DistCGs.txt', 'r') as f12:#f2
  with open('C:/CodeCore/Aromatics/DistComparator.txt','w') as f13: #f13
      f13.write("PDB chain resnameCG residCG forntCG distanceCG < distanceCA residCA frontCA"+'\n')
      for i in f12:
          Aromatic=False
          PDBCG=f12.readline(4)
          space=f12.readline(1)
          chain=f12.readline(1)
          space=f12.readline(1)
          residCG=f12.readline(4)
          space=f12.readline(1)
          resnameCG=f12.readline(3)
          space=f12.readline(2)
          residfrontCG=f12.readline(4)
          space=f12.readline(1)
          distCG=f12.readline(8)
          
          
          
          #print(type(distCG))
          with open('C:/CodeCore/Aromatics/DistCAs.txt', 'r') as f14:
           for j in f14:
                PDBCA=f14.readline(4)
                space=f14.readline(3)
                residCA=f14.readline(4)
                space=f14.readline(1)
                resnameCA=f14.readline(3)
                space=f14.readline(2)
                residfrontCA=f14.readline(4)
                space=f14.readline(1)
                distCA=f14.readline(8)
                
            #    print(PDBCA," ",type(distCA))
              
              #  f13.write(PDBCG+" reisdCA:"+ residCA+" residCG"+residCG+" "+str(type(distCA))+str(type(distCA))+'\n')
                if(resnameCG=="PHE" or resnameCG=="TYR" or resnameCG=="TRP" or resnameCG=="HIS"):
                    Aromatic=True 
                if(PDBCG==PDBCA and residCG==residCA and Aromatic==True and float(distCG)<float(distCA)):
                    f13.write(PDBCA+" "+chain+" "+resnameCG+" "+residCG+" "+residfrontCG+" ")
                    f13.write(distCG)
                    f13.write(" < ")
                    f13.write(distCA)
                    f13.write(residCA+" "+residfrontCA+'\n')
                  
                    print("residCA:",residCA," ",PDBCA," ",distCA," > ",distCG," resid",residCG)
    
       