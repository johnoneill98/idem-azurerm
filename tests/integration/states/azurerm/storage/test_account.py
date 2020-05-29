import pytest


@pytest.fixture(scope="module")
def name():
    yield "azurermtest"


@pytest.fixture(scope="module")
def sku():
    yield "Standard_GRS"


@pytest.fixture(scope="module")
def changed_sku():
    yield "Standard_LRS"


@pytest.fixture(scope="module")
def kind():
    yield "StorageV2"


@pytest.mark.run(before="test_absent")
@pytest.mark.asyncio
async def test_present(hub, ctx, name, resource_group, sku, kind, location):
    expected = {
        "changes": {
            "new": {
                "name": name,
                "resource_group": resource_group,
                "sku": sku,
                "kind": kind,
                "location": location,
            },
            "old": {},
        },
        "comment": f"Storage account {name} has been created.",
        "name": name,
        "result": True,
    }

    ret = await hub.states.azurerm.storage.account.present(
        ctx, name, resource_group, sku, kind, location
    )
    assert ret == expected


@pytest.mark.run(after="test_present", before="test_absent")
@pytest.mark.asyncio
async def test_changes(hub, ctx, name, resource_group, sku, changed_sku, kind, location):
    expected = {
        "changes": {"sku": {"new": changed_sku, "old": sku}},
        "comment": f"Storage account {name} has been created.",
        "name": name,
        "result": True,
    }
    ret = await hub.states.azurerm.storage.account.present(
        ctx, name, resource_group, changed_sku, kind, location
    )
    assert ret == expected


@pytest.mark.run(after="test_present")
@pytest.mark.asyncio
async def test_absent(hub, ctx, name, resource_group):
    expected = {
        "changes": {"new": {}, "old": {"name": name}},
        "comment": f"Storage account {name} has been deleted.",
        "name": name,
        "result": True,
    }

    ret = await hub.states.azurerm.storage.account.absent(ctx, name, resource_group)
    assert (
        ret["changes"]["new"] == expected["changes"]["new"]
        and ret["changes"]["old"]["name"] == expected["changes"]["old"]["name"]
    )
