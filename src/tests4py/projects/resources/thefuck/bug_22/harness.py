import sys


if __name__ == "__main__":
    assert len(sys.argv) == 4
    expected = sys.argv[1]
    expected = expected.replace("(", "")
    expected = expected[:-1]
    script = sys.argv[2]
    script = script.replace(",", "")
    std_err = sys.argv[3]
    std_err = std_err[:-1]
