from recursion import flatten

def maxvalue(treeset):
    if treeset == []:
        return float("-inf")
    anslist = []
    def maxfinder(bt):
        if len(bt) > 2:
            if len(bt[2]) > 2:
                anslist.append(bt[2][0])
                return maxfinder(bt[2])
            else:
                return max(anslist)
        else:
            return max(anslist)
    return maxfinder(treeset)

def minvalue(treeset):
    if treeset == []:
        return float("inf")
    anslist = []
    def minfinder(bt):
        if len(bt) > 2:
            if len(bt[1]) > 2:
                anslist.append(bt[1][0])
                return minfinder(bt[1])
            else:
                return min(anslist)
        else:
            return min(anslist)
    return minfinder(treeset)

def isempty(treeset):
    if treeset == [] or (len(treeset[1]) == len(treeset[2]) == 0):
        return True
    else:
        return False

def add(element,treeset):
    def _add(e, tree):
        if tree == []:
            tree.append(element)
            tree.append([])
            tree.append([])
            return
        elif e > tree[0]:
            if len(tree) >= 3:
                if not tree[2] == []:
                    if e > tree[2][0]:
                        return _add(e, tree[2][2])
                    else:
                        return _add(e, tree[2][1])
                else:
                    return _add(e, tree[2])
            else:
                tree.append([])
                return _add(e, tree)
        else:
            if len(tree) >= 3:
                if not tree[2] == []:
                    if e > tree[2][0]:
                        return _add(e, tree[1][2])
                    else:
                        return _add(e, tree[1][1])
                else:
                    return _add(e, tree[1])
            else:
                tree.append([])
                return _add(e, tree)

    return _add(element, treeset)

def get_values(treeset):
    data = treeset.copy()
    x = flatten(data)
    x.sort()
    x.reverse()
    return x

def contains(element, treeset):
    data = treeset.copy()
    x = flatten(data)
    if element in x:
        return True
    else:
        return False

def equals(treeset_a, treeset_b):
    a = flatten(treeset_a)
    b = flatten(treeset_b)
    if len(a) != len(b):
        return False
    else:
        for i in range(len(a)):
            if a[i] not in b:
                return False
        return True

# intialise TreeSet with data as nested list
class TreeSet:
    # self._root   self._right   self._left attributes
    def __init__(self, data = []):
        if isinstance(data, list):
            self._list = data.copy()
            if self._list == []:
                self._set = set()
            else:
                self._set = set(flatten(self._list))
                if not self._list == flatten(self._list):
                    pass
                else:
                    equis = self._list.copy()
                    self._list = []
                    for i in range(len(equis)):
                        def _add(e, tree):
                            if tree == [] or tree == None:
                                tree.append(e)
                                tree.append([])
                                tree.append([])
                                return
                            elif e > tree[0]:
                                if len(tree) >= 3:
                                    if not tree[2] == []:
                                        if e > tree[2][0]:
                                            return _add(e, tree[2][2])
                                        else:
                                            return _add(e, tree[2][1])
                                    else:
                                        return _add(e, tree[2])
                                else:
                                    tree.append([])
                                    return _add(e, tree)
                            else:
                                if len(tree) >= 3:
                                    if not tree[2] == []:
                                        if e > tree[2][0]:
                                            return _add(e, tree[1][2])
                                        else:
                                            return _add(e, tree[1][1])
                                    else:
                                        return _add(e, tree[1])
                                else:
                                    tree.append([])
                                    return _add(e, tree)
                        _add(equis[i],self._list)
                    del equis
                self._root = TreeSet(self._list[0])
                self._left = TreeSet(self._list[1])
                self._right = TreeSet(self._list[2])
        elif isinstance(data,(float,int)):
            data2 = [data]
            self._list = data2.copy()
        else:
            raise TypeError

    def isempty(self):
        data = self._list
        if data == []:
            return True
        elif len(data) >= 1:
            return False
        else:
            print(data)
            if isinstance(data[1],(float, int)):
                data[1] = [data[1], [], []]
            if isinstance(data[2],(float, int)):
                data[2] = [data[2], [], []]
            if (len(data[1]) == len(data[2]) == 0):
                return True
            else:
                return False

    #can't be referenced in __sub__(self, other) for SOME reason
    def difference(self, other):
        if not isinstance(other, TreeSet):
                raise TypeError
        else:
            ans = []
            x = flatten(self._list)
            y = flatten(other._list)
            for i in x:
                if i not in y:
                    ans.append(i)
                else:
                    pass
            return set(ans)

    def intersection(self, other):
        if not isinstance(other, TreeSet):
            raise TypeError
        else:
            ans = []
            x = flatten(self._list)
            y = flatten(other._list)
            for i in x:
                if i in y:
                    ans.append(i)
                else:
                    pass
            for j in y:
                if j in x:
                    ans.append(j)
                else:
                    pass
            return set(ans)

    def __sub__(self, other):
        if not isinstance(self, TreeSet):
            return NotImplemented
        else:
            def difference(self, other):
                if not isinstance(other, TreeSet):
                    raise TypeError
                else:
                    ans = []
                    x = flatten(self._list)
                    y = flatten(other._list)
                for i in x:
                    if i not in y:
                        ans.append(i)
                    else:
                        pass
                return set(ans)
            return difference(self, other)

    def __contains__(self, element):
        if not isinstance(self, TreeSet):
            return NotImplemented
        else:
            x = flatten(self._list)
            if element in x:
                return True
            else:
                return False            

    def __str__(self):
        if not isinstance(self,TreeSet):
            return NotImplemented
        else:
            if self.isempty():
                return "{""}"
            else:
                self._set = set(flatten(self._list))
                return str(self._set)

    def __and__(self, other):
        if not isinstance(self, TreeSet):
            return NotImplemented
        else:
            def intersection(self, other):
                if not isinstance(other, TreeSet):
                    raise TypeError
                else:
                    ans = []
                    x = flatten(self._list)
                    y = flatten(other._list)
                for i in x:
                    if i in y:
                        ans.append(i)
                    else:
                        pass
                for j in y:
                    if j in x:
                        ans.append(j)
                    else:
                        pass
                return set(ans)
            return intersection(self, other)

    def add(self, element):
        x = flatten(self._list)
        if element in x:
            return
        def _add(e, tree):
            if tree == []:
                tree.append(element)
                tree.append([])
                tree.append([])
                return
            elif e > tree[0]:
                if len(tree) >= 3:
                    if not tree[2] == []:
                        if e > tree[2][0]:
                            return _add(e, tree[2][2])
                        else:
                            return _add(e, tree[2][1])
                    else:
                        return _add(e, tree[2])
                else:
                    tree.append([])
                    return _add(e, tree)
            else:
                if len(tree) >= 3:
                    if not tree[2] == []:
                        if e > tree[2][0]:
                            return _add(e, tree[1][2])
                        else:
                            return _add(e, tree[1][1])
                    else:
                        return _add(e, tree[1])
                else:
                    tree.append([])
                    return _add(e, tree)
        return _add(element,self._list)

    def symmetric_difference(self, other):
        if not isinstance(other, TreeSet):
                raise TypeError
        else:
            ans = []
            x = flatten(self._list)
            y = flatten(other._list)
            for i in x:
                if i not in y:
                    ans.append(i)
                else:
                    pass
            for j in y:
                if j not in x:
                    ans.append(j)
            return set(ans)

    def __xor__(self, other):
        if not isinstance(self, TreeSet):
            return NotImplemented
        else:
            def symmetric_difference(self, other):
                if not isinstance(other, TreeSet):
                    raise TypeError
                else:
                    ans = []
                x = flatten(self._list)
                y = flatten(other._list)
                for i in x:
                    if i not in y:
                        ans.append(i)
                    else:
                        pass
                for j in y:
                    if j not in x:
                        ans.append(j)
                return set(ans)
            return symmetric_difference(self, other)

    def __eq__(self, other):
        if not isinstance(self, TreeSet):
            return NotImplemented
        else:
            def equals(treeset_a, treeset_b):
                a = set(flatten(treeset_a))
                b = set(flatten(treeset_b))
                if a == b:
                    return True
                else:
                    return False
            return equals(self._list, other._list)
    
    def union(self, other):
        ans = []
        x = flatten(self._list)
        y = flatten(other._list)
        for i in x:
            ans.append(i)
        for j in y:
            ans.append(j)
        return TreeSet(ans)

    def __or__(self, other):
        def union(self, other):
            ans = []
            x = flatten(self._list)
            y = flatten(other._list)
            for i in x:
                ans.append(i)
            for j in y:
                ans.append(j)
            return set(ans)
        return union(self, other)

    def isdisjoint(self, other):
        x = flatten(self._list)
        y = flatten(other._list)
        for i in x:
            if i in y:
                return False
        for j in y:
            if j in x:
                return False
        return True

    def issubset(self, other):
        x = flatten(self._list)
        y = flatten(other._list)
        for i in x:
            if i not in y:
                return False
        return True

    def issuperset(self, other):
        x = flatten(self._list)
        y = flatten(other._list)
        for i in y:
            if i not in x:
                return False
        return True
    
    # todo Incomplete
    def discard(self, element):
        return None
    # todo Incomplete
    def clear(self):
        return None
    # todo Incomplete
    def pop(self, element):
        return None

#sample_input = [8, [3, [1,[],[]],[6, [4,[],[]],[7,[],[]]]],[10, [],[14, [13,[],[]],[]]]]
