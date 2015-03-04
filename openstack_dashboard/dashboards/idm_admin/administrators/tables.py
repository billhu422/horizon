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

from django.conf import settings

from horizon import tables

from openstack_dashboard import api
from openstack_dashboard import fiware_api
from openstack_dashboard.dashboards.idm import utils as idm_utils
from openstack_dashboard.dashboards.idm import tables as idm_tables


class ManageAuthorizedMembersLink(tables.LinkAction):
    name = "manage_administrators"
    verbose_name = ("Authorize")
    url = "horizon:idm_admin:administrators:members"
    classes = ("ajax-modal",)
    icon = "check-square-o"

    def allowed(self, request, user):
        # Allowed if your allowed role list is not empty
        # TODO(garcianavalon) move to fiware_api
        default_org = api.keystone.user_get(
            request, request.user).default_project_id
        allowed = fiware_api.keystone.list_user_allowed_roles_to_assign(
            request,
            user=request.user.id,
            organization=default_org)
        app_id = getattr(settings, 'IDM_ID')
        return allowed.get(app_id, False)


class MembersTable(tables.DataTable):
    avatar = tables.Column(lambda obj: idm_utils.get_avatar(
        obj, 'img_medium', idm_utils.DEFAULT_USER_MEDIUM_AVATAR))
    name = tables.Column('name', verbose_name=('Members'))

    class Meta:
        name = "members"
        verbose_name = ("Authorized Administrators")
        table_actions = (ManageAuthorizedMembersLink, )
        multi_select = False
        row_class = idm_tables.UserClickableRow
        table_actions = (tables.FilterAction,)
