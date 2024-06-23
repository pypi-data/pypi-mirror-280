# See LICENSE.md file in project root directory

import os
import json
import time
import traceback
from functools import wraps
from base64 import b64decode
from datetime import datetime
from cloudevents.http import CloudEvent
from retry_requests import retry, RSession
from functions_framework import cloud_event

sess = retry(RSession(timeout=30), retries=3)

def log(*args):
    print("[" + str(datetime.now()) + "]", *args)

'''
@def_service(key)
def app(**kwargs)
    ...
    
Translates to: app = def_service(key)(app)

This means def_automation(key) must return a function that takes app as an argument and returns a function that takes **kwargs as arguments.
'''

API_URL = os.getenv('STAX_CX_API_URL', 'https://api.cx.stax.ai')

# Define automation wrapper decorator
def def_service(key:str):
    def decorator(app):
        
        # This is where it gets tricky... The app itself should be registered as a cloud function and we need to use the functions_framework.cloud_event decorator to do that.
        @cloud_event
        @wraps(app)
        def wrapper(e: CloudEvent):
            msg = b64decode(e.data["message"]["data"]).decode()
            
            t0 = time.time()
            # The message is a JSON string with the appropriate kwargs
            # It MAY have the 'team' key
            body = json.loads(msg)
            team = body.get('team')
            
            cx_api_headers = {
                "x-internal-key": key,
                "x-team-id": team, # Optional
            }
            
            try:
                # Call automation/app function
                msg = app(**body)
                dt = (time.time() - t0) * 1000
                log("✅ Complete! Execution time:", dt, "ms")

            except Exception as e:
                log("🚨 Error!")
                trace = traceback.format_exc()
                print(trace)

                # Report error to the Stax.ai API
                res = sess.post(f"{API_URL}/auto/_service", headers=cx_api_headers, json={
                    "type": "Error",
                    "error": "An error ocurred in the service",
                    "traceback": trace,
                    "execution_time": (time.time() - t0) * 1000
                })
                if res.status_code != 200:
                    log("🚨 Failed to report task error!")
                    return

        return wrapper
    return decorator