from django.contrib import admin


from .models import Article
#用来显示其他的field
class ArticleAdmin(admin.ModelAdmin):
	list_display =('title','pub_time','update_time',)

admin.site.register(Article,ArticleAdmin)

from .models import Autor
admin.site.register(Autor)

from .models import Application
admin.site.register(Application)