from django.contrib import admin

from sales.models import Company, Contacts, Product


@admin.action(description='Cancel the debt of selected companies')
def cancel_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


class ContactsInline(admin.StackedInline):
    model = Contacts
    extra = 0


class ProductInline(admin.TabularInline):
    model = Product


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [ContactsInline, ProductInline]
    list_display = ('type', 'title', 'supplier', 'debt')
    list_filter = ('contacts__city',)
    readonly_fields = ('created_at',)
    actions = [cancel_debt]
