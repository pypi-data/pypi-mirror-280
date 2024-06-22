import datetime
from datetime import datetime
from typing import Any, Literal, NotRequired, Optional, TypedDict

from pydantic import BaseModel, Field

from melting_schemas.meta import Creator
from melting_schemas.utils import StreamTimings, Timings

from ..completion.chat import ChatMLMessage, ChatModelSettings, Templating
from ..json_schema import FunctionJsonSchema
from ..meta import Creator
from ..utils import TokenUsage


class TCallModelSettings(BaseModel):
    model: str
    max_iterations: int = 10  # Maximum back and fourth allowed
    max_tokens: int | None = None  # defaults to inf
    temperature: float | None = None  # ValueRange(0, 2)
    top_p: float | None = None  # ValueRange(0, 1)
    frequency_penalty: float | None = None  # ValueRange(-2, 2) defaults to 0
    presence_penalty: float | None = None  # ValueRange(-2, 2) defaults to 0
    logit_bias: dict[str, int] | None = None  # valmap(ValueRange(-100, 100))
    stop: list[str] | None = None  # MaxLen(4)
    tool_choice: Literal["auto", "required"] = "auto"  # defaults to auto


class ToolCallChunk(TypedDict):
    finish_reason: Literal[
        "stop", "length", "tool_calls", "content_filter", "function_call"
    ]  # only present after the completion finished

    index: int
    id: str  # Only present in the first iteration, needs to be mapped based on index
    name: str  # Only present in the first iteration, needs to be mapped based on index
    arguments: str  # Incrementally added each iteration

    extra: NotRequired[dict[str, str]]  # Who knows if this will be necessary someday

    usage: TokenUsage  # Only present after the completion finished
    timings: Timings  # Injected after the completion finished


class ChatChunk(TypedDict):
    finish_reason: Literal[
        "stop", "length", "tool_calls", "content_filter", "function_call"
    ]  # only present after the completion finished
    delta: str

    usage: TokenUsage  # Only present after the completion finished
    timings: Timings  # Injected after the completion finished


class ToolCall(TypedDict):
    id: str
    name: str
    arguments: str
    response: NotRequired[Any]
    extra: NotRequired[dict[str, str]]


class ToolCallMLMessage(TypedDict):
    content: Optional[str]
    tool_calls: list[ToolCall]
    role: Literal["assistant"]


class ToolMLMessage(TypedDict):
    content: str
    name: str
    role: Literal["tool"]


class ToolJsonSchema(BaseModel):
    type: Literal["function"] = "function"
    function: FunctionJsonSchema


class StaticParams(BaseModel):
    query: dict[str, Any] = Field(default_factory=dict)
    body: dict[str, Any] = Field(default_factory=dict)


class DynamicParams(BaseModel):
    path: list[str] = Field(default_factory=list)
    query: list[str] = Field(default_factory=list)
    body: list[str] = Field(default_factory=list)


class ToolArgMap(BaseModel):
    location: str
    name: str


class HttpToolCallee(BaseModel):
    type: Literal["http"] = "http"
    method: Literal["GET", "POST"]
    forward_headers: list[str] = Field(default_factory=list)
    headers: dict[str, str] = Field(default_factory=dict)
    url: str
    static: StaticParams = Field(default_factory=StaticParams)
    dynamic: DynamicParams = Field(default_factory=DynamicParams)


class NoopToolCallee(BaseModel):
    type: Literal["noop"] = "noop"


class ToolSpec(BaseModel):
    name: str
    callee: HttpToolCallee | NoopToolCallee
    json_schema: ToolJsonSchema


class TCallRequest(BaseModel):
    tools: list[ToolSpec] | list[ToolJsonSchema] | list[str]
    messages: list[ChatMLMessage | ToolCallMLMessage | ToolMLMessage]
    settings: TCallModelSettings

    class Config:
        smart_unions = True
        examples = {
            "Raw Tool Selection": {
                "value": {
                    "tools": [
                        {
                            "type": "function",
                            "function": {
                                "name": "my_function",
                                "description": "This is my function",
                                "parameters": {
                                    "type": "object",
                                    "properties": {
                                        "my_param": {
                                            "type": "string",
                                            "description": "This is my parameter",
                                        }
                                    },
                                    "required": ["my_param"],
                                },
                            },
                        }
                    ],
                    "messages": [
                        {
                            "content": "Hello",
                            "role": "user",
                        }
                    ],
                    "settings": {
                        "model": "gpt-4o",
                        "tool_choice": "auto",
                    },
                }
            },
            "Raw Tool Calling": {
                "value": {
                    "tools": [
                        {
                            "type": "http",
                            "name": "my_function",
                            "callee": {
                                "method": "GET",
                                "forward_headers": ["x-user-email"],
                                "headers": {"authorization": "my-special-api-token"},
                                "url": "https://datasources.allai.digital/{name}/search",
                                "static": {
                                    "query": {"limit": 2},
                                    "body": {"top_k": 10},
                                },
                                "dynamic": {
                                    "path": ["name"],
                                    "body": ["top_k", "search_query"],
                                },
                            },
                            "json_schema": {
                                "type": "function",
                                "function": {
                                    "name": "my_function",
                                    "description": "This is my function",
                                    "parameters": {
                                        "type": "object",
                                        "properties": {
                                            "my_param": {
                                                "type": "string",
                                                "description": "This is my parameter",
                                            }
                                        },
                                        "required": ["my_param"],
                                    },
                                },
                            },
                        }
                    ],
                    "messages": [
                        {
                            "content": "Hello",
                            "role": "user",
                        }
                    ],
                    "settings": {
                        "model": "gpt-4o",
                        "tool_choice": "auto",
                    },
                }
            },
            "Native Tool Calling": {
                "value": {
                    "tools": ["example-tool-name"],
                    "messages": [
                        {
                            "content": "Hello",
                            "role": "user",
                        }
                    ],
                    "settings": {
                        "model": "gpt-4o",
                        "tool_choice": "auto",
                    },
                }
            },
        }


class TCallProcessedRequest(BaseModel):
    tools: list[ToolSpec] | list[ToolJsonSchema]
    messages: list[ChatMLMessage | ToolCallMLMessage | ToolMLMessage]
    settings: TCallModelSettings


class TCallCompletionCreationResponse(BaseModel):
    created_at: datetime
    created_by: Creator
    finish_reason: Literal["stop", "length", "function_call", "tool_calls"]
    id: str = Field(..., alias="_id")
    messages: list[ChatMLMessage | ToolCallMLMessage | ToolMLMessage]
    tool_calls: list[ToolCall]
    output: ChatMLMessage | ToolMLMessage | ToolCallMLMessage
    settings: ChatModelSettings
    templating: Optional[Templating]
    timings: Timings | StreamTimings
    usage: TokenUsage

    class Config:
        smart_unions = True
