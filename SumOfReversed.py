def sumOfReversed(arr):
    def reverse(num):
        newnum=[]
        newnum = list(str(num))
        newnum.reverse()
        for i in range(len(newnum)):
            if newnum[0]=='0':
                newnum.append(newnum.pop(0))
            else:
                break
        
        return int("".join(newnum))
    
    total = 0
    for j in range(len(arr)):
        total += reverse(arr[j])
    return total
