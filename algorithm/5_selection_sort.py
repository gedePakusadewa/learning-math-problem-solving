class Sh:
    def __init__(self, arr:list[int]):
        self.arr= arr

    def s_sort(self)->list[int]:
        arr= self.arr
        l= len(arr)
        tmp= arr[0]
        for i, dt in enumerate(arr):
            if arr[i] > self.smallest(arr[i:l-1]):
                tmp= arr[i]
                arr[i]= 

    def smallest(self, arr: list[int])->int:
        tmp= 0

        for i, dt in enumerate(tmp):
            if arr[tmp] > dt:
                tmp= i
        return tmp





def main():
    pass


if __name__ == '__main__':
    main()
