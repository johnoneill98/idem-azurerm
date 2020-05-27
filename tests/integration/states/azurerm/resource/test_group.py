import pytest


@pytest.mark.run(before="test_absent")
@pytest.mark.asyncio
async def test_present(hub, ctx, resource_group, location):
    expected = {
        "changes": {
            "new": {
                "location": location,
                "name": resource_group,
                "properties": {"provisioning_state": "Succeeded"},
            },
            "old": {},
        },
        "comment": f"Resource group {resource_group} has been created.",
        "name": resource_group,
        "result": True,
    }
    ret = await hub.states.azurerm.resource.group.present(ctx, resource_group, location)
    expected["changes"]["new"]["id"] = ret["changes"]["new"]["id"]
    assert ret == expected


@pytest.mark.run(after="test_present", before="test_absent")
@pytest.mark.asyncio
async def test_changes(hub, ctx, resource_group, location, tags):
    expected = {
        "changes": {
            "new": {
                "location": location,
                "name": resource_group,
                "properties": {"provisioning_state": "Succeeded"},
                "tags": tags,
            },
            "old": {},
        },
        "comment": f"Resource group {resource_group} has been created.",
        "name": resource_group,
        "result": True,
    }
    ret = await hub.states.azurerm.resource.group.present(
        ctx, resource_group, location, tags=tags
    )
    expected["changes"]["new"]["id"] = ret["changes"]["new"]["id"]
    assert ret == expected


@pytest.mark.run(after="test_present")
@pytest.mark.asyncio
async def test_absent(hub, ctx, resource_group, location, tags):
    expected = {
        "changes": {
            "new": {},
            "old": {
                "location": location,
                "name": resource_group,
                "properties": {"provisioning_state": "Succeeded"},
                "tags": tags,
            },
        },
        "comment": f"Resource group {resource_group} has been deleted.",
        "name": resource_group,
        "result": True,
    }
    ret = await hub.states.azurerm.resource.group.absent(ctx, resource_group)
    expected["changes"]["old"]["id"] = ret["changes"]["old"]["id"]
    assert ret == expected