#Jebel Macias
#Lab 5- Heap
#11/27/2018
class Heap:
    def __init__(self):
        self.heap_array = []

    #The insert function appends a new element
    #to the end of the list and then sorts
    #the heap
    def insert(self, k):
        self.heap_array.append(k)
        self.sort_list()

    #The extract min function takes the
    #first element in the heap, and
    #replaces it with the last element in
    #the heap.
    def extract_min(self):
        if self.is_empty():
            return None
        min_elem = self.heap_array[0]
        self.heap_array[0] = self.heap_array[len(self.heap_array)-1]
        self.heap_array.pop()
        self.sort_list()
        return min_elem

    #Return true if heap is empty
    def is_empty(self):
        return len(self.heap_array) == 0

    #Sorts the heap by replacing parent
    #nodes with children child is greater
    #than the parent node
    def sort_list(self):
        sorted = True
        while sorted == True:
            swapped = False
            for i in range(1, len(self.heap_array)):
                if self.heap_array[i] < self.heap_array[(i-1)//2]:
                    temp = self.heap_array[(i-1)//2]
                    self.heap_array[(i-1)//2] = self.heap_array[i]
                    self.heap_array[i] = temp
                    swapped = True
            if swapped == False:
                sorted = False

    #Prints the contents of the heap
    def print_list(self):
        print(self.heap_array)
        print()


def read_from_file(file_name):
    """The fucntion read_from_file takes any given
    file containing a list of words, and inserts each
    word into a new heap.
    """
    new_heap = Heap()
    #try:
    with open(file_name, 'r') as file:
      for line in file:
        list_word = line.split(",")
        for word in list_word:
          new_heap.insert(word)

    #except Exception as e:
    #    print("The file you input does not exist, try a different file name")
    #    return False
    return new_heap

def main():

    heap = False
    while heap ==False:
        userAnswer1 = input("-What is the name of the file containing the list of words?\n")
        heap = read_from_file(userAnswer1)

    print("--The heap generated--")
    heap.print_list()

    on = True
    while on:
        userAnswer2 = input("-Would you like to extract the minium from the heap?\n")
        if userAnswer2 == "y" or userAnswer2 =="yes":
            minimum_in_heap = heap.extract_min()
            if minimum_in_heap != None:
              print("--The min value in the heap is: " + minimum_in_heap + "--")
              print("--The new heap--")
              heap.print_list()
            else:
              print("The heap that is being extracted from is empty.")
              on = False
        else:
          on = False

main()
