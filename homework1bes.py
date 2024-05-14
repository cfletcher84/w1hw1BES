'''

1. For the message storage and retreival I would use a dictionary. I think that being able to assign the timestamp of the messages
as the keys and the messages as the actual values it would be easy to search for a specific message by timestamp. With the O(1) serach
complexity of indexing by key would make message retreival very efficient.

2. For real-time updates Websocket seems to be the way to go. It provides low latency because the connections reamin open rather than
random requests with polling or long polling. Websocket connections can be managed efficiently so there arent a bunch of idle connections
like with polling.

3. I think the for conversatons list a hash table/dictionary would work best. Again with the ability to search by key value pairs makes 
finding a specific thread simple by searching by 'name'. Filtering a dictionary can be done many different ways, we can use dictionary 
comprehension, the filter function, or even conditional statemtns and loops. 
'''

def simple_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)     

simple_sort([1,2,2,16,13,99,34,56,29])

def sorter(arr):
    arr.sort()
    print(arr)

sorter([1,2,2,16,13,99,34,56,29])


'''
1. Key opperations would be looping through the indexes, the nested for loop (which i belive is quadratic). The sorting and swapping
of the indexes will also add to our time complexity. There are better functions available to sort an array rather than this.

2. With this sort there is mulitple checks/swaps to get the list sorted. As this array grows it will become more and more complex
looping through every value and comparing/swapping when needed.

3. Using the .sort method seems like it would be the best way to sort an array. With the .sort method we are sorting within the 
existing list so no new lists are being created. 

'''