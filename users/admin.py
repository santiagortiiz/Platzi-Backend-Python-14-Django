# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from users.models import Profile

# Register your models here.
# admin.site.register(Profile)      # Alternative

@admin.register(Profile)    # Decorador encargado de registrar el modelo
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')

    search_fields = (
        # Search by the user relation field with double underscore as: relation__field
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    # Filter menu on the sidebar (they appear in the order that are set here)
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )

    fieldsets = (
        # (Category Title, { fields: ( 
        #   (row1 col1, row1 col2), 
        #   (row2 col1, row2 col2) 
        # ) } )
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified',)


class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)