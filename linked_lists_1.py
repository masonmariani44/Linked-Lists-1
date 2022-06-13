'''
Author: Mason Mariani

        Given linked lists, the program has the ability to check if
        it is sorted, sum the values within the list, pair two lists
        together within a tuple in two different ways, and print this
        tuple pairing.
'''

from list_node import *

def is_sorted(head):
    '''
    Takes the linked list object 'head' and uses it within the function.
    Loops through each value within the list and checks to see if the value
    that comes after it is greater than the current value in the iteration.
    If this is true for the entire list, the function returns true, and if not,
    it returns false.
    '''
    # Check to see if the list is None, return None if true
    if head is None:
        return None
    cur = head
    next_node = cur.next
    # Begin the loop through the linked list
    while next_node is not None:
        # Check to see if the next value is greater than the current value
        if next_node.val < cur.val:
            return False
        cur = next_node
        next_node = next_node.next
    # Retuens true if the above if statement never ran
    return True

def list_sum(head):
    '''
    Given the linked list object 'head', the function will iterate through
    each of its nodes to return the total sum of each interger within the
    list. Assumes each value is an interger. If head is None, the function
    returns a value of 0.
    '''
    # Check to see if the head is None, returns 0 if it is
    if head is None:
        return 0
    # Initialize total with the head value
    total = head.val
    cur = head.next
    # Begin iterating through the linked list, adding each cur to
    # the total variable
    while cur is not None:
        total += int(cur.val)
        cur = cur.next
    return total

def pair(list1, list2):
    '''
    Given two linked list objects, list1 and list2, the function will
    iterate through each value in each list and pair them together in
    the order in which they are in their respective lists. For example,
    each "first" node within the list is placed in a tuple together and
    added to the new returned list, and so on for the second, third and
    entirety of the linked list.
    '''
    # Check to determine if either list 1 or list2 is None
    if list1 is None or list2 is None:
        return None
    cur1 = list1
    cur2 = list2
    # Initialize the new linked list at the head of list1 and list2
    new_tuple = (cur1.val, cur2.val)
    new_tuple = str(new_tuple)
    new_list_head = ListNode(new_tuple)
    # next list1 and list2 values
    cur1 = cur1.next
    cur2 = cur2.next
    # create list which will be appended to
    new_list = new_list_head
    # start iteration over cur1 and cur2
    while cur1 is not None and cur2 is not None:
        new_node = (cur1.val, cur2.val)
        new_node = str(new_node)
        new_list.next = ListNode(new_node)
        new_list = new_list.next
        cur1 = cur1.next
        cur2 = cur2.next
    # return the origional head of the new list
    return new_list_head

def print_pair_partial(list1, list2):
    '''
    Iterates through the given lists: list1 and list2 and prints out
    each value in order and with accordance to the other list's values,
    similar to how the pair function combines each respective node together
    '''
    cur1 = list1
    cur2 = list2
    # iterate through list1 and list2
    while cur1 is not None or cur2 is not None:
        # checking for if a value reaches none to do a special print statement,
        # as the function continues even when one linked list has reached
        # its end
        if cur1 is None:
            print('1: ' + 'None' + '   2: ' + str(cur2.val))
            cur2 = cur2.next
        elif cur2 is None:
            print('1: ' + str(cur1.val) + '   2: ' + 'None')
            cur1 = cur1.next
        else:
            print('1: ' + str(cur1.val) + '   2: ' + str(cur2.val))
            cur1 = cur1.next
            cur2 = cur2.next

def pair_partial(list1, list2):
    '''
    list1 and list2 are the given paramaters, and will be used to iterate over
    and pair their values together, similar to how the pair function operates.
    However, similar to print_pair_partial, the function will continue to add
    new tuples, even when one linked list has reached its end by having a tuple
    be added with None in the place of the completed linked list iteration.
    '''
    if list1 is None and list2 is None:
        return None
    cur1 = list1
    cur2 = list2
    # initializing the new list that will be created and returned
    # check to see if any of the first values are None, and to create
    # the first head tuple accordingly
    if cur1 is None:
        head_tuple = (None, cur2.val)
    elif cur2 is None:
        head_tuple = (cur1.val, None)
    else:
        head_tuple = (cur1.val, cur2.val)
    head_tuple = str(head_tuple)
    new_list_head = ListNode(head_tuple)
    if cur1 is not None:
        cur1 = cur1.next
    if cur2 is not None:
        cur2 = cur2.next
    new_list = new_list_head
    # begin the iteration through list1 and list2
    while cur1 is not None or cur2 is not None:
        # adds tuples with values containing None when a list has
        # reached its end
        if cur1 is None:
            new_node = (None, cur2.val)
            new_node = str(new_node)
            new_list.next = ListNode(new_node)
            cur2 = cur2.next
        elif cur2 is None:
            new_node = (cur1.val, None)
            new_node = str(new_node)
            new_list.next = ListNode(new_node)
            cur1 = cur1.next
        else:
            new_node = (cur1.val, cur2.val)
            new_node = str(new_node)
            new_list.next = ListNode(new_node)
            cur1 = cur1.next
            cur2 = cur2.next
        # iterate new_list
        new_list = new_list.next
    return new_list_head
