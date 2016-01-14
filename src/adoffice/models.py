# -*- coding: utf-8 -*-
from django.db import models
from django.utils.html import strip_tags
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext, ugettext_lazy as _
from filebrowser.fields import FileBrowseField
from django.core.mail import send_mail
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

#class Page(models.Model):


class Category(MetaData):

    slug = models.SlugField(max_length=50)
    title = models.CharField(_(u'Tytuł'), default='', max_length=254, blank=False, null=False)
    items_title = models.CharField(_(u'Tytuł Katalogu'), default='', max_length=254, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    slogan = models.CharField(max_length=255, default='', blank=True)
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


class PageClass(models.Model):
    name = models.CharField(max_length=255, default='homepage', blank=False, null=False)

    def __unicode__(self):
        return self.name


class Page(MetaData):
    section1 = models.TextField(u'Sekcja-1', blank=True, null=True)
    section2 = models.TextField(u'Sekcja-2', blank=True, null=True)
    title = models.CharField(max_length=254, default='')
    pageclass = models.ForeignKey(PageClass, default='1', blank=False, null=False)

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
    _category = ''
    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(_(u'Opis'), blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    format_size = models.CharField(max_length=25, blank=True)
    category = models.ManyToManyField(Category, blank=True, null=True, name='categories')
    group_category = models.ManyToManyField(GroupCategory, blank=True, null=True)
    finishing = models.ManyToManyField(Finishing, blank=True, null=True)
    accessories = models.ManyToManyField(Accessories, blank=True, null=True)
    picture = models.ImageField(_(u'Obrazek'), default='pics/default.png', upload_to='pics/',
                                blank=False, null=False)
    document = FileBrowseField("PDF", max_length=200, directory="documents/", extensions=[".pdf"], blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'slug')

    def get_absolute_url(self):
        return reverse("adoffice:product", kwargs={"slug": self.slug, "category": self.categories.all()[0].slug})

    def get_next(self):
            self._category = self.categories.all()[0]
            next = Product.objects.filter(id__gt=self.id, categories__in=[self._category])
            if next:
                return next[0]
                return False

    def get_prev(self):
        self._category = self.categories.all()[0]
        prev = Product.objects.filter(id__lt=self.id, categories__in=[self._category]).order_by('-id')
        if prev:
            return prev[0]
            return False

    #def get_category(self):



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
    note = models.TextField(_(u'Wiadomość'), default='', blank=True, null=True)
    newsletter = models.BooleanField(_(u'Newsletter'), default=True, help_text=_(u'Chcę być informowany o nowościach i ofertach firmy Achilles.'))
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.email

    def save(self):
        if self.email:
            message = _("Zapytanie strona www ").format(self)
            subject = _(u"Dziękujemy za kontakt")
            #send_mail(subject, message, "no-replay@achilles.pl", [self.email, ])
            #print('Stored: {}'.format(self))
        super(Quota, self).save()

