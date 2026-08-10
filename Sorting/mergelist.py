def mergelist(a,  b):

    n = len(a)
    m = len(b)
    i =0
    j=0
    res= []

    while i< n and j < m :
        if a[i] < b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1

    while i < n:
        res.append(a[i])
        i+=1

    while j < m:
        res.append(b[j])
        j+=1

    return res

a = [10, 15]
b = [5, 6, 6, 30, 40]

print(mergelist(a,b))
