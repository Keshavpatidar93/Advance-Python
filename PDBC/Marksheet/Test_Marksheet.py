from Marksheet_Model import Marksheet_Model

def test_next_primary_key():
    model = Marksheet_Model()
    pri_key = model.next_Primary_Key()
    assert isinstance(pri_key,int)
    assert pri_key > 0
    print(f"Next Primary key is : {pri_key}")

def test_insert():
    obj = Marksheet_Model()
    data = {'id':21,'roll_no': 121,'name':'Raghav','phy':56,'che':78,'maths':45}
    obj.insert(data)

def test_update():
    obj = Marksheet_Model()
    data = {'id':13,'roll_no': 113,'name':'Vinod','phy':56,'che':78,'maths':45}
    obj.update(data)

def test_delete():
    obj = Marksheet_Model()
    obj.delete(21)

def test_get():
    model = Marksheet_Model()
    model.get(7)

def test_Find_by_roll():
    model = Marksheet_Model()
    model.Find_by_roll(112)

def test_search_data():
    model = Marksheet_Model()
    data = {'id':0,'roll_no': 0,'name':'r','phy':0,'che':0,'maths':0,'page_no':2,'page_size':2}
    model.search(data)



#test_next_primary_key()
#test_insert()
#test_update()
#test_delete()
#test_get()
#test_Find_by_roll()
test_search_data()