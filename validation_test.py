# validation_test.py
# France Cheong
# 20/12/2018

# Import file/class to test
from validation import Validation


def test_is_numeric(validation):
    print("\n1.Testing is_numeric()") 
    
    # True
    assert (validation.is_numeric(10))

    # False
    assert (not validation.is_numeric(10.002))
    assert (not validation.is_numeric("abc"))
    assert (not validation.is_numeric("10abc"))

def test_is_alphabetic(validation):
    print("\n2. Testing is_alphabetic()")

    # True
    assert (validation.is_alphabetic("abc"))

    # False
    assert (not validation.is_alphabetic(10))    
    assert (not validation.is_alphabetic(10.002)) 
    assert (not validation.is_alphabetic("10abc"))

def test_is_alphanumeric(validation):
    print("\n3. Testing is_alphanumeric()")

    # True
    assert (validation.is_alphanumeric(10))  
    assert (validation.is_alphanumeric("abc")) 
    assert (validation.is_alphanumeric("10abc")) 

    # False 
    assert (not validation.is_alphanumeric(10.02))
    assert (not validation.is_alphanumeric("_")) 
    assert (not validation.is_alphanumeric(" "))
    assert (not validation.is_alphanumeric(".")) 

def test_is_phone_number(validation):
    print("\n4. Testing is_phone_number()")

    # True
    assert (validation.is_phone_number("02 9999 9999")) 

    # False
    assert (not validation.is_phone_number("(02) 9999 9999"))
    assert (not validation.is_phone_number("0299999999"))
    assert (not validation.is_phone_number("02-9999-9999"))
    assert (not validation.is_phone_number("02.9999.9999"))
    assert (not validation.is_phone_number("+61 2 9999 9999"))
    assert (not validation.is_phone_number("0413 888 888"))

def test_is_email(validation):
    print("\n5. Testing is_email()")

    # True
    assert  (validation.is_email("xyz@abc.def")) 
    assert (validation.is_email("xyz@abcdef"))

    # False
    assert (not validation.is_email("xyzabcdef"))
    assert (not validation.is_email("@abcdef"))

def test_is_dob(validation):
    print("\n6. Testing is_dob()")

    # True
    assert (validation.is_dob("10/01/2000"))
    assert (validation.is_dob("12/12/1990"))
    assert (validation.is_dob("05/09/1985"))
    assert (validation.is_dob("24/09/2001"))


    # False
    assert (not validation.is_dob("02/30/2000"))
    assert (not validation.is_dob("32/09/1990"))

def test_is_creditCardNo(validation):
    print("\n7. Testing is_creditCardNo()")

    # True
    assert (validation.is_creditCardNo("1111222233334444"))
    assert (validation.is_creditCardNo("1111-2222-3333-4444"))

    # False
    assert (not validation.is_creditCardNo("1111-2222-3333-444"))   
    assert (not validation.is_creditCardNo("1111 2222 3333 444"))
    assert (not validation.is_creditCardNo("111122223333444X"))
    

def test_is_cardExpiry(validation):
    print("\n8. Testing is_cardExpiry()")

    # True
    assert (validation.is_cardExpiry("05/23"))
    assert (validation.is_cardExpiry("12/22"))

    # False
    assert (not validation.is_cardExpiry("5/23"))  # Missing leading 0 in month
    assert (not validation.is_cardExpiry("00/22")) # Month out of range
    assert (not validation.is_cardExpiry("12/5"))  # Missing leading 0 in year
    assert (not validation.is_cardExpiry("12/2022")) # Too many digits in year
    assert (not validation.is_cardExpiry("12/2")) # Too few digits in year
    assert (not validation.is_cardExpiry("12/22/23")) # Invalid format

def test_is_date(validation):
    print("\n8. Testing is_date()")
    # Valid dates
    assert (validation.is_date("02-28-2022"))
    assert (validation.is_date("12-31-2021"))

    # Invalid dates
    assert (not validation.is_date("2022-02-28"))
    assert (not validation.is_date("31-12-2021"))
    assert (not validation.is_date("02/28/2022"))


if __name__ == '__main__':
    
    print("\nTesting ...")

    # Instantiate a validation object
    validation = Validation()

    test_is_numeric(validation)

    test_is_alphabetic(validation)

    test_is_alphanumeric(validation)

    test_is_phone_number(validation)

    test_is_email(validation)

    test_is_dob(validation)

    test_is_creditCardNo(validation)

    test_is_cardExpiry(validation)