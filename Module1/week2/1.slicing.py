def max_kernel(num_list,k):
    
    output = []
    for i in range(len(num_list)):
        if len(output)==len(num_list)-k+1:
            break
        num_list1 = num_list.copy()
        a = num_list1[i:i+k]
        b = max(a)
        del num_list1[i:i+k]
        num_list1.insert(i, a)
        output.append(b)
        
    return output

num_list = [3,4 ,5 ,1 ,-44 ,5,10,12,33,1]
k = 3
assert max_kernel(num_list,k) == [5, 5, 5, 5, 10, 12, 33, 33]
result = max_kernel(num_list ,k)
print(result)

