from django.contrib import admin
from . models import Reeluser,Receipe,Ingredients,Comments,Slider,SocialLinks,Contact


class ReeluserAdmin(admin.ModelAdmin):

    list_display  = ('username', 'email','password')
    search_fields = ['username']

admin.site.register(Reeluser, ReeluserAdmin)

class IngredientsInline(admin.TabularInline):
    model = Ingredients
    extra = 3

class CommentsAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'subject')
admin.site.register(Comments, CommentsAdmin)

class ReceipeAdmin(admin.ModelAdmin):

    list_display = ('receipe_name', 'category', 'type','pub_date', 'recipe_image')
    search_fields = ['receipe_name']
    list_filter = ['pub_date']
    inlines = [IngredientsInline]
admin.site.register(Receipe, ReceipeAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display= ('slider_image','slider_caption1', 'slider_caption2', 'slider_caption3')
admin.site.register(Slider, SliderAdmin)


class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('icon_name', 'social_url')
admin.site.register(SocialLinks, SocialLinkAdmin )


class ContactAdmin(admin.ModelAdmin):

    fields = ('name', 'email', 'subject', 'msg')
admin.site.register(Contact, ContactAdmin)





