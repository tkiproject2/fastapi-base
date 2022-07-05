from decimal import Decimal
from fastapi.exceptions import HTTPException
from bson.decimal128 import Decimal128 
import re
from util.util_validate import ValidatePhoneNumber

class PhoneStr(str):
    # phonn = ValidPhoneNumber(str(v))
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):         
        v = str(v).replace("+62", "0")
        v = str(v).replace(" ", "")
        v = str(v).replace("-", "")
        if v[0:2] == "62":
            v = "0" . v[3:len(v)]

        phonnInt = False

        try:
            phonnInt = ValidatePhoneNumber(v)
        except:
            raise HTTPException(status_code=400, detail=str(v) + " Not a valid Phone Number")
        
        if phonnInt != False:
            return str(v)
        else:
            raise HTTPException(status_code=400, detail=str(v) + " Not a valid Phone Number")

class RealStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v): 
               
        if type(v) != str:            
            try:
                if type(v) == float:
                    v = str(int(v))
                    v = str(v).replace(".0", "")
                else:
                    v = str(v)
                
            except:
                raise HTTPException(status_code=400, detail="Not a valid String")    
        if not isinstance(v, str):
            raise HTTPException(status_code=400, detail="Not a valid String")
        if not v:
            if v.isdecimal():
                return str(v).replace(".0", "")
            else:
                return str(v)
                  
        if bool(re.compile('^[a-zA-Z\d\.\,\&\-\#\_\()\'\\/@\s]+$').match(v)):            
            if v.isdecimal():
                return str(v).replace(".0", "")
            else:
                return str(v)
        else:
            print(v) 
            raise HTTPException(status_code=400, detail=str(v) + " Unallowed character")

class DecimalStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):        
        if type(v) == str:
            try:
                v = Decimal128(v)
            except:
                raise HTTPException(status_code=400, detail="Not a valid Decimal Type")    
        elif type(v) == bool:
            try:
                v = Decimal128("0")
            except:
                raise HTTPException(status_code=400, detail="Not a valid Decimal Type")   
        elif type(v) == Decimal:
            try:
                v = Decimal128(str(v))
            except:
                raise HTTPException(status_code=400, detail="Not a valid Decimal Type")   
        elif type(v) == float:
            try:
                v = Decimal128(str(v))
            except:
                raise HTTPException(status_code=400, detail="Not a valid Decimal Type")   
        elif type(v) == int:
            try:
                v = Decimal128(str(v))
            except:
                raise HTTPException(status_code=400, detail="Not a valid Decimal Type")         
        if not isinstance(v, Decimal128):            
            raise HTTPException(status_code=400, detail="Not a valid Decimal Type")
        return float(str(v))