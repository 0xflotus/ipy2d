import netaddr
import ipaddress

def from_4(ipv4):
    arr = ipv4.split('.')
    return int(arr[0]) << 0x18 | int(arr[1]) << 0x10 | int(arr[2]) << 0x08 | int(arr[3]) << 0x00

def from_6(ipv6):
    ip = netaddr.IPAddress(ipv6)
    arr = ip.format(dialect=netaddr.ipv6_verbose).split(':')
    return int(arr[0], 0x10) << 0x70 | \
           int(arr[1], 0x10) << 0x60 | \
           int(arr[2], 0x10) << 0x50 | \
           int(arr[3], 0x10) << 0x40 | \
           int(arr[4], 0x10) << 0x30 | \
           int(arr[5], 0x10) << 0x20 | \
           int(arr[6], 0x10) << 0x10 | \
           int(arr[7], 0x10) << 0x00 

def to_4(num):
    return "{0}.{1}.{2}.{3}".format(num >> 0x18 & 0xff, \
                                    num >> 0x10 & 0xff, \
                                    num >> 0x08 & 0xff, \
                                    num >> 0x00 & 0xff)
                                
def to_6(num, compressed=False):
    ipv6 = "{0:>04x}:{1:>04x}:{2:>04x}:{3:>04x}:{4:>04x}:{5:>04x}:{6:>04x}:{7:>04x}".format( \
        num >> 0x70 & 0xffff, \
        num >> 0x60 & 0xffff, \
        num >> 0x50 & 0xffff, \
        num >> 0x40 & 0xffff, \
        num >> 0x30 & 0xffff, \
        num >> 0x20 & 0xffff, \
        num >> 0x10 & 0xffff, \
        num >> 0x00 & 0xffff)
    return ipv6 if not compressed else str(ipaddress.IPv6Address(ipv6).compressed)