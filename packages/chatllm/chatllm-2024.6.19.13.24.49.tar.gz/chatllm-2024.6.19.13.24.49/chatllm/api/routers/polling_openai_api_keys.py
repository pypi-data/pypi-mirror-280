#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : polling_openai_api_keys
# @Time         : 2024/6/17 17:26
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :


from meutils.pipe import *
from meutils.serving.fastapi.dependencies.auth import get_bearer_token, HTTPAuthorizationCredentials

from sse_starlette import EventSourceResponse
from fastapi import APIRouter, File, UploadFile, Query, Form, Depends, Request, HTTPException, status, \
    BackgroundTasks as BT

from openai.types.chat import ChatCompletion, ChatCompletionChunk

from meutils.llm.openai_utils import create_chat_completion_chunk
from meutils.schemas.openai_types import ChatCompletionRequest

from chatllm.completions.polling_openai_api_keys import Completions

router = APIRouter()

ChatCompletionResponse = Union[ChatCompletion, List[ChatCompletionChunk]]


@router.post("/chat/completions")
async def create_chat_completions(
    request: ChatCompletionRequest,
    auth: Optional[HTTPAuthorizationCredentials] = Depends(get_bearer_token),
):
    logger.debug(request)

    api_key = auth and auth.credentials or None  # redis+feishu
    api_keys = api_key.split(",") if "," in api_key else None  # 轮询keys

    client = Completions(provider=api_key, api_keys=api_keys)

    response = await client.acreate(request)

    if request.stream:
        return EventSourceResponse(create_chat_completion_chunk(response))

    return response


if __name__ == '__main__':
    from meutils.serving.fastapi import App

    app = App()

    app.include_router(router, '/v1')

    app.run()
