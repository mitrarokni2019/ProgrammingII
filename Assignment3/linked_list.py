""" linked_list.py

Student:Mitra Rokni
Mail: mitra.rokni.0545@student.uu.se
Reviewed by:
Date reviewed:
"""

class LinkedList:
    
    class Node:
        def __init__(self, data, succ,  rest=None):
            self.data = data
            self.succ = succ  
            self.rest= rest    
        
            
    def __init__(self):
        self.first = None

    
    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ
            
    def __in__(self, x):           # Discussed in the section on operator overloading 
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False 
        return False
        
    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')            
    
    
    # To be implemented
    
    def length(self):             # Optional
        return self._length(self.first)

    def _length(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._length(r.succ)
  
  
    def mean(self):               # Optional
        sum= self.sum(self.first)
        n= self.length()
        return  sum/n

    def sum(self, r):
        if r is None:
            return 0
        else:
            return r.data + self.sum(r.succ)
    
    
    def remove_last(self):        # Optional
        pass
    
    
    def remove(self, x):          # Compulsory
        return self._remove (self.first, x)

           
    def _remove (self,r, x):
        if r is  None or r.succ is None:
            return False
        if self.first.data==x:
            self.first=self.first.succ
            return True
        elif r.succ.data ==x :
            r.succ=r.succ.succ
            return True

        else:
            return self._remove(r.succ, x)

    
    
    def count(self, x):           # Optional
        return self._count(self.first, x)
    
    def _count(self, r, x):
        if r is  None:
            return 0
        elif r.data ==x:
            return 1+self._count(r.succ, x)
        else:
            return self._count(r.succ, x)

    
    def to_list(self):            # Compulsory
        list=[]
        self._to_list(self.first, list)
        return list
    
    def _to_list(self, r, list):
        if r is  None: 
            return False
        else:
            list.append(r.data)
            return self._to_list(r.succ, list)


    def remove_all(self, x):      # Compulsory
        if self.first.data ==  None:
            print ("there is nothing in the list")
        else:
            self.first = self._remove_all(x, self.first)
    
    def _remove_all(self, x, f):
        if f == None:
            return self.first

        if f.succ is not None and f.succ.data == x:
            f.succ = f.succ.succ

        elif f.data == x and f.succ is None:
            f= None
            
        if f is not None:
            return self._remove_all(x, f.succ)
        
    def __str__(self):            # Compulsary
        return '(' + ', '.join([str(x) for x in self]) + ')'
        
        
    """         result = ''
        for x in self:
            result += str(x) + ' '
        return '(' + result + ')' """
    
    
    def merge(self, lst):         # Compulsory
        pass
    
    


    def __getitem__(self, ind):
        h = self.length()
        if ind >= h:
            raise IndexError("Index out of range.")
        current = self.first
        for x in range(ind):
            current = current.succ
        return current.data
        
        #if ind == 0:
        #        return self.first
        #else:
        #        return self.rest[ind - 1]
        
        
        
        #if self is None:
        #    raise IndexError
        #elif ind == 0:
        #    return self.first
        #else:
        #    return self.rest.__getitem__(ind - 1)
        # Or equivalently, self.rest[ind - 1]





class Person:                     # Compulsory to complete
    def __init__(self,name, pnr):
        self.name = name
        self.pnr = pnr
        
    def __str__(self):
        return f"{self.name}:{self.pnr}"
    def __lt__(self, p):
        if self.pnr<p.pnr:
            return self.pnr<other.pnr   
    

def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()
    
    # Test code:

    


if __name__ == '__main__':
    main()
    


    

