from django.contrib import admin
from registration.models import *

class UserAdmin(admin.ModelAdmin):
    pass
search_fields = ('first_name', 'last_name', 'email')
list_display = ('first_name', 'last_name', 'email')
admin.site.register(User, UserAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)




class TestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Test, TestAdmin)


class TechTestAdmin(admin.ModelAdmin):
  pass
admin.site.register(TechTest,TechTestAdmin)

class HRTestAdmin(admin.ModelAdmin):
  pass
admin.site.register(HRTest,HRTestAdmin)

class QuantitativeTestAdmin(admin.ModelAdmin):
  pass
admin.site.register(QuantitativeTest,QuantitativeTestAdmin)

class VerbalsTestAdmin(admin.ModelAdmin):
  pass
admin.site.register(VerbalsTest,VerbalsTestAdmin)

class ReasoningTestAdmin(admin.ModelAdmin):
  pass
admin.site.register(ReasoningTest,ReasoningTestAdmin)

class EligibilityTestAdmin(admin.ModelAdmin):
  pass
admin.site.register(EligibilityTest,EligibilityTestAdmin)

class AptitudeTestAdmin(admin.ModelAdmin):
  pass
admin.site.register(AptitudeTest,AptitudeTestAdmin)

