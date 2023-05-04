from django.shortcuts import render
from Project6.models import City, Firm, Religion, Human
from django.shortcuts import redirect
# from Project6.dbFun import completionDB

def index(request):
    # completionDB()
    city = City.objects.all()
    firm = Firm.objects.all()
    religion = Religion.objects.all()
    human = Human.objects.all()
    return render(request, "index.html", {"city": city, "firm": firm, "religion": religion, "human": human})

def createCity(request):
    if request.method == "POST":
        city = City()
        city.name = request.POST.get('name')
        city.country = request.POST.get('country')
        city.square = request.POST.get('square')
        city.save()
    return redirect("index")

def deleteCity(request, id):
    city = City.objects.get(id=id)
    city.delete()
    return redirect("index")

def updateCity(request, id):
        city = City.objects.get(id=id)
        if request.method == "POST":
            city.name = request.POST.get('name')
            city.country = request.POST.get('country')
            city.square = request.POST.get('square')
            city.save()
            return redirect("index")
        else:
            return render(request, "updateCity.html", {"city": city})

def updateHuman(request, id):
    human = Human.objects.get(id=id)
    if request.method == "POST":
        human.name = request.POST.get('name')
        human.age = request.POST.get('age')
        human.nationality = request.POST.get('nationality')
        if request.POST.get('job') is not None and request.POST.get('job').strip():
            firmTemp, created = Firm.objects.get_or_create(name = request.POST.get('job'))
            human.job = firmTemp
        if request.POST.get('city') is not None and request.POST.get('city').strip():
            cityTemp, created = City.objects.get_or_create(name = request.POST.get('city'))
            human.city = cityTemp
        if request.POST.get('religion') is not None and request.POST.get('religion').strip():
            religionTemp, created  = Religion.objects.get_or_create(name = request.POST.get('religion'))
            human.religion = religionTemp
        human.save()
        return redirect("index")
    else:
        return render(request, "updateHuman.html", {"human": human})

def updateReligion(request, id):
    religion = Religion.objects.get(id=id)
    if request.method == "POST":
        religion.name = request.POST.get('name')
        religion.save()
        return redirect("index")
    else:
        return render(request, "updateReligion.html", {"religion": religion})

def updateFirm(request, id):
    firm = Firm.objects.get(id=id)
    if request.method == "POST":
        firm.name = request.POST.get('name')
        firm.income = request.POST.get('income')
        firm.save()
        return redirect('index')
    else:
        return render(request, "updateFirm.html", {"firm": firm})

def createHuman(request):
    if request.method == "POST":
        human = Human()
        human.name = request.POST.get('name')
        human.age = request.POST.get('age')
        human.nationality = request.POST.get('nationality')
        if request.POST.get('job') is not None and request.POST.get('job').strip():
            firmTemp, created = Firm.objects.get_or_create(name = request.POST.get('job'))
            human.job = firmTemp
        if request.POST.get('city') is not None and request.POST.get('city').strip():
            cityTemp, created = City.objects.get_or_create(name = request.POST.get('city'))
            human.city = cityTemp
        if request.POST.get('religion') is not None and request.POST.get('religion').strip():
            religionTemp, created  = Religion.objects.get_or_create(name = request.POST.get('religion'))
            human.religion = religionTemp
        
        human.save()
    return redirect("index")

def createReligion(request):
    if request.method == "POST":
        religion = Religion()
        religion.name = request.POST.get('name')
        religion.save()
    return redirect("index")

def createFirm(request):
    firm = Firm()
    if request.method == "POST":
        firm.name = request.POST.get('name')
        firm.income = request.POST.get('income')
        firm.save()
        return redirect('index')
    return redirect("index")

def deleteHuman(request, id):
    human = Human.objects.get(id=id)
    human.delete()
    return redirect("index")

def deleteReligion(request, id):
    religion = Religion.objects.get(id=id)
    religion.delete()
    return redirect("index")

def deleteFirm(request, id):
    firm = Firm.objects.get(id=id)
    firm.delete()
    return redirect("index")
# PUT измегить
# delete удалить
# GET читать
# POST добавить