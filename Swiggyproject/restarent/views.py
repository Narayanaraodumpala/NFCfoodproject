from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import View

from restarent.models import RestarentModel,Type_of_foodmodel,Food_model
from restarent.forms import *
from django.contrib import messages
from  django.shortcuts import redirect
from  restarent.models import Food_model
from django.views.generic import CreateView,ListView,UpdateView
# Create your views here.

def restaurent(request):
    return render(request,'restarent_templates/restaurent.html')


def reg_restaurent(request):
    return render(request,'restarent_templates/reg_restaurent.html',{'form':restaurentform(),})


def save_reg_resrtrent(request):
    rf = restaurentform(request.POST)
    if rf.is_valid():
        db = rf.save(commit=False)
        db.Restaurant_Otp = 725744
        db.Restaurant_Status = 'Pending'
        db.save()
        messages.success(request,"Once the admin approve the Registration you will receive an email and a text Message")
        return render(request,'restarent_templates/reg_restaurent.html',{'form':restaurentform()})
    else:
        return render(request,"restarent_templates/reg_restaurent.html",)


def show_rest(request):
    return render(request,'restarent_templates/show_rest.html',{'rem':RestarentModel.objects.all()})


def pending_restarent(request):
    rs= RestarentModel.objects.filter(Restaurant_Status='Pending')
    return render(request,'restarent_templates/pending_restarent.html',{'data':rs})


def approve_restarent(request):
    res=request.GET.get('restno')
    RestarentModel.objects.filter( Restaurant_Id=res).update(Restaurant_Status="Approved")
    return redirect("pending_restarent")


def cancel_restarent(request):
    res=request.GET.get('cn_rest')
    RestarentModel.objects.filter( Restaurant_Id=res).update(Restaurant_Status="Cancelled")
    return redirect('pending_restarent')


def app_resrt(request):
    rs=RestarentModel.objects.filter( Restaurant_Status="Approved")
    return render(request,'restarent_templates/approved.html',{'data':rs})


def can_rest(request):
    rs = RestarentModel.objects.filter(Restaurant_Status="Cancelled")
    return render(request, 'restarent_templates/cancelled.html', {'data': rs})


def login_restarent(request):
    return render (request,'restarent_templates/login_restarent.html',{'form':rest_login_form()})


def r_login_check(request):
    try:
     re=request.POST.get('Restaurent_Email')
     rp=request.POST.get('Restaurent_password')
     res=RestarentModel.objects.get( Restaurant_Email=re, Restaurant_Password=rp)
     if res.Restaurant_Status=='Pending':
        messages="Hello " + res.Restaurant_Name + ",Your Restaurent Is Not Approved , Still It Is In "+ "--"+ res.Restaurant_Status +"--"+  " Only. Please Contact The Authorites For Approving"
        return render(request,'restarent_templates/login_restarent.html',{'error':messages,'form':rest_login_form()})
     elif res.Restaurant_Status=='Cancelled':
        message=" Hello " + " "+ res.Restaurant_Name + ",Your Restaurent Is Not Approved , Still It Is In "+" "+res.Restaurant_Status +" "+ " Only. Please Contact The Authorites For Approving"
        return render(request,'restarent_templates/login_restarent.html',{'error':message,'form':rest_login_form()})
     else:
        return render(request,'restarent_templates/login_restarent_success.html')
    except RestarentModel.DoesNotExist:
        mess="Sorry You Are login With Wrong credintials"
    return render(request,'restarent_templates/login_restarent.html',{'form':rest_login_form(),'msg':mess})


class Type_of_food(View):
    def get(self,requset):
        return render(requset,'restarent_templates/login_restarent_success.html',{'form':Type_of_foodform()})
    def post(self,request):
        fd=request.POST['Food_Id']
        fn=request.POST["Food_Type"]
        Type_of_foodmodel(Food_Id=fd,Food_Type=fn).save()
        return render(request, 'restarent_templates/login_restarent_success.html',{'form': Type_of_foodform(), 'frm': Type_of_foodmodel.objects.all()})



def profile(request):
    return render(request,'profile.html')




class Add_profile(CreateView):
    template_name = 'add_profile.html'
    model = ProfileModel
    fields = "__all__"
    success_url = '/profile/'


class View_profile(ListView):
    template_name = 'profile.html'
    model = ProfileModel
    fields="__all__"
    success_url='/profile/'


class Edit_profile(UpdateView):
    def get(self,req):
        return render(req,'edit_profile.html')


class Login(View):
    def get(self,request):

        return render(request,'edit_profile.html',{'form':SessionForm()})

    def post(self,request):
        try:
         em= request.POST['Email']
         pa= request.POST['Password']
         user= UserProfileSessionModel.objects.get(Email=em,Password=pa)
         request.session["User_Name"]=user.Name
         request.session["User_Age"] = user.Age
         request.session["User_Gender"] = user.Gender
         request.session["User_Phone"] = user.Phone
         request.session["User_Email"] = user.Email
         request.session["User_Password"] = user.Password
         request.session["User_Door_No"] = user.Door_No
         request.session["User_Street"] = user.Street
         request.session["User_Area_Or_Village"] = user.Area_Or_Village
         request.session["User_City"] = user.City
         user=request.session.get('User_Name','User_Email')
         if user:
             print(user)
         return render(request,'profile.html')
        except UserProfileSessionModel.DoesNotExist:
            message="We Felt Sorry To Inform You that Your Credentials  Were Wrong ,So Please Login With Valid Credentials For THe Process Of Ordering The  Dish You Loved"
            return render(request,'edit_profile.html',{'message':message,'form':SessionForm()})


def register_user(request):
   na=request.POST['Name']
   ag= request.POST['Age']
   ge= request.POST['Gender']
   ph= request.POST['Phone']
   em= request.POST['Email']
   pa= request.POST['Password']
   dr= request.POST['Door_No']
   st=request.POST['Street']
   ar= request.POST['Area_Or_Village']
   ci=request.POST['City']
   UserProfileSessionModel(Name=na,Age=ag,Gender=ge,Phone=ph,Email=em,Password=pa,Door_No=dr,Street=st,Area_Or_Village=ar,City=ci).save()
   return render(request,'edit_profile.html',{'msg':"It's Pleasure  To Knowing You For The Regestration Process Is Done Successfully"+","+
                                                    "So Please Go To Home Page And Start Process The Ordering Of The Dishes You Loved ",'form':SessionForm()})


class Change_Profile(UpdateView):
    template_name = 'add_profile.html'
    model = ProfileModel
    fields = "__all__"
    success_url = '/profile/'

def add_comment_bag(request):
    fn=request.GET.get('fname')
    fp = request.GET.get('fprice')
    fi = request.GET.get('fimage')
    ft = request.GET.get('ftype')

    res=Food_model.objects.filter(Food_Name=fn,Food_price=fp,Food_Image=fi)

    return render(request,'add_comment_bag.html',{'data':res})





def save_cart(request):
    fid= request.POST['fid']
    fname=request.POST['fname']
    response=render(request,'success_cart.html')
    val=request.COOKIES.get(fid)
    max_age=172800
    if val:
        return render(request,'error.html',{'msg':'Oops...!! This Item Was Already Added To The Bag'})
    response.set_cookie(fid,fname,max_age=max_age)

    return response


def all_cart_items(request):
    data=request.COOKIES
    print(data)
    if data:
        no_of_items = len(request.COOKIES)-1
        print(no_of_items)
    else:
        no_of_items=0

    items = []  # empty list
    for x in data:
     print("x is"==x)
     if x == "csrftoken":


            continue
     else:
                obj = Food_model.objects.get(Food_id=x)
                items.append(obj)
    return render(request,'all_cart_items.html',{'datas':no_of_items,'res':items})


def remove_item(request):
   rid= request.POST['rid']
   response=redirect('all_cart_items')
   response.delete_cookie(rid)
   return response


def check_out(request):
    return render(request,'chekout.html')


def save_check_out(request):
    na= request.POST['name']
    em=request.POST['email']
    ad=request.POST['address']
    ci= request.POST['city']
    st= request.POST['state']
    zp=request.POST['zipcode']
    con= request.POST['country']
    CheckoutModel(Name=na,Email=em,Address=ad,City=ci,State=st,Zipcode=zp,Country=con).save()
    return render(request,'chekout.html')


def check_out_login(request):
    try:
     Name = request.POST['name']
     Email=request.POST['email']
     CheckoutModel.objects.get(Name=Name,Email=Email)
     return render(request,'check_out_login.html')
    except CheckoutModel.DoesNotExist:
        msg="Oops..!It's look Like You are trying To Login With Invalid Credentials"
        return render(request,'chekout.html',{'mesg':msg})


def search(request):
    if request.method=='POST':
      search= request.POST['serach']
      if search:
          res=Food_model.objects.filter(Food_Name__icontains=search)
          if res:

             return render(request,'search.html',{'data':res})
          else:
              return render(request,'search.html',{'message':'sorry no item is there with Your searched'})
      else:
          return render(request, 'search.html', {'msg': 'please enter some item name'})


def menu(request):
    res=Food_model.objects.all()
    return render(request,'menu.html',{'res':res})

def addcomments(request):

    return render(request,'addcomments.html',{'form':CommentForm()})


def save_comment(request):
   data = Commentmodel.objects.all()
   cf= CommentForm(request.POST,request.FILES)
   if cf.is_valid():
       cf.save()
       return render(request,'addcomments.html',{'msg':'Comment is submited, Thanks for commenting','form':CommentForm(),'res':data})
   else:
       return render(request,'addcomments.html',)


def view_comments(request):
    data=Commentmodel.objects.all()
    res=Replymodel.objects.all()
    return render(request,'view_comments.html',{'res':data,'data':res})


def blog(request):

    return render(request,'blog.html')


def abt_developer(request):
    return render(request,'abt_developer.html')