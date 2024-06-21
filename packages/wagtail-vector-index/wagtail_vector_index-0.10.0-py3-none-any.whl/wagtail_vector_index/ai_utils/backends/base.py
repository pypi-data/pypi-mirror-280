from collections.abc import Iterable, Iterator, Sequence
from dataclasses import dataclass
from typing import (
    Any,
    ClassVar,
    Generic,
    Literal,
    NotRequired,
    Protocol,
    Required,
    Self,
    TypedDict,
    TypeVar,
    overload,
)

from django.core.exceptions import ImproperlyConfigured

from .. import embeddings, tokens
from ..types import (
    AIResponse,
    AIStreamingResponse,
    ChatMessage,
)


class BaseConfigSettingsDict(TypedDict):
    MODEL_ID: Required[str]
    TOKEN_LIMIT: NotRequired[int | None]
    CHUNK_OVERLAP_CHARACTERS: NotRequired[int | None]


class BaseChatConfigSettingsDict(BaseConfigSettingsDict):
    pass


class BaseEmbeddingConfigSettingsDict(BaseConfigSettingsDict):
    EMBEDDING_OUTPUT_DIMENSIONS: NotRequired[int | None]


ConfigSettings = TypeVar(
    "ConfigSettings", bound=BaseConfigSettingsDict, contravariant=True
)


ChatConfigSettings = TypeVar(
    "ChatConfigSettings", bound=BaseChatConfigSettingsDict, contravariant=True
)

EmbeddingConfigSettings = TypeVar(
    "EmbeddingConfigSettings", bound=BaseEmbeddingConfigSettingsDict, contravariant=True
)


class ConfigClassProtocol(Protocol[ConfigSettings]):
    @classmethod
    def from_settings(cls, config: ConfigSettings, **kwargs: Any) -> Self: ...


@dataclass(kw_only=True)
class BaseConfig(ConfigClassProtocol[ConfigSettings]):
    model_id: str
    token_limit: int

    @classmethod
    def from_settings(
        cls,
        config: ConfigSettings,
        **kwargs: Any,
    ) -> Self:
        token_limit = cls.get_token_limit(
            model_id=config["MODEL_ID"], custom_value=config.get("TOKEN_LIMIT")
        )

        return cls(
            model_id=config["MODEL_ID"],
            token_limit=token_limit,
            **kwargs,
        )

    @classmethod
    def _get_token_limit(cls, *, model_id: str) -> int:
        """Backend-specific method for retriving the token limit for the provided model."""
        try:
            return tokens.get_default_token_limit(model_id=model_id)
        except tokens.NoTokenLimitFound as e:
            raise ImproperlyConfigured(
                f'"TOKEN_LIMIT" is not configured for model "{model_id}".'
            ) from e

    @classmethod
    def get_token_limit(cls, *, model_id: str, custom_value: int | None) -> int:
        """Determine a token limit either from the config, or from the backend-specific
        method."""
        if custom_value is not None:
            try:
                return int(custom_value)
            except ValueError as e:
                raise ImproperlyConfigured(
                    f'"TOKEN_LIMIT" is not an "int", it is a "{type(custom_value)}".'
                ) from e
        return cls._get_token_limit(model_id=model_id)


@dataclass(kw_only=True)
class BaseChatConfig(BaseConfig[ChatConfigSettings]):
    pass


@dataclass(kw_only=True)
class BaseEmbeddingConfig(BaseConfig[EmbeddingConfigSettings]):
    embedding_output_dimensions: int

    @classmethod
    def from_settings(
        cls,
        config: EmbeddingConfigSettings,
        **kwargs: Any,
    ) -> Self:
        embedding_output_dimensions = cls.get_embedding_output_dimensions(
            model_id=config["MODEL_ID"],
            custom_value=config.get("EMBEDDING_OUTPUT_DIMENSIONS"),
        )
        kwargs.setdefault("embedding_output_dimensions", embedding_output_dimensions)
        return super().from_settings(
            config=config,
            **kwargs,
        )

    @classmethod
    def _get_embedding_output_dimensions(cls, *, model_id: str) -> int:
        """Backend-specific method for retriving the embedding output dimensions for the provided model."""
        try:
            return embeddings.get_default_embedding_output_dimensions(model_id=model_id)
        except embeddings.EmbeddingOutputDimensionsNotFound as e:
            raise ImproperlyConfigured(
                f'"EMBEDDING_OUTPUT_DIMENSIONS" is not configured for model "{model_id}".'
            ) from e

    @classmethod
    def get_embedding_output_dimensions(
        cls, *, model_id: str, custom_value: int | None
    ) -> int:
        """Determine the embedding output dimensons either from the config, or from the backend-specific
        method."""
        if custom_value is not None:
            try:
                return int(custom_value)
            except ValueError as e:
                raise ImproperlyConfigured(
                    f'"EMBEDDING_OUTPUT_DIMENSIONS" is not an "int", it is a "{type(custom_value)}".'
                ) from e
        return cls._get_embedding_output_dimensions(model_id=model_id)


AnyBackendConfig = TypeVar("AnyBackendConfig", bound=BaseConfig)
ChatBackendConfig = TypeVar("ChatBackendConfig", bound=BaseChatConfig)
EmbeddingBackendConfig = TypeVar("EmbeddingBackendConfig", bound=BaseEmbeddingConfig)


class BaseBackend(Generic[AnyBackendConfig]):
    config_cls: ClassVar[type[BaseConfig]]
    config: AnyBackendConfig

    def __init__(self, *, config: AnyBackendConfig) -> None:
        self.config = config


class BaseChatBackend(BaseBackend[ChatBackendConfig]):
    """Base chat backend providing interface with `chat` and `achat` methods.

    These both return either an `AIResponse` or an `AIStreamingResponse` depending on the `stream` parameter.
    """

    config_cls: ClassVar[type[BaseChatConfig]]
    config: ChatBackendConfig

    @overload
    def chat(
        self, *, messages: Sequence[ChatMessage], stream: Literal[True], **kwargs
    ) -> AIStreamingResponse: ...

    @overload
    def chat(
        self,
        *,
        messages: Sequence[ChatMessage],
        stream: Literal[False] = False,
        **kwargs,
    ) -> AIResponse: ...

    def chat(
        self, *, messages: Sequence[ChatMessage], stream: bool = False, **kwargs
    ) -> AIResponse | AIStreamingResponse: ...

    @overload
    async def achat(
        self, *, messages: Sequence[ChatMessage], stream: Literal[True], **kwargs
    ) -> AIStreamingResponse: ...

    @overload
    async def achat(
        self,
        *,
        messages: Sequence[ChatMessage],
        stream: Literal[False] = False,
        **kwargs,
    ) -> AIResponse: ...

    async def achat(
        self, *, messages: Sequence[ChatMessage], stream: bool = False, **kwargs
    ) -> AIResponse | AIStreamingResponse:
        raise NotImplementedError("Async chat is not supported by this backend.")


class BaseEmbeddingBackend(BaseBackend[EmbeddingBackendConfig]):
    """Base embedding backend providing interface with `embed` and async `aembed` methods."""

    config_cls: ClassVar[type[BaseEmbeddingConfig]]
    config: EmbeddingBackendConfig

    def embed(self, inputs: Iterable[str], **kwargs) -> Iterator[list[float]]: ...

    async def aembed(self, inputs: Iterable[str]) -> Iterator[list[float]]:
        raise NotImplementedError("Async embed is not supported by this backend.")

    @property
    def embedding_output_dimensions(self) -> int:
        return self.config.embedding_output_dimensions
