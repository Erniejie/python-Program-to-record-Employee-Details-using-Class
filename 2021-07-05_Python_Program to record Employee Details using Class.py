#Program to record Employee Details using Class
class Employee:
    count = 0
    def __init__(self,Empname,Position,salary):
        self.Empname=Empname
        self.Position=Position
        self.salary = salary
        Employee.count+=1

    def TotalEmpl(self):
        print("There are %d employee" %Employee.count)
    def showDetails(self):
        print("Employee Name:",self.Empname, ",Designation:",self.Position,",Salary:",self.salary)

data1=Employee("Yijie","Manager",50000)
data2=Employee("Shen Fan","Production Manager",25000)
data3=Employee("Pamda","Engineer",80000)
data4=Employee("Yijie","Architect",30000)


data4.TotalEmpl()
print("Details of All Employees:")
data1.showDetails()
data2.showDetails()
data3.showDetails()
data4.showDetails()
        
        
