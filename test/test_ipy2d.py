from ipy2d import fun

def test_random_examples():
    assert fun.from_4("0.0.0.1") == 1, "Should be 1"
    assert fun.from_6("::1") == 1, "Should be 1"
    assert fun.from_6("2001:4860:4860::8888") == 42541956123769884636017138956568135816, "Should be 42541956123769884636017138956568135816"

    assert fun.to_4(5) == "0.0.0.5", "Should be 0.0.0.5"
    assert fun.to_6(42541956123769884636017138956568135817) == "2001:4860:4860:0000:0000:0000:0000:8889", "Should be 2001:4860:4860:0000:0000:0000:0000:8889"

def test_first_two_octets_ipv4():
    ints = [i for i in range(0, 0x100)]
    for i1 in [0]:
        for i2 in [0]:
            for i3 in ints:
                for i4 in ints:
                    i = i1 << 0x18 | i2 << 0x10 | i3 << 0x08 | i4
                    assert fun.from_4("{0}.{1}.{2}.{3}".format(i1, i2, i3, i4)) == i, "Should be {0}".format(i)
                    assert fun.to_4(i) == "{0}.{1}.{2}.{3}".format(i1, i2, i3, i4), "Should be {0}".format("{0}.{1}.{2}.{3}".format(i1, i2, i3, i4))

def test_compressed_ipv6():
    assert "::1" == fun.to_6(1, True), "Should be ::1"