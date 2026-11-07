from django.forms import ModelForm, TextInput, Textarea, URLInput, RadioSelect, DateTimeInput

from main.models import Experience, Skill, Projects

from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Experience name",
            "description": "Experience description",
            "category": "Experience category",
            "started_at": "Experience started at",
            "ended_at": "Experience ended at",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Internship",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your experience",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "internship/research/volunteer/part-time/full-time/freelance",
                    "maxlength": 255,
                }
            ),
            "started_at": DateTimeInput(),
            "ended_at": DateTimeInput(),
        }
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Experience name can't only contain HTML tags.")
        return title
    
    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

class SkillForm(ModelForm):
    class Meta:
        model = Skill

        fields = [
            "title",
            "level",
            "certification",
        ]

        labels = {
            "title": "Skill name",
            "level": "Skill level",
            "certification": "Skill certification",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Django",
                    "maxlength": 255,
                }
            ),
            "level": TextInput(
                attrs={
                    "placeholder": "beginner/intermediate/upper-intermediate/advanced/expert",
                    "maxlength": 255,
                }
            ),
            "certification": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Skill name can't only contain HTML tags.")
        return title
    
    def clean_level(self):
        return strip_tags(self.cleaned_data["level"]).strip()

class ProjectForm(ModelForm):
    class Meta:
        model = Projects

        fields = [
            "title",
            "description",
            "status",
            "type",
            "link",
        ]

        labels = {
            "title": "Project name",
            "description": "Project description",
            "status": "Project status",
            "type": "Project type",
            "link": "Project URL",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your project",
                    "rows": 3,
                }
            ),
            "status": TextInput(
                attrs={
                    "placeholder": "ongoing/finished",
                    "maxlength": 255,
                }
            ),
            "type": TextInput(
                attrs={
                    "placeholder": "solo/team",
                    "maxlength": 255,
                }
            ),
            "link": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Project name can't only contain HTML tags.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()