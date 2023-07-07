from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message('lucasr', 3) == 'cul_rsa'
    assert encrypt_message('lucasr', 4) == 'rs_acul'
    assert encrypt_message('lucasr', 9) == 'rsacul'
    with pytest.raises(TypeError):
        encrypt_message(3, 'lucas')