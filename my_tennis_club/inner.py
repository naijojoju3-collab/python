class outer:
 def __init__(self):
     self.name = "outer class"

 class inner:
   def __init__(self):
      self.name = "inner class"

   def display(self):
         print("this is the inner class")

Outer = outer()
print(Outer.name)
Inner = Outer.inner()
Inner.display()