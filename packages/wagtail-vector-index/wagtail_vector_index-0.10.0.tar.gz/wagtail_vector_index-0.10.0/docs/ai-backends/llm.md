# LLM

LLM is an alternative supported backend provider which uses the [`llm` library](https://github.com/simonw/llm) to enable communication with multiple AI providers.

To start using this backend, the `llm` package must be installed. This can be done by either adding `llm` to your requirements manually, or installing `wagtail-vector-index[llm]`.

## Chat Backend

```python
WAGTAIL_VECTOR_INDEX = {
    "CHAT_BACKENDS": {
        "default": {
            "CLASS": "wagtail_vector_index.ai_utils.backends.llm.LLMChatBackend",
            "CONFIG": {
                "MODEL_ID": "gpt-4o",
            },
        },
    },
}
```

If `MODEL_ID` is omitted, OpenAI's `gpt-3.5-turbo` will be used by default.

### Using other models

You can use the command line interface to see the "LLM" library's models installed in your environment:

```sh
llm models
```

Specify `MODEL_ID` in the configuration to use a different model. For example, to use GPT-4:

```python
WAGTAIL_VECTOR_INDEX = {
    "CHAT_BACKENDS": {
        "default": {
            "CLASS": "wagtail_vector_index.ai_utils.backends.llm.LLMChatBackend",
            "CONFIG": {
                "MODEL_ID": "gpt-4",
            },
        },
    },
}
```

!!! info

    The "LLM" library comes with OpenAI models installed by default.

    You can install other models using [the "LLM" library's plugin functionality](https://llm.datasette.io/en/stable/plugins/index.html).

### Customisations

There are two settings that you can use with the "LLM" backend:

-   `INIT_KWARGS`
-   `PROMPT_KWARGS`

#### `INIT_KWARGS`

These are passed to the "LLM" library as ["Model Options"](https://llm.datasette.io/en/stable/python-api.html#model-options).
You can use them to customize the model's initialization.

For example, for OpenAI models you can set a custom API key. By default the OpenAI Python library
will use the value of the `OPENAI_API_KEY` environment variable.

```python
WAGTAIL_VECTOR_INDEX = {
    "CHAT_BACKENDS": {
        "default": {
            "CLASS": "wagtail_ai.ai.llm.LLMBackend",
            "CONFIG": {
                # Model ID recognizable by the llm library.
                "MODEL_ID": "gpt-3.5-turbo",
                "INIT_KWARGS": {"key": "your-custom-api-key"},
            },
        }
    }
}
```

## Embedding Backend

This backend uses the ["LLM" library](https://llm.datasette.io/en/stable/) which offers support for many AI services through plugins.

By default, it is configured to use OpenAI's `ada-002` model.

### Using other models

You can use the command line interface to see the "LLM" library's embedding models installed in your environment:

```sh
llm embed-models
```

Then you can swap `MODEL_ID` in the configuration to use a different model:

```python
WAGTAIL_VECTOR_INDEX = {
    "EMBEDDING_BACKENDS": {
        "default": {
            "CLASS": "wagtail_vector_index.ai_utils.backends.llm.LLMEmbeddingBackend",
            "CONFIG": {
                "MODEL_ID": "mini-16",
            },
        },
    },
}
```

!!! info

    The "LLM" library comes with OpenAI models installed by default.

    You can install other models using [the "LLM" library's plugin functionality](https://llm.datasette.io/en/stable/plugins/index.html).

### Customisations

There "LLM" embedding backend can be customised with the following settings:

-   `INIT_KWARGS`

#### `INIT_KWARGS`

These are passed to the "LLM" library as ["Model Options"](https://llm.datasette.io/en/stable/python-api.html#model-options).
You can use them to customize the model's initialization.

For example, for OpenAI models you can set a custom API key. By default the OpenAI Python library
will use the value of the `OPENAI_API_KEY` environment variable.

## Using a custom OpenAI or OpenAI-compatible model

The "LLM" library supports adding custom OpenAI models. This may be necessary if:

-   You want to use a model that's not supported by the "LLM" library yet.
-   You want to use a proxy for OpenAI requests.

You can find the "LLM" library specific instructions at: https://llm.datasette.io/en/stable/other-models.html#adding-more-openai-models.

1. Find the "LLM" library's directory. You can set a custom one with the
   [`LLM_USER_PATH`](https://llm.datasette.io/en/stable/setup.html#setting-a-custom-directory-location)
   setting. To confirm the path, you can use the following shell command:
   `dirname "$(llm logs path)"`.
2. Create `extra-openai-models.yaml` as noted in
   [the "LLM" library's documentation](https://llm.datasette.io/en/stable/other-models.html#adding-more-openai-models).
   For example to set up a proxy:
    ```yaml
    - model_id: customgateway-gpt-3.5-turbo
      model_name: gpt-3.5-turbo
      api_base: "https://yourcustomproxy.example.com/"
      headers:
          apikey: your-api-key
    ```
3. Set the `MODEL_ID` in the Wagtail Vector Index settings in your Django project
   settings file to the `model_id` you added in `extra-openai-models.yaml`.
    ```python
    WAGTAIL_VECTOR_INDEX = {
        "CHAT_BACKENDS": {
            "default": {
                "CLASS": "wagtail_ai.ai.llm.LLMBackend",
                "CONFIG": {
                    # MODEL_ID should match the model_id in the yaml file.
                    "MODEL_ID": "customgateway-gpt-3.5-turbo",
                    # TOKEN_LIMIT has to be defined because you use a custom model name.
                    # You are looking to use the context window value from:
                    # https://platform.openai.com/docs/models/gpt-3-5
                    "TOKEN_LIMIT": 4096,
                },
            }
        }
    }
    ```
