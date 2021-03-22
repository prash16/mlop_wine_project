import pytest 

class NotInRange(Exception):
    #input_
    def __init__(self,message="value not in range"):
        #self.input=input_
        self.message= message
        super().__init__(self.message)
        
    pass

def test_generic():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange

### Other example for pytest ..panda function do assertion 

def test_someting_test():
    a=2
    b=2
   
    assert a==b


# def test_generic():
#     a = 2
#     b = 2
#     assert a == b