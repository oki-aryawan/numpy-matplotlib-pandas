import matplotlib.pyplot as plt

langs = ['C', 'C++', 'Pyhton', 'Java', 'PHP']
student = [22, 25, 32, 30, 15]
plt.bar(langs, student, 0.8)
plt.title("Computer Science 2022")
plt.xlabel("Programming Languages")
plt.ylabel("Number of Student")
plt.show()
