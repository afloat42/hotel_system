# doctor_dao_test.py
# France Cheong
# 11/10/2021

"""
The code is this file is implemented as procedural code i.e. no OOP

The test is best done on an empty database as the doc_id used is 1
And it can be run more than once
"""

# Import the DAO
# From file xxx.py import class Xxxx
# Note: Filenames with hyphens cannot be imported, use underscores
from hotel_dao import HotelDAO

'''
Test the create() method of the DoctorDAO class
'''
def test_create():

    # Print info for debugging
    print("\n1. Test create a doctor ...") #\n means print("\n") a blank line    
        
    # Instantiate the doctor DAO
    hotel_dao = HotelDAO()

    # Setup the data as a dictionary
    # Note: USE YOUR OWN DATA FOR TESTING
    """
    data = {}
    #data['hotel_id'] = "" # No - do not pass any value for doc_id
    data['name'] = "Angelina"
    data['phonenumber'] = "0416673315"
    data['address'] = "27 edmondshaw drive"
    data['postcode'] = "3000"
    data['city'] = "melbourne"
    """

    # Alternatively, the data could be set up in JSON format
    # Do not pass any value for doc_id
    data = {
        'name':"Angelina",
        'phonenumber': "0416673315",
        'address'   : "27 edmondshaw drive",
        'postcode'  : "3000",
        'city'   :"melbourne" # no comma on last item
    }

    # Call the create() method from the DAO
    # and pass the dictionary as parameter
    result = hotel_dao.create(data)

    # Print the result
    print(result)


def test_find_by_id():

    # Print info for debugging
    print("\n2. Test find by id ...")   
   
    # Instantiate the doctor DAO
    hotel_dao = HotelDAO()

    # Assign an doc_id
    hotel_id = 1 # exists
    #doc_id = 2 # does not exist?
    
    result = hotel_dao.find_by_id(hotel_id)

    # Print the result
    print(result)
    

def test_find_all():

    # Print info for debugging
    print("\n3. Test find all ...")   
   
    # Instantiate the doctor DAO
    hotel_dao = HotelDAO()

    result = hotel_dao.find_all()

    # Print the result
    print(result)

 
def test_find_by_name():

    # Print info for debugging
    print("\n4. Test find by name  ...")   
        
    # Instantiate the doctor DAO    
    hotel_dao = HotelDAO()
      
    # Assign a lastname  
    name = "Angelina" # exists
    #lastname = "xyz" # does not exist

    result = hotel_dao.find_by_name(name)

    # Print the result
    print(result)

def test_find_ids():

    # Print info for debugging
    print("\n5. Test find ids ...")   

    # Instantiate the doctor DAO
    hotel_dao = HotelDAO()

    # Call the find_ids() method from the DAO
    result = hotel_dao.find_ids()

    # Print the result
    print(result)


def test_update():

    # Print info for debugging
    print("\n6. Test update hotel ...")   

    # Instantiate the doctor DAO
    hotel_dao = HotelDAO()

    # Assign an doc_id 
    hotel_id = 1 # exists
    #doc_id = 2 # does not exist?

    # Create a dictionary and add items
    # Do not add the doc_id to the dict
    data = {}
    data['name'] = "Angelina"
    data['phonenumber'] = "16673315"
    data['address'] = "30 edmondshaw drive"
    data['postcode'] = "3000"
    data['city'] = "deer park"
        
    # Call the update() method from the DAO
    # and pass the doc_id and data as parameters    
    result = hotel_dao.update(hotel_id, data)

    # Print the result
    print(result)


def test_delete():

    #Print info for debugging
    print("\n7. Test delete a hotel ...")   

    hotel_dao = HotelDAO()

    # Assign an hotel_id
    hotel_id = 1 # exists
    #doc_id = 2 # does not exist?

    # Call the delete() method from the DAO
    # and pass the doc_id as parameter - could pass it directly
    result = hotel_dao.delete(hotel_id)

    # Print the result
    print(result)


if __name__ == "__main__":

    # You may wish to comment/uncomment the functions calls below
    # To select which ones to run or not to run

    # If you run test_create() twice in a row
    # You will try to insert the same record twice
    # You Will get an integrity error
    # Phone number has to be unique
    # Either comment out test_create() (to run the other function calls)
    # Or use DB Browser for SQLite to delete the record

    # You may want to run test_delete() last
    # Because if you delete the record as soon as you insert
    # You cannot run the other tests like test_find_by_id(), test_update()

    # Use DB Browser for SQLite to check if data was really inserted/updated/deleted

    # If the database is opened in DB Browser for SQLite, 
    # you might not run the tests as the database will be locked
    # Need to close the database in DB Browser for SQLite

    print("\nTesting Doctor DAO ...")
    print("Please ensure that you perform the tests on a blank database ...")
    print("First delete 'medical_centre.db' then run 'python create_tables.py' to create a blank database")

    print()
    input("Press Enter to continue or Ctrl+C to cancel ...")

    # 1. Test create method from doctor_dao.py
    test_create()
    
    # 2. Test find by id method from doctor_dao.py
    test_find_by_id()

    # 3. Test find all method from doctor_dao.py
    test_find_all()

    # 4. Test find by lastname method from doctor_dao.py
    test_find_by_name()

    # 5. Test find ids method from doctor_dao.py
    test_find_ids()

    # 6. Test update method from doctor_dao.py
    test_update()

    #7. Test delete method from doctor_dao.py
    test_delete()

    print("\nAll done!") 

    print("\nPlease use DB Browser for SQLite to check the database!") 