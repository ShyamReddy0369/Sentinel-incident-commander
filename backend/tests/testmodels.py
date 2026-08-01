from backend.chaos_engine.models import ServiceMetrics
from backend.chaos_engine.models import ServiceState


metrics = ServiceMetrics(
    cpu_usage=23.5,
    memory_usage=41.3,
    disk_usage=18.9,
    latency_ms=52,
    requests_per_second=187,
    error_rate=0.2,
    active_connections=14,
)

service = ServiceState(
    name="Authentication Service",
    owner="Identity Team",
    criticality="HIGH",
    metrics=metrics,
)

print(service)
