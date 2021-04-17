# API process and Jupyter cell compatibility
from multiprocessing import Process
from wait4it import wait_for
from app import app, run

_api_process = None

def start_api():
    global _api_process
    if _api_process:
        _api_process.terminate()
        _api_process.join()
    
    _api_process = Process(target=run, daemon=True)
    _api_process.start()
    wait_for(port=8022)

def delete_route(method: str, path: str):
    [app.routes.remove(route) for route in app.routes if method in route.methods and route.path == path]

start_api()