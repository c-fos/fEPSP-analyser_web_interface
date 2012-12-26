from db_read.models import Experiment, ExpToTag, ExpTagTable, Record, RecordTagTable, RecordToTag, Spike
from django.contrib import admin

class ExpToTagAdmin(admin.TabularInline):
    model = ExpToTag
    
class TagsForRecords(admin.TabularInline):
    model = RecordToTag
       
class RecordInline(admin.TabularInline):
    model = Record
    extra = 1
    ordering = ('-time',)

class ExpAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Experiment name',               {'fields': ['experimentName']}),
        ('Date information', {'fields': ['date'], 'classes': ['collapse']}),
        ('Is this experiment good enougth?', {'fields': ['mask'], 'classes': ['collapse']}),
        #('Description', {'fields': ['desc'], 'classes': ['collapse']}),
    ]
    inlines = [ExpToTagAdmin,RecordInline]
    list_display = ('experimentName', 'date','mask')
    #list_filter = ['date']
    #search_fields = ['name']
    date_hierarchy = 'date'

#===============================================================================
class TagAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tag name',               {'fields': ['tagName']}),
        ('Tag description', {'fields': ['tagDesc'], 'classes': ['collapse']}),
    ]
    inlines = [ExpToTagAdmin]
    list_display = ('tagName', 'tagDesc')
    list_filter = ['tagName']
    search_fields = ['tagName','tagDesc']

class RecordAdmin(admin.ModelAdmin):
    fieldsets = [
        ('filename',               {'fields': ['filename']}),
        ('Time', {'fields': ['time']}),
        ('numberofresponses', {'fields': ['numberofresponses']}),
        ('hardError', {'fields': ['hardError']}),
        ('softError', {'fields': ['softError']}),
        #('Description', {'fields': ['desc'], 'classes': ['collapse']}),
    ]
    inlines = [TagsForRecords]
    list_display = ('filename', 'time')
    
class RecordTagsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('tagName',               {'fields': ['tagName']}),
        ('tagDesc', {'fields': ['tagDesc']}),
    ]
    inlines = [TagsForRecords]
    list_display = ('tagName', 'tagDesc')
    
class SpikesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('number', {'fields': ['number']}),
        ('fibre', {'fields': ['fibre']}),
        ('ampl', {'fields': ['ampl']}),
    ]
    list_display = ('ampl','number', 'fibre')
#===============================================================================

admin.site.register(Experiment, ExpAdmin)
admin.site.register(ExpTagTable, TagAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(RecordTagTable, RecordTagsAdmin)
admin.site.register(Spike, SpikesAdmin)