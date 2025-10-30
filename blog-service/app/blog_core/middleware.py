import json
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

class SimpleLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        
        log_data = {
            "method": request.method,
            "path": request.path,
            "status_code": response.status_code,
            "duration_ms": round(duration * 1000, 2),
        }
        
        logger.info(json.dumps(log_data))
        return response