import matplotlib.pyplot as plt

ages=[22,25,68,56,35,45,11,25,34,35,12,32,45]

ages_bins=[20,30,40,50,60,70]

plt.hist(ages,ages_bins,color='pink',edgecolor='blue')

plt.title('Employee age data')
plt.xlabel('Employee ages')
plt.ylabel('Ages of employee')


plt.show()
