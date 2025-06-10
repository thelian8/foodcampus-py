from django.contrib import admin
from treenode.admin import TreeNodeModelAdmin
from treenode.forms import TreeNodeForm
from .models import FoodCategory

@admin.register(FoodCategory)
class FoodCategoryAdmin(TreeNodeModelAdmin):
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION
    form = TreeNodeForm
    list_display = ('name', 'description')
    search_fields = ('name',)