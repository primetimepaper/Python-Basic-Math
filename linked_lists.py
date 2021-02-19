#Stack and Queue uses dictionary, Deque uses 2dlist type custom class called a Node

class ListNode:
    def __init__(self, data = None):
        if isinstance(data, list):
            self._len = len(data)
            def links(self, data):
                d = {}
                d[None] = data[0]
                for i in range(len(data)):
                    if i + 1 < len(data):
                        d[data[i]] = data[i + 1]
                    else:
                        d[data[i]] = None
                return d
            self._links = links(self, data)
        else:
            self._len = 1

class LinkedStack:
    def __init__(self, data = None):
        ListN = ListNode(data)
        self._LN = ListN._len
        if isinstance(data, list):
            self._top = data[self._LN - 1]
            self._link = ListN._links
        else:
            self._top = data
    
    def __str__(self):
        if not isinstance(self, LinkedStack):
            return NotImplemented
        else:
            ans = []
            def recursion1(self):
                if self._top == None:
                    for k,v in self._link.items():
                        if self._link[k] == None:
                            self._top = k
                            break
                    ans.reverse()
                    return ans
                else:
                    ans.append(self._top)
                    for k,v in self._link.items():
                        if self._link[k] == self._top:
                            self._top = k
                            break
                    return recursion1(self)
            return "LinkedStack("+str(recursion1(self))+")"

    def push(self, value):
        for k,v in self._link.items():
            if self._link[k] == None:
                x = k
        self._link[x] = value
        self._link[value] = None
        self._top = value
        return

    def pop(self):
        if self._link == {}:
            raise ValueError
        else:
            for keys,values in self._link.items():
                if values == None:
                    ans = keys
            for key,value in self._link.items():
                if value == ans:
                    ans2 = key
            self._link[ans2] = None
            del self._link[ans]
            return ans

    def peek(self):
        return self._top

    def __len__(self):
        if not isinstance(self, LinkedStack):
            return NotImplemented
        else:
            return self._LN

class LinkedQueue:
    def __init__(self, data = None):
        ListN = ListNode(data)
        self._LN = ListN._len
        if isinstance(data, list):
            self._front = data[0]
            self._link = ListN._links
        else:
            self._front = data
    
    def __str__(self):
        if not isinstance(self, LinkedQueue):
            return NotImplemented
        else:
            ans = []
            def recursion1(self):
                if self._front == None:
                    self._front = self._link[self._front]
                    return ans
                else:
                    ans.append(self._front)
                    self._front = self._link[self._front]
                    return recursion1(self)
            return "LinkedQueue("+str(recursion1(self))+")"
    
    def pop(self):
        if self._link == {}:
            raise ValueError
        else:
            self._link[None] = self._link[self._front]
            x = self._front
            self._front = self._link[self._front]
            del self._link[x]
            return x

    def enqueue(self, value):
        for k,v in self._link.items():
            if self._link[k] == None:
                x = k
        self._link[x] = value
        self._link[value] = None
        self._front = value
        return

    def peek(self):
        return self._front

    def __len__(self):
        if not isinstance(self, LinkedStack):
            return NotImplemented
        else:
            return self._LN

class LinkedDeque:
    def __init__(self, data):
        class Node:
            def __init__(self, data = None, previous = None, next = None):
                #self._Node = [previous, data, next] Does not update in real time
                self._data = data
                self._previous = previous
                self._next = next
        
        self._data = []
        for i in range(len(data)):
            x = data[i]
            if i == 0:
                y = data[len(data) - 1]
            else:
                y = data[i - 1]
            if i == len(data) - 1:
                z = data[0]
            else:
                z = data[i + 1]
            self._data.append(Node(x,y,z))
        self._front = self._data[0]._data

    def __str__(self):
        if not isinstance(self, LinkedDeque):
            return NotImplemented
        else:
            ans = []
            for i in self._data:
                ans.append(i._data)
            return "LinkedDeque("+str(ans)+")"

    def __getitem__(self, key):
        if not isinstance(self, LinkedDeque):
            return NotImplemented
        else:
            return self._data[key]._data

    def __setitem__(self, key, value):
        if not isinstance(self, LinkedDeque):
            return NotImplemented
        else:
            self._data[key]._data = value
            if key == 0:
                self._data[len(self._data) - 1]._next = value
                self._data[1]._previous = value
            elif key == (len(self._data) - 1):
                self._data[len(self._data) - 2]._next = value
                self._data[0]._previous = value
            else:
                self._data[key + 1]._previous = value
                self._data[key - 1]._next = value
            return None
    
    def __delitem__(self, key):
        if not isinstance(self, LinkedDeque):
            return NotImplemented
        else:
            if key == 0:
                self._data[len(self._data) - 1]._next = self._data[1]._data
                self._data[1]._previous = self._data[len(self._data) - 1]._data
            elif key == (len(self._data) - 1):
                self._data[len(self._data) - 2]._next = self._data[0]._data
                self._data[0]._previous = self._data[len(self._data) - 2]._data
            else:
                self._data[key - 1]._next = self._data[key + 1]._data
                self._data[key + 1]._previous = self._data[key - 1]._data
            del self._data[key]
            return None

    def append(self, value):
        class Node:
            def __init__(self, data = None, previous = None, next = None):
                self._Node = [previous, data, next]
                self._data = data
                self._previous = previous
                self._next = next
        self._data.append(Node(value,self._data[len(self._data) - 1]._data,self._front))
        return

    def appendleft(self, value):
        class Node:
            def __init__(self, data = None, previous = None, next = None):
                self._Node = [previous, data, next]
                self._data = data
                self._previous = previous
                self._next = next
        ans = []
        for i in range(len(self._data)):
            if i == 0:
                ans.append(Node(value,self._data[len(self._data) - 1]._data,self._front))
            ans.append(self._data[i])
        self._data = ans
        del ans
        return

    def pop(self):
        x = self._data.pop()
        return x._data

    def popleft(self):
        x = self._data.pop(0)
        return x._data

    def __eq__(self, other):
        if not isinstance(self, LinkedDeque):
            return NotImplemented
        else:
            for i in range(len(self._data)):
                for j in range(len(self._data[i]._Node)):
                    if self._data[i]._Node[j] != other._data[i]._Node[j]:
                        return False
            return True

    def __add__(self, other):
        if not isinstance(self, LinkedDeque):
            return NotImplemented
        elif not isinstance(other, LinkedDeque):
            raise TypeError
        else:
            selfans = []
            otherans = []
            for i in self._data:
                selfans.append(i._data)
            for j in other._data:
                otherans.append(j._data)
            ans = LinkedDeque(selfans + otherans)
            return ans