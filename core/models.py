from django.db import models
from versatileimagefield.fields import VersatileImageField


def uploaded_image_filename(instance, filename):
    ext = filename.split(".")[-1]
    dt = timezone.now().strftime("%Y/%m/%d")
    return f"images/{dt}/{uuid.uuid4()}.{ext}"


class Image(models.Model):
    creator = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name='images')
    
    title = models.CharField(max_length=256)
    image = VersatileImageField(upload_to=uploaded_image_filename)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.image.url}"
