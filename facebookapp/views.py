from django.http.response import JsonResponse
from django.shortcuts import render
from . models import *
from random import random
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
# Create your views here.


def signup(request):
    try:
        email = request.POST['email']
        print(email)
        u_obj = login.objects.filter(username=email).exists()
        print(u_obj)
        if u_obj == False:
            firstnames = request.POST['fname']
            print(firstnames)
            lastnames = request.POST['lname']
            print(lastnames)
            mobile = request.POST['mobile']
            print(mobile)
            password = request.POST['password']
            print(password)
            day = request.POST['day']
            print(day)
            month = request.POST['month']
            print(month)
            year = request.POST['year']
            print(year)
            date = year+'-'+month+'-'+day
            gender = request.POST['gender']

            user_obje = user(firstname=firstnames, lastname=lastnames,
                             mobile=mobile, date=date, gender=gender)
            print(user_obje)
            user_obje.save()
            print(user_obje.id)
            login_obj = login(username=email, password=password,
                              user_id_id=user_obje.id)
            login_obj.save()
            return render(request, 'loginpage.html', {'message': 'User registered successfully'})
        else:
            return render(request, 'loginpage.html', {'msg': 'User already exist'})
    except Exception as e:
        print(e)
    return render(request, 'loginpage.html')


def logins(request):
    try:
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        print(password)
        logi_obj = login.objects.get(username=username, password=password)
        print(logi_obj.id)
        request.session['log'] = logi_obj.id
        print(request.session['log'])
        log_obj = user.objects.get(id=logi_obj.user_id_id)
        return render(request, 'dashboard.html', {'username': log_obj})
    except Exception as e:
        print(e)
    return render(request, 'loginpage.html')

# userlist = []


def fnlogout(request):
    del request.session['log']
    return render(request, 'loginpage.html')


def fndelete(request):
    logout = request.session['log']
    log_obj = login.objects.get(id=logout)
    print(log_obj.user_id_id)
    logout_obj = log_obj.user_id_id
    log_obj.delete()
    user_obj = user.objects.get(id=logout_obj)
    user_obj.delete()
    return render(request, 'loginpage.html', {'msgs': 'user deleted successfully'})
# def sample(request):
#     if request.method == 'POST':
#         firstname = request.POST['fname']
#         print(firstname)
#         lastname = request.POST['lname']
#         print(lastname)
#         userdict = {"firstname": firstname, "lastname": lastname}
#         userlist.append(userdict)

#     return render(request, 'sample.html')


# def userlist1(request):
#     # for i in userlist:
#     #     print(i)
#     return render(request, 'userlist.html', {"user": userlist})
def editprofile(request):
    eprofile = request.session['log']
    ep_obj = login.objects.get(id=eprofile)
    eprofile_obj = ep_obj.user_id_id
    eprof = user.objects.get(id=eprofile_obj)
    return render(request, 'editprofile.html', {'profile': eprof, 'prof': ep_obj})


def dashboard(request):
    return render(request, 'dashboard.html')


def fnupdatadata(request):
    # try:
    if request.method == 'POST':
        updata_data = request.POST['uid']
        updataid = sample3.objects.get(id=updata_data)
        updata_obj = [{'id': updataid.id, 'name': updataid.name,
                       'contact': updataid.contact, 'place': updataid.place}]
        return JsonResponse({'updata': updata_obj})
    # except Exception as e:
    #     print(e)
    # return render(request, 'sample2.html')


def fnupdate(request):
    if request.method == 'POST':
        upid = request.POST['upid']
        name = request.POST['name']
        contact = request.POST['contact']
        place = request.POST['place']
        sample3.objects.filter(id=upid).update(
            name=name, contact=contact, place=place)
        return JsonResponse({'result': 'data updated sucessfully'})


def fnchangepassword(request):
    try:
        cpass = request.session['log']
        cpass_obj = login.objects.get(id=cpass)
        opassword = request.POST['opassword']
        print(opassword)
        npassword = request.POST['newpassword']
        if cpass_obj.password == opassword:
            cpass_obj.password = npassword
            cpass_obj.save()
            return render(request, 'changepassword.html', {'msg': 'password changed successfully'})
    except Exception as e:
        print(e)
    return render(request, 'changepassword.html')


def sample2(request):
    if request.method == 'POST':
        name = request.POST['name']

        contact = request.POST['contact']
        contact2 = int(contact)
        print(type(contact2))
        place = request.POST['place']
        sample_obj = sample3(name=name, contact=contact2, place=place)
        sample_obj.save()
        return JsonResponse({'msg': 'Data inserted successfully'})
    data = sample3.objects.all()
    datajson = [{'id': i.id, 'name': i.name,
                 'contact': i.contact, 'place': i.place}for i in data]
    return JsonResponse({'datas': datajson})


def dele(request):
    delid = request.POST['id']
    sample3.objects.get(id=delid).delete()
    return JsonResponse({'msg': "data deleted succcessfully"})


def loadpage(request):
    return render(request, 'sample2.html')

# def sample1(request):
#     if request.method == 'POST':
#         firstname = request.POST['fname']
#         print(firstname)
#         lastname = request.POST['lname']
#         print(lastname)
#         eaddress = request.POST['address']
#         print(eaddress)
#         day = request.POST['day']
#         print(day)
#         month = request.POST['month']
#         print(month)
#         year = request.POST['year']
#         print(year)
#         date = year+'-'+month+'-'+day
#         gender = request.POST['gender']

#         user_obj = esample(firstname=firstname, lastname=lastname,
#                            address=eaddress, date=date, gender=gender)
#         print(user_obj)
#         user_obj.save()
#     return render(request, 'sample.html')


def fnsample(request):
    if request.method == 'POST':
        texts = request.POST['text1']
        print(texts)
        file = request.FILES['files']
        print(file)
        file_name = str(random())+file.name
        print(file_name)
        file_obj = FileSystemStorage()
        file_obj.save(file_name, file)
        files_obj = sample2(imagename=texts, filename=file_name)
        files_obj.save()
    files_obje = sample2.objects.all()
    print(files_obje)
    return render(request, 'sample1.html', {'files': files_obje})


@ api_view(['GET'])
def fnapi(request):
    user_obj = user.objects.all()
    jsonformat = [{'fname': i.firstname, 'lname': i.lastname,
                   'mobile': i.mobile, 'date': i.date, 'gender': i.gender}for i in user_obj]
    return JsonResponse({'json': jsonformat})


@ api_view(['POST'])
def fnpostapi(request):
    postapi = request.data
    post_obj = user(firstname=postapi['fname'], lastname=postapi['lname'],
                    mobile=postapi['mobile'], date=postapi['date'], gender=postapi['gender'])
    post_obj.save()
    return JsonResponse({'msg': 'data inserted'})


@ api_view(['DELETE'])
def fndeleteapi(request):
    delapi = request.data
    user.objects.get(id=delapi['id']).delete()
    return JsonResponse({'msg': 'data deleted successfully'})


@login_required()
def fndashboard(request):
    return render(request, 'registration/dashboard.html')


def fnregistration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})


@ api_view(['GET'])
def fntest(request):
    message = "Congrats,you have created an api"
    return Response(message)
