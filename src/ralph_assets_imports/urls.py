# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

from ralph_assets.views import (
    BackOfficeAddDevice,
    BackOfficeAddPart,
    BackOfficeBulkEdit,
    BackOfficeEditDevice,
    BackOfficeEditPart,
    BackOfficeSearch,
    DataCenterAddDevice,
    DataCenterAddPart,
    DataCenterBulkEdit,
    DataCenterSplitDevice,
    DataCenterEditDevice,
    DataCenterEditPart,
    DataCenterSearch,
    DeleteAsset,
    HistoryAsset,
)
from ralph_assets.views_import import DataCenterImportAssets

urlpatterns = patterns(
    '',
    url(r'^$',
        RedirectView.as_view(url='/assets/dc/search'),
        name='dc'),
    url(r'dc/$', RedirectView.as_view(url='/assets/dc/search'),
        name='dc'),
    url(r'back_office/$',
        RedirectView.as_view(url='/assets/back_office/search'),
        name='dc'),

    url(r'dc/search',
        login_required(DataCenterSearch.as_view()),
        name='dc'),
    url(r'dc/add/device/',
        login_required(DataCenterAddDevice.as_view()),
        name='dc'),
    url(r'dc/add/part/',
        login_required(DataCenterAddPart.as_view()),
        name='dc'),
    url(r'dc/edit/device/(?P<asset_id>[0-9]+)/$',
        login_required(DataCenterEditDevice.as_view()),
        name='dc_device_edit'),
    url(r'dc/edit/part/(?P<asset_id>[0-9]+)/$',
        login_required(DataCenterEditPart.as_view()),
        name='dc'),
    url(r'dc/history/device/(?P<asset_id>[0-9]+)/$',
        login_required(HistoryAsset.as_view()),
        name='dc'),
    url(r'dc/history/part/(?P<asset_id>[0-9]+)/$',
        login_required(HistoryAsset.as_view()),
        name='dc'),
    url(r'dc/bulkedit/$',
        login_required(DataCenterBulkEdit.as_view()),
        name='dc'),
    url(r'dc/delete/asset/$',
        login_required(DeleteAsset.as_view()),
        name='dc'),
    url(r'dc/split/asset/(?P<asset_id>[0-9]+)/$',
        login_required(DataCenterSplitDevice.as_view()),
        name='dc_device_split'),
    url(r'dc/import/$',
        login_required(DataCenterImportAssets.as_view()),
        name='dc_device_split'),

    url(r'back_office/search',
        login_required(BackOfficeSearch.as_view()),
        name='back_office'),
    url(r'back_office/add/device/',
        login_required(BackOfficeAddDevice.as_view()),
        name='back_office'),
    url(r'back_office/add/part/',
        login_required(BackOfficeAddPart.as_view()),
        name='back_office'),
    url(r'back_office/edit/device/(?P<asset_id>[0-9]+)/$',
        login_required(BackOfficeEditDevice.as_view()),
        name='back_office'),
    url(r'back_office/edit/part/(?P<asset_id>[0-9]+)/$',
        login_required(BackOfficeEditPart.as_view()),
        name='back_office'),
    url(r'back_office/history/device/(?P<asset_id>[0-9]+)/$',
        login_required(HistoryAsset.as_view()),
        name='back_office'),
    url(r'back_office/history/part/(?P<asset_id>[0-9]+)/$',
        login_required(HistoryAsset.as_view()),
        name='back_office'),
    url(r'back_office/bulkedit/$',
        login_required(BackOfficeBulkEdit.as_view()),
        name='back_office'),
    url(r'back_office/delete/asset/$',
        login_required(DeleteAsset.as_view()),
        name='back_office'),
)
