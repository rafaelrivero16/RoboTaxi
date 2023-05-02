# Write your code here :-)

#import PyLidar3
import Ultrasonic_Class #Declared as class HCSR04
import Maneuver_Class #Declared as class Maneuver

#Obstacle Detection Logic
#Beyond 150 cm --> Lidar
    #Use clustering logic to decide if there is a significant object
        #Include: approximate size(height and width), center location (x, y)
    #Big fat L, couldn't get the Lidar data onto the ESP32 without a ton of coding creating a micropython library for it
#Less than 10 cm --> perform manuever around the object
class Obstacle_Avoidance:

#Constructor - need to pass in ultrasonic class object and maneuver class object
    def __init__(self, ultras_objL, ultras_objR, ultras_objF, man_obj):
        self.ultrasonic_objL = ultras_objL
        self.ultrasonic_objR = ultras_objR
        self.ultrasonic_objF = ultras_objF
        self.maneuver_obj = man_obj

#Class Functions
    def check_surroundings(self):
        distL = self.ultrasonic_objL.distance_cm()
        distR = self.ultrasonic_objR.distance_cm()
        distF = self.ultrasonic_objF.distance_cm()

        if distL < 10:  #Checks if dist is less than 10 cm
            msgL = "Avoiding object on left"
            self.maneuver_obj.maneuverL #Update to Harpers class
        else:
            msgL = "No objects left within 10 cm. "

        if distR < 10:  #Checks if dist is less than 10 cm
            msgR = "Avoiding object on right"
            self.maneuver_obj.maneuverR #Update to Harpers class
        else:
            msgR = "No objects right within 10 cm. "

        if distL < 10:  #Checks if dist is less than 10 cm
            msgF = "Avoiding object in front"
            self.maneuver_obj.maneuverF #Update to Harpers class
        else:
            msgF = "No objects in front within 10 cm. "

        return msgL + msgR + msgF
#    def check_distance_mm(self):
#        dist = self.ultrasonic_obj.distance_mm()
#        return dist
