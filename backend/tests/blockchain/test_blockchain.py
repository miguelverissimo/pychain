import pytest
from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA


def test_blockchain():
    blockchain = Blockchain()
    assert blockchain.chain[0].hash == GENESIS_DATA["hash"]


def test_add_block():
    blockchain = Blockchain()
    data = "test data"
    blockchain.add_block(data)
    assert blockchain.chain[-1].data == data


@pytest.fixture
def blockchain_with_blocks():
    blockchain = Blockchain()
    for i in range(5):
        blockchain.add_block(f"block #{i}")
    return blockchain


def test_is_valid_chain(blockchain_with_blocks):
    Blockchain.is_valid_chain(blockchain_with_blocks.chain)


def test_is_valid_chain_invalid_genesis(blockchain_with_blocks):
    blockchain_with_blocks.chain[0].hash = 3000
    with pytest.raises(Exception, match="genesis block is invalid"):
        Blockchain.is_valid_chain(blockchain_with_blocks.chain)
