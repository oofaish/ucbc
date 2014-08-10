from django.contrib import admin
from simple.models import Page, Tag, Image, Category, Stylesheet, Script, Crew, Member, CommitteeRole, CommitteeRoleTitle, Season, Role

admin.site.register(Page)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Member)
admin.site.register(Crew)
admin.site.register(Season)
admin.site.register(CommitteeRole)
admin.site.register(CommitteeRoleTitle)
admin.site.register(Role)
admin.site.register(Script)
admin.site.register(Stylesheet)

