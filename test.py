import time

def cpu_intensive_task(n):
    result = 0
    for _ in range(n):
        result += 1
    return result

start_time = time.time()
cpu_intensive_task(1000000000)
end_time = time.time()

print(f"Time taken for 1000000000 iterations: {end_time - start_time} seconds")