import numpy as np

from abc import ABC, abstractmethod

class TropicalAlgebra(ABC):
    """
    Tropical algebra abstract base class.
    """
    @abstractmethod
    def __init__(self, data):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def dualadd(self, other):
        pass

    @abstractmethod
    def mult(self, other):
        pass
    
    @abstractmethod
    def dualmult(self, other):
        pass

    @abstractmethod
    def dot(self, other):
        pass

    @abstractmethod
    def dualdot(self, other):
        pass

    @abstractmethod
    def pow(self, n):
        pass

    @abstractmethod
    def dualpow(self, n):
        pass

    @property
    @abstractmethod
    def C(self):
        pass

    @property
    @abstractmethod
    def H(self):
        pass

class Manipulation:
    """
    Basic common manipulation for TropicalAlgebra classes.
    """
    def __init__(self, data):
        self.data = np.array(data)

    @property
    def T(self):
        """
        Getting the transposed array.
        """
        return self.__class__(self.data.T)
    
    def to_numpy(self):
        """
        Convert to the numpy array.
        """
        return self.data
    
    def to_list(self):
        """
        Convert to the python native list.
        """
        return self.data.tolist()
    
class MaxPlus(TropicalAlgebra, Manipulation):
    """
    Max-Plus Dual Semiring
    """
    def __init__(self, data):
        Manipulation.__init__(self, data)

    def __repr__(self):
        data_str = np.array2string(self.data, max_line_width=np.inf).replace('\n', '\n        ')
        return f"MaxPlus({data_str})"

    def __add__(self, other):
        return self.add(other)
    
    def __sub__(self, other):
        return self.dualadd(other)

    def __mul__(self, other):
        return self.mult(other)
    
    def __truediv__(self, other):
        return self.dualmult(other)

    def __matmul__(self, other):
        return self.dot(other)

    def __pow__(self, n):
        return self.pow(n)
        
    def add(self, other):
        if isinstance(other, (int, float)):
            other = MaxPlus([other])
        elif not isinstance(other, MaxPlus):
            return NotImplemented

        return MaxPlus(np.maximum(self.data, other.data))
    
    def dualadd(self, other):
        if isinstance(other, (int, float)):
            other = MaxPlus([other])
        elif not isinstance(other, MaxPlus):
            return NotImplemented

        return MaxPlus(np.minimum(self.data, other.data))
    
    def mult(self, other):
        if isinstance(other, (int, float)):
            other = MaxPlus([other])
        elif not isinstance(other, MaxPlus):
            return NotImplemented

        return MaxPlus(self.data + other.data)
    
    def dualmult(self, other):
        return self.mult(other)
        
    def dot(self, other):
        if isinstance(other, (int, float)):
            other = MaxPlus([other])
        elif not isinstance(other, MaxPlus):
            return NotImplemented

        if self.data.ndim <= 1 or other.data.ndim <= 1:
            return NotImplemented

        result = np.zeros((self.data.shape[0], other.data.shape[1]))
        for i in range(self.data.shape[0]):
            for j in range(other.data.shape[1]):
                result[i, j] = np.max(self.data[i, :] + other.data[:, j])

        return MaxPlus(result)
    
    def dualdot(self, other):
        if isinstance(other, (int, float)):
            other = MaxPlus([other])
        elif not isinstance(other, MaxPlus):
            return NotImplemented

        if self.data.ndim <= 1 or other.data.ndim <= 1:
            return NotImplemented

        result = np.zeros((self.data.shape[0], other.data.shape[1]))
        for i in range(self.data.shape[0]):
            for j in range(other.data.shape[1]):
                result[i, j] = np.min(self.data[i, :] + other.data[:, j])

        return MaxPlus(result)

    def pow(self, n):
        if n < 0:
            raise ValueError("Negative exponents are not supported for MaxPlus algebra.")
        elif n == 0:
            result = np.ones_like(self.data) * (-np.inf)
            for i in range(len(self.data)):
                result[i, i] = 0
            return MaxPlus(result)
        elif n == 1:
            return self
        else:
            result = self
            for _ in range(n - 1):
                result = result @ self
            return result
    
    def dualpow(self, n):
        if n < 0:
            raise ValueError("Negative exponents are not supported for MaxPlus algebra.")
        elif n == 0:
            result = np.ones_like(self.data) * (np.inf)
            for i in range(len(self.data)):
                result[i, i] = 0
            return MaxPlus(result)
        elif n == 1:
            return self
        else:
            result = self
            for _ in range(n - 1):
                result = result.dualdot(self)
            return result
        
    @property
    def C(self):
        """
        Getting the conjugation array.
        """
        return MaxPlus(-self.data)
    
    @property
    def H(self):
        """
        Getting the Hermitian array.
        """
        return self.T.C
    
class MinPlus(TropicalAlgebra, Manipulation):
    """
    Min-Plus Dual Semiring
    """
    def __init__(self, data):
        Manipulation.__init__(self, data)

    def __repr__(self):
        data_str = np.array2string(self.data, max_line_width=np.inf).replace('\n', '\n        ')
        return f"MinPlus({data_str})"
    
    def __add__(self, other):
        return self.add(other)
    
    def __sub__(self, other):
        return self.dualadd(other)

    def __mul__(self, other):
        return self.mult(other)
    
    def __truediv__(self, other):
        return self.dualmult(other)

    def __matmul__(self, other):
        return self.dot(other)

    def __pow__(self, n):
        return self.pow(n)
    
    def add(self, other):
        if isinstance(other, (int, float)):
            other = MinPlus([other])
        elif not isinstance(other, MinPlus):
            return NotImplemented

        return MinPlus(np.minimum(self.data, other.data))
    
    def dualadd(self, other):
        if isinstance(other, (int, float)):
            other = MinPlus([other])
        elif not isinstance(other, MinPlus):
            return NotImplemented

        return MinPlus(np.maximum(self.data, other.data))
    
    def mult(self, other):
        if isinstance(other, (int, float)):
            other = MinPlus([other])
        elif not isinstance(other, MinPlus):
            return NotImplemented

        return MinPlus(self.data + other.data)
    
    def dualmult(self, other):
        return self.mult(other)
        
    def dot(self, other):
        if isinstance(other, (int, float)):
            other = MinPlus([other])
        elif not isinstance(other, MinPlus):
            return NotImplemented

        if self.data.ndim <= 1 or other.data.ndim <= 1:
            return NotImplemented

        result = np.zeros((self.data.shape[0], other.data.shape[1]))
        for i in range(self.data.shape[0]):
            for j in range(other.data.shape[1]):
                result[i, j] = np.min(self.data[i, :] + other.data[:, j])

        return MinPlus(result)
    
    def dualdot(self, other):
        if isinstance(other, (int, float)):
            other = MinPlus([other])
        elif not isinstance(other, MinPlus):
            return NotImplemented

        if self.data.ndim <= 1 or other.data.ndim <= 1:
            return NotImplemented

        result = np.zeros((self.data.shape[0], other.data.shape[1]))
        for i in range(self.data.shape[0]):
            for j in range(other.data.shape[1]):
                result[i, j] = np.max(self.data[i, :] + other.data[:, j])

        return MinPlus(result)
    
    def pow(self, n):
        if n < 0:
            raise ValueError("Negative exponents are not supported for MinPlus algebra.")
        elif n == 0:
            result = np.ones_like(self.data) * (np.inf)
            for i in range(len(self.data)):
                result[i, i] = 0
            return MinPlus(result)
        elif n == 1:
            return self
        else:
            result = self
            for _ in range(n - 1):
                result = result @ self
            return result
    
    def dualpow(self, n):
        if n < 0:
            raise ValueError("Negative exponents are not supported for MinPlus algebra.")
        elif n == 0:
            result = np.ones_like(self.data) * (-np.inf)
            for i in range(len(self.data)):
                result[i, i] = 0
            return MinPlus(result)
        elif n == 1:
            return self
        else:
            result = self
            for _ in range(n - 1):
                result = result.dualdot(self)
            return result
        
    @property
    def C(self):
        """
        Getting the conjugation array.
        """
        return MinPlus(-self.data)
    
    @property
    def H(self):
        """
        Getting the Hermitian array.
        """
        return self.T.C