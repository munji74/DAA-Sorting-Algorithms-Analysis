import time

#function that does the sorting
def insertion(list):
    for i in range(1, len(list)):   #each unsorted element at i, the value at that index is stored in key
        key = list[i] #starts at index 1 because it assumes the first value is already sorted
        j = i - 1

        while j >= 0 and key < list[j]: 
            #check if j is greater than or equal to 0 and if key is less than the element at index j
            list[j + 1] = list[j]
            j -= 1 # key needs to be moved to the left to its correct position.

        list[j + 1] = key

list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 73, 21, 34, 25, 95, 20 , 34 , 45, 53, 58, 89]

#time taken for the function to work
start = time.time()
insertion(list) #call the function
end = time.time()

print("Sorted array:", list)
print(f"Time taken: {end - start:.10f} s")
