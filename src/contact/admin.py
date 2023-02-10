from django.contrib import admin

from contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        Contact.Fields.NAME,
        Contact.Fields.RANK,
        Contact.Fields.DISCORD,
        Contact.Fields.SERVER,
        Contact.Fields.CHARACTER_NAME,
    )
    readonly_fields = (Contact.Fields.WOW_IMAGE,)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    Contact.Fields.NAME,
                    Contact.Fields.RANK,
                    Contact.Fields.DISCORD,
                ),
            },
        ),
        (
            "World of Warcraft character",
            {
                "fields": (
                    Contact.Fields.SERVER,
                    Contact.Fields.CHARACTER_NAME,
                    Contact.Fields.WOW_IMAGE,
                ),
            },
        ),
    )
