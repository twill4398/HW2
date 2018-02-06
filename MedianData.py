# Code is Tyler Will's, recycled from a similar problem last semester in CSE331
import heapq


class MedianHeap:

    def __init__(self):
        '''
        @pre: constructor was properly called 
        @post: 4 values are initilized 
        - minH  an array that represents a heap of elements
        - maxH an array that represents a heap of elements 
        - minL  size/length of minH
        - maxL = size/length of maxH
        '''
        self.minH = []
        self.maxH = []
        self.minL = 0
        self.maxL = 0


    def get_median(self):
        '''
        @pre: there are 2 present heaps 
        @post: Known median post operation   
        returns the median value 
        '''
        if self.maxL > self.minL:
            med = self.maxH[0]
        elif self.minL > self.maxL:
            med = self.minH[0]
        else:
            med = (self.minH[0] + self.maxH[0])/2
            
        return int(med) if (med % 1 == 0) else med


    def rebalance_heaps(self):
        '''
        @pre: two heaps that differ by more than 1 in size
        @post: two heaps that differ by only one in size, obtained by shuffling elements
        '''

        if self.minL - self.maxL > 1:
            self.maxH.append(heapq.heappop(self.minH))
            self.maxL += 1
            self.minL += -1
            heapq._siftdown_max(self.maxH, 0, self.maxL - 1)

        elif self.maxL - self.minL > 1:
            heapq.heappush(self.minH, heapq._heappop_max(self.maxH))
            self.maxL += -1
            self.minL += 1

        assert abs(self.maxL - self.minL) <= 1, "Not balanced!"


    def heap_push(self, val):
        '''
        @pre: two balanced heaps
        @post: two heaps with val added in the right spot, balanced
        :param val: the value to be added to the median heap
        adds the value to the proper heap
        '''

        # If we're adding to the max heap
        if self.maxL == 0 or val < self.maxH[0]:
            self.maxH.append(val)
            self.maxL += 1
            heapq._siftdown_max(self.maxH, 0, self.maxL - 1)

        # Min heap is simpler
        else:
            heapq.heappush(self.minH, val)
            self.minL += 1

        self.rebalance_heaps()
        print(self.get_median())
        



    def heap_pop(self, val):
        '''
        @pre: two balanced heaps
        @push: two balanced heaps with val removed
        :param val: the value to be removed
        removes the value by searching the proper heap
        '''
        
        if val <= self.maxH[0] and not self.maxL == 0:
            index = self.maxH.index(val)
            while index > 0:
                up = (index + 1) / 2 - 1
                self.maxH[int(index)] = self.maxH[int(up)]
                index = up

            heapq._heappop_max(self.maxH)
            self.maxL += -1
        else:
            index = self.minH.index(val)
            self.minL += -1
            while index > 0:
                up = (index + 1) / 2 - 1
                self.minH[int(index)] = self.minH[int(up)]
                index = up
            heapq.heappop(self.minH)

        self.rebalance_heaps()
        print(self.get_median())

    def parse_command(self, command):
        '''
        @pre: string with valid command as first char and number as last chars 
        @post: returns a valid median value (AS A INTEGER)
        parses commands does proper ordering to find the median  
        '''
        command, val = command.strip().split()
        val = int(val)

        # Adding
        if command == 'a':
            self.heap_push(val)
        # Removing
        else:
            self.heap_pop(val)
    

num_ops = int(input())
medheap = MedianHeap()
    
for i in range(num_ops):
    try:
        medheap.parse_command(input())
    except (ValueError, IndexError):
        print("Wrong!")
