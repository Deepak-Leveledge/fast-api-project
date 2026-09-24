from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth,routes_predict
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers


app = FastAPI(title="Car price Prediction ")

#Link Middelware
app.add_middleware(LoggingMiddleware)

#Link Routes
app.include_router(routes_auth.router,tags=['Auth'])
app.include_router(routes_predict.router , tags=['Prediction'])

#Monitoring 
Instrumentator().instrument(app).expose(app)

#add expection
register_exception_handlers(app)