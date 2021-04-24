import statistics
import pandas as pd
import random
import datetime
begin_time = datetime.datetime.now()
masterList = []
i =0
for i in range(1000000):
    i = 0
    # list = [105,90,]
    for i in range(15):
        n = random.randint(90,105)
        print(n)
        masterList.append(n)
        # masterList.append(masterList)
    # print(list)
    # print(statistics.mean(list))
print(masterList)
print(statistics.mean(masterList))
print(datetime.datetime.now() - begin_time)