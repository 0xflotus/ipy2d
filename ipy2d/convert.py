import ipaddress


def from_4(ipv4: str) -> int:
    return int(ipaddress.IPv4Address(ipv4))


def from_6(ipv6: str) -> int:
    return int(ipaddress.IPv6Address(ipv6))


def to_4(num: int) -> str:
    return str(ipaddress.IPv4Address(num))


def to_6(num: int, compressed: bool = False) -> str:
    address = ipaddress.IPv6Address(num)
    return address.compressed if compressed else address.exploded
