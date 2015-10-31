from django.db import models

class HeaderLink(models.Model):
    header_link_text = models.CharField(max_length=200)


class HeaderSubLink(models.Model):
    header_link = models.ForeignKey(HeaderLink)
    header_sub_link_text = models.CharField(max_length=200)
