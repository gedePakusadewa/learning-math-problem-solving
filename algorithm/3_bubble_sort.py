

class Bs:
    
    data= [1]

    def __init__(self, data):
        self.data= data

    def bbs(self):
        dt= self.data
        #print(dt)
        tmp = 0
        #i = 0 # pointer position array
        stop= False
        
        l= len(dt) # array length

        while True:
            stop= True
            
            for i in range(l):
                if i+1 < l:
                    print(dt)
                    if dt[i] > dt[i+1]:
                        tmp= dt[i+1]
                        dt[i+1]= dt[i]
                        dt[i]= tmp
                        stop= False

            if (stop == True):
                break

        return dt

dt= [8, 56, 1, 78, 23, 5, 11, 55]
t1= Bs(dt)

print(t1.bbs())


