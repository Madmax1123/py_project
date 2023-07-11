from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.schemas.category import Category
from app.routes.deps import get_db_session
from app.use_cases.category import CategoryUseCases


routes = APIRouter(prefix='/category', tags=['Category'])


@routes.post('/add')
def add_category(
    category: Category,
    db_session: Session = Depends(get_db_session)
):
    uc = CategoryUseCases(db_session=db_session)
    uc.add_category(category=category)
    return Response(status_code=status.HTTP_201_CREATED)


@routes.get('/list')
def list_categories(
    db_session: Session = Depends(get_db_session)
):
    uc = CategoryUseCases(db_session=db_session)
    response = uc.list_categories()

    return response


@routes.delete('/delete/{id}')
def delete_category(
    id: int,
    db_session: Session = Depends(get_db_session)
):
    uc = CategoryUseCases(db_session=db_session)
    uc.delete_category(id=id)

    return Response(status_code=status.HTTP_200_OK)