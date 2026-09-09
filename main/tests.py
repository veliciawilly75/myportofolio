from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Skill


class MainTest(TestCase):
    def setUp(self):
        # Initiate experience object
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )
        # Initiate skill object
        self.skill = Skill.objects.create(
            title="Coding in C",
            level="beginner",
        )

    # Test main page
    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_skill")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    # Test experience model and page
    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Ongoing")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Currently none")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Ended")
        self.assertNotContains(response, "Ongoing")

    # Test skill model and page
    def test_skill_model(self):
        self.assertEqual(str(self.skill), "Coding in C")
        self.assertEqual(self.skill.level, "beginner")
        self.assertFalse(self.skill.prioritize)
        self.assertFalse(self.skill.highlight)

    def test_skill_page(self):
        response = self.client.get(reverse("main:show_skill"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skill.html")
        self.assertContains(response, self.skill.title)
        self.assertContains(response, "Beginner")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_skill_page(self):
        Skill.objects.all().delete()
        response = self.client.get(reverse("main:show_skill"))

        self.assertContains(response, "Currently none")

    def test_highlighted_skill(self):
        self.skill.level = 'advanced'
        self.skill.save()

        self.assertTrue(self.skill.highlight)
        self.assertFalse(self.skill.prioritize)

    def test_prioritized_skill(self):
        self.skill.level = 'upper-intermediate'
        self.skill.save()
    
        self.assertTrue(self.skill.prioritize)
        self.assertFalse(self.skill.highlight)

    def test_certif_unavailable(self):
        response = self.client.get(reverse("main:show_skill"))
        
        self.assertContains(response, "Certification unavailable")