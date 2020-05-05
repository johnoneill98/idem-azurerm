# -*- coding: utf-8 -*-
'''
Azure Resource Manager (ARM) PostgreSQL Database Operations Execution Module

.. versionadded:: 2.0.0

:maintainer: <devops@eitr.tech>
:maturity: new
:depends:
    * `azure <https://pypi.python.org/pypi/azure>`_ >= 4.0.0
    * `azure-common <https://pypi.python.org/pypi/azure-common>`_ >= 1.1.23
    * `azure-mgmt <https://pypi.python.org/pypi/azure-mgmt>`_ >= 4.0.0
    * `azure-mgmt-compute <https://pypi.python.org/pypi/azure-mgmt-compute>`_ >= 4.6.2
    * `azure-mgmt-network <https://pypi.python.org/pypi/azure-mgmt-network>`_ >= 4.0.0
    * `azure-mgmt-rdbms <https://pypi.org/project/azure-mgmt-rdbms/>`_ >= 1.9.0
    * `azure-mgmt-resource <https://pypi.python.org/pypi/azure-mgmt-resource>`_ >= 2.2.0
    * `azure-mgmt-storage <https://pypi.python.org/pypi/azure-mgmt-storage>`_ >= 2.0.0
    * `azure-mgmt-web <https://pypi.python.org/pypi/azure-mgmt-web>`_ >= 0.35.0
    * `azure-storage <https://pypi.python.org/pypi/azure-storage>`_ >= 0.36.0
    * `msrestazure <https://pypi.python.org/pypi/msrestazure>`_ >= 0.6.1
:platform: linux

:configuration: This module requires Azure Resource Manager credentials to be passed as keyword arguments
    to every function in order to work properly.

    Required provider parameters:

    if using username and password:
      * ``subscription_id``
      * ``username``
      * ``password``

    if using a service principal:
      * ``subscription_id``
      * ``tenant``
      * ``client_id``
      * ``secret``

    Optional provider parameters:

**cloud_environment**: Used to point the cloud driver to different API endpoints, such as Azure GovCloud.
    Possible values:
      * ``AZURE_PUBLIC_CLOUD`` (default)
      * ``AZURE_CHINA_CLOUD``
      * ``AZURE_US_GOV_CLOUD``
      * ``AZURE_GERMAN_CLOUD``

'''
# Python libs
from __future__ import absolute_import
import logging

# Azure libs
HAS_LIBS = False
try:
    import azure.mgmt.rdbms.postgresql.models  # pylint: disable=unused-import
    from msrestazure.azure_exceptions import CloudError
    from msrest.exceptions import ValidationError
    HAS_LIBS = True
except ImportError:
    pass

log = logging.getLogger(__name__)


async def create_or_update(hub, name, server_name, resource_group, charset=None, collation=None, **kwargs):
    '''
    .. versionadded:: 2.0.0

    Creates a new database or updates an existing database.

    :param name: The name of the database.

    :param server_name: The name of the server.

    :param resource_group: The name of the resource group. The name is case insensitive.

    :param charset: The charset of the database. Defaults to None.

    :param collation: The collation of the database. Defaults to None.

    CLI Example:

    .. code-block:: bash

        azurerm.postgresql.database.create_or_update test_name test_server test_group test_charset test_collation

    '''
    result = {}
    postconn = await hub.exec.utils.azurerm.get_client('postgresql', **kwargs)

    try:
        database = postconn.databases.create_or_update(
            database_name=name,
            server_name=server_name,
            resource_group_name=resource_group,
            charset=charset,
            collation=collation,
        )

        database.wait()
        result = database.result().as_dict()
    except CloudError as exc:
        await hub.exec.utils.azurerm.log_cloud_error('postgresql', str(exc), **kwargs)
        result = {'error': str(exc)}

    return result


async def delete(hub, name, server_name, resource_group, **kwargs):
    '''
    .. versionadded:: 2.0.0

    Deletes a database.

    :param name: The name of the database.

    :param server_name: The name of the server.

    :param resource_group: The name of the resource group. The name is case insensitive.

    CLI Example:

    .. code-block:: bash

        azurerm.postgresql.database.delete test_name test_server test_group

    '''
    result = False
    postconn = await hub.exec.utils.azurerm.get_client('postgresql', **kwargs)

    try:
        database = postconn.databases.delete(
            database_name=name,
            server_name=server_name,
            resource_group_name=resource_group,
        )

        database.wait()
        result = True
    except CloudError as exc:
        await hub.exec.utils.azurerm.log_cloud_error('postgresql', str(exc), **kwargs)
        result = {'error': str(exc)}

    return result


async def get(hub, name, server_name, resource_group, **kwargs):
    '''
    .. versionadded:: 2.0.0

    Gets information about a database.

    :param name: The name of the database.

    :param server_name: The name of the server.

    :param resource_group: The name of the resource group. The name is case insensitive.

    CLI Example:

    .. code-block:: bash

        azurerm.postgresql.database.get test_name test_server test_group

    '''
    result = {}
    postconn = await hub.exec.utils.azurerm.get_client('postgresql', **kwargs)

    try:
        database = postconn.databases.get(
            database_name=name,
            server_name=server_name,
            resource_group_name=resource_group,
        )

        result = database.as_dict()
    except CloudError as exc:
        await hub.exec.utils.azurerm.log_cloud_error('postgresql', str(exc), **kwargs)
        result = {'error': str(exc)}

    return result


async def list_by_server(hub, server_name, resource_group, **kwargs):
    '''
    .. versionadded:: 2.0.0

    List all the databases in a given server.

    :param server_name: The name of the server.

    :param resource_group: The name of the resource group. The name is case insensitive.

    CLI Example:

    .. code-block:: bash

        azurerm.postgresql.database.list_by_server test_server test_group

    '''
    result = {}
    postconn = await hub.exec.utils.azurerm.get_client('postgresql', **kwargs)

    try:
        databases = await hub.exec.utils.azurerm.paged_object_to_list(
            postconn.databases.list_by_server(
                server_name=server_name,
                resource_group_name=resource_group
            )
        )

        for database in databases:
            result[database['name']] = database
    except CloudError as exc:
        await hub.exec.utils.azurerm.log_cloud_error('postgresql', str(exc), **kwargs)
        result = {'error': str(exc)}

    return result