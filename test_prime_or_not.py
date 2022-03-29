import prime_or_not
import pytest


@pytest.mark.parametrize("num,result",[(3,True),(5,True),(8,True),(9,False)])
def test_check_prime(num,result):
    oddeven=prime_or_not.check_prime(num)
    assert oddeven == result