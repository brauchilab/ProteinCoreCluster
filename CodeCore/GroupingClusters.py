# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 06:57:37 2022

@author: DenyCB
"""
                                
"""------------------------------------------ List of pair of Aromatics nearest than threshold (5A) on core -------------------------------------------------"""                               
                               
# path='C:/CodeCore/Aromatics/minDistance.dcb'

# for CurrentPdbFile in os.listdir(path):

with open('C:/CodeCore/Aromatics/AromaticsUnderTreshold5.dcb','w') as w1:  
         
         
         with open('C:/CodeCore/Aromatics/minDist.dcb','r') as f1:  
             for i in f1:
                 PDBid=f1.readline(4)
                 space=f1.readline(6)
                 resid1=f1.readline(4)
                 space=f1.readline(1)
                 resid2=f1.readline(4)
                 space=f1.readline(1)
                 resname1=f1.readline(3)
                 space=f1.readline(1)
                 resname2=f1.readline(3)
                 space=f1.readline(1)
                 atomtype1=f1.readline(3)
                 space=f1.readline(1)
                 atomtype2=f1.readline(3)                     
                 space=f1.readline(2)
                 dist=f1.readline(8)
                 
                 if(dist==""):
                     break
                 
                 elif(float(dist)<=5):
                     print(PDBid," ",resid1," ",resid2," ",resname1," ",resname2," ",atomtype1," ",atomtype2," ",dist)
                     w1.write(PDBid+" "+resid1+" "+resid2+" "+resname1+" "+resname2+" "+atomtype1+" "+atomtype2+" "+dist+'\n')                               
                                
                                           
"""------------------------------------------ Grouping pair of Aromatics nearest than threshold (5A) on clusters -------------------------------------------------"""         
 
  
G1=set([])
G2=set([])
G3=set([])
G4=set([])
G5=set([])
G6=set([])
G7=set([])
G8=set([])

lastPDB="3J5P"

with open('C:/CodeCore/Aromatics/AromaticsUnderTreshold5.dcb', 'r') as f2:
      with open('C:/CodeCore/Aromatics/nucleos5A.dcb','w') as w2:
          for i in f2:
              
              
              
          
              PDBid=f2.readline(4)
              space=f2.readline(1)
              resid1=f2.readline(4)
              space=f2.readline(1)
              resid2=f2.readline(4)
              space=f2.readline(1)
              resname1=f2.readline(3)
              space=f2.readline(1)
              resname2=f2.readline(3)
              space=f2.readline(1)
              atomtype1=f2.readline(3)
              space=f2.readline(1)
              atomtype2=f2.readline(3)                     
              space=f2.readline(1)
              dist=f2.readline(8)
              
              
              # a=set([resid1,resid2])
              # print(a)
              # print(b)
              # if(len(a.intersection(b))!=0):
                  
              #   c=b.union(a)
                
              #   print(c)
                    
              #   b=set(c)     
              
              # else:
              #     b=a
              # print('\n')      
              
              
              
              if(PDBid!=lastPDB):
                  
                  print(lastPDB,'\n',G1,'\n',G2,'\n',G3,'\n',G4,'\n',G5,'\n',G6,'\n')
                  w2.write(lastPDB+'\n'+str(G1)+'\n'+str(G2)+'\n'+str(G3)+'\n'+str(G4)+'\n'+str(G5)+'\n'+str(G6)+'\n')
                  
                  G1=set([])
                  G2=set([])
                  G3=set([])
                  G4=set([])
                  G5=set([])
                  G6=set([])
                  G7=set([])
                  G8=set([])
                  lastPDB=PDBid
              
              
              currentPair=set([resid1,resid2])
              print(PDBid," ",currentPair)
              
              if(len(G1)==0):
                  G1=currentPair
              
              else:
                  
                  if(len(currentPair.intersection(G1))!=0):
                      
                      G1=G1.union(currentPair)
                      
                      
                      
                  else:
                      if(len(G2)==0):
                          G2=currentPair
                      
                      else:
                          
                          if(len(currentPair.intersection(G2))!=0):
                              
                              G2=G2.union(currentPair)
                              
                              
                              
                          else:
                              if(len(G3)==0):
                                  G3=currentPair
                             
                              else:
                                  
                                  if(len(currentPair.intersection(G3))!=0):
                                      
                                      G3=G3.union(currentPair)
                                      
                                  else:
                                      if(len(G4)==0):
                                          G1=currentPair
                                      
                                      else:
                                          
                                          if(len(currentPair.intersection(G4))!=0):
                                              
                                              G4=G4.union(currentPair)
                                              
                                              
                                              
                                          else:
                                              if(len(G5)==0):
                                                  G5=currentPair
                                              
                                              else:
                                                  
                                                  if(len(currentPair.intersection(G5))!=0):
                                                      
                                                      G5=G5.union(currentPair)
                                                      
                                                      
                                                      
                                                  else:
                                                      if(len(G6)==0):
                                                          G6=currentPair
                                                     
                                                      else:
                                                          
                                                          if(len(currentPair.intersection(G6))!=0):
                                                              
                                                              G6=G6.union(currentPair)
              
                              
              if(len(G1.intersection(G2))!=0):
                  G1=G1.union(G2)
                  G2=set()
                  # if(len(G3)!=0):
              elif(len(G2)!=0 and len(G3) and len(G2.intersection(G3))!=0):
                  G2=G2.union(G3)
                  G3=set()
              elif(len(G3)!=0 and len(G4) and len(G3.intersection(G4))!=0):
                  G3=G3.union(G4)
                  G4=set()
              elif(len(G4)!=0 and len(G5) and len(G4.intersection(G5))!=0):
                  G4=G4.union(G5)
                  G5=set()
              elif(len(G5)!=0 and len(G6) and len(G5.intersection(G6))!=0):
                  G5=G5.union(G6)
                  G6=set()
              elif(len(G1)!=0 and len(G3) and len(G1.intersection(G3))!=0):
                  G1=G1.union(G3)
                  G3=set()
              elif(len(G1)!=0 and len(G4) and len(G1.intersection(G4))!=0):
                  G1=G1.union(G4)
                  G4=set()
              elif(len(G1)!=0 and len(G5) and len(G1.intersection(G5))!=0):
                  G1=G1.union(G5)
                  G5=set()
              elif(len(G1)!=0 and len(G6) and len(G1.intersection(G6))!=0):
                  G1=G1.union(G6)
                  G6=set()
              elif(len(G2)!=0 and len(G4) and len(G2.intersection(G4))!=0):
                  G2=G2.union(G4)
                  G4=set()
              elif(len(G2)!=0 and len(G5) and len(G2.intersection(G5))!=0):
                  G2=G2.union(G5)
                  G5=set()
              elif(len(G2)!=0 and len(G6) and len(G2.intersection(G6))!=0):
                  G2=G2.union(G6)
                  G6=set()
              elif(len(G3)!=0 and len(G5) and len(G3.intersection(G5))!=0):
                  G3=G3.union(G5)
                  G5=set()
              elif(len(G3)!=0 and len(G6) and len(G3.intersection(G6))!=0):
                  G3=G3.union(G6)
                  G6=set()
              elif(len(G4)!=0 and len(G6) and len(G4.intersection(G6))!=0):
                  G4=G4.union(G6)
                  G6=set()
                  
              
          
          lastPDB=PDBid
  