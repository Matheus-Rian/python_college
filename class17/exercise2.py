tupleTimes = ('SP', 'CP', 'SPT', 'LLL', 'FUR', 'CRZ', 'INTZ', 'PAIN', 'RDP', 'KRU')

print(tupleTimes[0:5])
print(tupleTimes[6:10])

listTimes = list(tupleTimes)
listTimes.sort()
print(listTimes)
print(tupleTimes.index('SP'))
