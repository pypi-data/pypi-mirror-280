# unofficial_ffm_openai_client
An unofficial Formosa Foundation Model client implementation based on OpenAI and LangChain

## Introduction

This is an unofficial Python client implementation for the Formosa Foundation Model public endpoint, compatible with the OpenAI Python client and LangChain. Currently, it only implements the [Conversation API](https://docs.twcc.ai/docs/user-guides/twcc/afs/afs-modelspace/api-and-parameters/conversation-api) and supports the public endpoint. Note that the synchronous API is not yet implemented.

# Changelog

- 0.2.0 
  - Add a callback for counting token consumption in streaming and non-streaming mode.
  - Add json error handling for sync streaming mode.
  - Add token consumption info in the result of streaming and non-streaming mode.
- 0.1.3 - Support function calls.
- 0.1.2 - Support embeddings.

## Usage

Install using pypi:

```shell
pip install unofficial-ffm-openai
```

You can use it similarly to the original OpenAIChat, with a few different parameters:

```python
from ffm.langchain.language_models.ffm import FfmChatOpenAI

chat_ffm = FfmChatOpenAI(
    ffm_endpoint="https://api-ams.twcc.ai/api",
    max_tokens=1000,
    temperature=0.5,
    top_k=50,
    top_p=1.0,
    frequency_penalty=1.0,
    ffm_api_key="your key",
    ffm_deployment="ffm-mistral-7b-32k-instruct",  # or other model name
    streaming=True,
    callbacks=callbacks
)
```

```python
from ffm.embeddings import FFMEmbeddings

embedding = FFMEmbeddings(
    base_url="",
    api_key="your key")
```

### Callbacks

You cen use the ffm callbacks as using other callbacks such as openai callback, here is the example:

```python
from ffm.langchain.callbacks import get_ffm_callback

with get_ffm_callback() as cb:
    ...do something using llm...
    
    total_tokens = cb.total_tokens
    prompt_tokens = cb.prompt_tokens
    completion_tokens = cb.completion_tokens
    successful_requests = cb.successful_requests
```

* Note: Cost calculation has not been done yet but is in progress.

## Limitation

Currently, it has only been tested with the following dependencies:

```
langchain                         0.1.20
langchain-community               0.0.38
langchain-core                    0.1.52
langchain-openai                  0.1.7
langchain-text-splitters          0.0.2
langchainhub                      0.1.15
```

and the OpenAI client:

```
openai                            1.30.1
```

## TODO

* Full implementation for the synchronous API.