from django.db import models
from users.models import CustomUser
import uuid

class Leader(models.Model):
    leader = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.leader.full_name


class SendData(models.Model):
    class Faculty(models.TextChoices):
        TTKT = "TTKT", "Telekomunikatsiya texnologiyalari va kasb talimi"

    class Direction(models.TextChoices):
        AX = 'AX', 'Axborot xavfsizligi'
        DI = 'DI', 'Dasturiy injinering'

    num = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    full_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    leader = models.ForeignKey('Leader', on_delete=models.CASCADE)
    faculty = models.CharField(max_length=5, choices=Faculty.choices, default=Faculty.TTKT)
    direction = models.CharField(max_length=5, choices=Direction.choices, default=Direction.AX)
    subject = models.CharField(max_length=128)
    message = models.TextField()
    upload = models.FileField(upload_to='uploads')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class AnswerData(models.Model):
    username = models.CharField(max_length=128)
    answer = models.TextField()
    leader = models.ForeignKey('Leader', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username