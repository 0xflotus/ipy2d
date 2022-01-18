
def to_int(ip):
    arr = ip.split('.')
    return int(arr[0]) << 0x18 | int(arr[1]) << 0x10 | int(arr[2]) << 0x08 | int(arr[3]) << 0x00