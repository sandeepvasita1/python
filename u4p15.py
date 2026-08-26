import matplotlib.pyplot as plt

dept=['HR','IT','FINANCE','MARKETING','Sales']

ecount=[10,25,31,5,20]

plt.pie(ecount,labels=dept,autopct='%1.1f%%',startangle=90)

plt.title('Department on of employee')

plt.show()
