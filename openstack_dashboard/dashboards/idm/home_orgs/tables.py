# Copyright (C) 2014 Universidad Politecnica de Madrid
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.utils.translation import ugettext_lazy as _
    
from horizon import tables
from django.conf import settings


class ManageMembersLink(tables.LinkAction):
    name = "manage_members"
    verbose_name = _("Add")
    url = "horizon:idm:home_orgs:members"
    classes = ("ajax-modal",)

class MembersTable(tables.DataTable):
    name = tables.Column('name', verbose_name=_('Members'))
    avatar = tables.Column(lambda obj: settings.MEDIA_URL + getattr(
        obj, 'img_medium', 'dashboard/img/logos/medium/user.png'))
    default_avatar = tables.Column(lambda obj: settings.STATIC_URL + getattr(
        obj, 'img_medium', 'dashboard/img/logos/medium/user.png'))
    
    # show_avatar = True
    clickable = True

    class Meta:
        name = "members"
        verbose_name = _("Members")
        table_actions = (ManageMembersLink, )
        multi_select = False


class ApplicationsTable(tables.DataTable):
    name = tables.Column('name', verbose_name=_('Name'))
    url = tables.Column(lambda obj: getattr(obj, 'url', None))
    avatar = tables.Column(lambda obj: settings.MEDIA_URL + getattr(
        obj, 'img_medium', 'dashboard/img/logos/medium/app.png'))
    default_avatar = tables.Column(lambda obj: settings.STATIC_URL + getattr(
        obj, 'img_medium', 'dashboard/img/logos/medium/app.png'))
    
    clickable = True
    # show_avatar = True
    class Meta:
        name = "applications"
        verbose_name = _("Applications")
        # table_actions = (GoToApplicationsTable,)
        multi_select = False
        