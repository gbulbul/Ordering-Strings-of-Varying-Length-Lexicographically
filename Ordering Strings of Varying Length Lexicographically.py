# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:47:29 2024

@author: gbulb
"""

class all_possible_alternatives:
    def obtain_all_possible_alternatives(string_dna):
        for idx,i in enumerate(string_dna):
            for k in range(4):
                first_subgroup=i*k #1st_subgroup (A,AA,AAA,N,NN,NNN,D,DD,DDD)
                print(first_subgroup)
            for idx,m in enumerate(string_dna):
                for idx,j in enumerate(string_dna):
                    for idx,k in enumerate(string_dna):        
                        if i==m and i!=j and i!=k and j!=k:
                           STRING1,STRING2=i+j,i+k
                           if STRING1!=STRING2:
                               print(STRING1) #2nd_subgroup (2-mers)
                           STRING3,STRING4=i+j*2,i+k*2
                           if STRING3!=STRING4:
                                print(STRING3) #3rd_subgroup (3-mers like DNN,NAA,ANN)
                           STRING5,STRING6=i+j+i,i+k+i
                           if STRING5!=STRING6:
                                print(STRING5) #4th_subgroup (3-mers like DND,ADA,NDN)
                           STRING7,STRING8=i+j+k,i+k+j
                           if STRING7!=STRING8:
                                 print(STRING7) #5th_subgroup (3-mers like DNA,ADN,NDA)
                           STRING9,STRING10=i+i+k,i+i+j
                           if STRING9!=STRING10:
                                 print(STRING9)  #6th_subgroup (3-mers like DDN,AAD,NND)
                    
                       
if __name__=="__main__":
    string_dna=['D','N','A']
    STRING1, STRING2, STRING3, STRING4, STRING5, STRING6, STRING7, STRING8, STRING9, STRING10='','','','','','','','','',''
    all_possible_alternatives.obtain_all_possible_alternatives(string_dna)
        
    
        
        
    
