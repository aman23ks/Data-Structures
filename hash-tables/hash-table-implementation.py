# Although hash tables come built-in in the form of hash tables in python,
# here we will try to implement our own hash table.

class hash_table():
    # We initalize the size of the hash table(no. of buckets) with the size given to the class object.
    def __init__(self, size):
        self.size = size
        # We initalize an array of size 'size' with None.
        self.data = [None]*self.size

    # As in the aray implementation this method is used to print the attributes of the class object in dictionary format.
    def __str__(self):
        return str(self.__dict__)

    def _hash(self, key):  # Our custom hash function
        hash = 0
        for i in range(len(key)):
            # ord(key[i]) gives the unicode code point of the character key[i]
            hash = (hash + ord(key[i])*i) % self.size
        return hash  # The hash value obtained after applying the hash function to the key is returned

    def set(self, key, value):  # Function to insert a new key, value pair
        # Hash value of the key is calculated using the _hash function
        hash = self._hash(key)
        # If the 'hash' position of the data array is empty, we insert the key, value pair as a list
        if not self.data[hash]:
            self.data[hash] = [[key, value]]
        else:  # If the 'hash' position is not empty, implying a collision, we simply append the list of key,value pair to the lists already present
            self.data[hash].append([key, value])
        print(self.data)

    def get(self, key):  # Function to return the value of the key entered by the user
        # Hash value of the key is calculated by passsing the key to the _hash function
        address = self._hash(key)
        currentBucket = self.data[address]
        if currentBucket:  # Multiple items may exist in the position of the hash value returned by the hash function, so we have to chceck all of them
            # We loop over the entire list of lists that may be present in the 'hash' position of the data array
            for i in range(len(currentBucket)):
                # For every list in the list of lists(extracted by 'i'), we match the first element of the list with the given key
                if currentBucket[i][0] == key:
                    # If we get a match, we return the second element of that list, which is the value
                    return currentBucket[i][1]
        return None  # If we don't find the key, we return None


new_hash = hash_table(2)
# print(new_hash)

new_hash.set("grapes", 1000)

new_hash.set("apples", 50)

new_hash.get("apples")
