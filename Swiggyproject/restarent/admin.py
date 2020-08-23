from django.contrib import admin
from  restarent.models import Replymodel,Commentmodel
from  s_adminapp.models import Adminmodel
admin.site.register(Replymodel)
admin.site.register(Commentmodel)
admin.site.register(Adminmodel)