from fastapi import FastAPI

from quantum_core.core.config import settings
from quantum_core.core.responses import APIResponse 

from quantum_core.core.exceptions import (
    AppException,
    app_exception_handler,
    generic_exception_handler
)

# Create FastAPI application instance
app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

app.add_exception_handler(
    AppException,
    app_exception_handler
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)

# Root endpoint (system check)
@app.get("/")
def root():
    return APIResponse.success(
        message="Quantum Core running",
        data={
            "version": "1.0.0"
        }
    )


# Health check endpoint
@app.get("/health")
def health():
    return APIResponse.success(
        message="System healthy"
    )