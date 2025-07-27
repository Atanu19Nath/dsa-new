def maxsum_subarray(a,k):

    sum = 0
    maximum = float('-inf')
    i = 0
    j = 0

    while (j <len(a)):

        sum = sum + a[j]
        if j-i+1 < k:
            
            j = j + 1

        elif j-i+1 == k:

            maximum = max(maximum,sum)
            sum = sum - a[i]
            i = i + 1
            j = j + 1

    print(maximum)


a = [5,2,1,0,3]

maxsum_subarray(a,3)