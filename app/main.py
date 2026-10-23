from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, IPvAnyAddress
from typing import Literal
from uuid import uuid4

app = FastAPI(
    title="NetPulse API",
    version="0.1.0",
    description="Simulated network device inventory API for a QA and DevOps portfolio lab.",
)

DeviceStatus = Literal["online", "offline", "degraded", "maintenance"]


class DeviceCreate(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    management_ip: IPvAnyAddress
    device_type: Literal["router", "switch", "optical-module", "simulator"]
    site: str = Field(min_length=2, max_length=100)


class Device(DeviceCreate):
    id: str
    status: DeviceStatus = "online"


class Interface(BaseModel):
    name: str
    admin_status: Literal["up", "down"]
    oper_status: Literal["up", "down"]
    speed_mbps: int = Field(gt=0)
    packet_loss_percent: float = Field(ge=0, le=100)
    latency_ms: float = Field(ge=0)


_devices: dict[str, Device] = {
    "dev-router-001": Device(
        id="dev-router-001",
        name="edge-router-lab-01",
        management_ip="192.0.2.10",
        device_type="router",
        site="lab-east",
        status="online",
    ),
    "dev-switch-001": Device(
        id="dev-switch-001",
        name="access-switch-lab-01",
        management_ip="192.0.2.20",
        device_type="switch",
        site="lab-east",
        status="degraded",
    ),
}

_interfaces: dict[str, list[Interface]] = {
    "dev-router-001": [
        Interface(name="eth0", admin_status="up", oper_status="up",
                  speed_mbps=1000, packet_loss_percent=0.0, latency_ms=2.4),
        Interface(name="eth1", admin_status="up", oper_status="up",
                  speed_mbps=10000, packet_loss_percent=0.0, latency_ms=1.2),
    ],
    "dev-switch-001": [
        Interface(name="eth0", admin_status="up", oper_status="up",
                  speed_mbps=1000, packet_loss_percent=2.5, latency_ms=18.0),
    ],
}


@app.get("/health", tags=["service"])
def health():
    return {"status": "ok", "service": "netpulse-api", "version": app.version}


@app.get("/api/v1/devices", response_model=list[Device], tags=["devices"])
def list_devices():
    return list(_devices.values())


@app.get("/api/v1/devices/{device_id}", response_model=Device, tags=["devices"])
def get_device(device_id: str):
    device = _devices.get(device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device


@app.post("/api/v1/devices", response_model=Device, status_code=status.HTTP_201_CREATED,
          tags=["devices"])
def create_device(payload: DeviceCreate):
    normalized_ip = str(payload.management_ip)
    if any(str(d.management_ip) == normalized_ip for d in _devices.values()):
        raise HTTPException(status_code=409, detail="Management IP already registered")
    device_id = f"dev-{uuid4().hex[:12]}"
    device = Device(**payload.model_dump(), id=device_id, status="online")
    _devices[device_id] = device
    _interfaces[device_id] = []
    return device


@app.get("/api/v1/devices/{device_id}/interfaces",
         response_model=list[Interface], tags=["interfaces"])
def list_interfaces(device_id: str):
    if device_id not in _devices:
        raise HTTPException(status_code=404, detail="Device not found")
    return _interfaces.get(device_id, [])
