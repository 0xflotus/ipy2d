from ipy2d import fun

def main():
    assert fun.to_int("0.0.0.1") == 1, "Should be 1"

if __name__ == "__main__":
    main()