from typing import Optional, Any
from util.util_generate import RandomNumber, RandomString
from beanie import Document
from model.model_default import AddressData
from typing import List
from faker import Faker
from model.request.request_company import CreateCompanyRequest 

fake = Faker()

class CompanyDocument(Document):    
    name: str
    initial: str
    address: AddressData
    tags: List[str]
    picName: str
    picEmail: str
    picPhone: str
    maxUser: int
    logoImage: str = None
    customKey: str = None
    smsGateway: str = None
    waGateway: str = None
    emailGateway: str = None    


    def __init__(self, **data: Any):
        super().__init__(**data)
        print('do my stuff...')

    class Collection:
        name = "tbl_company"

    class Config:
        schema_extra = {
            "example": {
                "name": "PT " + fake.name(),
                "initial": RandomString(2),
                "address": {"street": fake.address()},
                "tags": [],
                "picName": fake.name(),
                "picEmail": fake.first_name() + "@coba.com",
                "picPhone": "0813" + RandomNumber(6),
                "maxUser": 1000,
            }
        }


