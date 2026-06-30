from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from quantum_core.database.session import get_db

from quantum_core.users.service import UserService
from quantum_core.users.schemas import (
    UserResponse,
    UserUpdate
)

from quantum_core.core.responses import APIResponse


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = (
        UserService
        .get_by_id(
            db,
            user_id
        )
    )

    return APIResponse.success(
        data=UserResponse.from_orm(user)
    )


@router.patch("/{user_id}")
def update_user(
    user_id: int,
    body: UserUpdate,
    db: Session = Depends(get_db)
):

    user = (
        UserService
        .update(
            db,
            user_id,
            body.email
        )
    )

    return APIResponse.success(
        message="User updated",
        data=UserResponse.from_orm(user)
    )


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    UserService.delete(
        db,
        user_id
    )

    return APIResponse.success(
        message="User deleted"
    )