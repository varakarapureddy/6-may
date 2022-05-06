#program to print student fields (sno,sname,gender,group,result) using dictionary method.
s={1:['vara','male','bca',9.0],2:['nani','male','bca',9.0],3:['seshu','male','bca',9.0]}
n=int(input("enter student no:"))
print("name of the student:",s[n][0])
print("Gender is:",s[n][1])
print("Group of the student:",s[n][2])
print("Result of the student:",s[n][3])
