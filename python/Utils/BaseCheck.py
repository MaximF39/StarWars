

class BaseCheck:

    def __init__(self):
        for k, v in self.base_check.items():
            if not isinstance(getattr(self, k), eval(v)):
                raise TypeError(f"{k} is not a type {v}")
        # if hasattr(self, "base_check"):
        #     if isinstance(self.base_check, dict):
        #         for k, v in self.base_check.items():
        #             if not isinstance(getattr(self, k), eval(v)):
        #                 raise TypeError(f"{k} is not a type {v}")
        #     else:
        #         raise TypeError('base_check is not a type dict')
        # else:
        #     raise NameError("name base_check is not defined")

class m(BaseCheck):
    base_check = ['sss', 'sss']
    def __init__(self):
        BaseCheck.__init__(self)

m()
