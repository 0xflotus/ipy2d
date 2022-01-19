import netaddr
import ipaddress


def from_4(ipv4):
    octets = ipv4.split(".")
    return (
        int(octets[0]) << 0x18
        | int(octets[1]) << 0x10
        | int(octets[2]) << 0x08
        | int(octets[3]) << 0x00
    )


def from_6(ipv6):
    ip = netaddr.IPAddress(ipv6)
    hextet = ip.format(dialect=netaddr.ipv6_verbose).split(":")
    return (
        int(hextet[0], 0x10) << 0x70
        | int(hextet[1], 0x10) << 0x60
        | int(hextet[2], 0x10) << 0x50
        | int(hextet[3], 0x10) << 0x40
        | int(hextet[4], 0x10) << 0x30
        | int(hextet[5], 0x10) << 0x20
        | int(hextet[6], 0x10) << 0x10
        | int(hextet[7], 0x10) << 0x00
    )


def to_4(num):
    return "{0}.{1}.{2}.{3}".format(
        num >> 0x18 & 0xFF, num >> 0x10 & 0xFF, num >> 0x08 & 0xFF, num >> 0x00 & 0xFF
    )


def to_6(num, compressed=False):
    ipv6 = "{0:>04x}:{1:>04x}:{2:>04x}:{3:>04x}:{4:>04x}:{5:>04x}:{6:>04x}:{7:>04x}".format(
        num >> 0x70 & 0xFFFF,
        num >> 0x60 & 0xFFFF,
        num >> 0x50 & 0xFFFF,
        num >> 0x40 & 0xFFFF,
        num >> 0x30 & 0xFFFF,
        num >> 0x20 & 0xFFFF,
        num >> 0x10 & 0xFFFF,
        num >> 0x00 & 0xFFFF,
    )
    return ipv6 if not compressed else str(ipaddress.IPv6Address(ipv6).compressed)
