'''Flight simulator. Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
The program should print out current orientation, and applied tilt correction. 
The program should run in infinite loop, until user breaks the loop. 
Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
With every simulation step the orentation should be corrected, applied and printed out.
'''


# this program requires an argument "time" [seconds] passed with the command line
# simulation class is responsible for turbulances and for tilt correction that is needed after turublences.
# option 1 in simulation menu is for the former and option 2 for the later. 3. Exit is obvious
# Plane class inherits from simulation and takes as input the angle received from the simulation
# upon this information of the angle the plane changes the orientation in which it is flying(N,W,S,E) 

import random
import sys




class Simulation(object):
	def __init__(self):
		self.angle = random.gauss(20,3)
		self.x = 0

	def generator(self):				
		while(self.x!=3):
		  print "Welcome in our menu.\n "

		  if(self.angle < 5 and self.angle > -5):
			print "It is advised to make no further changes."
			
			
		  print "1. show current angle (includes turbulences)" 
		  print "2. tilt correction (make up for turbulences)"
		  print "3. exit"

		  self.x = input("Please choose an option from menu\n>>")
		  #print x
		  if(self.x == 1):
			self.angle = self.angle + random.gauss(2,1)
			print "current angle between the plane wings and earth is {} \n".format(self.angle)
		  elif(self.x == 2): 
			self.angle = self.angle - random.gauss(10,2)
			print "angle is {} now\n".format(self.angle)
		  elif(self.x == 3): 
			yield self.angle
			print "quiting...\n"
			
			
			
# plane works like this:
# eastern orientation is 0 degress, Northern = 90deg, Western = 180deg, 
# Southern orientation equals to 270 degress, then 360degress means coming back to former Eastern orientation			
class Plane(Simulation):
	def __init__(self, speed = 500, angle = 0):
		self.angle = angle				# angle between the plane and the earth
		self.speed = speed				# this is very first parameter, initially set to 500 km/h
		self.current_orientation = 0	# this's plane initial orientation
		self.change_param = 0.05		# this is paramater indicating how prone the plane is to orientation changes
		self.sim = Simulation()			# instantiate an object of superior class Simulation.
	
	def simulator(self, time):
		
		current_angle = self.sim.generator()
		self.angle = current_angle.next()
		print "You will now see how plane orientation changes due to tilt correction that was applied\n"
		for time in range(time):
			# current orientation formula consists of 4 parameters
			self.current_orientation = self.speed*self.change_param*self.angle/180*time	
			if self.current_orientation > 360:
				self.current_orientation -= 360
			print "Current orientation is {} in {} second".format(self.current_orientation, time)
	
	
		
if __name__ == "__main__":
	
	print "Hello World!"	
	plane_first = Plane()
	plane_first.simulator(int(sys.argv[1]))
		
