import requests
from fastapi import Request
from starlette.concurrency import run_in_threadpool
from datetime import datetime
import time
import asyncio
import os

class HitCounterMiddleware:
    def __init__(self, app, project_name: str, base_api_url: str = None):
        self.app = app
        self.project_name = project_name
        self.base_api_url = base_api_url or os.environ.get("HITCOUNTER_URL") or "http://192.168.101.231:10101"
        self.fixed_endpoint = "/track_hit"

    def _track_hit(self, request: Request, response_time: float):
        if not self.base_api_url:
            return

        payload = {
            "project_name": self.project_name,
            "endpoint": request.url.path,
            "client_ip": request.client.host,
            "timestamp": datetime.now().isoformat(),
            "request_method": request.method,
            "response_time": response_time,
        }

        def send_request():
            try:
                full_url = f"{self.base_api_url.rstrip('/')}{self.fixed_endpoint}"
                requests.post(full_url, json=payload, timeout=5).raise_for_status()
            except requests.exceptions.RequestException:
                pass  # Silently fail

        asyncio.create_task(run_in_threadpool(send_request))

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            start_time = time.time()
            await self.app(scope, receive, send)
            self._track_hit( Request(scope, receive), time.time() - start_time)
        else:
            await self.app(scope, receive, send)