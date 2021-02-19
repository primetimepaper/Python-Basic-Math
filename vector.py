class Vector:
    def __init__(self, data = [], *args):
        if isinstance(data, list):
            self._vector = data.copy()
        else:
            data2 = [data]
            for arg in args:
                if not isinstance(arg, (int, float)):
                    raise TypeError
                else:
                    data2.append(arg)
            self._vector = data2.copy()

    def __str__(self):
        data = self._vector
        if data == []:
            return "<>"
        else:
            ans = "<"
            for i in data:
                ans += str(float(i))
                if i != data[len(data) - 1]:
                    ans += ", "
            ans += ">"
            return ans        
    
    def dim(self):
        return len(self._vector)
    
    def get(self, index):
        data = self._vector
        return data[index]
    
    def set(self, index, value):
        data = self._vector
        data[index] = value

    def addlist(self, other_vector):
        if not isinstance(other_vector, list):
            raise TypeError
        for j in range(len(other_vector)):
            if not isinstance(other_vector[j], (float, int)):
                raise TypeError
        if self.dim() != len(other_vector):
            raise ValueError
        ans = []
        for i in range(len(other_vector)):
            ans.append(self.get(i) + other_vector[i])
        return ans
    
    def add(self, other_vector):
        if not isinstance(other_vector, Vector):
            raise TypeError
        for j in range(other_vector.dim()):
            if not isinstance(other_vector.get(j), (float, int)):
                raise TypeError
        if self.dim() != other_vector.dim():
            raise ValueError
        ans = []
        for i in range(other_vector.dim()):
            ans.append(float(self.get(i)) + float(other_vector.get(i)))
        return Vector(ans)

    def equals(self, other_vector):
        if self.dim() != other_vector.dim():
            return False
        for i in range(self.dim()):
            if float(self.get(i)) != float(other_vector.get(i)):
                return False
        return True

    def __eq__(self, other_vector):
        if not isinstance(self, Vector):
            return NotImplemented
        if not isinstance(other_vector, Vector):
            return False
        else:
            if self._vector == other_vector._vector:
                return True
            else:
                return False

    def ne(self, other_vector):
        if not isinstance(self, Vector):
            return NotImplemented
        elif not isinstance(other_vector, Vector):
            return False
        else:
            if self._vector != other_vector._vector:
                return True
            else:
                return False
    
    def __add__(self, other_vector):
        if not isinstance(self, Vector):
            return NotImplemented
        elif not isinstance(other_vector, Vector):
            raise TypeError
        elif self.dim() != other_vector.dim():
            raise ValueError
        else:
            ans = []
            a = max(len(self._vector),len(other_vector._vector))
            b = min(len(self._vector),len(other_vector._vector))
            for i in range(a):
                if i < b:
                    ans.append(float(self._vector[i]+other_vector._vector[i]))
                elif len(self._vector) == a:
                    ans.append(float(self._vector[i]))
                else:
                    ans.append(float(other_vector._vector[i]))
            return Vector(ans)
        
    def __getitem__(self, key):
        if not isinstance(self, Vector):
            return NotImplemented
        else:
            return self._vector[key]
    
    def __setitem__(self, index, value):
        if not isinstance(self, Vector):
            return NotImplemented
        else:
            return self.set(index, value)

    def __iadd__(self, y):
        if not isinstance(self, Vector):
            return NotImplemented

        if isinstance(y, Vector):
            for j in range(y.dim()):
                if not isinstance(y.get(j), (float, int)):
                    raise TypeError
            if self.dim() != y.dim():
                raise ValueError
            for i in range(y.dim()):
                self.set(i, (float(self.get(i)) + float(y.get(i))))
            return self
        elif isinstance(y, (int, float)):
            self._vector[i] = self._vector[i] + y
            return self
        else:
            raise TypeError

    def scalar_product(self, factor):
        ans = []
        for i in range(self.dim()):
            if not isinstance(self[i], (int, float)):
                raise TypeError
            else:
                ans.append(float(factor * self[i]))
        self = Vector(ans)
        return self

    def __rmul__(self, factor):
        if not isinstance(self, Vector):
            return NotImplemented
        else:
            return self.scalar_product(factor)

    def __imul__(self, factor):
        if not isinstance(self, Vector):
            return NotImplemented
        else:
            self = self.scalar_product(factor)
            return self