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

    def __getitem__(self,item):
        print(222, item )
        return self

    @property
    def a(self):
        return self


    @property
    def b(self):
        return self

    def __call__(self,*args,**kwargs):
        return self


c=calc()
print(      c+111+222   )
# print(      c+111+"222"   )
c[""][9999][:][...][:,:]

c.a.b

# ====================================================


def f(*arg):
    print(arg)
    if arg == "":
        ...
    return f

f("唱歌")("跳舞")