import redis
import time
import json

redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

def process_task(task_id):
    task_data = redis_client.hgetall(f"task:{task_id}")
    if not task_data:
        return
    redis_client.hset(f"task:{task_id}", "status", "processing")
    time.sleep(2)  # Simulate task processing
    redis_client.hset(f"task:{task_id}", mapping={
        "status": "completed",
        "result": f"Processed {task_data['task']}"
    })

while True:
    task_id = redis_client.brpop("task_queue", timeout=5)
    if task_id:
        process_task(task_id[1])