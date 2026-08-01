from time import sleep

from backend.chaos_engine.telemetry import TelemetryGenerator

telemetry = TelemetryGenerator()

for _ in range(10):
    metrics = telemetry.update()

    print("=" * 50)
    print(f"CPU: {metrics.cpu_usage:.1f}%")
    print(f"Memory: {metrics.memory_usage:.1f}%")
    print(f"Disk: {metrics.disk_usage:.1f}%")
    print(f"Latency: {metrics.latency_ms} ms")
    print(f"Requests/sec: {metrics.requests_per_second}")
    print(f"Error Rate: {metrics.error_rate}%")
    print(f"Connections: {metrics.active_connections}")

    sleep(1)
