import pytest
from app.db.connection import Session
from app.db.models import Category as CategoryModel
from app.db.models import Product as ProductModel


@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()


@pytest.fixture()
def categories_on_db(db_session):
    categories = [
        CategoryModel(name='Clothing', slug='clothing'),
        CategoryModel(name='Car', slug='car'),
        CategoryModel(name='Kitchen itens', slug='kitchen-itens'),
        CategoryModel(name='Decoration', slug='decoration')
    ]

    for category in categories:
        db_session.add(category)
    db_session.commit()

    for category in categories:
        db_session.refresh(category)
    
    yield categories

    for category in categories:
        db_session.delete(category)
    db_session.commit()


@pytest.fixture()
def product_on_db(db_session):
    category = CategoryModel(name='Car', slug='car')
    db_session.add(category)
    db_session.commit()

    product = ProductModel(
        name='Shirt Abibas',
        slug='shirt-abibas',
        price=100.99,
        stock=20,
        category_id=category.id
    )

    db_session.add(product)
    db_session.commit()

    yield product

    db_session.delete(product)
    db_session.delete(category)
    db_session.commit()