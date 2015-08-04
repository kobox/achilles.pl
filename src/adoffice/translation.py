# -*- coding: utf-8 -*-
__author__ = 'ko'

from modeltranslation.translator import translator, TranslationOptions
from .models import Category, GroupCategory, Product, Finishing, Page


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'slogan', 'description', 'meta_description', 'keywords', 'items_title')


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'description', 'meta_description', 'keywords')


class GroupCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class FinishingTranslationOptions(TranslationOptions):
    fields = ('title',)


class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'section1', 'section2')

translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(GroupCategory, GroupCategoryTranslationOptions)
translator.register(Finishing, FinishingTranslationOptions)
translator.register(Page, PageTranslationOptions)