from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image

class NFe (models.Model):
    number = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=100)
    sender = models.CharField(max_length=200)
    recipient = models.CharField(max_length=200)

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    number_nfe = models.ForeignKey(NFe,to_field='number',on_delete=models.CASCADE)
    sequence = models.IntegerField()
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Tag {self.id} - NFe {self.number_nfe.number}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        qr_content = f"{self.id}"
        qrcode_img = qrcode.make(qr_content,box_size=5)
        canvas = Image.new('RGB',(150,150),'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code_{self.id}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
     
