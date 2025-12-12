from __future__ import annotations
import os
from openai import AsyncOpenAI

_default_openai_key: str | None = None
_default_openai_client: AsyncOpenAI | None = None
_use_responses_by_default: bool = True
_default_base_url: str = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")


# 基础 URL 配置（新增）
def set_default_base_url(url: str) -> None:
    """设置默认 OpenAI API 基础 URL（覆盖环境变量 OPENAI_BASE_URL）"""
    global _default_base_url
    _default_base_url = url


def get_default_base_url() -> str:
    """获取当前默认的 OpenAI API 基础 URL"""
    return _default_base_url


# 客户端管理（修改 get_default_openai_client 逻辑）
def get_default_openai_client() -> AsyncOpenAI:
    """获取默认客户端，若未初始化则自动创建（整合 key 和 base_url 配置）"""
    global _default_openai_client
    if _default_openai_client is None:
        # 优先使用已设置的 key，其次读取环境变量
        api_key = _default_openai_key or os.getenv("OPENAI_API_KEY")
        # 初始化客户端（若未提供 api_key，OpenAI 库会自动处理环境变量）
        _default_openai_client = AsyncOpenAI(
            api_key=api_key,
            base_url=_default_base_url
        )
    return _default_openai_client


# 原有函数保持不变（仅补充类型注释）
def set_default_openai_key(key: str) -> None:
    """设置默认 OpenAI API 密钥"""
    global _default_openai_key
    _default_openai_key = key


def get_default_openai_key() -> str | None:
    """获取当前默认的 OpenAI API 密钥"""
    return _default_openai_key


def set_default_openai_client(client: AsyncOpenAI) -> None:
    """手动设置默认 OpenAI 客户端（会覆盖自动创建的客户端）"""
    global _default_openai_client
    _default_openai_client = client


def set_use_responses_by_default(use_responses: bool) -> None:
    """设置是否默认使用 Responses API"""
    global _use_responses_by_default
    _use_responses_by_default = use_responses


def get_use_responses_by_default() -> bool:
    """获取是否默认使用 Responses API 的配置"""
    return _use_responses_by_default