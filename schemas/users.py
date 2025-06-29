from pydantic import BaseModel



class ProfileSchemas(BaseModel):
    first_name: str
    last_name: str