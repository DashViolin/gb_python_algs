def process_packets(packets, size):
    buffer = []
    result = [0] * len(packets)
    for i, (arrival, duration) in enumerate(packets):
        while buffer and buffer[0] <= arrival:
            buffer.pop(0)
        if len(buffer) >= size:
            result[i] = -1
        else:
            result[i] = max(arrival, buffer[-1] if buffer else 0)
            buffer.append(result[i] + duration)
    return result


size, n = map(int, input().split())
packets = []
if n:
    for _ in range(n):
        packets.append(tuple(map(int, input().split())))
    result = process_packets(size=size, packets=packets)
    print(*result, sep='\n')
