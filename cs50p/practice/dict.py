tasks = [
    {"title": "Buy milk", "status": "pending"},
    {"title": "Study Python", "status": "pending"},
    {"title": "Go for a walk", "status": "pending"}
]

for task in tasks:
    if task["status"] == "pending":
        print(task["title"])
