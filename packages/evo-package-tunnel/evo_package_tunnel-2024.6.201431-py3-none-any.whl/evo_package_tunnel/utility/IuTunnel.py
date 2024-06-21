#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git | 
#========================================================================================================================================

from evo_framework import *
from evo_package_tunnel.utility.UTunnel import UTunnel
# ---------------------------------------------------------------------------------------------------------------------------------------
# IuTunnel
# ---------------------------------------------------------------------------------------------------------------------------------------
""" IuTunnel
"""
class IuTunnel(object):
   
    @staticmethod
    async def doMethod0():
        return await UTunnel.getInstance().doMethod0()