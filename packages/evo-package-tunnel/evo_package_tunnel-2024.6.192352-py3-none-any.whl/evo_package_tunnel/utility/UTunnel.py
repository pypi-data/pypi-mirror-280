#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git | 
#========================================================================================================================================

from evo_framework import *
# ---------------------------------------------------------------------------------------------------------------------------------------
# UTunnel
# ---------------------------------------------------------------------------------------------------------------------------------------
""" UTunnel
"""
class UTunnel:  
    __instance = None

    def __init__(self):
        if UTunnel.__instance != None:
            raise Exception("ERROR_SINGLETON")
        else:
            UTunnel.__instance = self       
# -----------------------------------------------------------------------------
    @staticmethod
    def getInstance():
        if UTunnel.__instance == None:
            uObject = UTunnel()
            uObject.doInit()
            
        return UTunnel.__instance
# -----------------------------------------------------------------------------
    def doInit(self):
        try:
            pass
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# -----------------------------------------------------------------------------   
    async def doMethod0(self):
        try:
            return None
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
