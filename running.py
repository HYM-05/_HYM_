#main file, running multiples python file at the same time
import threading
import subprocess

def run_script(script_name):
    subprocess.run(["python", script_name])

if __name__ == "__main__":
    script1_thread = threading.Thread(target=run_script, args=(r"D:\HOC TAP\code\pygame\main.py",))
    script2_thread = threading.Thread(target=run_script, args=(r"D:\HOC TAP\code\pygame\timeLimiter.py",))

    script1_thread.start()
    script2_thread.start()

    script1_thread.join()
    script2_thread.join()
