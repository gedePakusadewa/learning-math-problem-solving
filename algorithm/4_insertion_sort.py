class Is:

    def __init__(self, raw_data):
        self.raw_data= raw_data

    def ist(self):
        dt= self.raw_data
        stop= False
        i_r= 0 # increment to right
        l= len(dt)
        tmp= 0
        print(dt)
        while i_r < l-1:
            #stop= True
            #print(dt)
            if i_r == l:
                break
            if dt[i_r] > dt[i_r+1]:
                tmp= dt[i_r+1] 
                dt[i_r+1]= dt[i_r]
                dt[i_r]= tmp
                #stop= False
                for i in range(i_r, 0, -1):
                    if i == 0:
                        break
                    if dt[i]<dt[i-1]:
                        tmp= dt[i-1]
                        dt[i-1]= dt[i]
                        dt[i]= tmp
                        #stop= False
            i_r= i_r + 1
       
        return dt


dt= [56, 23, 89, 2, 98, 38, 0, 12, 67]
t1= Is(dt)
print(t1.ist())

            
