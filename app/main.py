from fastapi import FastAPI
from app.routes.category_routes import routes as category_routes
from app.routes.product_routes import route_def as product_routes

app = FastAPI()
@app.get('/noob')
def check():
    return True 


app.include_router(category_routes)
app.include_router(product_routes)