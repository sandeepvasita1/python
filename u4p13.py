import matplotlib.pyplot as plt

eid=[101,102,103,104]
eid2=[105,106,107,108]

dep1=[25000,30000,35000,40000]
dep2=[45000,50000,55000,60000]

plt.bar(eid,dep1)
plt.bar(eid2,dep2)


plt.title('Department salary')
plt.xlabel('Employee Id')
plt.ylabel('Salarys')

plt.legend('eid')
plt.show()
