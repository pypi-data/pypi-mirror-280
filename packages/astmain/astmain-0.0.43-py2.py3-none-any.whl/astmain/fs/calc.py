class calc:
    val="ccc"

    def __init__(self):
        self._val=0
    def __add__(self,other):
        print(  111111111111111111111 , other  )
        if isinstance (other,str):
            self._val=  self._val+ int( other)
            return    self._val
        else:
            self._val=   self._val+ other
            return    self._val









c=ccc()
print(      c+5+6   )