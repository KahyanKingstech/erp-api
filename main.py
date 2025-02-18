from fastapi import FastAPI
import api1, api2, api3  # Import the API modules

app = FastAPI()

# Include the routers from different API modules
app.include_router(api1.router, prefix="/module1")
app.include_router(api2.router, prefix="/module2")
app.include_router(api3.router, prefix="/module3")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}