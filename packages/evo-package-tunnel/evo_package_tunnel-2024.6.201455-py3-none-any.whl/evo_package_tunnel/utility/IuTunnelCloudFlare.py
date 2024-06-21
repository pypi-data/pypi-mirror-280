import subprocess
import re
import threading
import time
import asyncio
from evo_framework.core.evo_core_log.utility.IuLog import IuLog
from evo_framework.core.evo_core_api.entity.EApiConfig import EApiConfig


class IuTunnelCloudFlare:
    @staticmethod
    async def do_use_cloudflare(locaPort: int) -> str:
        try:
            IuLog.doInfo(__name__, f"do_use_cloudflare locaPort:{locaPort}")
            IuLog.doVerbose(__name__, "Starting Cloudflare Tunnel...")
            
            # Start the Cloudflare Tunnel and capture its output
            process = subprocess.Popen(
                ["pycloudflared", "tunnel", "--url", f"http://127.0.0.1:{locaPort}"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            # Read the output line by line and search for the URL for 10 seconds
            start_time = time.time()
            while time.time() - start_time < 10:  # Run for 10 seconds
                stdout_line = process.stdout.readline()
                stderr_line = process.stderr.readline()
                
                if ".trycloudflare.com" in stdout_line:
                    url = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", stdout_line)
                    if url:
                        IuLog.doVerbose(__name__, f"Tunnel URL: {url.group()}")
                        return url.group()

                if stderr_line:
                    IuLog.doVerbose(__name__, f"stderr: {stderr_line.strip()}")
                    raise Exception(f"ERROR_CLOUDFLARE: {stderr_line.strip()}")

            # After 10 seconds, continue running without printing
            while True:
                stdout_line = process.stdout.readline()
                stderr_line = process.stderr.readline()
                
                if process.poll() is not None:
                    break
                
                if stderr_line:
                    IuLog.doVerbose(__name__, f"stderr: {stderr_line.strip()}")
                    raise Exception(f"ERROR_CLOUDFLARE: {stderr_line.strip()}")
                    
                await asyncio.sleep(0.1)  # Allow other tasks to run

        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise
