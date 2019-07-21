class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def _up_heapify(self):
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]


'''
# My solution
class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def insert(self, data):
        """
        Insert `data` into the heap
        """
        self.cbt[self.next_index] = data
        self.next_index += 1
        # to get the parents:
        current_position = self.next_index

        if current_position > 0:

            parent_position = (current_position - 1) // 2

            current_value = self.cbt[current_position]
            parent_value = self.cbt[parent_position]

            # program swap
            while current_value > parent_value:
                self.cbt[current_position] = parent_value
                self.cbt[parent_position] = current_value

                current_position = parent_position
                parent_position = (current_position - 1) // 2
                current_value = self.cbt[current_position]
                parent_value = self.cbt[parent_position]
'''
