import uvicorn  
from app import fastapi_app



if __name__ == "__main__":

    uvicorn.run("main:fastapi_app")
