from fastapi import APIRouter, Response, Depends, status
from sqlalchemy.orm import Session
from app.routes.deps import get_db_session
from app.use_cases.product import ProductUseCases
from app.schemas.product import Product, ProductInput


route_def = APIRouter(prefix='/product')


@route_def.post('/add')
def add_product(
    product_input: ProductInput,
    db_session: Session = Depends(get_db_session)
):
    uc = ProductUseCases(db_session=db_session)
    uc.add_product(
        product=product_input.product,
        category_slug=product_input.category_slug
    )

    return Response(status_code=status.HTTP_201_CREATED)

@route_def.put('/update/{id}', description='Update product')
def update_product(
    id: int,
    product: Product,
    db_session: Session = Depends(get_db_session)
):
    uc = ProductUseCases(db_session=db_session)
    uc.update_product(id=id, product=product)

    return Response(status_code=status.HTTP_200_OK)