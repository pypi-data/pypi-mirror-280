from evo_framework.core.evo_core_log.utility.IuLog import IuLog
from evo_framework.core.evo_core_system.utility.IuSystem import IuSystem
from evo_framework.core.evo_core_api.entity.EApiConfig import EApiConfig
import re
import asyncio
class IuTunnelPinggy:
    @staticmethod
    async def do_use_pinggy(apiToken:str, locaPort:int) -> str:
        try:
           # Your existing method logic, with modifications to call do_exec_async correctly
            
            outputLog = "output_pinggy.log"
            timeAwait = 5
            # Combine the command into a single string for shell execution
            command = f"nohup ssh -p 443 -o StrictHostKeyChecking=no -R0:localhost:{locaPort} a.pinggy.io -T > {outputLog} 2>&1 &"
            await IuSystem.do_exec_async(command)
            IuLog.doInfo(__name__, f"await:{timeAwait}")
            await asyncio.sleep(timeAwait)

            data = None
            with open(f"{outputLog}", "r") as file:
                data = file.read()

            IuLog.doInfo(__name__, f"data:{data}")

            if data == None:
                raise Exception("CAN_NOT_READ_FILE")

            urls = re.findall(r"https://[^\s]+", data)
            remoteUrl = urls[1] if urls else None

            if remoteUrl == None:
                raise Exception("CAN_NOT_CREATE_REMOTE_URL")

            IuLog.doInfo(__name__, f"REMOTE_URL:{remoteUrl}")
            return remoteUrl
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise exception