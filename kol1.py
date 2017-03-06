'''Flight simulator. Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
The program should print out current orientation, and applied tilt correction. 
The program should run in infinite loop, until user breaks the loop. 
Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
With every simulation step the orentation should be corrected, applied and printed out.
'''
import random


y = 1
if(y==1):
  print "hello world!"


angle = random.gauss(20,3)
x=0
while(x!=3):
  print "Welcome in our menu.\n "

  if(angle < 5 and angle > -5):
    print "It is advised to make to further changes."
    
    


  print "1. show current orientation" 
  print "2. tilt correction"
  print "3. exit"

  x = input("Please choose an option from menu\n>>")
  #print x
  if(x==1):
    angle = angle + random.gauss(2,1)
    print "current angle between the plane wings and earth is ", angle, "\n correction process."
  elif(x==2): 
    angle = angle - random.gauss(10,2)
    print "angle is ", angle, " now"
  elif(x==3):
    print "quiting..."                        
