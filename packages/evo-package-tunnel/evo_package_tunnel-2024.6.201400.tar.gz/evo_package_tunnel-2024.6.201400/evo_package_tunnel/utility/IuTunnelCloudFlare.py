import subprocess
import re
import threading
import time

from evo_framework.core.evo_core_log.utility.IuLog import IuLog
from evo_framework.core.evo_core_api.entity.EApiConfig import EApiConfig
class IuTunnelCloudFlare:
    @staticmethod
    async def do_use_cloudflare(locaPort:int) -> str:
        try:
           
            IuLog.doInfo(__name__, f"do_use_cloudflare locaPort:{locaPort}")
            IuLog.doVerbose(__name__, "Starting Cloudflare Tunnel...")
            # Start the Cloudflare Tunnel and capture its output
            process = subprocess.Popen(['pycloudflared', 'tunnel', '--url', f'http://127.0.0.1:{locaPort}'],
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

            # Read the output line by line and search for the URL for 10 seconds
            start_time = time.time()
            while time.time() - start_time < 10:  # Run for 10 seconds
                line = process.stdout.readline()
                if '.trycloudflare.com' in line:
                    url = re.search(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com', line)
                    if url:
                        IuLog.doVerbose(__name__, f"Tunnel URL: {url.group()}")
                        return url.group()
                        #break

            # After 10 seconds, continue running without printing
            while True:
                process.stdout.readline()
                if process.poll() is not None:
                    break
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise