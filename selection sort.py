import time

#function that does the sorting
def selection(list):
    n = len(list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]

list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 73, 21 , 34 , 25, 95, 20 ]

#time taken as the function does the sorting
start = time.time()
selection(list) #call the function
end = time.time()

print("Sorted array:", list)
print(f"Time taken: {end - start:.10f} seconds")
