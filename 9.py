class Vehicle:
    def __init__(self,Model,Make,Year,Weight,NeedsMaintenance,TripsSinceMaintenance):
        self.Model=Model
        self.Make=Make
        self.Year=Year
        self.Weight=Weight
        self.NeedsMaintenance=NeedsMaintenance
        self.TripsSinceMaintenance=TripsSinceMaintenance


    def setModel(self,Model):
        self.Model=Model

    def getModel(self):
        return self.Model

    def setMake(self,make):
        self.Make=make

    def getMake(self):
        return self.Make

    def setYear(self,year):
        self.Year=year

    def getYear(self):
        return self.Year

    def setWeight(self,weight):
        self.Weight=weight

    def getWeight(self):
        return self.Weight

    def Repair(self):
        self.TripsSinceMaintenance=0
        self.NeedsMaintenance=False
        print("Vehical is Repaired")

class Cars(Vehicle):
    def __init__(self,Model,Make,Year,Weight,NeedsMaintenance,TripsSinceMaintenance):
        Vehicle.__init__(self,Model,Make,Year,Weight,NeedsMaintenance,TripsSinceMaintenance)
        self.isDriving=False
    def drive(self):
        self.isDriving=True
        print("Driving",self.isDriving)
    def stop(self):
        self.isDriving=False
        self.TripsSinceMaintenance+=1
        print(self.TripsSinceMaintenance)

    def Maintenance(self):
        if(int(self.TripsSinceMaintenance)>10):
            self.NeedsMaintenance=True
            print("Vehicle needs Maintenance")
            print("Sending for Repairing")
            self.Repair()
        else:
            print("Vehicle does not need maintenance")


v1=Cars("car","volvo",1700,500,False,0)
v1.drive()
v1.stop()
v1.drive()
v1.stop()
v1.drive()
v1.stop()
v1.drive()
v1.stop()
v1.drive()
v1.stop()
v1.drive()
v1.stop()
v1.drive()
v1.stop()
v1.drive()
v1.stop()
v1.drive()
v1.stop()
v1.drive()
v1.stop()
v1.drive()
v1.stop()
v1.drive()
v1.stop()
v1.drive()
v1.stop()
v1.Maintenance()
