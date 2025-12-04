from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.db import models
from .models import Profile, Skill
from .forms import RegisterForm, LoginForm, SkillForm, ResumeUploadForm


# Home
def home(request):
   return render(request, "home.html")


# Register
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")

        # CREATE USER ⭐
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Registered Successfully")
        return redirect("login")  # redirect to login page

    return render(request, "register.html")


# Login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect("dashboard")  # your dashboard page
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login")

    return render(request, "login.html")

# Logout
@login_required
def logout_user(request):
   logout(request)
   return redirect("login")


# Dashboard
def dashboard(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    skills = Skill.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"profile": profile, "skills": skills})




# Add skill
@login_required
def add_skill(request):
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            messages.success(request, "Skill added successfully!")
            return redirect("dashboard")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SkillForm()
    return render(request, "add_skill.html", {"form": form})

# Edit skill
@login_required
def edit_skill(request, id):
   skill = get_object_or_404(Skill, id=id, user=request.user)
   if request.method == "POST":
       form = SkillForm(request.POST, instance=skill)
       if form.is_valid():
           form.save()
           messages.success(request, "Skill updated successfully!")
           return redirect("dashboard")
       else:
           messages.error(request, "Please fix errors in the form.")
   else:
       form = SkillForm(instance=skill)
   return render(request, "edit_skill.html", {"form": form})


# Delete skill
@login_required
def delete_skill(request, id):
   skill = get_object_or_404(Skill, id=id, user=request.user)
   skill.delete()
   messages.success(request, "Skill deleted successfully!")
   return redirect("dashboard")


# Career suggestion
@login_required
def career_suggestions(request):
    skills = Skill.objects.filter(user=request.user)

    # Convert to one big lowercase string for easy matching
    skills_text = " ".join([s.skill_name.lower() for s in skills])

    suggestions = []

    if "python" in skills_text and "django" in skills_text:
        suggestions.append("Full Stack Developer")
        suggestions.append("Backend Developer")

    if "python" in skills_text and "machine" in skills_text:
        suggestions.append("Machine Learning Engineer")
        suggestions.append("Data Scientist")

    if "flask" in skills_text:
        suggestions.append("Python Backend Developer")

    if "html" in skills_text and "css" in skills_text and "javascript" in skills_text:
        suggestions.append("Frontend Developer")

    if not suggestions:
        suggestions.append("Keep improving your skills, baby ❤️")

    return render(request, "career_suggestions.html", {
        "skills": skills,
        "suggestions": suggestions
    })

# Upload CV (uses Profile.resume)
@login_required
def upload_resume(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ResumeUploadForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Resume uploaded successfully!")
            return redirect("upload_resume")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ResumeUploadForm(instance=profile)
    return render(request, "upload_cv.html", {"form": form})


@login_required
def admin_analytics(request):
    total_users = User.objects.count()
    total_skills = Skill.objects.count()

    # GROUP SKILLS BY NAME & COUNT THEM
    popular_skills = (
        Skill.objects
        .values('skill_name')
        .annotate(count=Count('skill_name'))
        .order_by('-count')
    )

    return render(request, 'admin_analytics.html', {
        'total_users': total_users,
        'total_skills': total_skills,
        'popular_skills': popular_skills,
    })
