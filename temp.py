import random
import csv

iris_data = ['setosa', 'versicolor', 'virginica']

file_1 = []

for i in range(100): file_1.append(iris_data[random.randint(0,2)])

with open("file_1.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(file_1)

with open('file_1.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    print(data)

file_2 = []

for i in range(100): file_2.append(iris_data[random.randint(0,2)])

with open("file_2.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(file_2)