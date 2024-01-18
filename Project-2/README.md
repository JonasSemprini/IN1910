# H20_project2_tovut_jonassna
Project 2 for tovut (tovut@mail.uio.no) and jonassna (jonassna@mail.uio.no)

### Tovut command for compile
I used makefile to compile and run my code. The code for makefile is as follows:
LinkedList: LinkedList.cpp
	c++ -std=c++11 -Wall $< -o $@
  
And similar for the rest of the files. Then in terminal i wrote
$ make LinkedList

$./LinkedList

### jonassna command for compile
* c++ -std=c++11 -Wall array_list.cpp -o array_list
* c++ -std=c++11 -Wall linked_list.cpp -o linked_list
* c++ -std=c++11 -Wall circular_linked_list.cpp -o circular_linked_list

### List of exercises we managed to run
* All excercises in project were properly ran trough compilation. (1, 2, 4)

#### Exercise 4g)
With n = 68 and k = 7, we predict the location for survival will be seat 68.

# Time Complexity Analysis (Big Oh)

### Get element i by index
* Dynamic array: O(1). The elements of the ArrayList are indexed by giving the head pointer an initially known value, and since the values are sequentiel in memory the time complexity is always constant.
* LinkedList: O(N). The elements of a linked list are indexed by running down the list, element by element (since the pointer moves one step ahead for every time step). This results in an average number of operations linear with the size of the list.

### Insert at front
* Dynamic array: O(N). When inserting a value in the front of a Dynamic Array, it must be certain that there exists free memory ahead of our array. To ensure this requirement the whole array must be re-allocated such that every element together with the newly added first element is stored in memory.
* LinkedList: O(1). In the context of a linked list the operation of inserting an element in front is only based of the head-pointers position. When adding an arbitrary element at the front of the list, the current head pointer must be shifted back to the newly initiated pointer, pointing at the first element of the list. The time complexity of this operation remains constant regardless of list length.


### Insert at back (append)
* Dynamic array: O(n)^* .Amortized cost seeing as the process is constant in time over an average amount of numerous operations. We index ourselves to the end of the affirmed value in the array and append. We grow capacity if there is no capacity left, which requires re-allocating of the list. Therefore there will either be a single operation or multiple operations. We expect worst-case scenario, thus time complexity is linear . 

* LinkedList: O(1). For LinkedList, we can access the tail of the list. We do not need to run through all the nodes. After we have obtained the last node, we designate it as the new tail with few operations. The time complexity is minuscule considering a large amount of data will need the same amount of operations as a small amount of data, thus the time complexity remains constant regardless of list length.

### Insert into middle of list
* Dynamic array: O(n) . We will have to re-allocate the data before and after the index we want to insert. The time complexity is linear

* Linked List: O(n) . For linked list, we need to obtain the node before the wanted noted and the process reqiuers going through every node before. After that a few operations will give the index its new value. The time complexity is linear.  

### Remove element from front
* Dynamic array: O(n). When we wish to remove at the front, we will have to move every element in the list an index down. We have to go through the entire list and the time complexity is linear for all types of lists. 

* LinkedList: O(1). For LinkedList we can set the second element in the list as head with few operations. Hence every other node is untouched. Removing from front with LinkedList is not time consuming at all and its time complexity remains constant.  


### Remove element from back
* Dynamic array: O(1). When we wish to remove from the back, we can shrink the size of the list by one. Removing the last element is not time-consuming at all for a Dynamic Array, hence its time complexity is constant.

* LinkedList: O(n). For LinkedList we have to get the penultimate node by going through every other node before. When we have reached the penultimate node we can set that node to tail and decrement the size. Removing the last element can be time-consuming for LinkedList and its time complexity is linear.

### Remove element from middle
* Dynamic array: O(n). When we wish to remove from the middle, we will have to rewrite the elements before and after the chosen index onto a new array, delete the contents in the original array and then rename the copied as the original. Re-allocating can be time-consuming and its time complexity is linear.

* LinkedList: O(n). For LinkedList we have to get the node before the chosen node by going through every other node before. When obtained, we can go through operations and delete the chosen node. Removing the middle node can be time-consuming and its time complexity is linear.

### Print method 
* Dynamic array: O(n). When printing out the elements in a single line, we have to go through each element in the list. For larger arrays the time complexity is linear and cost accumulates with larger lists.

* LinkedList: O(n). The same goes for LinkedList. We will have to go through each node to print them and larger arrays cost more, hence time complexity is linear. 
