from fastapi import FastAPI

from quantum_core.core.config import settings
from quantum_core.core.responses import APIResponse 



# Create FastAPI application instance
app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
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