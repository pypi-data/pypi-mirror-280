class DotDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

    def __call__(self, key, *args, **kwargs):
        print("key            :", key)
        ret=self.__getitem__(key)(*args, **kwargs)
        return ret


def func111():
    print("ctx            :", 111)


def func222():
    print("ctx            :", 222)


fff333 = DotDict({
    "aaa": 111,
    "read": func111,
    "write": func222,
})

fff333("read")()  # Output: ctx            : 111
fff333("write")()  # Output: ctx            : 222
fff333("read")().func111()  # Output: ctx            : 111
