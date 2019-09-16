from django.db import models

# Create your models here.
class Item(models.Model):
	EMP_ID=models.CharField(max_length=20,primary_key = True)
	EMPLOYEE_NAME = models.CharField(max_length=20)
	
	
	
	def save(self):
		self.EMPLOYEE_NAME = self.EMPLOYEE_NAME.upper()
		super(Item,self).save()
		
		
		
	SALARY= models.IntegerField()
	DEPARTMENT=models.CharField(max_length = 20,blank=True)
	DOB=models.DateField()
	DOJ=models.DateField()


	#def __str__(self):
		#return self.description
	
