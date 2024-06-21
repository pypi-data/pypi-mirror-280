def bi_search(val,left,right,arr):
    while left<right:
        mid = (left+right+1)//2
        if arr[mid]<=val:
            left = mid
        else:
            right = mid-1
    return right