#!/usr/bin/env python
import socket
import time
import sys


# ping -p 53 8.8.8.8


def main():
    # Create socket

    # Create payload
    packet = (
        b"x00"
        * 56  # Should be ReadableBuffer with "__buffer__". Sending 56 bytes of 00
    )
    print(packet)
    # Pass the payload to socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sock.sendto(packet, ("8.8.8.8", 53))
    # Wait for response
    start_time = time.time()
    sock.recvfrom(1024)
    end_time = time.time()
    time_to_receive_response = end_time - start_time
    print(f"Time to Receive Response:{time_to_receive_response}")


if __name__ == "__main__":
    main()
