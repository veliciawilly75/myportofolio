from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from main.models import Experience, Skill, Projects
from main.forms import ProjectForm, ExperienceForm, SkillForm
import datetime
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Projects.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "project_url": project.link,
                "link_available": project.link_available,
                "status": project.status,
                "type": project.type,
                "is_solo": project.is_solo,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
                "is_editor": is_editor(request),
            }
        })

    return JsonResponse(data, safe=False)

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

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def create_skill(request):
    if not request.user.is_superuser:
            raise PermissionDenied
        
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

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
            raise PermissionDenied
        
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
    last_login = request.COOKIES.get('last_login', 'No login session yet / Cookie not found')

    context = {
        "name": "Velicia Willy",
        "npm": "2506657384",
        "study_program": "Bachelor's Degree in Computer Science",
        "bio": (
            "CS Student at Universitas Indonesia trying to earn money by "
            "becoming a teaching assistant."
        ),
        "last_login":last_login,
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
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Velicia Willy",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "projects.html", context)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
            raise PermissionDenied
        
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience successfully deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_skill")

@login_required(login_url="/login/")
def delete_skill(request, skill_id):
    if not request.user.is_superuser:
            raise PermissionDenied
        
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill successfully deleted!")
        return redirect("main:show_skill")

    return redirect("main:show_skill")

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
            raise PermissionDenied
        
    project = get_object_or_404(Projects, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project successfully deleted!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def update_project(request, project_id):
    if not (request.user.is_superuser or is_editor(request)):
            raise PermissionDenied
        
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

@login_required(login_url="/login/")
def update_skill(request, skill_id):
    if not (request.user.is_superuser or is_editor(request)):
            raise PermissionDenied
        
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

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not (request.user.is_superuser or is_editor(request)):
            raise PermissionDenied
        
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

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account successfully made. Please login.")
        return redirect("main:login")

    context = {
        "name": "Velicia Willy",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Velicia Willy",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Projects, id=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def experience_toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, id=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

def is_editor(request):
     return request.user.groups.filter(name='Editor').exists()

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)