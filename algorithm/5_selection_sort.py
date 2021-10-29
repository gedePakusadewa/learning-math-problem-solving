class Sh:
    def __init__(self, arr:list):
        self.arr= arr

    def s_sort(self)->list:
        arr= self.arr
        print(arr)
        l= len(arr)
        tmp= arr[0]
        for i, dt in enumerate(arr):
            smallest_index= self.smallest(arr[i:l])
            if arr[i] > arr[smallest_index + i]:
                tmp= arr[i]
                arr[i]= arr[smallest_index + i]
                arr[smallest_index + i]= tmp
            #print(arr)
        return arr

    def smallest(self, arr:list)->int:
        tmp= 0

        for i, dt in enumerate(arr):
            if arr[tmp] > dt:
                tmp= i
        return int(tmp)





def main():
    arr= [45, 89, 12, 5, 6, -1, 3, 67, 0]
    s= Sh(arr)
    print(s.s_sort())


if __name__ == '__main__':
    main()
