print('\n\t Applications of Search Algorithms\n\t #Section 3')

List = [10, 4, 1, 15, -3]

orderedList1 = sorted(List)
orderedList2 = List.sort()

print(
f'''
 ——————————
 List = {List}
 orderedList1 = {orderedList1}
 orderedList2 = {orderedList2}
 List = {List}
 ——————————''')

# //

List = [7, 4]

if List[0] > List[1]:
    aux, List[1] = List[1], List[0]
    List[0] = aux

print(f'\n ——————————\n {List}\n ——————————')

# //

List = [5, -1]

if List[0] > List[1]:
    List[0], List[1] = List[1], List[0]

print(f'\n ——————————\n {List}\n ——————————')

# //

'''
 1. Complexity O(N²): in this group are the selection sort, bubble sort and insertion sort algorithms. These algorithms are slow for sorting large lists, but are more intuitive to understand and have simpler coding.
 2. Complexity O(N log N): from this group, we will study the merge sort and quick sort algorithms. Such algorithms have superior performance, but are a little more complex to implement.
'''

# // SelectionSort

'''
 • Iteration 1: Goes through the entire list, looking for the smallest value to occupy position 0.
 • Iteration 2: starting from position 1, it goes through the entire list, looking for the smallest value to occupy position 1.
 • Iteration 3: starting from position 2, it goes through the entire list, looking for the smallest value to occupy position 2.
 • This process is repeated N-1 times, where N is the length of the list.
'''

# //

def executSelectionSort(List):
    n = len(List)
    
    for i in range(0, n):
        lowerIndex = i
        for j in range(i + 1, n):
            if List[j] < List[lowerIndex]:
                lowerIndex = j
        List[i], List[lowerIndex] = List[lowerIndex], List[i]

    return List

List = [10, 9, 5, 8, 11, -1, 3]
print(f'\n ——————————\n {executSelectionSort(List)}\n ——————————')

# //

def executSelectionSort2(List):
    orderedList = []

    while List:
        Min = min(List)
        orderedList.append(Min)
        List.remove(Min)

    return orderedList

List = [10, 9, 5, 8, 11, -1, 3]
print(f'\n ——————————\n {executSelectionSort2(List)}\n ——————————')

# // BubbleSort

'''
 • Iteration 1: selects the value at position 0 and compares it with its neighbor – if it is smaller, there is an exchange; if not, select the next one and compare, repeating the process.
 • Iteration 2: selects the value at position 0 and compares it with its neighbor, if it is a smaller change, otherwise it selects the next one and compares it, repeating the process.
 • Iteration N - 1: selects the value at position 0 and compares it with its neighbor – if it is smaller, there is an exchange; if not, select the next one and compare, repeating the process.
'''

# //

def executBubbleSort(List):
    n = len(List)

    for i in range(n - 1):
        for j in range(n - 1):
            if List[j] > List[j + 1]:
                List[j], List[j + 1] = List[j + 1], List[j]

    return List

List = [10, 9, 5, 8, 11, -1, 3]
print(f'\n ——————————\n {executBubbleSort(List)}\n ——————————')

# // InsertionSort

'''
 • Start: it is assumed that the list has a single value and, consequently, is ordered.
 • Iteration 1: It is assumed that a new value needs to be inserted into the list; in this case, it is compared with the existing value to see if a position change needs to be made.
 • Iteration 2: It is assumed that a new value needs to be inserted into the list; in this case, it is compared with the already existing values ​​to see if position changes need to be made.
 • Iteration N: it is assumed that a new value needs to be inserted into the list; in this case, it is compared with all existing values ​​(from the beginning) to see if any position changes need to be made.
'''

# //

def executInsertionSort(List):
    n = len(List)
    for i in range(1, n):
        insertValue = List[i]
        j = i - 1
        
        while j >= 0 and List[j] > insertValue:
            List[j + 1] = List[j]
            j -= 1
        List[j + 1] = insertValue
    
    return List

List = [10, 9, 5, 8, 11, -1, 3]
print(f'\n ——————————\n {executInsertionSort(List)}\n ——————————')

# // MergeSort

'''
 • Division step:
    1. Based on the original list, find the middle and separate it into two lists: left_1 and right_2.
    2. Based on left_1 sublist, if the amount of elements is greater than 1, find the middle and separate it into two lists: left_1_1 and right_1_1.
    3. Based on the left_1_1 sublist, if the number of elements is greater than 1, find the middle and separate it into two lists: left_1_2 and right_1_2.
    4. Repeat the process until you find a list with length 1.
    5. Call the merge step.
    6. Repeat the process for all sublists.

 • Merge step:
    1. Given two lists, each of which contains 1 value – to sort, simply compare these values ​​and swap, generating a sublist with two sorted values.
    2. Given two lists, each of which contains 2 values ​​– to order, just choose the smallest value in each one and generate a sublist with four ordered values.
    3. Repeat the process of comparing and merging the values ​​until you reach the original list, now sorted.
'''

# //

def executMergeSort(List):
    if len(List) <= 1: return List
    else:
        middle = len(List) // 2
        left = executMergeSort(List[:middle])
        right = executMergeSort(List[middle:])

        return executMerge(left, right)
    
def executMerge(left, right):
    subOrderedList = []
    topLeft, topRight = 0, 0
    
    while topLeft < len(left) and topRight < len(right):
        if left[topLeft] <= right[topRight]:
            subOrderedList.append(left[topLeft])
            topLeft += 1
        else:
            subOrderedList.append(right[topRight])
            topRight += 1

    subOrderedList += left[topLeft:]
    subOrderedList += right[topRight:]

    return subOrderedList

List = [10, 9, 5, 8, 11, -1, 3]
print(f'\n ——————————\n {executMergeSort(List)}\n ——————————')

# // QuickSort

'''
 1. First iteration: the original list will be broken through a value called a pivot. After the break, the values ​​that are smaller than the pivot should be on its left and the larger ones on its right. The pivot is inserted at the proper location, swapping the position with the current value.
 2. Second iteration: Now there are two lists, the right and left of the pivot. Again, two new pivots are chosen and the same process is carried out, placing the smaller ones on the right and the larger ones on the left. In the end, the new pivots occupy their correct positions.
 3. Third iteration: looking at the two new sublists (right and left), the process of choosing pivots and separating is repeated.
 4. In the last iteration, the list will be ordered, as a result of the previous steps.
'''

# //

def executQuickSort(List, start, end):
    if start < end:
        pivot = executePartition(List, start, end)
        executQuickSort(List, start, pivot - 1)
        executQuickSort(List, pivot + 1, end)

    return List
        
def executePartition(List, start, end):
    pivot = List[end]
    left = start

    for right in range(start, end):
        if List[right] <= pivot:
            List[right], List[left] = List[left], List[right]
            left += 1

    List[left], List[end] = List[end], List[left]
    return left

List = [10, 9, 5, 8, 11, -1, 3]
print(f'\n ——————————\n {executQuickSort(List, start = 0, end = len(List) - 1)}\n ——————————')

# //

def executQuickSort2(List):
    if len(List) <= 1: return List

    pivot = List[0]
    equals  = [value for value in List if value == pivot]
    minors = [value for value in List if value <  pivot]
    bigger = [value for value in List if value >  pivot]

    return executQuickSort2(minors) + equals + executQuickSort2(bigger)

List = [10, 9, 5, 8, 11, -1, 3]
print(f'\n ——————————\n {executQuickSort2(List)}\n ——————————')