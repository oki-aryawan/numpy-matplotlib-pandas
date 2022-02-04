import matplotlib.pyplot as plt

gdp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
life_expec = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

plt.plot(gdp, life_expec)
plt.xscale('log')
plt.xlabel('DGP')
plt.ylabel('Life Expectation')
plt.show()
