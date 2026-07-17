class studentmarks:
    def __init__(self):
        self.market=[]
    def accept(self):
        n=int(input("no of students:"))
        for i in range(n):
            x=int(input("enter students marks:"))
            selfmarks.append(x)
            print(self.marks)
    def avg(self):
        total=0
        for x in self.marks:
            total+=x
            avgg=total//len(self.marks)
            return avgg
    def minn(self):
        for x in self.marks:
            if x<min:
                min=x
                return min
    def maxx(self):
        max=self.marks[0]
        for x in self.marks:
            if x>max:
                max=x
            return max
    def length(self):
        count=0
        for i in range (self.marks):
            count +=1
            return count
            ob=studentmarks()
            ob.accept()
            while true:
                print('1.avg')
                print('2.min')
                print('3.max')
                print('4.length')
                choice=int(input("enter choice"))
            if choice==1:
                print("avgg:",ob.avg())
            elif choice==2:
                print("minn:",ob.min())
            elif choice==3:
                print("max:",ob.max())
            elif choice==4:
                print("length:",ob.length())
            elif choice==5:
                break
            else:
                prnint("not valid choice")
