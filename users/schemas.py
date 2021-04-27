from ninja import Schema

class UserRegister(Schema):
    # Lo que entra a la request
    first_name: str 
    last_name: str
    user_type: int
    date_of_birth: str
    email: str
    password: str
    created_at: str


class UserOut(Schema):
    # Lo que se entrega en la request
    id: int
    username: str
    name: str
    email: str
    user_type: str