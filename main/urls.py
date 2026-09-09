from django.urls import path

from main.views import show_main, show_experience, show_skill, show_projects

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("skill/", show_skill, name="show_skill"),
    path("projects/", show_projects, name="show_projects"),
]