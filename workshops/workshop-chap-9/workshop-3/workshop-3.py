import csv

list=[['Звездные войны','Терминатор','Искусственный интелект'],['Дурак','Матильда','Левиафан'],['Люди в черном','Я - робот','Эволюция']]

with open('st.csv', 'w') as file:
    w=csv.writer(file,delimiter=',')
    w.writerow(list[0])
    w.writerow(list[1])
    w.writerow(list[2])
