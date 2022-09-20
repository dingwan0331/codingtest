class Binary:
    def __init__(self,number=0) -> None:
        print("__init__")
        self.number = number

    def __str__(self):
        result = ''
        for i in self.number:
            result += str(i)
        return result

    def __len__(self):
        return len(self.number)

    def __add__(self,other):
        return int(self.__str__(),2) + int(other.__str__(),2)

    def __repr__(self):
        return list(self)
    def __getitem__(self, index): # index 를 인자로 받아야 한다.​​​​       
        return self.number[index]

data = [1,0]
data1 = [1]

b1 = Binary(data)
b2 = Binary(data1)

print(b1+b2)