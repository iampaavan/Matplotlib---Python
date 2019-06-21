import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data-6.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# figure, (axis1, axis2) = plt.subplots(nrows=2, ncols=1, sharex=True)
figure1, axis1 = plt.subplots()
figure2, axis2 = plt.subplots()
axis1.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')

axis2.plot(ages, py_salaries, label='Python')
axis2.plot(ages, js_salaries, label='JavaScript')


axis1.legend()
axis1.set_title('Median Salary (USD) by Age')
# axis1.set_xlabel('Ages')
axis1.set_ylabel('Median Salary (USD)')

axis2.legend()
# axis2.set_title('Median Salary (USD) by Age')
axis2.set_xlabel('Ages')
axis2.set_ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()

figure1.savefig('third.png')
figure2.savefig('fourth.png')
