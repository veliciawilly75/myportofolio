from django.urls import path

from main.views import (
   show_main,
   show_experience,
   show_skill,
   show_projects,
   create_project,
   create_experience,
   create_skill,
   get_projects_json,
   delete_project,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("skill/", show_skill, name="show_skill"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("experience/add/", create_experience, name="create_experience"),
    path("skill/add/", create_skill, name="create_skill"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
]