from django.shortcuts import render,HttpResponse,redirect
from blogapp.models import Post 
from django.db.models import Q
from blogapp.forms import StudentForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from blogapp.forms import UserForm
from django.contrib.auth import authenticate,login,logout
 
 # Create your views here.
def home(request):
   #return  HttpResponse("hello this is first response!!")
   print("in home function")
   return redirect('/udash')






#passing data from views to html file

def view_html(request):
      # data={'name':'Itvedant','location':'Eclass','module':'Django'}
      #data['name']="Itvedant"
      data={}
      #data['x']=100
      #data['x']=400
      #data['y']=200
      data['d']=[100,200,300,400,500]
      
      
      return render(request,'udashboard.html',data)

   

def user_dashboard(request):
   
    return render(request,'udashboard.html')

def about(request):
   
    return render(request,'about.html')

def contact(request):
   
    return render(request,'contact.html')

def index (request):
    q1=Q(is_deleted=1)
    q2=Q(active=1)
    rec=Post.objects.filter(q1 & q2).order_by('-dt')
    content={}
    content['data']=rec
    return render(request,'index.html',content)


def post(request):

    return render(request,'post.html')

def create_post(request):
    
    userid=request.user.id

    if request.method=="POST":
         
         t=request.POST['ptitle']
         s=request.POST['sdesc']
         d=request.POST['det_desc']
         c=request.POST['cat']
         act=request.POST['pactive']
         
         '''
         print("title:",t)
         print("small description:",s)
         print("Details:",d)
         print("category:",c)
         print("whether active:",act)

         '''
         
         p=Post.objects.create(title=t,sdesc=s,det=d,cat=c,active=act,is_deleted="1",uid=userid)
         print(p)
         p.save()
         #return HttpResponse("record is inserted successfully!!!")
         return redirect('/udash')
         
    else:
        
       return render(request,'create_post.html')

def user_dashboard(request):
     
    #rec=Post.objects.all()
    #print(rec)
    userid=request.user.id
    q1=Q(is_deleted=1)
    q2=Q(uid=userid)
    rec=Post.objects.filter(q1 & q2) #where=is_deleted=1
    content={}
    content['data']=rec
    return render(request,'udashboard.html',content)

def delete(request,rid):
   #p=Post.objects.get(id=rid)
   #p.delete()
   p=Post.objects.filter(id=rid)
   p.update(is_deleted="0")
   return redirect('/udash')

def edit(request,rid):

    if request.method=="POST":
            utitle=request.POST['ptitle']
            usdesc=request.POST['sdesc']
            udet=request.POST['det_desc']
            ucat=request.POST['cat']
            uactive=request.POST['pactive']
        
            p=Post.objects.filter(id=rid)
            p.update(title=utitle,sdesc=usdesc,det=udet,cat=ucat,active=uactive)

            return redirect('/udash')
    else:


           p=Post.objects.get(id=rid)
           #print(p)
           content={}
           content['data']=p
           return render(request,'edit.html',content)

def catfilter( request,catopt):
    q1=Q(cat=catopt)
    q2=Q(is_deleted=1)
    rec=Post.objects.filter(q1 & q2)
    content={}
    content['data']=rec


    
    return render(request,'udashboard.html',content)

def actfilter(request,actopt):
    q1=Q(active=actopt)
    q2=Q(is_deleted=1)
    rec=Post.objects.filter(q1 & q2)
    content={}
    content['data']=rec
    return render(request,'udashboard.html',content)

def djangoform(request):
    fm=StudentForm()
    content={}
    content['form']=fm
    return render(request,'djangoform.html',content)
    
def user_register(request):
    if request.method=="POST":
        #fm=UserCreationForm(request.POST)
        fm=UserForm(request.POST)
        #print(fm)
        if fm.is_valid():
          fm.save()
          return HttpResponse("user Created Successfully!!!")
        else:
            return HttpResponse("Failed to create User!!")
    else:

       #fm=UserCreationForm()
       fm=UserForm()
       content={}
       content['form']=fm
       return render(request,'register.html',content)

def user_login(request):

    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        #print(fm)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            
            print(uname)
            print(upass)
            u=authenticate(username=uname,password=upass)
            #print("value in u:",u) 
            if u:#true
                login(request,u)
                return redirect('/udash')
            
        else:
            content={}
            content['data']="invalid username and password"
            content['form']=fm
            return render(request,'login.html',content)          

    else:
        fm=AuthenticationForm()
        content={}
        content['form']=fm
        return render(request,'login.html',content)

def setcookies(request):

    res=render(request,'setcookie.html')
    res.set_cookie('name','ITVEDANT')
    res.set_cookie('per','98.7')
    return res

def getcookies(request):
    content={}
    content['n']=request.COOKIES['name']
    content['p']=request.COOKIES['per']

    return render(request,'getcookie.html',content)

def setsession(request):
    request.session['username']="ITVEDANT"
    request.session['password']="redhat123@"
    return render(request,'setsession.html')

def getsession(request):
    data={}
    data['uname']=request.session['username']
    data['upass']=request.session['password']
    return render(request,'getsession.html',data)
    

def user_logout(request):
    
    logout(request)#to destroy session

    return redirect('/')