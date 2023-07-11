import pytest
from app.schemas.product import Product, ProductInput


def test_product_schema():
    product = Product(
        name='Shirt Mike',
        slug='shirt-mike',
        price=22.99,
        stock=22
    )

    assert product.dict() == {
        'name': 'Shirt Mike',
        'slug': 'shirt-mike',
        'price': 22.99,
        'stock': 22
    }

def test_product_schema_invalid_slug():
    with pytest.raises(ValueError):
        product = Product(
            name='Shirt Mike',
            slug='shirt mike',
            price=22.99,
            stock=22
        )

    with pytest.raises(ValueError):
        product = Product(
            name='Shirt Mike',
            slug='shírt-mike',
            price=22.99,
            stock=22
        )

    with pytest.raises(ValueError):
        product = Product(
            name='Shirt Mike',
            slug='Shirt-mike',
            price=22.99,
            stock=22
        )    

def test_product_schema_invalid_price():
    with pytest.raises(ValueError):
        product = Product(
            name='Shirt Mike',
            slug='shirt-mike',
            price=0,
            stock=22
        )


def test_product_input_schema():
    product = Product(
        name='Shirt Mike',
        slug='shirt-mike',
        price=22.99,
        stock=22
    )

    product_input = ProductInput(
        category_slug='clothing',
        product=product
    )

    assert product_input.dict() == {
        "category_slug": "clothing",
        "product": {
            "name": "Shirt Mike",
            "slug": "shirt-mike",
            "price": 22.99,
            "stock": 22
        }
    }