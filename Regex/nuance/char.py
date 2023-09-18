import collections

def commonChars(A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        result = collections.Counter(A[0])
        for a in A:
            result &= collections.Counter(a)
        return list(result.elements())


num = ['bloy', 'babel', 'bulb']

print(commonChars(num))