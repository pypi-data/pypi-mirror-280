from pyngrok import ngrok, conf
from evo_framework.core.evo_core_log.utility.IuLog import IuLog
from evo_framework.core.evo_core_api.entity.EApiConfig import EApiConfig
class IuTunnelNgrok:
    @staticmethod
    async def do_use_ngrok(apiToken:str, locaPort:int) -> str:
        try:
            conf.get_default().auth_token = apiToken
            remoteUrl = ngrok.connect(str(locaPort)).public_url
            IuLog.doInfo(__name__, f"Ngrok remoteUrl:{remoteUrl}")
            return remoteUrl
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise exception