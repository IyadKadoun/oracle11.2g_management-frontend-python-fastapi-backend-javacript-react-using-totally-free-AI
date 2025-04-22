from fastapi import FastAPI
from .routers import jabicenter, collector, clearancetyp
from .database import Base, engine

from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(jabicenter.router)
app.include_router(collector.router)
app.include_router(clearancetyp.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)