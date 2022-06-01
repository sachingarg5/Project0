from service.validation_service import *
import pytest

@pytest.mark.parametrize("test_name, expected",(
    ("D",False),(" ",False),(".....",False),("sachin",True),("Tom",True),
    ("hdsdhfjdhfhdfsdffdfdfd",False),("    sfdf",False),("656545",False),("sachin ss",False),("fggam55",True)))
def test_validate_first_name(test_name,expected):
    assert validate_first_name(test_name)==expected


@pytest.mark.parametrize("test_name, expected",(
    ("D",False),(" ",False),(".....",False),("sachin",True),("Tom",True),
    ("hdsdhfjdhfhdfsdffdfdfd",False),("    sfdf",False),("656545",False),("sachin ss",False),("Sam55",True)))
def test_validate_last_name(test_name,expected):
    assert validate_last_name(test_name)==expected


@pytest.mark.parametrize("test_name, expected",(
    ("D",False),(" ",False),(".....",False),("sachin56",True),("Tom",False),
    ("hdsdhfjdhfhdfsdffdfdfd",False),("    sfdf",False),("656545",True),("sachin ss",False),("Samhid55",True),("_sdfdfdf",False),("shjfh_",False),(".67User",False)))
def test_validate_username(test_name,expected):
    assert validate_username(test_name)==expected

@pytest.mark.parametrize("test_name, expected",(
    ("D",False),(" ",False),(".....",False),("Aachin@56",True),("Tom",False),
    ("hdsdhfjdhfhdfsdffdfdfd",False),("    sfdf",False),("Ab_656545",True),("sachin ss",False),("Samhid#55",True),("_sdfdfdf",False),("shjfh_",False),(".67User",False)))
def test_validate_password(test_name,expected):
    assert validate_password(test_name)==expected

@pytest.mark.parametrize("test_name, expected",(
    ("D",False),(" ",False),(".....",False),("Aachin@56",False),("Heating",True),("25454544",False),
    ("hdsdhfjdhfhdfsdffdfdfd",True),(" need to move furniture",True),("Fix door and paint",True),("Heating",True),("roof fix",True),("H.V.A.C",True),("_sdfdfdf",False),("shjfh_",False),(".Shower",False)))
def test_validate_job_type(test_name,expected):
    assert validate_job_type(test_name)==expected

@pytest.mark.parametrize("test_name, expected",(
    ("D",False),(" ",False),(".....",False),("drill work@56",True),("Controller shows error",True),("length 25, height 45",True),
    ("hdsdhfjdhfhdfsdffdfdfd",True),("1524, green data rd. tx, Ontario, J9I 6U8",True),("Fix door and paint",True),("roof fix",True),("H.V.A.C",True),("_sdfdfdf",False),("shjfh_",False),(".Shower",False)))
def test_validate_job_description(test_name,expected):
    assert validate_description(test_name)==expected


def test_validate_job_budget():
    assert validate_budget(565)==True
    assert validate_budget(5565.56)==True
    assert validate_budget(-565)==False
    

@pytest.mark.parametrize("test_name, expected",(
    ("D",False),(" ",False),(".....",False),("Aachin@56",False),("1234567890",True),("25454544",False),
    ("hdsdhfjdhfhdfsdffdfdfd",False),("125&84",False),("#####",False),("+1112333155",False),("125.123.1251",False),("112-985-8958",False)))
def test_validate_contact_no(test_name,expected):
    assert validate_contact(test_name)==expected