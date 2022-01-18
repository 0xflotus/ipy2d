from ipy2d import fun

def main():
    assert fun.from_4("0.0.0.1") == 1, "Should be 1"
    assert fun.from_6("::1") == 1, "Should be 1"
    assert fun.from_6("2001:4860:4860::8888") == 42541956123769884636017138956568135816, "Should be 42541956123769884636017138956568135816"

    assert fun.to_4(5) == "0.0.0.5", "Should be 0.0.0.5"
    assert fun.to_6(42541956123769884636017138956568135817) == "2001:4860:4860:0000:0000:0000:0000:8889", "Should be 2001:4860:4860:0000:0000:0000:0000:8889"

if __name__ == "__main__":
    main()