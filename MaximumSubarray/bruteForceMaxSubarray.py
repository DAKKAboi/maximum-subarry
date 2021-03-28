def bruteForceMax(array):
    length = len(array)

    i = 0
    j = 0
    maxSubLocation = [0,0]
    maxSubValue = 0
    tempSubValue = 0
    
    while i <= (length - 1):
      
        j = i
        tempSubValue = 0

        while j <= (length - 1):
            
            tempSubValue = tempSubValue + array[j]

            if tempSubValue > maxSubValue:
                maxSubValue = tempSubValue
                maxSubLocation = [i,j]
            j = j + 1
        i = i + 1

    return [maxSubValue, maxSubLocation]

