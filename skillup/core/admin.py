from django.contrib import admin
from .models import Profile, Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
   list_display = ('id', 'skill_name', 'user')  # remove 'rating'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
   list_display = ('id', 'user', 'name', 'email')
