# -*- coding: utf-8 -*-
"""
Azure Resource Manager (ARM) Graph RBAC User Execution Module

.. versionadded:: 2.4.0

:maintainer: <devops@eitr.tech>
:configuration: This module requires Azure Resource Manager credentials to be passed as keyword arguments
    to every function or via acct in order to work properly.

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

"""
# Python libs
import logging

# Azure libs
HAS_LIBS = False
try:
    from azure.graphrbac.models.graph_error import GraphErrorException
    from azure.core.exceptions import (
        ResourceNotFoundError,
        HttpResponseError,
        ResourceExistsError,
    )
    from msrest.exceptions import SerializationError

    HAS_LIBS = True
except ImportError:
    pass


__func_alias__ = {"list_": "list"}

log = logging.getLogger(__name__)


def __virtual__(hub):
    """
    Only load when Azure SDK imports successfully.
    """
    return HAS_LIBS


async def list_(hub, ctx, user_filter=None, **kwargs):
    """
    .. versionadded:: 2.4.0

    Gets list of users for the current tenant.

    :param user_filter: The filter to apply to the operation.

    CLI Example:

    .. code-block:: bash

        azurerm.graphrbc.user.list user_filter="displayName eq 'Test Buddy'"

    """
    result = {}

    graphconn = await hub.exec.azurerm.graphrbac.client.get(
        ctx, resource="https://graph.windows.net", **kwargs
    )

    try:
        users = graphconn.users.list(filter=user_filter)
        for user in users:
            result[user.object_id] = user.as_dict()
    except (AttributeError, GraphErrorException, HttpResponseError) as exc:
        result = {"error": str(exc)}

    return result
