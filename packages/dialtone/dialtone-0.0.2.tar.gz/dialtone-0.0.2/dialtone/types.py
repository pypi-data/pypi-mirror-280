from enum import StrEnum
from pydantic import BaseModel
from typing import Literal, List, Dict, Any, Optional


class Tool(BaseModel):
    type: Literal["function"]
    function: Dict[str, Any]


class ToolCallFunction(BaseModel):
    name: str
    arguments: Dict[str, Any]


class ToolCall(BaseModel):
    id: str
    type: Literal["function"]
    function: ToolCallFunction


class ChatMessage(BaseModel):
    role: Literal["system", "user", "assistant", "tool"]
    content: str
    tool_calls: Optional[List[ToolCall]] = None

    def to_dict(self):
        result: Dict[str, Any] = {
            "role": self.role,
            "content": self.content,
        }
        if self.tool_calls:
            result["tool_calls"] = (
                [
                    {
                        "id": tool_call.id,
                        "type": tool_call.type,
                        "function": {
                            "name": (
                                tool_call.function.name if tool_call.function else None
                            ),
                            "arguments": (
                                tool_call.function.arguments
                                if tool_call.function
                                else None
                            ),
                        },
                    }
                    for tool_call in self.tool_calls
                ]
                if self.tool_calls
                else None
            )
        return result


class Provider(StrEnum):
    OpenAI = "openai"
    Groq = "groq"
    DeepInfra = "deepinfra"
    Fireworks = "fireworks"
    Together = "together"
    Replicate = "replicate"
    Anthropic = "anthropic"
    Google = "google"
    Cohere = "cohere"

    def __str__(self):
        return self.value


class LLM(StrEnum):
    claude_3_opus = "claude-3-opus-20240229"
    claude_3_sonnet = "claude-3-sonnet-20240229"
    claude_3_haiku = "claude-3-haiku-20240307"
    gpt_4o = "gpt-4o-2024-05-13"
    gpt_3_5_turbo = "gpt-3.5-turbo-0125"
    gemini_1_5_pro = "gemini-1.5-pro"
    gemini_1_5_flash = "gemini-1.5-flash"
    command_r_plus = "command-r-plus"
    command_r = "command-r"
    llama_3_70b = "llama3-70b-8192"

    def __str__(self):
        return self.value


class Choice(BaseModel):
    model: LLM
    provider: Provider
    message: ChatMessage


class TokenUsage(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


class ChatCompletion(BaseModel):
    choices: List[Choice]
    usage: TokenUsage


class OpenAIConfig(BaseModel):
    api_key: str


class AnthropicConfig(BaseModel):
    api_key: str


class GoogleConfig(BaseModel):
    api_key: str


class CohereConfig(BaseModel):
    api_key: str


class GroqConfig(BaseModel):
    api_key: str


class ReplicateConfig(BaseModel):
    api_key: str


class FireworksConfig(BaseModel):
    api_key: str


class TogetherConfig(BaseModel):
    api_key: str


class DeepInfraConfig(BaseModel):
    api_key: str


class Llama3RouterConfig(BaseModel):
    tools_providers: List[Provider] = []
    no_tools_providers: List[Provider] = []


class ProviderConfig(BaseModel):
    openai: Optional[OpenAIConfig] = None
    anthropic: Optional[AnthropicConfig] = None
    google: Optional[GoogleConfig] = None
    cohere: Optional[CohereConfig] = None
    groq: Optional[GroqConfig] = None
    replicate: Optional[ReplicateConfig] = None
    fireworks: Optional[FireworksConfig] = None
    together: Optional[TogetherConfig] = None
    deepinfra: Optional[DeepInfraConfig] = None

    @classmethod
    def OpenAI(cls, api_key: str) -> OpenAIConfig:
        return OpenAIConfig(api_key=api_key)

    @classmethod
    def Anthropic(cls, api_key: str) -> AnthropicConfig:
        return AnthropicConfig(api_key=api_key)

    @classmethod
    def Google(cls, api_key: str) -> GoogleConfig:
        return GoogleConfig(api_key=api_key)

    @classmethod
    def Cohere(cls, api_key: str) -> CohereConfig:
        return CohereConfig(api_key=api_key)

    @classmethod
    def Groq(cls, api_key: str) -> GroqConfig:
        return GroqConfig(api_key=api_key)

    @classmethod
    def Replicate(cls, api_key: str) -> ReplicateConfig:
        return ReplicateConfig(api_key=api_key)

    @classmethod
    def Fireworks(cls, api_key: str) -> FireworksConfig:
        return FireworksConfig(api_key=api_key)

    @classmethod
    def Together(cls, api_key: str) -> TogetherConfig:
        return TogetherConfig(api_key=api_key)

    @classmethod
    def DeepInfra(cls, api_key: str) -> DeepInfraConfig:
        return DeepInfraConfig(api_key=api_key)


class RouterModelConfig(BaseModel):
    llama_3_70b: Llama3RouterConfig

    @classmethod
    def Llama3(
        cls,
        tools_providers: List[Provider] = [],
        no_tools_providers: List[Provider] = [],
    ) -> Llama3RouterConfig:
        return Llama3RouterConfig(
            tools_providers=tools_providers, no_tools_providers=no_tools_providers
        )


class Dials(BaseModel):
    quality: float
    cost: float
    speed: Optional[float] = None

    def sum_to_one(self) -> bool:
        return (self.quality + self.cost + (self.speed if self.speed else 0)) == 1


class DialtoneClient(BaseModel):
    provider_config: ProviderConfig
    dials: Dials
    router_model_config: Optional[RouterModelConfig] = None
    base_url: Optional[str] = None
    include_models: Optional[List[LLM]] = None
    exclude_models: Optional[List[LLM]] = None


class RouteDecision(BaseModel):
    model: LLM
    providers: List[Provider]
    inference_time: float
    quality_predictions: Dict[str, float]
    routing_strategy: str
