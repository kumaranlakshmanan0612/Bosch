class Pyclass:
  def __init__(self):
    self.lis=[]
    self.size=0
  def __init__(self,a):
    self.lis=[]
    self.lis.append(a)
    self.size=1
  def appen(self,a):
    self.lis.append(a)
    self.size=self.size+1
  def display(self):
    strr='['
    for i in self.lis:
      strr=strr+str(i)
      strr=strr+','
    ans=strr[0:len(strr)-1]
    print(f"{ans}]")
  def getlen(self):
    return self.size
o1=Pyclass(4)
o1.appen(3)
o1.appen(1)
o1.appen(2)
print(o1.getlen())
print(type("display"))
o1.display()
print(type(o1))