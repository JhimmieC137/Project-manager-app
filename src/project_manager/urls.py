from rest_framework.routers import SimpleRouter

from src.project_manager.views import *

projects_router = SimpleRouter()

projects_router.register(r'projects', ProjectsViewSet)