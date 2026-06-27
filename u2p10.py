Create a program name “employee.py” and implement the 
functions DA, HRA, PF, and ITAX. Create another program 
that uses the function of employee module and calculates gross 
and net salaries of an employee 
  
import employee

bsal=int(input("enter the basic salary"))

hra=employee.hra(bsal)
da=employee.da(bsal)

g_sal=bsal+hra+da

print(f"hra:{hra:.2f}")
print(f"da:{da:.2f}")
print(f"gross salary:{g_sal:.2f}")

pf=employee.pf(g_sal)
itax=employee.itax(g_sal)

n_sal=g_sal-(pf+itax)

print(f"pf:{pf:.2f}")
print(f"itax:{itax:.2f}")
print(f"n_sal:{n_sal:.2f}")
