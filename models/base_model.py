#!/usr/bin/python3
#Base class 
import uuid
from datetime import datetime
class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4().hex
        self.created_at = datetime.now()
        self.updated_at = datetime.now()    
    def __str__(self) -> str:
        print(id)
        
