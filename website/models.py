from django.db import models


class Record(models.Model):
	vreme_dodavanja = models.DateTimeField(auto_now_add=True)
	ime = models.CharField(max_length=50)
	prezime =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	broj_telefona = models.CharField(max_length=15)
	adresa =  models.CharField(max_length=100)
	grad =  models.CharField(max_length=50)
	postanski_broj =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.ime} {self.prezime}")