from django.shortcuts import render

from main.models import Experience, Skill, Projects


def show_main(request):
    context = {
        "name": "Velicia Willy",
        "npm": "2506657384",
        "study_program": "Computer Science",
        "bio": (
            "CS Student at Universitas Indonesia trying to earn money by"
            "becoming a teaching assistant."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Velicia Willy",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_skill(request):
    context = {
        "name": "Velicia Willy",
        "skill_list": Skill.objects.all(),
    }
    return render(request, "skill.html", context)

def show_projects(request):
    context = {
        "name": "Velicia Willy",
        "projects_list": Projects.objects.all(),
    }
    return render(request, "projects.html", context)