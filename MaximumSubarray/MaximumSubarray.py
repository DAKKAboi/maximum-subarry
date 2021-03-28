import bruteForceMaxSubarray as brute
import RecursiveMaxSubarray as recurse
import time
import RandomListGenerator


array = RandomListGenerator.listGen(100,-1000,1000)
print('list generated')

bruteTimeStart = time.time()

print(brute.bruteForceMax(array))

bruteTimeStop = time.time()
bruteTime = bruteTimeStop - bruteTimeStart

recurseTimeStart = time.time()

print (recurse.recursiveMax(array))

recurseTimeStop = time.time()
recurseTime = recurseTimeStop - recurseTimeStart

print('brute force time =  ' + str(bruteTime))
print('recursive time =    ' + str(recurseTime))

