def minsum_subarray(a,k):

    sum = 0
    minimum = float('inf')
    i = 0
    j = 0

    while (j <len(a)):

        sum = sum + a[j]
        if j-i+1 < k:
            
            j = j + 1

        elif j-i+1 == k:

            minimum = min(minimum,sum)
            sum = sum - a[i]
            i = i + 1
            j = j + 1

    print(minimum)


a = [5,2,1,0,3]

minsum_subarray(a,3)