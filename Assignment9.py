
class Vehicle:
    #initializing default valiues
    def __init__(self):
        self.make="None"
        self.model="None"
        self.year=0
        self.weight=0
        self.NeedsMaintenance=False
        self.TripsSinceMaintenance=0
    #to set attributes of the vehicle class
    def setmake(self,Name,Make,Model,Year,Weight):
        self.name=Name
        self.make=Make
        self.model=Model
        self.year=Year
        self.weight=Weight
    def repair(self):
        self.NeedsMaintenance=False
        self.TripsSinceMaintenance=0


class Cars(Vehicle):
     def __init__(self,make,model,year,weight,NeedsMaintenance,TripsSinceMaintenance):
         Vehicle.__init__(self,make,model,year,weight,NeedsMaintenance,TripsSinceMaintenance)
         self.isDriving=False

     def Drive(self):
         isDriving=True

     def Stop(self):
         isDriving=False
         Vehicle.TripsSinceMaintenance+=1
     def Maintenance(self):
         if(int(Vehicle.TripsSinceMaintenance)>100):
             Vehicle.NeedsMaintenance=True
             print("Vehicle needs Maintenance")
         else:
             print("Vehicle does not need maintenance")


#Talking the cars for a couple of trips and printing their data

myCar1=Cars("x","Nissan",1998,3500,False,0)
myCar1.Drive()
myCar1.Stop()
myCar1.Drive()
myCar1.Stop()
myCar1.Maintenance()
print(myCar1.TripsSinceMaintenance)
print(myCar1.make)
print(myCar1.model)
print(myCar1.year)
print(myCar1.weight)


myCar2=Cars("y","BMW",2012,5000,False,0)
myCar2.Drive()
myCar2.Stop()
myCar2.Drive()
myCar2.Stop()
myCar2.Drive()
myCar2.Stop()
myCar2.Drive()
myCar2.Stop()
myCar2.Drive()
myCar2.Stop()
myCar2.Drive()
myCar2.Stop()
myCar2.Drive()
myCar2.Stop()
myCar2.Drive()
myCar2.Stop()

myCar2.Maintenance()
print(myCar2.TripsSinceMaintenance)
print(myCar2.make)
print(myCar2.model)
print(myCar2.year)
print(myCar2.weight)



myCar3=Cars("z","Tesla",2017,2200,False,0)
myCar3.Drive()
myCar3.Stop()
myCar3.Drive()
myCar3.Stop()
myCar3.Drive()
myCar3.Stop()
myCar3.Drive()
myCar3.Stop()
myCar3.Drive()
myCar3.Stop()
myCar3.Drive()
myCar3.Stop()
myCar3.Maintenance()
print(myCar3.TripsSinceMaintenance)
print(myCar3.make)
print(myCar3.model)
print(myCar3.year)
print(myCar3.weight)
