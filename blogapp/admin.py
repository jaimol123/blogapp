from django.contrib import admin
from . models import Reeluser,Receipe,Ingredients,Comments,Slider,SocialLinks,Contact,FooterImage


class ReeluserAdmin(admin.ModelAdmin):

    list_display  = ('username', 'email','password')
    search_fields = ['username']



class IngredientsInline(admin.TabularInline):
    model = Ingredients
    extra = 3

class CommentsAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'subject')


class ReceipeAdmin(admin.ModelAdmin):

    list_display = ('receipe_name', 'category', 'type', 'recipe_image')
    search_fields = ['receipe_name']
    list_filter = ['pub_date']
    inlines = [IngredientsInline]



class SliderAdmin(admin.ModelAdmin):
    list_display= ('slider_image','slider_caption1', 'slider_caption2', 'slider_caption3')



class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('icon_name', 'social_url')



class ContactAdmin(admin.ModelAdmin):

    fields = ('contact_name', 'contact_email', 'contact_subject', 'contact_msg')




admin.site.register(Contact, ContactAdmin)
admin.site.register(Reeluser, ReeluserAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Receipe, ReceipeAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(SocialLinks, SocialLinkAdmin )
admin.site.register(FooterImage, admin.ModelAdmin)
