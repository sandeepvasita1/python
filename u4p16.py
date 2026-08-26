import matplotlib.pyplot as plt

years=[2020,2021,2022,2023,2024]
profits=[5000,6000,7000,8000,9000]

plt.plot(years,profits,marker='o')

plt.title('Company profit')
plt.xlabel('years')
plt.ylabel('profits')


plt.show()
