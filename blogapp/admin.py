from django.contrib import admin
from . models import Reeluser,Receipe,Ingredients,Comments,Slider,SocialLinks,Contact,FooterImage,Feature,AboutUs,PlaceLocation,Rating,Details
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields
from django.conf import settings
from django.utils.html import format_html



class ReeluserAdmin(admin.ModelAdmin):

    list_display  = ('username', 'email','password')
    search_fields = ['username']



class IngredientsInline(admin.TabularInline):
    model = Ingredients
    extra = 3

class CommentsAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'subject', 'rating', 'date')


class ReceipeAdmin(admin.ModelAdmin):

    list_display = ('receipe_name', 'category', 'type', 'recipe_image')
    search_fields = ['receipe_name']
    list_filter = ['pub_date']
    inlines = [IngredientsInline]



class SliderAdmin(admin.ModelAdmin):

    search_display = ['slider_caption1', 'slider_caption2', 'slider_caption3']
    list_editable = ( 'slider_caption1', 'slider_caption2', 'slider_caption3' )
    list_display= ('slider_image','slider_caption1', 'slider_caption2', 'slider_caption3')



class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('icon_name', 'social_url')



class ContactAdmin(admin.ModelAdmin):

    list_display = ('contact_name', 'contact_email', 'contact_subject', 'contact_msg')

class AboutUsAdmin(admin.TabularInline):

    model = AboutUs
    extra = 3

class FeatureAdmin(admin.ModelAdmin):



    fields = ('text1', 'text2','heading','image1', 'image2')
    inlines = [AboutUsAdmin]



class RatingAdmin(admin.ModelAdmin):

    list_display = ('receipe_name', 'avg' ,'total' , 'image')


class PlaceLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'latitude', 'longitude',)
        }),
    )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('assets/css/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'assets/js/location_picker.js',
            )
class FooterAdmin(admin.ModelAdmin):

    list_display = ('image',)

    # readonly_fields = ['image_tag',]

class DetailAdmin(admin.ModelAdmin):
    list_display = ('address', ' phone_number')


admin.site.register(Rating, RatingAdmin)
admin.site.register(PlaceLocation,PlaceLocationAdmin )
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Reeluser, ReeluserAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Receipe, ReceipeAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(SocialLinks, SocialLinkAdmin )
admin.site.register(FooterImage, FooterAdmin)
admin.site.register(Details,DetailAdmin )

