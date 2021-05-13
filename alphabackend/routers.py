from ninja import NinjaAPI
from users.router import router as users_router
from properties.router import router as properties_router
from appointments.router import router as appointments_router
from communications.router import router as communications_router
from .security import UserAuth

api = NinjaAPI(auth=UserAuth())
api.add_router("/users", users_router, tags=["users"])# funciona igual con o sin slash
api.add_router("/properties", properties_router, tags=["properties"])
api.add_router("/appointments", appointments_router, tags=["appointments"])
api.add_router("/communications", communications_router, tags=["communications"])