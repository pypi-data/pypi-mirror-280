from django.contrib import admin
from .models import ChatSession,SimilarQuestion,Feedback

admin.site.register(ChatSession),
admin.site.register(SimilarQuestion)
admin.site.register(Feedback)

