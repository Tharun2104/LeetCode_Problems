# Creating a ListNode to use
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Linkedlist:
    def __init__(self,*values):
        self.head = None
        for i in values[::-1]:
            self.insert_at_beginning(i)
    def insert_at_beginning(self,value):
        current_node = self.head
        new_node = ListNode(value)
        new_node.next = current_node
        self.head = new_node
    def insert_at_the_end(self,value):
        current_node = self.head
        new_node = ListNode(value)
        if(len(self) == 0):
            new_node.next = current_node
            self.head = new_node
        else:
            while current_node:
                if not current_node.next:
                    current_node.next = new_node
                    new_node.next = None
                    break
                else:
                   current_node = current_node.next
    def insert_at_index(self,index,value):
        current_node = self.head
        new_node = ListNode(value)
        current_node_index = 0
        if(index == 0):
            # insert_at_beginning(value)
            new_node.next = current_node
            self.head = new_node
        elif(1<=index<len(self)):
            while current_node:
                if(index == current_node_index+1):
                    next_node = current_node.next
                    current_node.next =new_node
                    new_node.next = next_node
                    break
                else:
                    current_node = current_node.next
                    current_node_index +=1
    def delete_at_begining(self):
        self.head = self.head.next
    def delete_at_end(self):
        current_node = self.head
        while current_node:
            if not current_node.next.next:
                current_node.next = None
                break
            else:
                current_node = current_node.next
    def delete_a_value(self,value):
        current_node = self.head
        previous_node = None
        while current_node:
            if(current_node.val == value):
                if(previous_node == None):
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
                return current_node.val
            else:
                previous_node = current_node
                current_node = current_node.next
        return -1
    def search_value(self, value):
        current_node = self.head
        current_node_index = 0
        while current_node:
            if(current_node.val == value):
                return current_node_index
            else:
                current_node = current_node.next
                current_node_index +=1
        return -1
    def __len__(self):
        current_node = self.head
        count = 0
        while (current_node):
            count +=1
            current_node = current_node.next
        return count

    def __repr__(self):
        value = []
        current_node = self.head
        while current_node:
            value.append(str(current_node.val))
            current_node = current_node.next
        # value.append(None)
        if value:
            value.append(str(None))
            return "->".join(value)
        else:
            return "Linked list is empty"