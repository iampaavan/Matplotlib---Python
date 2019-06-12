from matplotlib import pyplot as plt
import csv
from collections import Counter

with open('data.csv', 'r') as file_reader:
    csv_reader = csv.DictReader(file_reader)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(";"))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title('Most Popular Languages')
plt.ylabel('Programming Language')
plt.xlabel('Number of people who use')

plt.tight_layout()
# plt.savefig('thirdplot.png')
plt.show()
