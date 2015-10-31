from django.db import models


class FooterText(models.Model):
    footer_text = models.CharField(max_length=500)
