print("Enter Basic Pay: ")
basic=int(input())
gross=0
hra=0
da=0
if(basic<10000):
 hra=.5*basic
 da=.2*basic
else:
 hra=3500
 da=.6*basic
print("Gross Salary :",hra+da+basic)

