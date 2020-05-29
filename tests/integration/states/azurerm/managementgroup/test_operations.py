import pytest


@pytest.fixture(scope="module")
def name():
    yield "azurerm-mgroup"


@pytest.fixture(scope="module")
def display_name():
    yield "azurerm-mgroup"


@pytest.fixture(scope="module")
def changed_display_name():
    yield "azurerm-mgroup-changed"


@pytest.mark.run(before="test_absent")
@pytest.mark.asyncio
async def test_present(hub, ctx, name, display_name):
    expected = {
        "changes": {"new": {"name": name, "display_name": display_name,}, "old": {},},
        "comment": f"Management Group {name} has been created.",
        "name": name,
        "result": True,
    }

    ret = await hub.states.azurerm.managementgroup.operations.present(
        ctx, name, display_name=display_name
    )
    assert ret == expected


@pytest.mark.run(after="test_present", before="test_absent")
@pytest.mark.asyncio
async def test_changes(hub, ctx, name, changed_display_name, display_name):
    expected = {
        "changes": {"display_name": {"new": changed_display_name, "old": display_name}},
        "comment": f"Management Group {name} has been created.",
        "name": name,
        "result": True,
    }
    ret = await hub.states.azurerm.managementgroup.operations.present(
        ctx, name, changed_display_name
    )
    assert ret == expected


@pytest.mark.run(after="test_present")
@pytest.mark.asyncio
async def test_absent(hub, ctx, name):
    expected = {
        "changes": {"new": {}, "old": {"name": name}},
        "comment": f"Management Group {name} has been deleted.",
        "name": name,
        "result": True,
    }

    ret = await hub.states.azurerm.managementgroup.operations.absent(ctx, name)
    assert (
        ret["changes"]["new"] == expected["changes"]["new"]
        and ret["changes"]["old"]["name"] == expected["changes"]["old"]["name"]
    )
