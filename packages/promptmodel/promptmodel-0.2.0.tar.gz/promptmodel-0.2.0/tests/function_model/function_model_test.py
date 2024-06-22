import pytest
from unittest.mock import AsyncMock, MagicMock

from typing import Generator, AsyncGenerator, List

from promptmodel.types.response import LLMResponse, LLMStreamResponse
from promptmodel import FunctionModel, DevClient
from promptmodel.dev_app import FunctionModelInterface

client = DevClient()


def test_find_client(mocker):
    pm = FunctionModel("test")
    assert client.function_models == [FunctionModelInterface(name="test")]


def test_get_config(mocker, mock_fetch_prompts):
    fetch_prompts = mocker.patch(
        "promptmodel.function_model.LLMProxy.fetch_prompts", mock_fetch_prompts
    )
    # mock registering_meta
    mocker.patch("promptmodel.function_model.RegisteringMeta", MagicMock())
    function_model = FunctionModel("test")
    assert len(client.function_models) == 1
    config = function_model.get_config()
    assert len(config.prompts) == 2


def test_run(mocker, mock_fetch_prompts: AsyncMock, mock_async_log_to_cloud: AsyncMock):
    fetch_prompts = mocker.patch(
        "promptmodel.llms.llm_proxy.LLMProxy.fetch_prompts", mock_fetch_prompts
    )
    async_log_to_cloud = mocker.patch(
        "promptmodel.llms.llm_proxy.LLMProxy._async_log_to_cloud",
        mock_async_log_to_cloud,
    )
    mocker.patch("promptmodel.function_model.RegisteringMeta", MagicMock())
    function_model = FunctionModel("test")
    res: LLMResponse = function_model.run({})
    fetch_prompts.assert_called_once()
    async_log_to_cloud.assert_called_once()
    assert res.raw_output is not None
    assert res.error is None or res.error is False
    assert res.api_response is not None
    assert res.parsed_outputs is None

    fetch_prompts.reset_mock()
    async_log_to_cloud.reset_mock()
    mocker.patch(
        "promptmodel.utils.config_utils.read_config",
        return_value={"connection": {"initializing": True}},
    )
    res = function_model.run()
    print(res)
    fetch_prompts.assert_not_called()
    async_log_to_cloud.assert_not_called()


@pytest.mark.asyncio
async def test_arun(
    mocker, mock_fetch_prompts: AsyncMock, mock_async_log_to_cloud: AsyncMock
):
    fetch_prompts = mocker.patch(
        "promptmodel.llms.llm_proxy.LLMProxy.fetch_prompts", mock_fetch_prompts
    )
    async_log_to_cloud = mocker.patch(
        "promptmodel.llms.llm_proxy.LLMProxy._async_log_to_cloud",
        mock_async_log_to_cloud,
    )
    mocker.patch("promptmodel.function_model.RegisteringMeta", MagicMock())
    function_model = FunctionModel("test")

    res: LLMResponse = await function_model.arun({})
    fetch_prompts.assert_called_once()
    async_log_to_cloud.assert_called_once()
    assert res.raw_output is not None
    assert res.error is None or res.error is False
    assert res.api_response is not None
    assert res.parsed_outputs is None

    fetch_prompts.reset_mock()
    async_log_to_cloud.reset_mock()
    mocker.patch(
        "promptmodel.utils.config_utils.read_config",
        return_value={"connection": {"initializing": True}},
    )
    res = await function_model.arun()
    print(res)
    fetch_prompts.assert_not_called()
    async_log_to_cloud.assert_not_called()


def test_stream(
    mocker, mock_fetch_prompts: AsyncMock, mock_async_log_to_cloud: AsyncMock
):
    fetch_prompts = mocker.patch(
        "promptmodel.llms.llm_proxy.LLMProxy.fetch_prompts", mock_fetch_prompts
    )
    async_log_to_cloud = mocker.patch(
        "promptmodel.llms.llm_proxy.LLMProxy._async_log_to_cloud",
        mock_async_log_to_cloud,
    )
    mocker.patch("promptmodel.function_model.RegisteringMeta", MagicMock())
    function_model = FunctionModel("test")

    res: Generator[LLMStreamResponse, None, None] = function_model.stream({})
    chunks: List[LLMStreamResponse] = []
    for chunk in res:
        chunks.append(chunk)
    fetch_prompts.assert_called_once()
    async_log_to_cloud.assert_called_once()

    assert chunks[-1].api_response is not None
    assert len([chunk for chunk in chunks if chunk.error is not None]) == 0
    assert len([chunk for chunk in chunks if chunk.parsed_outputs is not None]) == 0
    assert len([chunk for chunk in chunks if chunk.raw_output is not None]) > 0

    fetch_prompts.reset_mock()
    async_log_to_cloud.reset_mock()
    mocker.patch(
        "promptmodel.utils.config_utils.read_config",
        return_value={"connection": {"initializing": True}},
    )
    res = function_model.stream()
    print(res)
    fetch_prompts.assert_not_called()
    async_log_to_cloud.assert_not_called()


@pytest.mark.asyncio
async def test_astream(
    mocker, mock_fetch_prompts: AsyncMock, mock_async_log_to_cloud: AsyncMock
):
    fetch_prompts = mocker.patch(
        "promptmodel.llms.llm_proxy.LLMProxy.fetch_prompts", mock_fetch_prompts
    )
    async_log_to_cloud = mocker.patch(
        "promptmodel.llms.llm_proxy.LLMProxy._async_log_to_cloud",
        mock_async_log_to_cloud,
    )
    mocker.patch("promptmodel.function_model.RegisteringMeta", MagicMock())
    function_model = FunctionModel("test")

    res: AsyncGenerator[LLMStreamResponse, None] = await function_model.astream({})
    chunks: List[LLMStreamResponse] = []
    async for chunk in res:
        chunks.append(chunk)
    fetch_prompts.assert_called_once()
    async_log_to_cloud.assert_called_once()

    assert chunks[-1].api_response is not None
    assert len([chunk for chunk in chunks if chunk.error is not None]) == 0
    assert len([chunk for chunk in chunks if chunk.parsed_outputs is not None]) == 0
    assert len([chunk for chunk in chunks if chunk.raw_output is not None]) > 0

    fetch_prompts.reset_mock()
    async_log_to_cloud.reset_mock()
    mocker.patch(
        "promptmodel.utils.config_utils.read_config",
        return_value={"connection": {"initializing": True}},
    )
    res = await function_model.astream({})
    print(res)
    fetch_prompts.assert_not_called()
    async_log_to_cloud.assert_not_called()


def test_run_and_parse(
    mocker, mock_fetch_prompts: AsyncMock, mock_async_log_to_cloud: AsyncMock
):
    fetch_prompts = mocker.patch(
        "promptmodel.llms.llm_proxy.LLMProxy.fetch_prompts", mock_fetch_prompts
    )
    async_log_to_cloud = mocker.patch(
        "promptmodel.llms.llm_proxy.LLMProxy._async_log_to_cloud",
        mock_async_log_to_cloud,
    )
    mocker.patch("promptmodel.function_model.RegisteringMeta", MagicMock())
    function_model = FunctionModel("test")
    res: LLMResponse = function_model.run_and_parse({})
    fetch_prompts.assert_called_once()
    async_log_to_cloud.assert_called_once()
    assert res.raw_output is not None
    assert res.error is None or res.error is False
    assert res.api_response is not None
    assert res.parsed_outputs == {}

    fetch_prompts.reset_mock()
    async_log_to_cloud.reset_mock()
    mocker.patch(
        "promptmodel.utils.config_utils.read_config",
        return_value={"connection": {"initializing": True}},
    )
    res = function_model.run_and_parse({})
    print(res)
    fetch_prompts.assert_not_called()
    async_log_to_cloud.assert_not_called()


@pytest.mark.asyncio
async def test_arun_and_parse(
    mocker, mock_fetch_prompts: AsyncMock, mock_async_log_to_cloud: AsyncMock
):
    fetch_prompts = mocker.patch(
        "promptmodel.llms.llm_proxy.LLMProxy.fetch_prompts", mock_fetch_prompts
    )
    async_log_to_cloud = mocker.patch(
        "promptmodel.llms.llm_proxy.LLMProxy._async_log_to_cloud",
        mock_async_log_to_cloud,
    )
    mocker.patch("promptmodel.function_model.RegisteringMeta", MagicMock())
    function_model = FunctionModel("test")

    res: LLMResponse = await function_model.arun_and_parse({})
    fetch_prompts.assert_called_once()
    async_log_to_cloud.assert_called_once()
    assert res.raw_output is not None
    assert res.error is None or res.error is False
    assert res.api_response is not None
    assert res.parsed_outputs == {}

    fetch_prompts.reset_mock()
    async_log_to_cloud.reset_mock()
    mocker.patch(
        "promptmodel.utils.config_utils.read_config",
        return_value={"connection": {"initializing": True}},
    )
    res = await function_model.arun_and_parse({})
    print(res)
    fetch_prompts.assert_not_called()
    async_log_to_cloud.assert_not_called()


def test_stream_and_parse(
    mocker, mock_fetch_prompts: AsyncMock, mock_async_log_to_cloud: AsyncMock
):
    fetch_prompts = mocker.patch(
        "promptmodel.llms.llm_proxy.LLMProxy.fetch_prompts", mock_fetch_prompts
    )
    async_log_to_cloud = mocker.patch(
        "promptmodel.llms.llm_proxy.LLMProxy._async_log_to_cloud",
        mock_async_log_to_cloud,
    )
    mocker.patch("promptmodel.function_model.RegisteringMeta", MagicMock())
    function_model = FunctionModel("test")

    res: Generator[LLMStreamResponse, None, None] = function_model.stream_and_parse({})
    chunks: List[LLMStreamResponse] = []
    for chunk in res:
        chunks.append(chunk)
    fetch_prompts.assert_called_once()
    async_log_to_cloud.assert_called_once()

    assert chunks[-1].api_response is not None
    assert len([chunk for chunk in chunks if chunk.error is not None]) == 0
    assert len([chunk for chunk in chunks if chunk.parsed_outputs is not None]) == 0
    assert len([chunk for chunk in chunks if chunk.raw_output is not None]) > 0

    fetch_prompts.reset_mock()
    async_log_to_cloud.reset_mock()
    mocker.patch(
        "promptmodel.utils.config_utils.read_config",
        return_value={"connection": {"initializing": True}},
    )
    res = function_model.stream_and_parse({})
    print(res)
    fetch_prompts.assert_not_called()
    async_log_to_cloud.assert_not_called()


@pytest.mark.asyncio
async def test_astream_and_parse(
    mocker, mock_fetch_prompts: AsyncMock, mock_async_log_to_cloud: AsyncMock
):
    fetch_prompts = mocker.patch(
        "promptmodel.llms.llm_proxy.LLMProxy.fetch_prompts", mock_fetch_prompts
    )
    async_log_to_cloud = mocker.patch(
        "promptmodel.llms.llm_proxy.LLMProxy._async_log_to_cloud",
        mock_async_log_to_cloud,
    )
    mocker.patch("promptmodel.function_model.RegisteringMeta", MagicMock())
    function_model = FunctionModel("test")

    res: AsyncGenerator[
        LLMStreamResponse, None
    ] = await function_model.astream_and_parse({})
    chunks: List[LLMStreamResponse] = []
    async for chunk in res:
        chunks.append(chunk)
    fetch_prompts.assert_called_once()
    async_log_to_cloud.assert_called_once()

    assert chunks[-1].api_response is not None
    assert len([chunk for chunk in chunks if chunk.error is not None]) == 0
    assert len([chunk for chunk in chunks if chunk.parsed_outputs is not None]) == 0
    assert len([chunk for chunk in chunks if chunk.raw_output is not None]) > 0

    fetch_prompts.reset_mock()
    async_log_to_cloud.reset_mock()
    mocker.patch(
        "promptmodel.utils.config_utils.read_config",
        return_value={"connection": {"initializing": True}},
    )
    res = await function_model.astream_and_parse({})
    print(res)
    fetch_prompts.assert_not_called()
    async_log_to_cloud.assert_not_called()
