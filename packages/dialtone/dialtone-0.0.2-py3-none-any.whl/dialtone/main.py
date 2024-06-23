import requests
from typing import Any, Dict, Optional, List
from pydantic import ValidationError, BaseModel
from dialtone.types import (
    ProviderConfig,
    RouterModelConfig,
    ChatCompletion,
    Choice,
    ChatMessage,
    Tool,
    DialtoneClient,
    Dials,
    RouteDecision,
    TokenUsage,
    LLM,
)

DEFAULT_BASE_URL = "https://anneal--llm-router-web-fastapi-app.modal.run"


class Completions(BaseModel):
    client: DialtoneClient

    def create(self, messages: list[ChatMessage], tools: list[Tool] = []):
        params = {
            "messages": [message.to_dict() for message in messages],
            "dials": self.client.dials.model_dump(),
            "provider_config": self.client.provider_config.model_dump(),
        }
        if self.client.router_model_config:
            params["router_model_config"] = self.client.router_model_config.model_dump()
        if tools:
            params["tools"] = [tool.model_dump() for tool in tools]
        if self.client.include_models:
            params["include_models"] = self.client.include_models
        if self.client.exclude_models:
            params["exclude_models"] = self.client.exclude_models

        try:
            response = requests.post(
                f"{self.client.base_url}/chat/completions", json=params
            )
            response.raise_for_status()
            response_json = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            raise e

        return ChatCompletion(
            choices=[
                Choice(
                    model=response_json["model"],
                    provider=response_json["provider"],
                    message=response_json["message"],
                )
            ],
            usage=TokenUsage(**response_json["usage"]),
        )


class Chat(BaseModel):
    client: DialtoneClient
    completions: Completions

    def __init__(self, client: DialtoneClient):
        completions = Completions(client=client)
        super().__init__(client=client, completions=completions)

    def route(self, messages: list[ChatMessage], tools: list[Tool] = []):
        params = {
            "messages": [message.to_dict() for message in messages],
            "dials": self.client.dials.model_dump(),
            "provider_config": self.client.provider_config.model_dump(),
        }
        if self.client.router_model_config:
            params["router_model_config"] = self.client.router_model_config.model_dump()
        if tools:
            params["tools"] = [tool.model_dump() for tool in tools]
        if self.client.include_models:
            params["include_models"] = self.client.include_models
        if self.client.exclude_models:
            params["exclude_models"] = self.client.exclude_models

        try:
            response = requests.post(f"{self.client.base_url}/chat/route", json=params)
            response.raise_for_status()
            response_json = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            raise e

        return RouteDecision(
            model=response_json["model"],
            providers=response_json["providers"],
            inference_time=response_json["inference_time"],
            quality_predictions=response_json["quality_predictions"],
            routing_strategy=response_json["routing_strategy"],
        )


class Dialtone:
    chat: Chat
    client: DialtoneClient

    def __init__(
        self,
        provider_config: ProviderConfig | Dict[str, Any],
        dials: Dials | Dict[str, Any] = Dials(quality=0.5, cost=0.5, speed=0),
        router_model_config: Optional[RouterModelConfig | Dict[str, Any]] = None,
        base_url: str = DEFAULT_BASE_URL,
        include_models: Optional[List[LLM | str]] = None,
        exclude_models: Optional[List[LLM | str]] = None,
    ):
        try:
            if isinstance(provider_config, dict):
                provider_config = ProviderConfig(**provider_config)
        except ValidationError as e:
            raise ValidationError(f"Invalid provider_config: {e}")

        try:
            if router_model_config:
                if isinstance(router_model_config, dict):
                    router_model_config = RouterModelConfig(**router_model_config)
            else:
                router_model_config = None
        except ValidationError as e:
            raise ValidationError(f"Invalid router_model_config: {e}")

        try:
            if not isinstance(dials, Dials):
                dials = Dials(**dials)
        except ValidationError as e:
            raise ValidationError(f"Invalid dials: {e}")

        try:
            typed_include_models = None
            if include_models:
                typed_include_models = [
                    LLM(model) if isinstance(model, str) else model
                    for model in include_models
                ]
        except ValueError as e:
            raise ValidationError(f"Invalid include_models: {e}")

        try:
            typed_exclude_models = None
            if exclude_models:
                typed_exclude_models = [
                    LLM(model) if isinstance(model, str) else model
                    for model in exclude_models
                ]
        except ValueError as e:
            raise ValidationError(f"Invalid exclude_models: {e}")

        self.client = DialtoneClient(
            provider_config=provider_config,
            router_model_config=router_model_config,
            base_url=base_url,
            dials=dials,
            include_models=typed_include_models,
            exclude_models=typed_exclude_models,
        )
        self.chat = Chat(client=self.client)
