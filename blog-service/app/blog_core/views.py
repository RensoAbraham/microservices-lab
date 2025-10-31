from django.http import JsonResponse
from django.db import connection
from django_redis import get_redis_connection

def healthz(request):
    try:
        connection.cursor()
        
        redis_conn = get_redis_connection("default")
        redis_conn.ping()

        return JsonResponse({"status": "ok", "db": "ok", "redis": "ok"})

    except Exception as e:
        return JsonResponse(
            {"status": "error", "details": str(e)}, 
            status=503
        )