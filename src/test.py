from utils.Person import *

list = PersonList.from_csv('../data/data.csv')
print(list.stats)