#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git # 
#========================================================================================================================================

from evo_framework import *
from evo_package_openai.entity import *
from evo_package_assistant import *
from openai import OpenAI, AuthenticationError, AssistantEventHandler


# ---------------------------------------------------------------------------------------------------------------------------------------
# UOpenai
# ---------------------------------------------------------------------------------------------------------------------------------------
""" UOpenai
"""
class UOpenai:  
    __instance = None

    def __init__(self):
        if UOpenai.__instance != None:
            raise Exception("ERROR_SINGLETON")
        else:
            UOpenai.__instance = self       
# ---------------------------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getInstance():
        if UOpenai.__instance == None:
            uObject = UOpenai()
            uObject.doInit()
            
        return UOpenai.__instance
# ---------------------------------------------------------------------------------------------------------------------------------------
    def doInit(self):
        try:
            pass
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------  
    async def doChatStream(self, eOpenaiInput:EOpenaiInput):
        try:
            IuLog.doVerbose(__name__,f"{eOpenaiInput}")
            eOpenaiOutput = EOpenaiOutput()
            eOpenaiOutput.doGenerateID()

            if eOpenaiInput is None:
                raise Exception("ERROR_eOpenaiInput_IS_NONE")
            
            if eOpenaiInput.openaiToken is None:
                raise Exception("ERROR_openaiToken_IS_NONE")
            
            if eOpenaiInput.text is None:
                raise Exception("ERROR_text_IS_NONE")
            
            if eOpenaiInput.model is None:
                raise Exception("ERROR_model_IS_NONE")
            
            if eOpenaiInput.eAssistantID is None:
                raise Exception("ERROR_eAssistantID_IS_NONE")
            
            client = OpenAI(api_key=eOpenaiInput.openaiToken)
            
            eAssistant = await self.doGetEAssistant(eOpenaiInput.eAssistantID)
            
            if eAssistant is None:
                raise Exception(f"ERROR_eAssistant_IS_NONE_{eOpenaiInput.eAssistantID}")
            

            self.doInitEAssistant(eAssistant)
            
            arrayMessage = eAssistant.arrayMessage
            arrayMessage.append(
                    {
                        "role": "user",
                        "content": eOpenaiInput.text,
                    }
                )
            
            if eAssistant.callback is not None:
                cAssistantParser = eAssistant.callback()
            else:
                cAssistantParser = CAssistantCallbackStream()
            
            stream = client.chat.completions.create(
                        model = eOpenaiInput.model,
                        messages = arrayMessage,
                        stream = True,
                    )
            IuLog.doVerbose(__name__,f"arrayMessage:\n{arrayMessage}")      
            for chunk in stream:   
                contentText=chunk.choices[0].delta.content
                
                eApiText = cAssistantParser.onParser(contentText) 
                eOpenaiOutput.eApiText=eApiText
                eOpenaiOutput.doGenerateTime()
                    
                IuLog.doVerbose(__name__, f"{eOpenaiOutput}")
               
                yield eOpenaiOutput
                
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doChat(self, eOpenaiInput:EOpenaiInput):
        try:
            eOpenaiOutput = EOpenaiOutput()
            eOpenaiOutput.doGenerateID()
            try:
                
                if eOpenaiInput is None:
                    raise Exception("ERROR_eOpenaiInput_IS_NONE")
                
                if eOpenaiInput.openaiToken is None:
                    raise Exception("ERROR_openaiToken_IS_NONE")
                
                if eOpenaiInput.text is None:
                    raise Exception("ERROR_text_IS_NONE")
                
                if eOpenaiInput.model is None:
                    raise Exception("ERROR_model_IS_NONE")
                
                if eOpenaiInput.eAssistantID is None:
                    raise Exception("ERROR_eAssistantID_IS_NONE")
                
                client = OpenAI(api_key=eOpenaiInput.openaiToken)
               
                eAssistant = await self.doGetEAssistant(eOpenaiInput.eAssistantID)
                
                if eAssistant is None:
                    raise Exception(f"ERROR_eAssistant_IS_NONE_{eOpenaiInput.eAssistantID}")
                

                self.doInitEAssistant(eAssistant)
                
                arrayMessage = eAssistant.arrayMessage
                arrayMessage.append(
                        {
                            "role": "user",
                            "content": eOpenaiInput.text,
                        }
                    )
                
                if eAssistant.callback is not None:
                    cAssistantParser = eAssistant.callback()
                else:
                    cAssistantParser = CAssistantCallbackStream()
                    cAssistantParser.isParseHeader = False
                  
                stream = client.chat.completions.create(
                            model = eOpenaiInput.model,
                            messages = arrayMessage,
                           # stream = True,
                        )
                        
                for chunk in stream:   
                    eApiText = cAssistantParser.onParser(chunk.choices[0].delta.content) 
                    eOpenaiOutput.eApiText=eApiText
                    eOpenaiOutput.doGenerateTime()
                    yield eOpenaiOutput
     
            except Exception as exception:          
                if isinstance(exception, AuthenticationError):
                    error = f"{exception.code}"
                else:
                    error=f"{exception}"        
                eOpenaiOutput.isError = True
                eOpenaiOutput.error = error
                
                yield eOpenaiOutput
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doGetEAssistant(self, id:str ) -> EAssistant:
        try:
            eAssistant = await IuAssistant.doGet(id)
            return eAssistant
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    def doInitEAssistant(self, eAssistant: EAssistant):
        try:
            if eAssistant.arrayMessage is None:
                arrayMessage = []
                for eEassistantMessage in eAssistant.mapEAssistantMessage.values():
                    if isinstance(eEassistantMessage, EAssistantMessage):
                        arrayMessage.append(
                            {
                                "role": eEassistantMessage.enumAssistantRole.name.lower(),
                                "content": eEassistantMessage.message,
                            }
                        )

                eAssistant.arrayMessage = arrayMessage
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------

    async def doOpenaiOld(self):
        try:
            inputApiKey = CSetting.getInstance().doGet("ACCESS_TOKEN_OPENAI")
            client = OpenAI(api_key=inputApiKey)
            
            assistant = client.beta.assistants.create(
            name="Math Tutor",
            instructions="You are a personal math tutor. Write and run code to answer math questions.",
            tools=[{"type": "code_interpreter"}],
            model="gpt-3.5-turbo-0125",
            )

            thread = client.beta.threads.create()

            message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content="I need to solve the equation `3x + 11 = 15`. Can you help me?"
            )
            
            # First, we create a EventHandler class to define
            # how we want to handle the events in the response stream.
            
            class EventHandler(AssistantEventHandler):    
                @override
                def on_text_created(self, text) -> None:
                    print("on_text_created", text)
                    print(f"\nassistant > ", end="", flush=True)
                    
                @override
                def on_text_delta(self, delta, snapshot):
                    print(delta.value, end="", flush=True)
                    
                def on_tool_call_created(self, tool_call):
                    print(f"\nassistant > {tool_call.type}\n", flush=True)
                
                def on_tool_call_delta(self, delta, snapshot):
                    if delta.type == 'code_interpreter':
                        if delta.code_interpreter.input:
                            print(delta.code_interpreter.input, end="", flush=True)
                        if delta.code_interpreter.outputs:
                            print(f"\n\noutput >", flush=True)
                            for output in delta.code_interpreter.outputs:
                                if output.type == "logs":
                                    print(f"\n{output.logs}", flush=True)
            

            with client.beta.threads.runs.stream(
                thread_id=thread.id,
                assistant_id=assistant.id,
                instructions="Please address the user as Jane Doe. The user has a premium account.",
                event_handler=EventHandler(),
            ) as stream:
                stream.until_done()
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doGetModel(self) -> EOpenaiModelMap:
        try:
            inputApiKey = CSetting.getInstance().doGet("ACCESS_TOKEN_OPENAI")
            client = OpenAI(api_key=inputApiKey)
            
            arrayModel = (client.models.list())
            
            eOpenaiModelMap = EOpenaiModelMap()
            eOpenaiModelMap.doGenerateID()
            
            for model in arrayModel:
                eOpenaiModel = EOpenaiModel()
                eOpenaiModel.id = model.id
                eOpenaiModel.created = model.created
                eOpenaiModelMap.mapEModel.doSet(eOpenaiModel)
            
            return eOpenaiModelMap
        except Exception as exception:
            IuLog.doException(__name__, exception)
            raise
  
  