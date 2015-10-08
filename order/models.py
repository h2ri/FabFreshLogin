from django.db import models

# Create your models here.
STATUS = (
    ('1','created'),
    ('2', 'processed'),
    ('3','delivered'),
    ('4','cancelled'),
    )

class orders(models.Model):
    owner = models.ForeignKey('auth.User', related_name='orders')
    id = models.AutoField(primary_key=True)
    amount =  models.FloatField(blank=True,null=True)
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    created_at_time = models.DateTimeField(auto_now_add=True, blank=True)
    delivered_at_time = models.DateTimeField(blank=True,null=True)
    roadrunner_order_id = models.CharField(max_length=200,blank=True,null=True)
