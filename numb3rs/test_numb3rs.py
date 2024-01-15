from numb3rs import validate

def main():
    test_valid_ipv4()
    test_invalid_ipv4()

def test_valid_ipv4():
    """
    Test the validate function with valid IPv4
    addresses.
    """
    assert numb3rs.validate("192.168.0.1") == True  # A typical private IP address
    assert numb3rs.validate("10.0.0.1") == True  # Another private IP address
    assert numb3rs.validate("0.0.0.0") == True  # The special case of the all-zeroes IP address
    assert numb3rs.validate("255.255.255.255") == True  # The maximum valid IP address
    assert numb3rs.validate("172.16.0.1") == True  # Yet another private IP address
    assert numb3rs.validate("8.8.8.8") == True  # A public DNS server IP address
    assert numb3rs.validate("192.168.01.1") == True  # Leading zeros in an octet

def test_invalid_ipv4():
    """
    Test the validate function with various
    invalid IPv4 addresses.
    """
    assert numb3rs.validate("256.0.0.0") == False  # Out of range octet
    assert numb3rs.validate("192.168.0.256") == False  # Out of range octet
    assert numb3rs.validate("192.168..1") == False  # Missing octet
    assert numb3rs.validate("192.168.0.1.2") == False  # Extra octet
    assert numb3rs.validate("10.10.10.10.10") == False  # Five octets
    assert numb3rs.validate("2001:0db8:85a3:0000:0000:8a2e:03
    70:7334") == False  # An IPv6 address



if __name__ == "__main__":
    main()


