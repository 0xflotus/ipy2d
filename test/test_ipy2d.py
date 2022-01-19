from ipy2d import convert
import pytest


def test_random_examples():
    assert convert.from_4("0.0.0.1") == 1, "Should be 1"
    assert convert.from_6("::1") == 1, "Should be 1"
    assert (
        convert.from_6("2001:4860:4860::8888") == 42541956123769884636017138956568135816
    ), "Should be 42541956123769884636017138956568135816"

    assert convert.to_4(5) == "0.0.0.5", "Should be 0.0.0.5"
    assert (
        convert.to_6(42541956123769884636017138956568135817)
        == "2001:4860:4860:0000:0000:0000:0000:8889"
    ), "Should be 2001:4860:4860:0000:0000:0000:0000:8889"
    assert (
        convert.to_6(0x20014860486000000000000000008889)
        == "2001:4860:4860:0000:0000:0000:0000:8889"
    ), "Should be 2001:4860:4860:0000:0000:0000:0000:8889"
    assert (
        convert.to_6(convert.from_6("0000:0000:0000:dead:beef:0000:0000:0000"))
        == "0000:0000:0000:dead:beef:0000:0000:0000"
    ), "Should be 0000:0000:0000:dead:beef:0000:0000:0000"


def test_first_two_octets_ipv4():
    ints = [i for i in range(0, 0x100)]
    for i1 in [0]:
        for i2 in [0]:
            for i3 in ints:
                for i4 in ints:
                    i = i1 << 0x18 | i2 << 0x10 | i3 << 0x08 | i4
                    assert (
                        convert.from_4(".".join(map(str, [i1, i2, i3, i4]))) == i
                    ), "Should be {0}".format(i)
                    assert convert.to_4(i) == ".".join(
                        map(str, [i1, i2, i3, i4])
                    ), ".".join(map(str, [i1, i2, i3, i4]))


def test_compressed_ipv6():
    assert "::1" == convert.to_6(1, compressed=True), "Should be ::1"
    assert "2001:4860:4860::8889" == convert.to_6(
        0x20014860486000000000000000008889, compressed=True
    ), "Should be 2001:4860:4860::8889"
    assert "1023::3a:3:0" == convert.to_6(
        0x1023_0000_0000_0000_0000_003A_0003_0000, compressed=True
    ), "Should be 1023::3a:3:0"
    assert "::dead:beef:0:0:0" == convert.to_6(
        1051570404137199630024704, compressed=True
    ), "Should be ::dead:beef:0:0:0"


@pytest.mark.skip(reason="this test takes to long!")
def test_all_ipv4():
    ints = [i for i in range(0x00, 0x100)]
    for i1 in ints:
        for i2 in ints:
            for i3 in ints:
                for i4 in ints:
                    i = i1 << 0x18 | i2 << 0x10 | i3 << 0x08 | i4
                    assert (
                        convert.from_4(".".join(map(str, [i1, i2, i3, i4]))) == i
                    ), "Should be {0}".format(i)
                    assert convert.to_4(i) == ".".join(
                        map(str, [i1, i2, i3, i4])
                    ), "Should be {0}".format(".".join(map(str, [i1, i2, i3, i4])))
