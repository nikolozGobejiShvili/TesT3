import ref

def test_gauge():
    assert ref.gauge(50) == "50%"
    assert ref.gauge(0) == "E"
    assert ref.gauge(100) == "F"

    