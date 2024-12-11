from fastapi import FastAPI
from routers.products import router  # Import the routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registering the routes
app.include_router(router)

"""
FastAPI application setup for a product inventory system.

This FastAPI app sets up the core application, including CORS (Cross-Origin 
Resource Sharing) middleware to allow requests from specified origins. It 
also includes the product-related API routes by importing and including 
them from the `products` router module.

Attributes:
    origins (list): A list of allowed origins that can make requests to the 
                     API. In this case, it allows requests from the 
                     'http://localhost:8000' domain.

Methods:
    add_middleware: Adds the CORS middleware to the app to enable 
                    cross-origin requests.
    include_router: Registers the product-related API routes with the app.

Example:
    To run this FastAPI application, use the following command:
        uvicorn main:app --reload

    The application will accept API requests from the specified origins 
    and route product-related operations accordingly.
"""

