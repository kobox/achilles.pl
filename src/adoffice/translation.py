# -*- coding: utf-8 -*-
__author__ = 'ko'

from modeltranslation.translator import translator, TranslationOptions
from .models import Category, GroupCategory, Product


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'description')


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'description')


class GroupCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(GroupCategory, GroupCategoryTranslationOptions)