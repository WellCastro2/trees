from django.contrib import admin

from core.models import Account, Tree, PlantedTree



class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_filter = ('active',)
    list_editable = ('active',)
    search_fields = ('name',)


class TabPlantedAdmin(admin.TabularInline):
    model = PlantedTree
    extra = 0


class TreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name')
    search_fields = ('name',)
    inlines = [TabPlantedAdmin,]


class PlantedTreeAdmin(admin.ModelAdmin):
    list_display = ('tree', 'user', 'age', 'lat', 'long')
    search_fields = ('tree',)


admin.site.register(Account, AccountAdmin)
admin.site.register(Tree, TreeAdmin)
admin.site.register(PlantedTree, PlantedTreeAdmin)
