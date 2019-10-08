#This is function file where it is being defined. After running this script, write
#the function name with parameters in parentheses and press enter for execution of function

def lcm(x, y):  
   if x > y:  
       greater = x  
   else:  
       greater = y  
   while(True):  
       if((greater % x == 0) and (greater % y == 0)):  
           lcm = greater  
           break  
       greater += 1
   return lcm
           #print('The L.C.M. of given numbers is', lcm)
        

 
 
