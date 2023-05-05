import csv

with open('fyx_chinamoney.csv', 'r') as file:
    reader = csv.reader(file)

    data_list = []
    temp_list = []
    count = 0

    for row in reader:
        temp_list.append(row[0])
        count += 1
        if count == 80:
            count = 0
            data_list.append(temp_list.copy())
            temp_list = []

if temp_list:
    data_list.append(temp_list)

for i in data_list:
    print('代码数：', len(i), i)
