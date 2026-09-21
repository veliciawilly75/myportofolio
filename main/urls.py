from django.urls import path

from main.views import (
   show_main,
   show_experience,
   show_skill,
   show_projects,
   create_project,
   create_experience,
   create_skill,
   update_project,
   update_skill,
   update_experience,
   get_projects_json,
   get_skills_json,
   get_experiences_json,
   delete_project,
   delete_skill,
   delete_experience,
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
    path("projects/<uuid:project_id>/update/", update_project, name="update_project"),
    path("skill/<uuid:skill_id>/update/", update_skill, name="update_skill"),
    path("experience/<uuid:experience_id>/update/", update_experience, name="update_experience"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("api/skill/", get_skills_json, name="get_skills_json"),
    path("api/experience/", get_experiences_json, name="get_experiences_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path("skill/<uuid:skill_id>/delete/",delete_skill,name="delete_skill"),
    path("experience/<uuid:experience_id>/delete/",delete_experience,name="delete_experience"),
]