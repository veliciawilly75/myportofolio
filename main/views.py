from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Experience, Skill, Projects
from main.forms import ProjectForm, ExperienceForm, SkillForm

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Projects.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def get_skills_json(request):
    title_query = request.GET.get("title", "").strip()
    skills = Skill.objects.all()

    if title_query:
        skills = skills.filter(title__icontains=title_query)

    skills_json = serializers.serialize("json", skills)
    return HttpResponse(skills_json, content_type="application/json")

def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience successfully added!")
        return redirect("main:show_experience")

    context = {
        "name": "Velicia Willy",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def create_skill(request):
    form = SkillForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New skill successfully added!")
        return redirect("main:show_skill")

    context = {
        "name": "Velicia Willy",
        "form": form,
    }
    return render(request, "skill_form.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New project successfully added!")
        return redirect("main:show_projects")

    context = {
        "name": "Velicia Willy",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def show_main(request):
    context = {
        "name": "Velicia Willy",
        "npm": "2506657384",
        "study_program": "Bachelor's Degree in Computer Science",
        "bio": (
            "CS Student at Universitas Indonesia trying to earn money by "
            "becoming a teaching assistant."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experiences_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Velicia Willy",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def show_skill(request):
    json_response = get_skills_json(request)

    skills = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    skills = [skill.object for skill in skills]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Velicia Willy",
        "skill_list": skills,
        "title_query": title_query,
    }
    return render(request, "skill.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Velicia Willy",
        "projects_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience successfully deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_skill")

def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill successfully deleted!")
        return redirect("main:show_skill")

    return redirect("main:show_skill")

def delete_project(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project successfully deleted!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def update_project(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project successfully updated!")
        return redirect("main:show_projects")
    
    context = {
        "name": "Velicia Willy",
        "form": form,
        "project": project,
    }
    return render(request, "components/project_update.html", context)

def update_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    form = SkillForm(request.POST or None, instance=skill)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Skill successfully updated!")
        return redirect("main:show_skill")
    
    context = {
        "name": "Velicia Willy",
        "form": form,
        "skill": skill,
    }
    return render(request, "components/skill_update.html", context)

def update_experience(request, experience_id):
    experience = get_object_or_404(Experience, id=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience successfully updated!")
        return redirect("main:show_experience")
    
    context = {
        "name": "Velicia Willy",
        "form": form,
        "experience": experience,
    }
    return render(request, "components/experience_update.html", context)