# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 18:00:12 2018

@author: Someindra
"""
#Class to create walk through simulation of the program
class program_flow(object):
    def __init__(self, filept):
        self.code=filept.read();
        self.a=self.code.split()
        self.operation_stack=list();
        self.temp_stack=list();
        self.simulation_data=list();
        self.initial_count=0
        self.progressive_count=0


    
    def create_walkthrough_simulation_data(self):
        
        for i in range(len(self.a)):
        
            words=self.a[i];
      
            if '{' in words:
                self.operation_stack.append(('{'))
                self.temp_stack.append(i);
            if '}' in words:
                x=self.operation_stack.pop();
                y=self.temp_stack.pop();
                progressive_count=i-y;
                self.simulation_data.append((x,progressive_count))
                progressive_count=0;
        return self.simulation_data;
            
            
    
            
            
    
    
    

    
