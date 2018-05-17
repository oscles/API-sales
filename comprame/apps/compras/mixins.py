import datetime
from django.db import models
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class ManagerMain(models.Manager):
    def get_queryset(self):
        return super(ManagerMain, self).get_queryset().filter(deleted_at__isnull=True)


class ManagerAllMain(models.Manager):
    def get_queryset(self):
        return super(ManagerAllMain, self).get_queryset()


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    objects = ManagerMain()
    objects_all = ManagerAllMain()

    class Meta:
        abstract = True


class DefaultViewSetMixin(object):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )
    filter_backends = (SearchFilter, OrderingFilter,)
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class ModelViewSetMixin(ModelViewSet):

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_at = datetime.datetime.now()
        instance.save()
        response = {'result':'Ok'}
        return Response(response, status=status.HTTP_204_NO_CONTENT)
