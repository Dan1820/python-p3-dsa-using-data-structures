class Myarray():
    def __init__(self) -> None:
        self.dictionary={}
        self.length=0
    def push(self,value):
        self.dictionary[self.length]=value
        self.length +=1

    def pop(self):
        if self.length==0:
            return None
        self.length -=1
        return self.dictionary.pop(self.length)
    def shift(self,value):
        pass

    def unshift(self):
        pass
    
arr=Myarray()

arr.push(1)
arr.push(2)
arr.push(3)
arr.push(4)
print(arr.pop())