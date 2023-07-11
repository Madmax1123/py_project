import pytest
from app.schemas.category import Category


def test_category_schema():
    category = Category(
        name='Clothing',
        slug='clothing'
    )

    assert category.dict() == {
        'name': 'Clothing',
        'slug': 'clothing'
    }


def test_category_schema_invalid_slug():
    with pytest.raises(ValueError):
        category = Category(
            name='Clothing',
            slug='bed clothing'
        )

    with pytest.raises(ValueError):
        category = Category(
            name='Clothing',
            slug='Clothing'
        )

    
    with pytest.raises(ValueError):
        category = Category(
            name='Clothing',
            slug='clóthing'
        )    