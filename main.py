from fastapi import FastAPI # type: ignore
from routers import healthCheckControllr
from routers import cctvController
from routers import videoController

app = FastAPI()
app.include_router(healthCheckControllr.router)
app.include_router(cctvController.router)
app.include_router(videoController.router)

