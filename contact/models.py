from django.db import models

# Create your models here.
class Contact(models.Model):
    """ Contact model for database """

    SUBJECT_CHOICES = (
        ("Whiskey", "Whiskey"),
        ("Order", "Order"),
        ("Account", "Account"),
        ("Other", "Other"),
    )

    class Meta:
       
        verbose_name_plural = 'Enquiries'
        ordering = ['-date']

    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(
        max_length=20,
        choices=SUBJECT_CHOICES,
        default="Bouquets"
    )
    query = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return f"Query about {self.subject} by {self.name}"
