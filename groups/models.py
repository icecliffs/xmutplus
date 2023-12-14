from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        if self.parent:
            return f"{self.parent.name} / {self.name}"
        else:
            return f"ROOT / {self.name}"
class Groups(models.Model):
    name = models.CharField(max_length=255)
    group_id = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    flag = models.CharField(max_length=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.category.name} / ({self.name}, {self.url})"

class WebSite(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    vpn = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.category.name} / ({self.name}, {self.url})"
