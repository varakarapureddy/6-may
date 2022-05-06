#program to print employee fields(empno,empname,empdesign,empdoj,empsalary,empcity) using dictionary method.
empname={1:['vara'],2:['nani'],3:['seshu']}
empdesign={1:['web developer'],2:['developer'],3:['code developer']}
empdoj={1:['sep 4'],2:['oct 25'],3:['aug 3']}
empsalary={1:[26000],2:[26000],3:[26000]}
empplace={1:['pithapuram'],2:['chandraplam'],3:['chandraplam']}
n=int(input("enter employee no:"))
print("name of the employee:",empname[n][0])
print("Design of the emplolyee:",empdesign[n][0])
print("Employee date of joining:",empdoj[n][0])
print("Employee salary:",empsalary[n][0])
print("Place of the Employee:",empplace[n][0])
