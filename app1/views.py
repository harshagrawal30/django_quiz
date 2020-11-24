from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from app1.models import que,choice
from django.urls import reverse
from django.utils import timezone
import dateutil,datetime,pytz
from django.contrib.auth.models import User,auth
from account2.models import user_info
from account3.models import user_res



        



# Create your views here.
def index(request):
    question=que.objects.all()
    coice=choice.objects.all()
   
    
    user1=user_info.objects.all()
    
    return render(request,'home.html',{'classnum':user1})
    #if user.username1==User.username:
    #return render(request,'home.html',{'classnum':user.username1})


def class5TH(request):
   
    question=que.objects.filter(Class=5)
    usr=user_res.objects.all()
    usser=None
    usq=[]
    qq=[]
    trs=[]
    v=1
    if request.user.is_authenticated:
        for user in usr:
            if user.username==request.user.username:
                usser=user
                
                usq.append(usser.question_id)
                
        for ques in question:
            if request.user.is_authenticated:
                for user in usr:
                    if user.username == request.user.username:
                        if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                            if user.question_id==ques.id:
                                trs.append(usser.question_id)

            if (datetime.datetime.now()>=ques.pub_date.replace(tzinfo=None)):
                if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                    qq.append(ques.id)
        for q1 in usq:
            for q2 in qq:
                if(q1==q2):
                    qq.remove(q2)
        if not trs:
            v=0
        if not usq:
            u=0
            
        else:
            u=1
        if not qq:
            q=0
        else:
            q=1    
        return render(request,'que_page.html',{'question':question,'question_text2':qq,'question_text1':usq,'usser':usr,'q':q,'u':u,'v':v})
    else:
        return render(request,'que_page.html',{'question':question})


def class6TH(request):
    
    question=que.objects.filter(Class=6)
    usr=user_res.objects.all()
    usser=None
    usq=[]
    qq=[]
    
    trs=[]
    v=1
    if request.user.is_authenticated:
        for user in usr:
            if user.username==request.user.username:
                usser=user
                
                usq.append(usser.question_id)
                
        for ques in question:
            if request.user.is_authenticated:
                for user in usr:
                    if user.username == request.user.username:
                        if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                            if user.question_id==ques.id:
                                trs.append(usser.question_id)

            if (datetime.datetime.now()>=ques.pub_date.replace(tzinfo=None)):
                if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                    qq.append(ques.id)
        for q1 in usq:
            for q2 in qq:
                if(q1==q2):
                    qq.remove(q2)
        if not trs:
            v=0
        if not usq:
            u=0
            
        else:
            u=1
        if not qq:
            q=0
        else:
            q=1    
        return render(request,'que_page.html',{'question':question,'question_text2':qq,'question_text1':usq,'usser':usr,'q':q,'u':u,'v':v})
    else:
        return render(request,'que_page.html',{'question':question})

def class7TH(request):
    question=que.objects.filter(Class=7)
    
    usr=user_res.objects.all()
    usser=None
    usq=[]
    qq=[]
    trs=[]
    v=1
    if request.user.is_authenticated:
        for user in usr:
            if user.username==request.user.username:
                usser=user
                
                usq.append(usser.question_id)
                
        for ques in question:
            if request.user.is_authenticated:
                for user in usr:
                    if user.username == request.user.username:
                        if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                            if user.question_id==ques.id:
                                trs.append(usser.question_id)

            if (datetime.datetime.now()>=ques.pub_date.replace(tzinfo=None)):
                if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                    qq.append(ques.id)
        for q1 in usq:
            for q2 in qq:
                if(q1==q2):
                    qq.remove(q2)
        if not trs:
            v=0
        if not usq:
            u=0
            
        else:
            u=1
        if not qq:
            q=0
        else:
            q=1    
        return render(request,'que_page.html',{'question':question,'question_text2':qq,'question_text1':usq,'usser':usr,'q':q,'u':u,'v':v})
    else:
        return render(request,'que_page.html',{'question':question})

def class8TH(request):
    question=que.objects.filter(Class=8)
    usr=user_res.objects.all()
    usser=None
    usq=[]
    qq=[]
    trs=[]
    v=1
    if request.user.is_authenticated:
        for user in usr:
            if user.username==request.user.username:
                usser=user
                
                usq.append(usser.question_id)
                
        for ques in question:
            if request.user.is_authenticated:
                for user in usr:
                    if user.username == request.user.username:
                        if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                            if user.question_id==ques.id:
                                trs.append(usser.question_id)

            if (datetime.datetime.now()>=ques.pub_date.replace(tzinfo=None)):
                if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                    qq.append(ques.id)
        for q1 in usq:
            for q2 in qq:
                if(q1==q2):
                    qq.remove(q2)
        if not trs:
            v=0
        if not usq:
            u=0
            
        else:
            u=1
        if not qq:
            q=0
        else:
            q=1    
        return render(request,'que_page.html',{'question':question,'question_text2':qq,'question_text1':usq,'usser':usr,'q':q,'u':u,'v':v})
    else:
        return render(request,'que_page.html',{'question':question})


def class9TH(request):
    question=que.objects.filter(Class=9)
    usr=user_res.objects.all()
    usser=None
    usq=[]
    qq=[]
    trs=[]
    v=1
    if request.user.is_authenticated:
        for user in usr:
            if user.username==request.user.username:
                usser=user
                
                usq.append(usser.question_id)
                
        for ques in question:
            if request.user.is_authenticated:
                for user in usr:
                    if user.username == request.user.username:
                        if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                            if user.question_id==ques.id:
                                trs.append(usser.question_id)

            if (datetime.datetime.now()>=ques.pub_date.replace(tzinfo=None)):
                if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                    qq.append(ques.id)
        for q1 in usq:
            for q2 in qq:
                if(q1==q2):
                    qq.remove(q2)
        if not trs:
            v=0
        if not usq:
            u=0
            
        else:
            u=1
        if not qq:
            q=0
        else:
            q=1    
        return render(request,'que_page.html',{'question':question,'question_text2':qq,'question_text1':usq,'usser':usr,'q':q,'u':u,'v':v})
    else:
        return render(request,'que_page.html',{'question':question})

def class9TH_M(request):
    question=que.objects.filter(Class=9,maths=1)
    usr=user_res.objects.all()
    usser=None
    usq=[]
    qq=[]
    trs=[]
    v=1
    if request.user.is_authenticated:
        for user in usr:
            if user.username==request.user.username:
                usser=user
                
                usq.append(usser.question_id)
                
        for ques in question:
            if request.user.is_authenticated:
                for user in usr:
                    if user.username == request.user.username:
                        if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                            if user.question_id==ques.id:
                                trs.append(usser.question_id)

            if (datetime.datetime.now()>=ques.pub_date.replace(tzinfo=None)):
                if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                    qq.append(ques.id)
        for q1 in usq:
            for q2 in qq:
                if(q1==q2):
                    qq.remove(q2)
        if not trs:
            v=0
        if not usq:
            u=0
            
        else:
            u=1
        if not qq:
            q=0
        else:
            q=1    
        return render(request,'que_page.html',{'question':question,'question_text2':qq,'question_text1':usq,'usser':usr,'q':q,'u':u,'v':v})
    else:
        return render(request,'que_page.html',{'question':question})

def class9TH_S(request):
    question=que.objects.filter(Class=9,science=1)
    usr=user_res.objects.all()
    usser=None
    usq=[]
    qq=[]
    trs=[]
    v=1
    if request.user.is_authenticated:
        for user in usr:
            if user.username==request.user.username:
                usser=user
                
                usq.append(usser.question_id)
                
        for ques in question:
            if request.user.is_authenticated:

                for user in usr:
                    if user.username == request.user.username:
                        if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                            if user.question_id==ques.id:
                                trs.append(usser.question_id)

            if (datetime.datetime.now()>=ques.pub_date.replace(tzinfo=None)):
                if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                    qq.append(ques.id)
        for q1 in usq:
            for q2 in qq:
                if(q1==q2):
                    qq.remove(q2)
        if not trs:
            v=0
        if not usq:
            u=0
            
        else:
            u=1
        if not qq:
            q=0
        else:
            q=1    
        return render(request,'que_page.html',{'question':question,'question_text2':qq,'question_text1':usq,'usser':usr,'q':q,'u':u,'v':v})
    else:
        return render(request,'que_page.html',{'question':question})


def class10TH(request):
    question=que.objects.filter(Class=10)
    usr=user_res.objects.all()
    usser=None
    usq=[]
    qq=[]
    trs=[]
    v=1
    if request.user.is_authenticated:
        for user in usr:
            if user.username==request.user.username:
                usser=user
                
                usq.append(usser.question_id)
                
        for ques in question:
            if request.user.is_authenticated:
                for user in usr:
                    if user.username == request.user.username:
                        if user.question_id==ques.id:
                            trs.append(usser.question_id)

            if (datetime.datetime.now()>=ques.pub_date.replace(tzinfo=None)):
                if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                    qq.append(ques.id)
        for q1 in usq:
            for q2 in qq:
                if(q1==q2):
                    qq.remove(q2)
        if not trs:
            v=0
        if not usq:
            u=0
            
        else:
            u=1
        if not qq:
            q=0
        else:
            q=1    
        return render(request,'que_page.html',{'question':question,'question_text2':qq,'question_text1':usq,'usser':usr,'q':q,'u':u,'v':v})
    else:
        return render(request,'que_page.html',{'question':question})

def class10TH_S(request):
    question=que.objects.filter(Class=10,science=1)
    usr=user_res.objects.all()
    usser=None
    usq=[]
    qq=[]
    trs=[]
    v=1
    if request.user.is_authenticated:
        for user in usr:
            if user.username==request.user.username:
                usser=user
                
                usq.append(usser.question_id)
                
        for ques in question:
            if request.user.is_authenticated:
                for user in usr:
                    if user.username == request.user.username:
                        if user.question_id==ques.id:
                            trs.append(usser.question_id)

            if (datetime.datetime.now()>=ques.pub_date.replace(tzinfo=None)):
                if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                    qq.append(ques.id)
        for q1 in usq:
            for q2 in qq:
                if(q1==q2):
                    qq.remove(q2)
        if not trs:
            v=0
        if not usq:
            u=0
            
        else:
            u=1
        if not qq:
            q=0
        else:
            q=1    
        return render(request,'que_page.html',{'question':question,'question_text2':qq,'question_text1':usq,'usser':usr,'q':q,'u':u,'v':v})
    else:
        return render(request,'que_page.html',{'question':question})

def class10TH_M(request):
    question=que.objects.filter(Class=10,maths=1)
    usr=user_res.objects.all()
    usser=None
    usq=[]
    qq=[]
    trs=[]
    v=1
    if request.user.is_authenticated:
        for user in usr:
            if user.username==request.user.username:
                usser=user
                
                usq.append(usser.question_id)
                
        for ques in question:
            if request.user.is_authenticated:
                for user in usr:
                    if user.username == request.user.username:
                        if user.question_id==ques.id:
                            trs.append(usser.question_id)

            if (datetime.datetime.now()>=ques.pub_date.replace(tzinfo=None)):
                if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                    qq.append(ques.id)
        for q1 in usq:
            for q2 in qq:
                if(q1==q2):
                    qq.remove(q2)
        if not trs:
            v=0
        if not usq:
            u=0
            
        else:
            u=1
        if not qq:
            q=0
        else:
            q=1    
        return render(request,'que_page.html',{'question':question,'question_text2':qq,'question_text1':usq,'usser':usr,'q':q,'u':u,'v':v})
    else:
        return render(request,'que_page.html',{'question':question})



def ques(request,question_id):
    question=que.objects.get(id=question_id)
    option=[]
    questions=choice.objects.filter(question_id=question_id)
    for opt in questions:
        option.append(opt)
    return render(request,'que-opt.html',{'question':question,'opt':option})


def check(request,question_id):
    
    question = get_object_or_404(que, pk=question_id)
    qqq=que.objects.all()
    
    if request.user.is_authenticated:
        username=request.user.username
    clas=question.Class
    user1=user_info.objects.all()
    selected_choice = question.choice_set.get(pk=request.POST['opts'])
    if question.end_date.replace(tzinfo=None)>=datetime.datetime.now():
        if request.user.is_authenticated:
            u_r=user_res()
            u_r.username=request.user.username
            u_r.question_text=question
            u_r.solved=True
            u_r.question_id=question_id
            for qq in qqq:
                if qq.id == question_id:
                    u_r.maths=qq.maths
                    u_r.science=qq.science
                    u_r.physics=qq.physics
                    u_r.biology=qq.biology
                    u_r.chemistry=qq.chemistry
                    
            ch=choice()
            ch=choice.objects.filter(question_id=question_id)
            for cho in ch:
                if cho.correct_ans==1:
                    u_r.correct_ans=cho.choice_text
            if selected_choice.correct_ans==1:
                solved="solved correctly"
                
                u_r.solved_c_n=True
                
    
        
    
            else:
                solved="solved incorrectly"
                u_r.solved_c_n=False
            u_r.save();
    for user2 in user1:
        if user2.username1 == username:
            if user2.classnum ==5:
                return redirect('/app1/C5_que_page')
            if user2.classnum ==6:
                return redirect('/app1/C6_que_page')
            if user2.classnum ==7:
                return redirect('/app1/C7_que_page')    
            if user2.classnum ==8:
                return redirect('/app1/C8_que_page') 
            if user2.classnum ==9:
                return redirect('/app1/C9_que_page') 
            if user2.classnum ==10:
                return redirect('/app1/C10_que_page')  



    

def login(request):
    return redirect('login')

def logout(request):
    return redirect('logout')

def logout1(request,question_id):
    return redirect('logout')


def result(request):
    if request.method=='POST':
        sub=request.POST['subject']
        usr=user_res.objects.all()
        usrname=user_info.objects.all()
        questn=que.objects.all()
        usser=None
        tq=0
        usq=[]
        qq=[]
        trs=[]
        crs=[]
        tq1=[]
        tsp1=0
        uuser=None
        tq3=0
        z=1
        for ussseeer in usrname:
            if ussseeer.username1==request.user.username:
                uuser=ussseeer
        if uuser==None:
            return render(request,'login.html')
        if sub == 'ALL':
            question=user_res.objects.all()
        if sub == 'maths':
            question=user_res.objects.filter(maths=1)
        elif sub=='science':
            question=user_res.objects.filter(science=1)
        elif sub=='chemistry':
            question=user_res.objects.filter(chemistry=1)
        elif sub=='biology':
            question=user_res.objects.filter(biology=1)
        elif sub=='physics':
            question=user_res.objects.filter(physics=1)
        if request.user.is_authenticated:
            for ques in questn:
                for ussseeer in usrname:
                    if ussseeer.username1==request.user.username:
                        if ques.Class==ussseeer.classnum:
                            if ques.pub_date>request.user.date_joined:
                                tq1.append(1)
                                
                                    
                            else:
                                pass
                
                if ques.pub_date>request.user.date_joined:
                    tq+=1
            for user in usr:
                if user.username==request.user.username:
                    usser=user
                    usq.append(usser.solved)
            
                    if usser.solved_c_n==1:
                        qq.append(usser.solved_c_n)
                    
                    for ques in questn:
                        if usser.question_id==ques.id:
                            if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                                trs.append(usser.question_id)
                                if usser.solved_c_n==1:
                                    crs.append(usser.question_id)

        for tq2 in tq1:
            tq3+=tq2
        uuser.Total_Question_faced=tq3
        uuser.save();

        if( len(usq)!=0 ):
            tsp=int((len(qq)/len(usq))*100)
            tsp1=int((len(qq)/uuser.Total_Question_faced)*100)
           
        else:
            tsp=0   
        if len(trs)!=0:
            rsp=int((len(crs)/len(trs))*100)
        else:
            z=0
            rsp=0
        return render(request,'result.html',{'T_solved':len(usq),'T_C_solved':len(qq),'usrname':usrname,'z':z,
        'T_R_solved':len(trs),'C_R_solved':len(crs),'tsp':tsp,'rsp':rsp,'quest':question,'usssser':usr,'tq':uuser.Total_Question_faced,'tsp1':tsp1})
    else:
        usr=user_res.objects.all()
        usrname=user_info.objects.all()
        questn=que.objects.all()
        usser=None
        usq=[]
        qq=[]
        trs=[]
        crs=[]
        trq=0
        uuser=None
        tq1=[]
        tq3=0
        tsp1=0
        z=1
        for ussseeer in usrname:
            if ussseeer.username1==request.user.username:
                uuser=ussseeer
        if uuser==None:
            return render(request,'login.html')
        question=que.objects.all()
        if request.user.is_authenticated:
            for ques in questn:
                for ussseeer in usrname:
                    if ussseeer.username1==request.user.username:
                        if ques.Class==ussseeer.classnum:
                            if ques.pub_date>request.user.date_joined:
                                tq1.append(1)
                            
                                
                        else:
                            pass
            
            for user in usr:
                if user.username==request.user.username:
                    usser=user
                    usq.append(usser.solved)
                    if usser.solved_c_n==1:
                        qq.append(usser.solved_c_n)
                    
                    for ques in question:
                        if usser.question_id==ques.id:
                            if (datetime.datetime.now()<=ques.end_date.replace(tzinfo=None)):
                                trs.append(usser.question_id)
                                if usser.solved_c_n==1:
                                    crs.append(usser.question_id)
       
        for tq2 in tq1:
            tq3+=tq2
        uuser.Total_Question_faced=tq3
        uuser.save();
        if( len(usq)!=0 ):
            tsp=int((len(qq)/len(usq))*100)
            tsp1=int((len(qq)/uuser.Total_Question_faced)*100)
        else:
            tsp=0   
        if len(trs)!=0:
            rsp=int((len(crs)/len(trs))*100)
        else:
            z=0
            rsp=0
        return render(request,'result.html',{'T_solved':len(usq),'T_C_solved':len(qq),'usrname':usrname,'z':z,
        'T_R_solved':len(trs),'C_R_solved':len(crs),'tsp':tsp,'rsp':rsp,'usr':usr,'question':question,'tq':uuser.Total_Question_faced,'tsp1':tsp1})