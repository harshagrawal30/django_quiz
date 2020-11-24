from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('app1/C5_que_page',views.class5TH,name='5THclass'),
    
     path('app1/<int:question_id>/C5_que_page',views.class5TH,name='5THclassq'),
    path('app1/C6_que_page',views.class6TH,name='6THclass'),
    path('app1/C7_que_page',views.class7TH,name='7THclass'),
     path('app1/C8_que_page',views.class8TH,name='8THclass'),
      path('app1/C9_que_page',views.class9TH,name='9THclass'),
       path('app1/C9_M_que_page',views.class9TH_M,name='9THclass_M'),
        path('app1/C9_S_que_page',views.class9TH_S,name='9THclass_S'),
      
       path('app1/C10_que_page',views.class10TH,name='10THclass'),
         path('app1/C10_M_que_page',views.class10TH_M,name='10THclass_M'),
        path('app1/C10_S_que_page',views.class10TH_S,name='10THclass_S'),
    path('app1/<int:question_id>/',views.ques,name='ques'),
    path('app1/<int:question_id>/check',views.check,name='check'),
    
    path('app1/account2/login',views.login,name='login'),
    path('app1/account2/logout',views.logout,name='logout'),  
    path('app1/<int:question_id>/account2/logout',views.logout1,name='logout'),
    path('app1/Result',views.result,name='result')
]