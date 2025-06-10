from django.db import models
from treenode.models import TreeNodeModel

class FoodCategory(TreeNodeModel):
    treenode_display_field = 'name'
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta(TreeNodeModel.Meta):
        verbose_name = 'Food Category'
        verbose_name_plural = 'Food Categories'

    def __str__(self):
        return self.name