# Copyright (c) 2018 Orange.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from neutron_interconnection.services.common import config as inter_config


def list_remote_keystone_auth_opts():
    return [
        ('remote_keystone_auth', inter_config.remote_keystone_auth_opts),
    ]


def list_state_scheduler_opts():
    return [
        ('state_scheduler', inter_config.state_scheduler_opts),
    ]


def list_drivers_opts():
    return [
        ('drivers', inter_config.drivers_opts),
    ]
