# Copyright (c) 2022-present, FriendliAI Inc. All rights reserved.

"""Friendli T5 Checkpoint Converter."""

from __future__ import annotations

from typing import Any, Dict, List, cast

import torch
from transformers import T5Config  # type: ignore[import]

from friendli.enums import ModelDataType
from friendli.errors import CheckpointConversionError, NotSupportedCheckpointError
from friendli.logging import logger
from friendli.modules.converter.base import (
    DECODER_PREFIX,
    ENCODER_PREFIX,
    EncoderDecoderConverter,
)
from friendli.modules.converter.schema import ConvertInfo


class T5Converter(EncoderDecoderConverter):
    """T5ForConditionalGeneration Architectures Converter Class."""

    def check_config(self) -> None:
        """Check if T5 architectures' config can be converted to Friendli format."""
        super().check_config()
        try:
            if not (
                cast(T5Config, self.config).is_gated_act
                ^ cast(T5Config, self.config).tie_word_embeddings
            ):
                raise NotSupportedCheckpointError(
                    invalid_option=f"'is_gated_act={cast(T5Config, self.config).is_gated_act}'and "
                    f"'tie_word_embeddings={cast(T5Config, self.config).tie_word_embeddings}'",
                    valid_options=[
                        "'is_gated_act' and 'tie_word_embeddings' should be different."
                    ],
                )

            if cast(T5Config, self.config).layer_norm_epsilon != 1e-6:
                raise NotSupportedCheckpointError(
                    invalid_option="'layer_norm_epsilon="
                    f"{cast(T5Config, self.config).layer_norm_epsilon}'",
                    valid_options=[1e-6],
                )
        except AttributeError as exc:
            raise CheckpointConversionError(str(exc)) from exc

    def _decoder_final_ln_weight_reshape(
        self, params: List[torch.Tensor]
    ) -> torch.Tensor:
        """Special handle for T5."""
        assert len(params) == 1
        param = params[0]

        if cast(T5Config, self.config).tie_word_embeddings:
            param = param * (cast(T5Config, self.config).d_model ** -0.5)

        return param

    def pos_embed_weight_reshape(
        self,
        params: List[torch.Tensor],
    ) -> torch.Tensor:
        """Reshape positional embedding weights in T5."""
        assert len(params) == 1
        return params[0]

    def get_attributes(self) -> Dict[str, Any]:
        """Get checkpoint attributes."""
        config = cast(T5Config, self.config)

        logger.warn(
            "The 'max_input_length' and 'max_output_length' fields are left blank as "
            "they cannot be automatically configured. "
            "Determine the 'max_input_length' and 'max_output_length' according to your "
            "needs. The T5 model does not rely on absolute position embeddings, "
            "allowing you to choose any suitable value."
        )

        eos_token_id = self.get_eos_token_id()
        decoder_start_token_id = self.get_decoder_start_token_id()
        attr = {
            "model_type": self.model_type,
            "dtype": self.data_type.value,
            "head_size": self.encoder_head_size,
            "num_heads": self.encoder_num_attention_heads,
            "hidden_size": self.encoder_hidden_size,
            "ff_intermediate_size": self.decoder_ff_intermediate_size,
            "num_encoder_layers": self.encoder_layer_num,
            "num_decoder_layers": self.decoder_layer_num,
            "max_input_length": "FILL ME",
            "max_output_length": "FILL ME",
            "num_pos_emb_buckets": config.relative_attention_num_buckets,
            "max_pos_distance": config.relative_attention_max_distance,
            "vocab_size": config.vocab_size,
            "eos_token": eos_token_id if eos_token_id is not None else "FILL ME",
            "decoder_start_token": (
                decoder_start_token_id
                if decoder_start_token_id is not None
                else "FILL ME"
            ),
        }
        return attr

    @property
    def model_type(self) -> str:
        """Model type."""
        if cast(T5Config, self.config).is_gated_act:
            return "t5-v1_1"
        return "t5"

    @property
    def encoder_convert_info_list(
        self,
    ) -> List[ConvertInfo]:
        """The list of conversion informations for transformer blocks in T5's encoder."""
        convert_info_list = []
        for i in range(self.encoder_layer_num):
            layer_prefix = f"{self.encoder_layer_prefix}{i}."
            converted_prefixe = f"{ENCODER_PREFIX}/h_._{i}/"
            convert_info_list.extend(
                [
                    ConvertInfo(
                        param_names=[f"{layer_prefix}layer.0.layer_norm.weight"],
                        data_type=self.data_type,
                        converted_name=f"{converted_prefixe}ln_1/gamma:0",
                        reshape_fn=self.ln_weight_reshape,
                    ),
                    ConvertInfo(
                        param_names=[f"{layer_prefix}layer.1.layer_norm.weight"],
                        data_type=self.data_type,
                        converted_name=f"{converted_prefixe}ln_2/gamma:0",
                        reshape_fn=self.ln_weight_reshape,
                    ),
                    ConvertInfo(
                        param_names=[
                            f"{layer_prefix}layer.0.SelfAttention.q.weight",
                            f"{layer_prefix}layer.0.SelfAttention.k.weight",
                            f"{layer_prefix}layer.0.SelfAttention.v.weight",
                        ],
                        data_type=self.data_type,
                        converted_name=f"{converted_prefixe}attn/c_attn/weight:0",
                        reshape_fn=self.qkv_weight_reshape,
                    ),
                    ConvertInfo(
                        param_names=[f"{layer_prefix}layer.0.SelfAttention.o.weight"],
                        data_type=self.data_type,
                        converted_name=f"{converted_prefixe}attn/c_proj/weight:0",
                        reshape_fn=self.linear_weight_reshape,
                    ),
                ]
            )

            if cast(T5Config, self.config).is_gated_act:
                convert_info_list.extend(
                    [
                        ConvertInfo(
                            param_names=[
                                f"{layer_prefix}layer.1.DenseReluDense.wi_0.weight"
                            ],
                            data_type=self.data_type,
                            converted_name=f"{converted_prefixe}mlp/c_gate/weight:0",
                            reshape_fn=self.linear_weight_reshape,
                        ),
                        ConvertInfo(
                            param_names=[
                                f"{layer_prefix}layer.1.DenseReluDense.wi_1.weight"
                            ],
                            data_type=self.data_type,
                            converted_name=f"{converted_prefixe}mlp/c_fc/weight:0",
                            reshape_fn=self.linear_weight_reshape,
                        ),
                        ConvertInfo(
                            param_names=[
                                f"{layer_prefix}layer.1.DenseReluDense.wo.weight"
                            ],
                            data_type=self.data_type,
                            converted_name=f"{converted_prefixe}mlp/c_proj/weight:0",
                            reshape_fn=self.linear_weight_reshape,
                        ),
                    ]
                )
            else:
                convert_info_list.extend(
                    [
                        ConvertInfo(
                            param_names=[
                                f"{layer_prefix}layer.1.DenseReluDense.wi.weight"
                            ],
                            data_type=self.data_type,
                            converted_name=f"{converted_prefixe}mlp/c_fc/weight:0",
                            reshape_fn=self.linear_weight_reshape,
                        ),
                        ConvertInfo(
                            param_names=[
                                f"{layer_prefix}layer.1.DenseReluDense.wo.weight"
                            ],
                            data_type=self.data_type,
                            converted_name=f"{converted_prefixe}mlp/c_proj/weight:0",
                            reshape_fn=self.linear_weight_reshape,
                        ),
                    ]
                )

        return convert_info_list

    @property
    def decoder_convert_info_list(
        self,
    ) -> List[ConvertInfo]:
        """The list of conversion informations for transformer blocks in T5's decoder."""
        convert_info_list = []
        for i in range(self.decoder_layer_num):
            layer_prefix = f"{self.decoder_layer_prefix}{i}."
            converted_prefixe = f"{DECODER_PREFIX}/h_._{i}/"
            convert_info_list.extend(
                [
                    ConvertInfo(
                        param_names=[f"{layer_prefix}layer.0.layer_norm.weight"],
                        data_type=self.data_type,
                        converted_name=f"{converted_prefixe}ln_1/gamma:0",
                        reshape_fn=self.ln_weight_reshape,
                    ),
                    ConvertInfo(
                        param_names=[f"{layer_prefix}layer.1.layer_norm.weight"],
                        data_type=self.data_type,
                        converted_name=f"{converted_prefixe}ln_2/gamma:0",
                        reshape_fn=self.ln_weight_reshape,
                    ),
                    ConvertInfo(
                        param_names=[f"{layer_prefix}layer.2.layer_norm.weight"],
                        data_type=self.data_type,
                        converted_name=f"{converted_prefixe}ln_3/gamma:0",
                        reshape_fn=self.ln_weight_reshape,
                    ),
                    ConvertInfo(
                        param_names=[
                            f"{layer_prefix}layer.0.SelfAttention.q.weight",
                            f"{layer_prefix}layer.0.SelfAttention.k.weight",
                            f"{layer_prefix}layer.0.SelfAttention.v.weight",
                        ],
                        data_type=self.data_type,
                        converted_name=f"{converted_prefixe}attn/c_attn/weight:0",
                        reshape_fn=self.qkv_weight_reshape,
                    ),
                    ConvertInfo(
                        param_names=[f"{layer_prefix}layer.0.SelfAttention.o.weight"],
                        data_type=self.data_type,
                        converted_name=f"{converted_prefixe}attn/c_proj/weight:0",
                        reshape_fn=self.linear_weight_reshape,
                    ),
                    ConvertInfo(
                        param_names=[
                            f"{layer_prefix}layer.1.EncDecAttention.q.weight",
                            f"{layer_prefix}layer.1.EncDecAttention.k.weight",
                            f"{layer_prefix}layer.1.EncDecAttention.v.weight",
                        ],
                        data_type=self.data_type,
                        converted_name=f"{converted_prefixe}cross_attn/c_attn/weight:0",
                        reshape_fn=self.qkv_weight_reshape,
                    ),
                    ConvertInfo(
                        param_names=[f"{layer_prefix}layer.1.EncDecAttention.o.weight"],
                        data_type=self.data_type,
                        converted_name=f"{converted_prefixe}cross_attn/c_proj/weight:0",
                        reshape_fn=self.linear_weight_reshape,
                    ),
                ]
            )

            if cast(T5Config, self.config).is_gated_act:
                convert_info_list.extend(
                    [
                        ConvertInfo(
                            param_names=[
                                f"{layer_prefix}layer.2.DenseReluDense.wi_0.weight"
                            ],
                            data_type=self.data_type,
                            converted_name=f"{converted_prefixe}mlp/c_gate/weight:0",
                            reshape_fn=self.linear_weight_reshape,
                        ),
                        ConvertInfo(
                            param_names=[
                                f"{layer_prefix}layer.2.DenseReluDense.wi_1.weight"
                            ],
                            data_type=self.data_type,
                            converted_name=f"{converted_prefixe}mlp/c_fc/weight:0",
                            reshape_fn=self.linear_weight_reshape,
                        ),
                        ConvertInfo(
                            param_names=[
                                f"{layer_prefix}layer.2.DenseReluDense.wo.weight"
                            ],
                            data_type=self.data_type,
                            converted_name=f"{converted_prefixe}mlp/c_proj/weight:0",
                            reshape_fn=self.linear_weight_reshape,
                        ),
                    ]
                )
            else:
                convert_info_list.extend(
                    [
                        ConvertInfo(
                            param_names=[
                                f"{layer_prefix}layer.2.DenseReluDense.wi.weight"
                            ],
                            data_type=self.data_type,
                            converted_name=f"{converted_prefixe}mlp/c_fc/weight:0",
                            reshape_fn=self.linear_weight_reshape,
                        ),
                        ConvertInfo(
                            param_names=[
                                f"{layer_prefix}layer.2.DenseReluDense.wo.weight"
                            ],
                            data_type=self.data_type,
                            converted_name=f"{converted_prefixe}mlp/c_proj/weight:0",
                            reshape_fn=self.linear_weight_reshape,
                        ),
                    ]
                )

        return convert_info_list

    @property
    def non_transformer_convert_info_list(
        self,
    ) -> List[ConvertInfo]:
        """The convert_info_list for non-transformer blocks in T5."""
        convert_info_list = [
            ConvertInfo(
                param_names=[f"shared.weight"],
                data_type=self.data_type,
                converted_name="wte/weight:0",
                reshape_fn=self.token_embed_weight_reshape,
            ),
            ConvertInfo(
                param_names=[
                    "encoder.block.0.layer.0.SelfAttention.relative_attention_bias.weight"
                ],
                data_type=ModelDataType.FP32,
                converted_name=f"{ENCODER_PREFIX}/wpe/weight:0",
                reshape_fn=self.pos_embed_weight_reshape,
            ),
            ConvertInfo(
                param_names=[
                    "decoder.block.0.layer.0.SelfAttention.relative_attention_bias.weight"
                ],
                data_type=ModelDataType.FP32,
                converted_name=f"{DECODER_PREFIX}/wpe/weight:0",
                reshape_fn=self.pos_embed_weight_reshape,
            ),
            ConvertInfo(
                param_names=["encoder.final_layer_norm.weight"],
                data_type=self.data_type,
                converted_name=f"{ENCODER_PREFIX}/ln_f/gamma:0",
                reshape_fn=self.ln_weight_reshape,
            ),
            ConvertInfo(
                param_names=["decoder.final_layer_norm.weight"],
                data_type=self.data_type,
                converted_name=f"{DECODER_PREFIX}/ln_f/gamma:0",
                reshape_fn=self._decoder_final_ln_weight_reshape,
            ),
        ]

        if not cast(T5Config, self.config).tie_word_embeddings:
            convert_info_list.append(
                ConvertInfo(
                    param_names=["lm_head.weight"],
                    data_type=self.data_type,
                    converted_name="head_fc/weight:0",
                    reshape_fn=self.head_weight_reshape,
                )
            )

        return convert_info_list

    @property
    def encoder_layer_prefix(self) -> str:
        """The layer name prefix used before T5 encoder's transformer block number."""
        return "encoder.block."

    @property
    def decoder_layer_prefix(self) -> str:
        """The layer name prefix used before T5 decoder's transformer block number."""
        return "decoder.block."

    @property
    def encoder_layer_num(self) -> int:
        """The number of transformer blocks in T5 encoder."""
        return cast(T5Config, self.config).num_layers

    @property
    def encoder_hidden_size(self) -> int:
        """The hidden size of T5 encoder."""
        return cast(T5Config, self.config).d_model

    @property
    def encoder_num_attention_heads(self) -> int:
        """The number of attention heads of T5 encoder."""
        return cast(T5Config, self.config).num_heads

    @property
    def encoder_head_size(self) -> int:
        """The head size of T5 encoder."""
        return cast(T5Config, self.config).d_kv

    @property
    def encoder_ff_intermediate_size(self) -> int:
        """The intermediate of the linear layer in T5 encoder's MLP."""
        return cast(T5Config, self.config).d_ff

    @property
    def decoder_layer_num(self) -> int:
        """The number of transformer blocks in T5 decoder."""
        return cast(T5Config, self.config).num_decoder_layers

    @property
    def decoder_hidden_size(self) -> int:
        """The hidden size of T5 decoder."""
        return cast(T5Config, self.config).d_model

    @property
    def decoder_num_attention_heads(self) -> int:
        """The number of attention heads of T5 decoder."""
        return cast(T5Config, self.config).num_heads

    @property
    def decoder_num_kv_attention_heads(self) -> int:
        """The number of key-value attention heads of t5 decoder."""
        return self.decoder_num_attention_heads

    @property
    def decoder_head_size(self) -> int:
        """The head size of T5 decoder."""
        return cast(T5Config, self.config).d_kv

    @property
    def decoder_ff_intermediate_size(self) -> int:
        """The intermediate of the linear layer in T5 decoder's MLP."""
        return cast(T5Config, self.config).d_ff
