from omniblack.secret import Secret, Password
from copy import copy, deepcopy


def test_init():
    s = Secret('test')
    assert s.reveal() == 'test'


def test_repr():
    s = Secret('test')
    assert repr(s) == '<Secret Redacted>'


def test_str():
    s = Secret('test')
    assert str(s) == '<Secret Redacted>'


def test_copy():
    """
    Copy should return new instances.
    The revealed values should be the same.
    """
    s = Secret('test')
    c = copy(s)
    dc = deepcopy(s)

    assert s is not c
    assert s is not dc

    assert c is not dc

    assert c.reveal() == s.reveal() == dc.reveal()


def test_random():
    """Test a wide range of secret lengths.

    At one moment I had a bug where a length of 3 would segfault.
    """

    secrets = tuple(
        Secret.random_secret(num)
        for num in range(1, 101)
    )

    secret_lens = tuple(
        len(s)
        for s in secrets
    )

    secret_revealed_lens = tuple(
        len(s.reveal())
        for s in secrets
    )

    assert secret_lens == tuple(range(1, 101)) == secret_revealed_lens


def test_check_quality():
    s = Password('test')
    s.check_quality()


def test_random_password():
    Password.random_password()


def test_hash():
    Password('test').hash()


def test_verify():
    p = Password('test')
    h = p.hash()

    assert p.verify_password_against(h)


def test_need_rehash():
    p = Password('test')
    assert p.need_rehash()
    assert not p.hash().need_rehash()
