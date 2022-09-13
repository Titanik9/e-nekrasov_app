from django.db import models
from django.urls import reverse

#model for Portfolio(card with sites)

class Sites(models.Model):
    slug = models.SlugField('Unique name')
    title = models.CharField('Name of site', max_length=100)
    desc = models.TextField('Text for site')
    img = models.ImageField('Image', default='default.png', upload_to='site_image')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('site-detail', kwargs={'slug': self.slug})

