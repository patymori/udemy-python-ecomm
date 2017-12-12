import os
import random

from django.db import models


def get_file_extension(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_file(instance, filename):
    # print(instance)
    # print(filename)
    new_filename = random.randint(1, 999999999)
    name, ext = get_file_extension(filename)
    final_filename = '{}{}'.format(new_filename, ext)
    return "products/{}/{}".format(new_filename, final_filename)


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=1.00)
    image = models.ImageField(upload_to=upload_image_file,
                              null=True,
                              blank=True)

    def __str__(self):
        return self.title
