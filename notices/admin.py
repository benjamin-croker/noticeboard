from notices.models import Notice
from django.contrib import admin

# class NoticesInLine(admin.StackedInline):
#     model = Notice
#     extra = 1

admin.site.register(Notice)