from django.contrib import admin
from .models import Ticket, Review


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('get_ticket_title', 'headline',
                    'rating', 'user', 'time_created')

    def get_ticket_title(self, obj):
        return obj.ticket.title

    get_ticket_title.short_description = 'Ticket Title'


admin.site.register(Review, ReviewAdmin)
