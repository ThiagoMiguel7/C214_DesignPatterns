from sorter import Sorter

class MergeSort(Sorter):
    def sort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            left = self.sort(left)
            right = self.sort(right)

            return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result