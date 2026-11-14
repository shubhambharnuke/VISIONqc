import time
import requests
import numpy as np

BASE_URL = "http://localhost:8000"

def test_health_latency(n_requests=100):
    latencies = []
    print(f"Benchmarking /health ({n_requests} requests)...")
    for _ in range(n_requests):
        t0 = time.perf_counter()
        r = requests.get(f"{BASE_URL}/health")
        t1 = time.perf_counter()
        if r.status_code == 200:
            latencies.append((t1 - t0) * 1000)
    
    p50 = np.percentile(latencies, 50)
    p95 = np.percentile(latencies, 95)
    p99 = np.percentile(latencies, 99)
    print(f"Health check latency: P50: {p50:.2f}ms | P95: {p95:.2f}ms | P99: {p99:.2f}ms")

if __name__ == "__main__":
    try:
        test_health_latency()
    except Exception as e:
        print(f"Benchmark error: {e}")
