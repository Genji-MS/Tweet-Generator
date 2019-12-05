
class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        √: Running time: O(n) Why and under what conditions?"""
        count = 0
        for item in self.items():
            count += 1
        return count
        # √: Loop through all nodes and count one for each

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        √: Running time: O(1) Why and under what conditions?"""
        new_node = Node(item)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        # √: Create new node to hold given item
        # √: Append node after tail, if it exists

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        √: Running time: O(1) Why and under what conditions?"""
        new_node = Node(item)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        # √: Create new node to hold given item
        # √: Prepend node before head, if it exists

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        √: Best case running time: O(n) Why and under what conditions?
        √: Worst case running time: O(n^2) Why and under what conditions?"""
        if self.head != None:
            for item in self.items():
                if quality(item) is True:
                    return item

        # √: Loop through all nodes to find item where quality(item) is True
        # √: Check if node's data satisfies given quality function

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        √: Best case running time: O(n) Why and under what conditions?
        √: Worst case running time: O(n) Why and under what conditions?"""
        found = False
        prev_item = None
        crnt_item = self.head        
        while crnt_item is not None:
            #print (f'prev_:{prev_item} current_:{current_item} search_:{item}')
            if crnt_item.data == item:
                found = True
                if self.head == crnt_item:
                    #move the value of our next item to the current head, if it exists
                    if crnt_item.next != None:
                        self.head = crnt_item.next
                    else:
                        self.head = None
                        self.tail = None
                else:
                    #rerouting around the current item
                    prev_item.next = crnt_item.next
                    if self.tail == crnt_item:
                        self.tail = prev_item
                break
            else:
                #remember the previous item, and seek the next one
                prev_item = crnt_item
                crnt_item = crnt_item.next
        if found == False:
            raise ValueError('Item not found: {}'.format(item))
        
        # √: Loop through all nodes to find one whose data matches given item
        # √: Update previous node to skip around node with matching data
        # √: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

    def enquene(self, item):
        self.append(item)
    
    def dequene(self):
        item = self.head.data
        self.delete(item)

    def iterate(self):
        pass

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting enquene:')
    for item in ['A', 'B', 'C']:
        print('enquene({!r})'.format(item))
        ll.enquene(item)
        print('list: {}'.format(ll))

    print('\nTesting dequene:')
    print('\nBefore: {}'.format(ll))
    ll.dequene()
    print('\nAfter: {}'.format(ll))
    print("\nenquene ('D')")
    ll.enquene('D')
    print('list: {}'.format(ll))

if __name__ == '__main__':
    test_linked_list()