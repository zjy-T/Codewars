
ip = "128.32.10.1"
def ip_to_int32(ip):
    lst = ip.split(".")
    ret = []
    for i in lst:
        ret.append((format(int(i), 'b')).zfill(8))

    ipbin = "".join(ret)
    int32 = int(ipbin, 2)

    return int32

print(ip_to_int32(ip))

### Passed ###