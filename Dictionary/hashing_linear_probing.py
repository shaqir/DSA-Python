class Dictionary:
  
  def __init__(self,size):
    self.size = size
    self.slots = [None] * self.size
    self.data = [None] * self.size

  def put(self,key,value):
    hash_value = self.hash_function(key)

    if self.slots[hash_value] == None:
      self.slots[hash_value] = key
      self.data[hash_value] = value
    
    else:
      if self.slots[hash_value] == key:
        self.data[hash_value] = value
      else:
        new_hash_value = rehash_function(hash_value)
        while self.slots[new_hash_value] != None and self.slots[new_hash_value] != key:
          new_hash_value = rehash_function(hash_value)
        if self.slots[new_hash_value] == None:
          self.slots[new_hash_value] = key
          self.data[new_hash_value] = value
        else:
          self.data[new_hash_value] = value



  def hash_function(self,key):
    return abs(hash(key)) % self.size

  def rehash_function(self,old_hash):
    return (old_hash + 1) % self.size

  def __setitem__(self,key,value):
    self.put(key,value)  


D1 = Dictionary(3)
D1.put("Java",50)
D1.put("Python",80)
D1["PHP"] = 70
print(D1.data)
print(D1.slots)