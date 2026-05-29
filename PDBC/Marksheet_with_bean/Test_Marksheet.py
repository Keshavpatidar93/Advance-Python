from Marksheet_Bean import *
from Marksheet_Model import *

def test_insert():
    bean = Marksheet_Bean()
    bean.set_roll_no(121)
    bean.set_name("Sunil")
    bean.set_phy(89)
    bean.set_che(95)
    bean.set_maths(79)

    model =  Marksheet_Model()
    model.insert(bean)

def test_update():
    param ={'id':8,'roll_no':108,'name':'faaa','phy':78,'che':67,'maths':89}
    model = Marksheet_Model()
    model.update(param)

def test_delete():
    model = Marksheet_Model()
    model.delete(21)

def test_get():
    model = Marksheet_Model()
    list = model.get(14)
    for i in list:
        print(i)

def test_find_by_roll():
    model = Marksheet_Model()
    list = model.find_by_roll(116)
    for i in list:
        print(i)

def test_search():
    param = {'id': 0, 'roll_no': 0, 'name': 'r', 'phy': 0, 'che': 0, 'maths': 0,'page_no':1,'page_size':2}
    model = Marksheet_Model()
    list = model.search(param)
    for i in list:
        print(i)



#test_insert()
#test_update()
#test_delete()
#test_get()
#test_find_by_roll()
test_search()