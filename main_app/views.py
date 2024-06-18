from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user , logout
from django.contrib.auth.models import User

from .models import Exams, Context


from .questiongenerator import QuestionGenerator
# Create your views here.
def index(request):
    return render(request , "home.html")

def login(request):
    if request.method == "POST":
        username = str(request.POST.get('username')) 
        password = str(request.POST.get('password'))

        user = authenticate(username=username,password=password)
        print(user)
        
        if user is not None:
            login_user(request, user)
            messages.success(request , "Logged In Successfully.")
            return render(request, "home.html", {'name':username})
        if user is None:
            messages.error(request, "Bad credentials")

    return render(request , "login.html")


def signup(request):
    username = str(request.POST.get('username')) 
    password = str(request.POST.get('password'))
    email = str(request.POST.get('email')) 

    if request.method == "POST":
        if User.objects.filter(username=username).first():
            messages.error(request, "This username is not available")
            return redirect("/signup")
        
        myuser = User.objects.create_user(username,email,password)         
        myuser.is_active = True

        myuser.save()

        messages.success(request, "Account Created Successfully Please Login")
        return redirect('/login')
    return render(request , "signup.html")

def logoutuser(request):
    logout(request)
    return redirect('/')

def generate(request):
    if request.method == "POST":
        messages.success(request, "Creating Exam Paper please wait..")
        course = str(request.POST.get('course'))
        name_paper = str(request.POST.get('name_exam'))
        exam_type = str(request.POST.get('exam_type'))
        level = str(request.POST.get('dif_lvl'))
        paper  = Exams()
        
        paper.course = course
        paper.name = name_paper
        paper.Exam_Type = exam_type
        paper.Difficulty_Level = level
        paper.user = request.user


        data = Context()
        course_av = data.__class__.objects.all()
        for c in course_av:
            if c.course == course:
                qg = QuestionGenerator()
                questions =qg.generate(c.data , num_questions=5) 
                print(questions)
                toadd = ""
                for question in questions:
                    toadd = toadd + question['question'] +","
                paper.questions = toadd
        paper.save()   
        return redirect('/exam_portal')
    return render(request , "generate.html")


def portal(request):
    messages.success(request, "Your Paper is ready...")
    papers = Exams()
    paper= papers.__class__.objects.all()
    context = {}
    arr = []
    # print(p.questions)
    l =0
    for i in paper:
        l = l +1
    q = ""
    for i in paper[l-1].questions:
        if i != ",":
            q = q+i
        if i == ",":
            arr.append(q)
            q = ""   
    con = {
        'question':arr,
    }
    print(con)
    return render(request , "portal.html" , con)

def analysis(requests):
    paper = Exams()
    exams = paper.__class__.objects.all()
    context = {}
    arr = []
    print("hey :" + exams[0].questions)
    l =0
    for i in exams:
        l = l +1
    q = ""
    for i in exams[l-1].questions:
        print(i)
        if i != ",":
            q = q+i
        if i == ",":
            arr.append(q)
            q = ""   

    questions_dic = {
        'question':arr,
    }


    all_exams = []
    for each in exams:
        if each.user == requests.user:
            context = {
                'name' : each.name,
                'course' : each.course,
                'Exam_Type' : each.Exam_Type,
                'Difficulty_Level' : each.Difficulty_Level,
                'questions' : questions_dic,
                'answers' : each.answers,
            }
            all_exams.append(context)
    con = {
        'papers' :all_exams
    }
    print(con)
    return render(requests , "analysis.html" , con)


