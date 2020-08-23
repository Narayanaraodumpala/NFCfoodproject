from django.shortcuts import render, redirect
from django.views.generic import CreateView,ListView
from s_adminapp.models import Adminmodel,UserModel,orderFoodModel
from s_adminapp.forms import *
from restarent.forms import restaurentform,SessionForm
from restarent.models import RestarentModel,Food_model,UserProfileSessionModel
from django.core.mail import send_mail
from Swiggyproject.settings import EMAIL_HOST_USER
import random
import qrcode
import socket
socket.getaddrinfo('localhost', 25)
otp=0
# Create your views here.
def admin_login(request):
    return render(request,'login.html',{'form':Admin_LoginForm,'mod':Adminmodel()})


def admin_login_check(request):
    user=request.POST['user_name']
    passwo=request.POST['password']
    Adminmodel(User_Name=user,Password=passwo).save()
    return  render(request,'login.html',{'msg':'saved'})


def register(request):
    return render(request,'regester.html',{'form':Admin_LoginForm()})


def admin_regiater_check(request):
    u=request.POST['user']
    p=request.POST.get('pas')
    print(u)
    print(p)
    Adminmodel.objects.get(User_Name=u,Password=p)
    request.session['status'] = True
    return render(request,'admin_home.html',)


def logout(request):
    request.session['status']=False
    return redirect('register')


def state(request):
    return render(request,'satate.html',{"form":StateForm(),"Sate_Mo":StateModel.objects.all()})


def save_state(request):
    sf=StateForm(request.POST)
    if sf.is_valid():
        sf.save()

        return  render(request,'satate.html',{'msg':'state details is saved'})
    else:
        return render(request,'satate.html',{'form':StateForm()})


def update_sate(request):
    sno=request.GET.get('s_no')
    sname=request.GET.get('s_name')
    d1={'sno':sno,'sname':sname}
    return render(request,'satate.html',{'update_data':d1,'form':StateForm(),"State_Mo":StateModel.objects.all()})


def update_save_state(request):
    ups=request.POST['s1']
    upsn=request.POST['s2']
    StateModel.objects.filter(State_no=ups).update(State_Name=upsn)
    return redirect('state')


def delate_save_state(request):
    dsn=request.GET.get('s_no')
    dsnn=request.GET.get('s_name')
    StateModel.objects.get(State_no=dsn,State_Name=dsnn).delete()
    return redirect('state')


def city(request):
    return render(request,'city.html',{'form':CityForm(),'cm':CityModel.objects.all()})


def city_save(request):
    cf=CityForm(request.POST)
    if cf.is_valid():
        cf.save()
        return redirect('city')


def area(request):
    return render(request,'Area.html',{'Aform':AreaForm(),'am':AreaModel.objects.all(),})


def area_save(request):
    af=AreaForm(request.POST)
    if af.is_valid():
        af.save()
        return redirect('Area')


def type_of_Place(request):
    return render(request,'restarent_templates/type_of_restarent.html',{'form': Type_of_plce(),'trm':Type_of_resModel.objects.all()})


def save_rest_type(request):
    tf=Type_of_plce(request.POST)
    if tf.is_valid():
        tf.save()
    return redirect('Type_of_Place')


class Add_food(CreateView):
      template_name = 'restarent_templates/add_food.html'
      model = Food_model
      fields = "__all__"
      success_url = '/add_food/'


class View_food(ListView):
    template_name = 'restarent_templates/view_food.html'
    model = Food_model
    fields="__all__"
    success_url='/add_food/'
    qs=Food_model.objects.all()
    paginate_by = 32


def veg_food(request):
    user_list = Food_model.objects.filter(Food_Type=12122221)
    # page = request.GET.get('page', 1)
    #
    # paginator = Paginator(user_list, 6)
    # try:
    #     users = paginator.page(page)
    # except EmptyPage:
    #     users = paginator.page(paginator.num_pages)

    return render(request, 'restarent_templates/veg_food.html', { 'model':user_list })


def non_veg(request):
    nv=Food_model.objects.filter(Food_Type=1245785)
    return render(request,'restarent_templates/non_veg.html',{'nv':nv})


def sea_food(request):
    sf=Food_model.objects.filter(Food_Type=15478)
    return render(request,'restarent_templates/sea_food.html',{'sf':sf})


def desserts(request):
    dm=Food_model.objects.filter(Food_Type=12453654)
    return render(request,'restarent_templates/desserts.html',{'dm':dm})


def drinks(request):
    drf=Food_model.objects.filter(Food_Type=55238252)
    return render(request,'restarent_templates/drinks.html',{'drm':drf})


class All_types(ListView):
    template_name = 'restarent_templates/All_types.html'
    model = Food_model
    fields="__all__"
    success_url='/all_foods/'


def about(request):
    return render(request,'aboutt.html')


def careesr(request):
    return render(request,'careers.html')


def contact(request):
    return render(request,'contact.html')


def code_of_conduct(request):
    return render(request,'code_of_conduct.html')


def community(request):
    return render(request,'comunity.html')


def developers(request):
    return render(request,'developers.html')


def privacy(request):
    return render(request,'privacy.html')


def terms(request):
    return render(request,'terms.html')


def security(request):
    return render(request,'security.html')




# Create your views here.


def user_login(request):
 try:
   e= request.POST['Email']
   p= request.POST['Password']
   user = UserProfileSessionModel.objects.get(Email=e, Password=p)
   request.session["User_Name"] = user.Name
   request.session["User_Age"] = user.Age
   request.session["User_Gender"] = user.Gender
   request.session["User_Phone"] = user.Phone
   request.session["User_Email"] = user.Email
   request.session["User_Password"] = user.Password
   request.session["User_Door_No"] = user.Door_No
   request.session["User_Street"] = user.Street
   request.session["User_Area_Or_Village"] = user.Area_Or_Village
   request.session["User_City"] = user.City

   rno=random.randint(100000,999999)
   global otp
   otp=rno
   print(otp)
   qr=qrcode.make('Otp Of Your Booked Dish'+' '+str(rno))
   qr.save(r"s_adminapp/static/qr images/nandu.jpg")
   return render(request,'user_login_success.html')
 except UserProfileSessionModel.DoesNotExist:
     message='please login with valid credintials'
     return render(request,'userlogin.html',{'msg':message,'form':UserregisterForm()})

def order_dish(request):
     pname = request.GET.get('pname')
     pprice = request.GET.get('pprice')
     pimage = request.GET.get('pimage')

     print(pname)
     print(pprice)
     print(pimage)

     res = Food_model.objects.filter(Food_Name=pname, Food_price=pprice, Food_Image=pimage)
     global fres
     fres = res
     return render(request, 'user_login.html',
                   {'model': UserProfileSessionModel.objects.all(), 'form':SessionForm(), 'res': res})




def Save_user(request):
    na= request.POST['Name']
    ag = request.POST['Age']
    ph=request.POST['Phone']
    ge = request.POST['Gender']
    dr = request.POST['Door_No']
    st = request.POST['Street']
    em=request.POST['Email']
    pa=request.POST['Password']
    ar = request.POST['Area_Or_Village']
    ci = request.POST['City']

    UserModel(Email=em,Password=pa,Name=na,Age=ag,Phone=ph,Gender=ge,Door_No=dr,Street=st,Area_Or_Village=ar,City=ci).save()
    return render(request,'userlogin.html',{'form':UserregisterForm(),'msg':'user is Added'})

def validate_otp(request):
    uotp=request.POST['otp']

    if uotp==str(otp):
        return render(request, 'otp_success.html',)
    else:
        messafe="You Entered A Wrong OTP..,Please Enter A Valid OTP"
        return render(request,'user_login_success.html',{'messg':messafe})


def email(request):
   Email=request.POST['e1']
   Subject=  "Enjoy The Taste Of Food"
   Message="Hello Foodie.This Is RNFC .This is Your OTP"+ ' '+str(otp)
   send_mail(Subject,Message,EMAIL_HOST_USER,[Email])
   return render(request,'user_login_success.html',{'mesg':'OTP Sent To Mail'})

def order_place(request):
    user = request.session.get('User_Name', 'User_Email')
    if user:
        print(user)
        return render(request,'otp_success.html')


def confirm_Order(request):

    return render(request,'confirm_Order.html')


def get_Order(request):
    Email=request.POST['e1']
    Subject = "Hello Foodie.. ! Your just order a food from NFC."
    Message = "We Will get You the  Updates in very soon  Once Your Order Is Packed and ready out for delivery .. Thank u for choosing NFC."
    send_mail(Subject, Message, EMAIL_HOST_USER, [Email])
    return render(request,'confirm_Order.html')