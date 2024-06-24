from __future__ import annotations

from typing import (
    Optional, Dict, List
)
from enum import Enum
from pydantic import BaseModel, field_validator, Field


class WorkerStatus(Enum):
    # The worker be started, and not working yet
    Inflight = "Inflight"
    # The worker is free
    Free = 'Free'
    # The worker is busy now
    Busy = 'Busy'


class Worker(BaseModel):
    worker_id: str
    gpu_type: Optional[str] = Field(None, description='')
    region: str
    started_at: int
    last_service_time: int
    number_of_successes: int
    number_of_failures: int
    # if number_of_successes great than zero, this worker cloud not be scale down
    number_of_sessions: int
    average_response_time: float
    status: WorkerStatus

    @staticmethod
    def from_json(data: any) -> Worker:
        return Worker.model_validate_json(data)

    @classmethod
    @field_validator('gpu_type')
    def prevent_none(cls, v):
        return v


class QueueReason(Enum):
    #
    NotDispatch = "NotDispatch"
    # all worker is busy
    QueueDueBusy = 'QueueDueBusy'
    # session worker is busy
    QueueDueSession = 'QueueDueSession'


class Request(BaseModel):
    # time of enter the queued_request.py
    queue_time: int
    # queued_request.py reason
    queue_reason: QueueReason

    @staticmethod
    def from_json(data: any) -> Request:
        return Request.model_validate_json(data)


Queue = Dict[QueueReason, int]
Worker = Dict[WorkerStatus, int]


class Factors(BaseModel):
    # 10 -> queued_request.py information at 10 seconds ago
    # 30 -> queued_request.py information at 30 seconds ago
    # 60 -> queued_request.py information at 60 seconds ago
    queue_histories: Optional[Dict[int, Queue]] = Field(default={})

    # queue statistic
    queue: Optional[Queue] = Field(default=None)

    # utilization, unsupported yet
    utilization: Optional[int] = Field(default=None)

    workers: Optional[List[Worker]] = Field(default=[])

    worker: Optional[Worker] = Field(default=None)

    worker_histories: Optional[Dict[int, Worker]] = Field(default=None)

    @staticmethod
    def from_json(data) -> Factors:
        return Factors.model_validate_json(data)
