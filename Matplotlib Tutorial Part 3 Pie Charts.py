from matplotlib import pyplot as plt

# slices = [60, 40, 30, 20]
# labels = ['Sixty', 'Forty', 'Extra1', 'Extra2']
# colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

# Top 15 Language Popularity
slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']

# Top 5 Language Popularity
people = [59219, 55466, 47544, 36443, 35917]
languages = ['Javascript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]

# plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'})
plt.pie(people, labels=languages, wedgeprops={'edgecolor': 'black'}, explode=explode, shadow=True,
        startangle=90, autopct='%1.1f%%')

plt.title('My Awesome Pie Chart')
plt.tight_layout()
plt.show()
