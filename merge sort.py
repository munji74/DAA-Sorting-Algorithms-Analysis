import time

#function that does the sorting

def merge(list):
    if len(list) > 1:
        middle = len(list) // 2 # if the elements in the list are more than 1 divide the list into 2 parts
        left = list[:middle]  #store the elements to the left of the middle value
        right = list[middle:] #store the elements to the right of the middle value

        #recursively call the merge function to divide the list into saller sub lists
        merge(left)
        merge(right)
        #merging continues recursively, combining smaller sorted lists into larger sorted lists
        
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1         
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 73, 21, 34, 25, 95, 20 , 34 , 45, 53, 58, 89]

#time taken for the function to work
start = time.time() 
merge(list) #call the function
end = time.time()

print("Sorted list:", list)
print(f"Time: {end - start:.10f} s")
