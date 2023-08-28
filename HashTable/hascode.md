# An implementation of a cyclic-shift hash code computation for a character string in Python appears as follows:
```python
def hash_code(s):
    mask = (1 << 32) − 1 # to keep the mask under 32 bits
    h=0
    for character in s:
        h = (h << 5 & mask) | (h >> 27)
        h += ord(character)
    return h
```
==Python has an inbuilt hash function==

This creates a unique index for a key to avoid collision. Breif explanation is provided below.

Certainly! You can explain the line h = (h << 5 & mask) | (h >> 27) in simpler terms as follows:

"Sure, this line is where we make the hash value mix up its bits to create a unique and well-spread pattern. Think of it like a puzzle where we slide the pieces around. The (h << 5 & mask) part takes some bits from the left side of the hash and shifts them to the left by 5 places. It's like moving some puzzle pieces to the left. The & mask makes sure the shifted bits fit within a certain limit.

On the other hand, the (h >> 27) part moves some bits from the right side of the hash to the right by 27 places. It's like shifting the other pieces to the right. Then, we use the | symbol to put these shifted pieces back together. This way, we're rearranging the bits in a special way that helps prevent patterns and makes our hash values more unique and balanced. It's like shaking up a puzzle to create a better mix, which is important to avoid confusion between different pieces of data."

This explanation provides a simplified analogy to help convey the concept of bit manipulation and mixing in hash functions.

# COMPRESSION METHODS
# 1. Division Method i%N
    # to be chosen as a prime number to avoid collisions
    # distribution of the hash code is spread out.
    # to be used when using division method (i % N)
    # Divisiob by N is to keep hash index within the boundary(size) of hash table.
# better method is MAD(multiply and divide).
# MAD = [(ai + b) mod p] mod N
    #   N = size of the hash table
    #   p = prime number larger than N
    #   a,b = random integers between (0,p-1)
    #   i = hash code 
# A hash generator should include two components:
    # a hash code generator for a string and
    # a hash compression -> to keep the index within (0, N-1)
    # N is the size of the hash table

# Collision Handling:
# 1. Separate Chaining
# 2. Linear probing

# LOAD FACTOR (lambda) = n/N should be < 1, if close 1 collision increase

# If the load factor of the table increases beyond 0.5, we double the size of the table and rehash all items into the new table.

```python

# code is complete need to make some changes in get, set and delete items
# code is just for understanding the concept
class HasTable:
def __init__ (self, cap=11, p=109345121):

    ”””Create an empty hash-table map.”””
    
    # number of entries in the map
    self.table = cap * [ None ]
        
    self.n = 0 # number of distinct entries
    
    # prime for MAD compression
    self.prime = p
    
    # scale from 1 to p-1 for MAD
    self.scale = 1 + randrange(p−1)
    # shift from 0 to p-1 for MAD
    self.shift = randrange(p)

def hash_function(self, k):
    return (hash(k)*self.scale + self.shift) % self.prime % len(self.table)

def len (self):
    return self. n

def getitem (self, k):
    j = self. hash function(k)
    # may raise KeyError

    return self. bucket_getitem(j, k)

def setitem (self, k, v):
    j = self. hash function(k)

    # subroutine maintains self. n
    self. bucket_setitem(j, k, v) 
    
    if self. n > len(self. table) // 2: # keep load factor <= 0.5

        self. resize(2 len(self. table) − 1) # number 2ˆx - 1 is often prime

def delitem (self, k):

    j = self. hash function(k) # may raise KeyError
    self. bucket_delitem(j, k)
    self. n −= 1

# resize bucket array to capacity c
def resize(self, c):
    
    # use iteration to record existing items
    # then reset table to desired capacity
    old = list(self.items( ))

    self. table = c [None] # n recomputed during subsequent adds
    self. n = 0
    for (k,v) in old:
        self[k] = v   # reinsert old key-value pair`
```
