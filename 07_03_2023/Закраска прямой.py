N = int(input())
cargo = []
for _ in range(N):
    arrival, processing = map(int, input().split())
    cargo.append((arrival, processing))

cargo.sort()

machines = []
for arrival, processing in cargo:
    for i in range(len(machines)):
        if machines[i] <= arrival:
            machines[i] = arrival + processing
            break
    else:
        machines.append(arrival + processing)

print(len(machines))
