from Project6.models import City, Firm, Religion, Human


def completionDB():
    obj1 = City(name = "Москва", country = "Россия", square = "2511")
    obj2 = City(name = "Минск", country = "Беларусь", square = "349")
    obj3 = City(name = "Брест", country = "Беларусь", square = "146")
    obj4 = City(name = "Казань", country = "Татарстан", square = "516")

    City.objects.bulk_create([obj1, obj2, obj3, obj4])

    obj1 = Religion(name = "Христианство")
    obj2 = Religion(name = "Ислам")

    Religion.objects.bulk_create([obj1, obj2])

    obj1 = Firm(name = "Кирпичный завод", income = "36")
    obj2 = Firm(name = "Авиакомпания", income = "120")
    obj3 = Firm(name = "Биржа по продажам", income = "50")

    Firm.objects.bulk_create([obj1, obj2, obj3])
    
    
    firmK, created = Firm.objects.get_or_create(name = "Кирпичный завод")
    firmB, created = Firm.objects.get_or_create(name = "Биржа по продажам")
    firmA, created = Firm.objects.get_or_create(name = "Авиакомпания")
    cityB, created = City.objects.get_or_create(name = "Брест")
    cityMos, created = City.objects.get_or_create(name = "Москва")
    cityK, created = City.objects.get_or_create(name = "Казань")
    cityMin, created = City.objects.get_or_create(name = "Минск")
    religion2, created = Religion.objects.get_or_create(name = "Ислам")
    religion1, created = Religion.objects.get_or_create(name = "Христианство")


    Human.objects.create(name = "Тимур", age = "25", nationality = "Татарин", job = firmA, city = cityK, religion = religion2)
    Human.objects.create(name = "Вадим", age = "26", nationality = "Русский", job = firmK, city = cityB, religion=religion1)
    Human.objects.create(name = "Ольга", age = "31", nationality = "Русская", job = firmB, city = cityMos, religion = religion1)
    Human.objects.create(name = "Даниил", age = "30", nationality = "Русский", job = firmK, city = cityMin, religion = None)
