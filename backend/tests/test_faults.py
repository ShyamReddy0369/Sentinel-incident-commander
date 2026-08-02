from backend.chaos_engine.models import ServiceMetrics
from backend.chaos_engine.fault_injector import (
    CPUSpikeFault,
    MemoryLeakFault,
)
from backend.chaos_engine.health import HealthEngine

engine = HealthEngine()

metrics = ServiceMetrics(
    cpu_usage=30,
    memory_usage=40,
    disk_usage=20,
    latency_ms=40,
    requests_per_second=120,
    error_rate=0.2,
    active_connections=15,
)

print("=" * 60)
print("Initial State")
print(metrics)
print("Health:", engine.evaluate(metrics))

cpu_fault = CPUSpikeFault()

cpu_fault.apply(metrics)

print("\nAfter CPU Spike")
print(metrics)
print("Health:", engine.evaluate(metrics))

memory_fault = MemoryLeakFault()

memory_fault.apply(metrics)

print("\nAfter Memory Leak")
print(metrics)
print("Health:", engine.evaluate(metrics))
