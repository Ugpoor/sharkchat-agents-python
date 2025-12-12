from openai import AsyncOpenAI
import os
from typing_extensions import Literal

from .models import _openai_shared
from .tracing import set_tracing_export_api_key


def set_default_openai_key(key: str, use_for_tracing: bool) -> None:
    _openai_shared.set_default_openai_key(key)

    if use_for_tracing:
        set_tracing_export_api_key(key)


def set_default_openai_client(client: AsyncOpenAI, use_for_tracing: bool) -> None:
    _openai_shared.set_default_openai_client(client)

    if use_for_tracing:
        set_tracing_export_api_key(client.api_key)


def set_default_openai_api(api: Literal["chat_completions", "responses"]) -> None:
    if api == "chat_completions":
        _openai_shared.set_use_responses_by_default(False)
    else:
        _openai_shared.set_use_responses_by_default(True)

# 新增：可选接口，允许通过代码设置基础 URL（非必须，环境变量优先）
def set_default_openai_base_url(url: str) -> None:
    """设置默认 OpenAI 基础 URL（覆盖环境变量 OPENAI_BASE_URL）"""
    _openai_shared.set_default_base_url(url)