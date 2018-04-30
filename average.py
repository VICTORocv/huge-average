__author__ = 'Victor'

import threadpool, time

def getAverage(oneValueOfB):
    count = 0
    sum = 0
    for k, v in pairs.items():
        if v == oneValueOfB:
            count += 1
            sum += k
    print sum/count,",",oneValueOfB


#pairs for testing
pairs1 = {}
pairs1 = pairs1.fromkeys(range(10000000), 1)

pairs2 = {}
pairs2 = pairs2.fromkeys(range(10000001,20000000), 2)

pairs3 = {}
pairs3 = pairs3.fromkeys(range(20000001,30000000), 3)

pairs4 = {}
pairs4 = pairs4.fromkeys(range(30000001,40000000), 4)

pairs5 = {}
pairs5 = pairs5.fromkeys(range(40000001,50000000), 5)

pairs = dict(pairs1.items() + pairs2.items() + pairs3.items() + pairs4.items() + pairs5.items())


#Duplicate removal of b
pairsValues = pairs.values()
pairsValue = list(set(pairsValues))
quantityOfB = len(pairsValue)

time_start = time.time()
#For each b, setting up a thread with threadpool
pool = threadpool.ThreadPool(quantityOfB)
requests = threadpool.makeRequests(getAverage, pairsValue)
[pool.putRequest(req) for req in requests]
pool.wait()
time_end = time.time()
print time_end-time_start
