import pytest
from les_10 import multiplay
async def multiplay(a, b):
    return a * b
@pytest.mark.asyncio
@pytest.mark.parametrize(
    'a, b, c',
    (
        (4, 2, 8),
        (2, 3, 6),
        (8, 7, 56),
        (-12, 4, -48),
        ('a', 3, 'aaa')
    )
)
async def test_multiply(a, b, c):
    assert await multiplay(a, b) == c
