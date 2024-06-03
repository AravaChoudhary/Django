from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML','MASALA'),
        ( 'GR', 'GINGER'), 
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'), 
        ('EL', 'ELACHI'),
    ]
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/chai')
    date_added = models.DateTimeField(default=timezone.now)

    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)

    description = models.TextField(default='')

    def __str__(self):
        return self.name
    

#One --> Many
class chainreview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    Date_Added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review {self.chai.name}'


#Many --> Many
class Store(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    chai_varieties = models.ManyToManyField(ChaiVariety,related_name='store')

    def __str__(self):
        return self.name
    
#One --> One

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety,on_delete=models.CASCADE,related_name='certificate')
    certificare_number = models.CharField(max_length=100)
    Issues_Date = models.DateTimeField(default=timezone.now)
    Valid_till = models.DateTimeField()

    def __str__(self):
        return f'{self.chai.name} certificate'