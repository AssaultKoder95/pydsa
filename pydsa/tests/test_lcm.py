from pydsa.lcm import lcm


def test_lcm():
    assert lcm(4, 10) == 20
    assert lcm(80, 25) == 400
    assert lcm(41, 12) == 492
    assert lcm(10251, 210) == 717570
    assert lcm(126, 105) == 630
    assert lcm(145, 780) == 22620
    
