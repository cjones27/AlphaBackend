from ninja import NinjaAPI
from users.router import router as users_router
from properties.router import router as properties_router
from appointments.router import router as appointments_router

api = NinjaAPI()
api.add_router("/users", users_router, tags=["users"])# funciona igual con o sin slash
api.add_router("/properties", properties_router, tags=["properties"])
api.add_router("/appointments", appointments_router, tags=["appointments"])