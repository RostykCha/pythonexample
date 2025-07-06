import time

def wait_for(condition_fn, timeout=5, interval=0.1):
    start = time.time()
    while time.time() - start < timeout:
        if condition_fn():
            return True
        time.sleep(interval)
    raise TimeoutError('condition not met within timeout')
