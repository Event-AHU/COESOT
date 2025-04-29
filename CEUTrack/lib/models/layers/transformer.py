
import copy
import torch
import torch.nn.functional as F
from torch import nn
from torch.nn import MultiheadAttention


class Transformer(nn.Module):
    def __init__(self, d_model=512, nhead=8, num_encoder_layers=4, dim_feedforward=2048,
                 dropout=0.1, activation="relu", normalize_before=False):
        super().__init__()

        adapt_layer = TransformerAdaptLayer(d_model, nhead, dim_feedforward, dropout, activation, normalize_before)
        adapt_norm = nn.LayerNorm(d_model)
        self.adapter = TransformerAdapter(adapt_layer, num_encoder_layers, adapt_norm)

        self._reset_parameters()

        self.d_model = d_model
        self.nhead = nhead

    def _reset_parameters(self):
        for p in self.parameters():
            if p.dim() > 1:
                nn.init.xavier_uniform_(p)

    def forward(self, srcs):
        memory_input = self.adapter(srcs[0], srcs[1:]).squeeze(0)
        return memory_input


class TransformerAdapter(nn.Module):
    def __init__(self, decoder_layer, num_layers, norm=None, return_intermediate=False):
        super().__init__()
        self.layers = _get_clones(decoder_layer, num_layers)
        self.num_layers = num_layers
        self.norm = norm
        # self.return_intermediate = return_intermediate

    def forward(self, tgt, memory, tgt_mask=None, memory_mask=None, tgt_key_padding_mask=None,
                memory_key_padding_mask=None, pos=None, query_pos=None):
        output = tgt            # test img of input

        for layer in range(self.num_layers):
            output = self.layers[layer](memory[layer], output, tgt_mask=tgt_mask, memory_mask=memory_mask, pos=pos, query_pos=query_pos,
                           tgt_key_padding_mask=tgt_key_padding_mask, memory_key_padding_mask=memory_key_padding_mask)
        if self.norm is not None:
            output = self.norm(output)

        return output


class TransformerAdaptLayer(nn.Module):

    def __init__(self, d_model, nhead, dim_feedforward=2048, dropout=0.1,
                 activation="relu", normalize_before=False):
        super().__init__()
        # self.self_attn = MultiheadAttention(d_model, nhead, dropout=dropout)
        self.multihead_attn = MultiheadAttention(d_model, nhead, dropout=dropout)
        # Implementation of Feedforward model
        self.linear1 = nn.Linear(d_model, dim_feedforward)
        self.dropout = nn.Dropout(dropout)
        self.linear2 = nn.Linear(dim_feedforward, d_model)

        # self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.norm3 = nn.LayerNorm(d_model)
        # self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)
        self.dropout3 = nn.Dropout(dropout)

        self.activation = _get_activation_fn(activation)
        self.normalize_before = normalize_before

    def forward_post(self, tgt, memory, tgt_mask=None, memory_mask=None, tgt_key_padding_mask=None,
                     memory_key_padding_mask=None, pos=None, query_pos=None):
        # tgt2 = self.self_attn(tgt, tgt, value=tgt, attn_mask=tgt_mask,
        #                       key_padding_mask=tgt_key_padding_mask)[0]
        # tgt = tgt + self.dropout1(tgt2)
        # tgt = self.norm1(tgt)
        tgt2 = self.multihead_attn(query=tgt, key=memory, value=memory,
                                   attn_mask=memory_mask, key_padding_mask=memory_key_padding_mask)[0]
        tgt = tgt + self.dropout2(tgt2)
        tgt = self.norm2(tgt)
        tgt2 = self.linear2(self.dropout(self.activation(self.linear1(tgt))))
        tgt = tgt + self.dropout3(tgt2)
        tgt = self.norm3(tgt)
        return tgt

    def forward(self, tgt, memory, tgt_mask=None, memory_mask=None, tgt_key_padding_mask=None,
                memory_key_padding_mask=None, pos=None, query_pos=None):
        if self.normalize_before:
            return self.forward_pre(tgt, memory, tgt_mask, memory_mask,
                                    tgt_key_padding_mask, memory_key_padding_mask, pos, query_pos)
        return self.forward_post(tgt, memory, tgt_mask, memory_mask,
                                 tgt_key_padding_mask, memory_key_padding_mask, pos, query_pos)


def _get_clones(module, N):
    return nn.ModuleList([copy.deepcopy(module) for i in range(N)])


def build_transformer(cfg, hidden_dim):
    return Transformer(
        d_model=hidden_dim//2,
        # dropout=0.1,
        # nhead=8,
        dim_feedforward=cfg.MODEL.TRANSFORMER.DIM_FEEDFORWARD,
        num_encoder_layers=cfg.MODEL.TRANSFORMER.LAYER,
        # num_decoder_layers=cfg.dec_layers,
        # normalize_before=cfg.pre_norm,
        # return_intermediate_dec=True,
    )


def _get_activation_fn(activation):
    """Return an activation function given a string"""
    if activation == "relu":
        return F.relu
    if activation == "gelu":
        return F.gelu
    if activation == "glu":
        return F.glu
    raise RuntimeError(F"activation should be relu/gelu/glu, not {activation}.")
