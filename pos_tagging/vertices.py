# This file defines the links between variables in the inference and generation networks of the PoS_tagging task

import torch.nn as nn

from components.links import GRULink
from pos_tagging.variables import *


def get_graph(h_params, word_embeddings, pos_embeddings):
    xin_size, yin_size, zin_size = h_params.embedding_dim, h_params.pos_embedding_dim, h_params.z_size
    xout_size, yout_size, zout_size = h_params.vocab_size, h_params.tag_size, h_params.z_size

    # Inference
    x_inf, y_inf, z_inf = XInfer(h_params, word_embeddings), YInfer(h_params, pos_embeddings), ZInfer(h_params)
    x_to_z = GRULink(xin_size, h_params.encoder_h, zout_size, h_params.encoder_l, Gaussian.parameters)
    x_z_to_y = GRULink(xin_size+zin_size, h_params.encoder_h, yout_size, h_params.encoder_l, Categorical.parameters,
                       pos_embeddings)

    # Generation
    x_gen, y_gen, z_gen = XGen(h_params, word_embeddings), YGen(h_params, pos_embeddings), ZGen(h_params)
    z_to_y = GRULink(zin_size, h_params.decoder_h, yout_size, h_params.decoder_l, Categorical.parameters,
                     pos_embeddings)
    z_y_to_x = GRULink(yin_size+zin_size, h_params.decoder_h, xout_size, h_params.decoder_l, Categorical.parameters,
                       word_embeddings)

    return {'infer': nn.ModuleList([nn.ModuleList([x_inf, x_to_z, z_inf]),
                                    nn.ModuleList([x_inf, x_z_to_y, y_inf]),
                                    nn.ModuleList([z_inf, x_z_to_y, y_inf])]),
            'gen':   nn.ModuleList([nn.ModuleList([z_gen, z_to_y, y_gen]),
                                    nn.ModuleList([z_gen, z_y_to_x, x_gen]),
                                    nn.ModuleList([y_gen, z_y_to_x, x_gen])])}, y_inf, x_gen

