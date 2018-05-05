__author__ = 'Victor'

import threadpool, time


def getAverage(oneValueOfB):
    sum = 0
    number = pairsValue.index(oneValueOfB)
    listSum = listA[listSlice[number]:listSlice[number+1]]
    count = listSlice[number+1] - listSlice[number]
    for each in listSum:
        sum += each
    print sum/count,",",oneValueOfB

#pairs for testing
pairs1 = {}
pairs1 = pairs1.fromkeys(range(1000000), 1)

pairs2 = {}
pairs2 = pairs2.fromkeys(range(1000001,2000000), 2)

pairs3 = {}
pairs3 = pairs3.fromkeys(range(2000001,3000000), 3)

pairs4 = {}
pairs4 = pairs4.fromkeys(range(3000001,4000000), 4)

pairs5 = {}
pairs5 = pairs5.fromkeys(range(4000001,5000000), 5)

pairs6 = {}
pairs6 = pairs6.fromkeys(range(5000001,6000000), 6)

pairs7 = {}
pairs7 = pairs7.fromkeys(range(6000001,7000000), 7)

pairs8 = {}
pairs8 = pairs8.fromkeys(range(7000001,8000000), 8)

pairs9 = {}
pairs9 = pairs9.fromkeys(range(8000001,9000000), 9)

pairs = dict(pairs1.items() + pairs2.items() + pairs3.items() + pairs4.items()
  + pairs5.items() + pairs6.items() + pairs7.items() + pairs8.items() + pairs9.items())


listPairs = []
listA = []
listB = []

time_start = time.time()
#Put the pairs in a list
for key,value in pairs.items():
    listPairs.append((key,value))
#Ranking according to b
listPairs.sort(key=lambda k: k[1])

for item in listPairs:
    listA.append(item[0])
    listB.append(item[1])
time_end = time.time()
print time_end - time_start


#Duplicate removal of b
pairsValue = list(set(listB))
quantityOfB = len(pairsValue)

listSlice = []
for each in pairsValue:
    listSlice.append(listB.index(each))
listSlice.append(len(listA))

#For each b, setting up a thread with threadpool
time_start = time.time()
pool = threadpool.ThreadPool(quantityOfB)
requests = threadpool.makeRequests(getAverage, pairsValue)
[pool.putRequest(req) for req in requests]
pool.wait()
time_end = time.time()
print time_end-time_start
