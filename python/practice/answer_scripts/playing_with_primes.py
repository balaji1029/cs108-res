k_series_list=[2, 3, 5, 5, 7, 7] #This will store all the numbers of k series
#Initializing it with some numbers makes our work much easier

def isPrime(n):
    if n==1:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True

#This function updates the k_series_list to the new maximum index required.
def update_k_series_list(old_max, new_max):
    for pointer in range(old_max+1, new_max+1):
        if k_series_list[pointer-2]-k_series_list[pointer-3]==2:
            k_series_list.append(k_series_list[pointer-2])
        else:
            temp=k_series_list[pointer-2]+1
            #Begin from the next number of the previous index to find the next prime number
            while not isPrime(temp):
                temp+=1
            k_series_list.append(temp)

f=open("q1-input.txt", "r")
q=int(f.readline()) #Using f.readline() gives you text line by line starting from the very first.
#Don't forget to type cast to int.
max_query_till_now=6 #This keeps the maximum value of query till now (right now it is size of k series list)

for i in range(0, q):
    query=int(f.readline())
    if query>max_query_till_now:
        update_k_series_list(max_query_till_now, query)
        max_query_till_now=query
    print(k_series_list[query-1])

f.close()