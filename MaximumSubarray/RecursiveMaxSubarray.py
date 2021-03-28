import math

def recursiveMax(array):

    def findMaxCrossSubarray(array, low, mid, high):
        leftSum = -math.inf
        sum = 0

        i = mid
        while i >= low:
            sum = sum + array[i]
            if sum > leftSum:
                leftSum = sum
                maxLeft = i
            i = i - 1

        rightSum = -math.inf
        sum = 0

        j = mid + 1
        while j <= high:
            sum = sum + array[j]
            if sum > rightSum:
                rightSum = sum
                maxRight = j
            j = j + 1

        return [(leftSum + rightSum), [maxLeft, maxRight]]
    
    def findMaxSubarray(array, low, high):
        if high == low:
            return array[low], [low, high]
        else:
            mid = math.floor((low + high)/2)
            
            [leftSum, [leftLow, leftHigh]] = findMaxSubarray(array, low, mid)
            [rightSum, [rightLow, rightHigh]] = findMaxSubarray(array, mid + 1, high)
            [crossSum, [crossLow, crossHigh]] = findMaxCrossSubarray(array, low, mid, high)

            if leftSum >= rightSum and leftSum >= crossSum:
                return [leftSum, [leftLow, leftHigh]]
            elif rightSum >= leftSum and rightSum >= crossSum:
                return [rightSum, [rightLow, rightHigh]]
            else:
                return [crossSum, [crossLow, crossHigh]]

    return findMaxSubarray(array, 0, len(array) - 1)
