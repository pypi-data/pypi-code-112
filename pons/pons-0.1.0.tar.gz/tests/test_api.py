from eth_account import Account
import pytest
import trio

from pons import *


async def test_payment(test_provider):

    client = Client(provider=test_provider)

    root_account = test_provider.root_account
    root_client = client.with_signer(root_account)

    acc1 = Account.create()
    acc1_client = client.with_signer(acc1)

    # Fund the deployer account

    root_balance = await client.get_balance(root_account.address)
    to_transfer = Wei.from_unit(10, 'ether') # or `10 * ether`?
    await root_client.transfer(acc1.address, to_transfer)
    # TODO: check that block has changed
    root_balance_after = await client.get_balance(root_account.address)
    acc1_balance_after = await client.get_balance(acc1.address)
    assert acc1_balance_after == to_transfer
    assert root_balance - root_balance_after > to_transfer


async def test_contract(test_provider, compiled_contract):

    client = Client(provider=test_provider)

    root_account = test_provider.root_account
    root_client = client.with_signer(root_account)

    acc1 = Account.create()
    acc1_client = client.with_signer(acc1)

    # Fund the deployer account

    root_balance = await client.get_balance(root_account.address)
    to_transfer = Wei.from_unit(10, 'ether') # or `10 * ether`?
    await root_client.transfer(acc1.address, to_transfer)
    # TODO: check that block has changed
    root_balance_after = await client.get_balance(root_account.address)
    acc1_balance_after = await client.get_balance(acc1.address)
    assert acc1_balance_after == to_transfer
    assert root_balance - root_balance_after > to_transfer

    # Deploy the contract

    # TODO: can we estimate gas?
    deployed_contract = await acc1_client.deploy(compiled_contract, 12345, 56789)

    # Transact with the contract

    acc2 = Account.create()
    call = deployed_contract.abi.setState(111)
    await acc1_client.transact(deployed_contract.address, call)

    # Call the contract

    call = deployed_contract.abi.getState(123)
    result = await client.call(deployed_contract.address, call)
    assert result == 111 + 123
