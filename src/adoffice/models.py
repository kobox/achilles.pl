# -*- coding: utf-8 -*-
from django.db import models
from django.utils.html import strip_tags
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext, ugettext_lazy as _
# Create your models here.


class MetaData(models.Model):
    """
    Abstract model that provides meta data for content.
    """

    _meta_title = models.CharField(_(u"Tytuł sekcji meta"), null=True, blank=True,
                                   max_length=500, help_text=_(u"Opcjonalny HTML title tag."))
    meta_description = models.TextField(_(u"Opis sekcji meta"), blank=True)
    keywords = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Set the description field on save.
        """
        self.meta_description = strip_tags(self.meta_description)
        super(MetaData, self).save(*args, **kwargs)

    def meta_title(self):
        """
        Accessor for the optional ``_meta_title`` field, which returns
        the string version of the instance if not provided.
        """
        return self._meta_title or str(self)


class Segment(models.Model):
    title = models.CharField(max_length=254)

    def __unicode__(self):
        return self.title


class Category(MetaData):

    slug = models.SlugField(max_length=50)
    title = models.CharField(_(u'Tytuł'), default='', max_length=254, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    description = models.TextField(_(u'Opis'), blank=True, null=True)
    picture = models.ImageField(_(u'Kategoria'), default='pics/default.png', upload_to='pics/',
                                blank=False, null=False)
    header = models.CharField(_(u'Klasa obrazka'), max_length=50, default='sec1', blank=True, null=True)
    order = models.IntegerField(default=0, blank=False, null=False)
    parent_category = models.ForeignKey('self', blank=True, null=True, related_name="subcategories")
    segment = models.ForeignKey(Segment, default='1', blank=False, null=False)
    #products = models.ManyToManyField(Product, blank=True, null=True)

    def __unicode__(self):
        return self.title


#subcategories = Category.objects.filter(parent_category__id=target_category.id)
class GroupCategory(models.Model):
    title = models.CharField(max_length=254)

    def __unicode__(self):
        return self.title


class Finishing(models.Model):
    title = models.CharField(max_length=254)

    def __unicode__(self):
        return self.title


class Accessories(models.Model):
    title = models.CharField(max_length=254)

    def __unicode__(self):
        return self.title


class Product(MetaData):
    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(_(u'Opis'), blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    format_size = models.CharField(max_length=10, blank=True)
    category = models.ManyToManyField(Category, blank=True, null=True)
    group_category = models.ManyToManyField(GroupCategory, blank=True, null=True)
    finishing = models.ManyToManyField(Finishing, blank=True, null=True)
    accessories = models.ManyToManyField(Accessories, blank=True, null=True)
    picture = models.ImageField(_(u'Obrazek'), default='pics/default.png', upload_to='pics/',
                                blank=False, null=False)

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'slug')

    def get_absolute_url(self):
        return reverse("adoffice:product", kwargs={"slug": self.slug, "category": self.category.all()[0].slug})


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    picture = models.ImageField(_(u'Obrazek'), default='pics/default.png', upload_to='pics/',
                                blank=False, null=False)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.product.title


class Quota(models.Model):
    email = models.EmailField()
    full_name = models.CharField(_(u'Imię i Nazwisko'), max_length=254, default='', blank=False, null=False)
    company = models.CharField(_(u'Firma'), max_length=254, default='', blank=True, null=True)
    phone = models.CharField(_(u'Telefon'), max_length=254, default='')
    note = models.TextField(_(u'Uwagi'), default='', blank=True, null=True)
    newsletter = models.BooleanField(_(u'Newsletter'), default=True, help_text=_(u'Chcę być informowany o nowościach i ofertach firmy Achilles.'))
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.email


