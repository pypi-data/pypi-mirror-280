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

    def __getattr__(self,item):
        return self


    def __truediv__(self,item):
        return self
    
    def __floordiv__(self,item):
        return self


# https://www.bilibili.com/video/BV1x1421C7bM/

# https=www=com=index=baodu=html=calc()
https=www=index=calc()
https//www.baodu.com/index.html
