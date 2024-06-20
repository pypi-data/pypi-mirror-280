#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git | 
#========================================================================================================================================

from evo_framework import *
# ---------------------------------------------------------------------------------------------------------------------------------------
# UCyborgai
# ---------------------------------------------------------------------------------------------------------------------------------------
""" UCyborgai
"""
class UCyborgai:  
    __instance = None

    def __init__(self):
        if UCyborgai.__instance != None:
            raise Exception("ERROR_SINGLETON")
        else:
            UCyborgai.__instance = self       
# -----------------------------------------------------------------------------
    @staticmethod
    def getInstance():
        if UCyborgai.__instance == None:
            uObject = UCyborgai()
            uObject.doInit()
            
        return UCyborgai.__instance
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
