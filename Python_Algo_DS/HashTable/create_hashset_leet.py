"""
Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.

-- __getitem__
    __setitem__
    
    1<<5 -> adds 5 zero to the right in the binary representation
            of 1
    24 >> 2 -> deletes 2 bits from the right in the binary
                representation of 24
        24 >> 2 = 11000 -> 110
"""


class MyHashSet:

    def __init__(self):
        # to be chosen as a prime number to avoid collisions
        # distribution of the hash code is spread out.
        # to be used when using division method (i % N)
        self.h_size = 1000 
        self.hashtable = [[] for _ in range(1000)]

    def gethash(self, key):
        # check for int. since no key conversion to index is done
        # as all the keys are integer values
        if isinstance(key, int):
            # dividing by 1000 is hash compression to keep the 
            # hash index within the boundary(size) of hash table
            # better method is MAD(multiply and divide).
            # MAD = [(ai + b) mod p] mod N,
            #   N = size of the hash table
            #   p = prime number larger than N
            #   a,b = random integers between (0,p-1)
            #   i = hash code 
            # A hash generator should include two components:
                # a hash code generator for a string and
                # a hash compression -> to keep the index within (0, N-1)
                # N is the size of the hash table
            
            
            
            return key % 1000 
        
    def add(self, key: int) -> None:
        hash_indx = self.gethash(key)
        if key not in self.hashtable[hash_indx]:
            self.hashtable[hash_indx].append(key)


    def remove(self, key: int) -> None:
        hash_indx = self.gethash(key)
        if key in self.hashtable[hash_indx]:
            self.hashtable[hash_indx].remove(key)        

        

    def contains(self, key: int) -> bool:
        hash_indx = self.gethash(key)
        return key in self.hashtable[hash_indx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)