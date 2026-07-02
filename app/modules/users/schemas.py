from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):

    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):

    email: EmailStr | None = None 