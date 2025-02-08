from django.contrib import admin
from Events.models import Event, Band, EventBand


# Register your models here.

class BandInline(admin.StackedInline):
    model = EventBand
    extra = 0


class EventAdmin(admin.ModelAdmin):
    exclude = ('user',)
    inlines = [BandInline,]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(EventAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return obj and obj.user == request.user

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user


admin.site.register(Band)
admin.site.register(EventBand)
admin.site.register(Event, EventAdmin)
