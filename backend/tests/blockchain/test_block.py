import pytest
import time
from backend.blockchain.block import Block, GENESIS_DATA
from backend.config import MINE_RATE, SECONDS
from backend.util.hex_to_binary import hex_to_binary


def test_mine():
    previous_block = Block.genesis()
    data = "test data"
    block = Block.mine(previous_block, data)

    assert isinstance(block, Block)
    assert block.data == data
    assert hex_to_binary(block.hash)[0 : block.difficulty] == "0" * block.difficulty


def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)
    for key, val in GENESIS_DATA.items():
        getattr(genesis, key) == val


def test_adjust_difficulty_slow_mining():
    last_block = Block.mine(Block.genesis(), "foo")
    mined_block = Block.mine(last_block, "bar")

    assert mined_block.difficulty == last_block.difficulty + 1


def test_adjust_difficulty_fast_mining():
    last_block = Block.mine(Block.genesis(), "foo")
    time.sleep(MINE_RATE / SECONDS)
    mined_block = Block.mine(last_block, "bar")

    assert mined_block.difficulty == last_block.difficulty - 1


def test_adjust_difficulty_limits_at_1():
    last_block = Block(
        time.time_ns(), "test_previous_hash", "test_hash", "test_data", 1, 0
    )
    time.sleep(MINE_RATE / SECONDS)
    mined_block = Block.mine(last_block, "bar")

    assert mined_block.difficulty == 1


@pytest.fixture
def prev_block():
    return Block.genesis()


@pytest.fixture
def block(prev_block):
    return Block.mine(prev_block, "foo")


def test_is_valid_block(prev_block, block):
    Block.is_valid_block(prev_block, block)


def test_is_valid_block_tampered_prev_hash(prev_block, block):
    block.prev_hash = "tampered_prev_hash"
    with pytest.raises(Exception, match="previous hash mismatch"):
        Block.is_valid_block(prev_block, block)


def test_is_valid_block_tampered_proof_of_work(prev_block, block):
    block.hash = "fffffffffff"
    with pytest.raises(Exception, match="proof of work constraints not met"):
        Block.is_valid_block(prev_block, block)


def test_is_valid_block_tampered_difficulty(prev_block, block):
    block.difficulty = 10
    block.hash = f'{"0" * block.difficulty}26a874e8975b8972f'
    with pytest.raises(Exception, match="difficulty expectation not met"):
        Block.is_valid_block(prev_block, block)


def test_is_valid_block_tampered_hash(prev_block, block):
    correct_hash = block.hash
    block.hash = "0000000000000000000000000000000000000facada"
    with pytest.raises(
        Exception, match=f"hash mismatch got: {block.hash} want: {correct_hash}"
    ):
        Block.is_valid_block(prev_block, block)
