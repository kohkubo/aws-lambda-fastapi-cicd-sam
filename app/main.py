from api.v1.api import router as api_router
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title='Serverless Lambda FastAPI')

app.include_router(api_router, prefix="/api/v1")


@app.get("/",  tags=["Endpoint Test"])
def main_endpoint_test():
    return {"message": "Welcome CI/CD Pipeline with GitHub Actions222!"}


handler = Mangum(app=app)
