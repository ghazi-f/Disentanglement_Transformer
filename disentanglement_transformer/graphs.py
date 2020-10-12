# This file defines the links between variables in the inference and generation networks of the PoS_tagging task

import torch.nn as nn

from components.links import CoattentiveTransformerLink, ConditionalCoattentiveTransformerLink, LastStateMLPLink
from disentanglement_transformer.variables import *


# def get_disentanglement_graph(h_params, word_embeddings):
#     xin_size, zin_size = h_params.embedding_dim, h_params.z_size
#     xout_size, zout_size = h_params.vocab_size, h_params.z_size
#     z_repnet = nn.LSTM(h_params.z_size, h_params.z_size, h_params.text_rep_l,
#                        batch_first=True,
#                        dropout=h_params.dropout)
#     lv_number = h_params.n_latents
#
#     # Generation
#     x_prev_gen = XPrevGen(h_params, word_embeddings, has_rep=False)
#     x_gen, z_gen = XGen(h_params, word_embeddings), ZGen(h_params, z_repnet, allow_prior=True )
#     z_xprev_to_x = ConditionalCoattentiveTransformerLink(xin_size, zout_size, xout_size,
#                                                          h_params.decoder_l, Categorical.parameter_activations,
#                                                          word_embeddings, highway=h_params.highway, sbn=None,
#                                                          dropout=h_params.dropout, n_mems=lv_number,
#                                                          memory=['z'], targets=['x_prev'], nheads=4)
#
#     # Inference
#     x_inf, z_inf = XInfer(h_params, word_embeddings, has_rep=False), ZInfer(h_params, z_repnet)
#     x_to_z = CoattentiveTransformerLink(xin_size, h_params.encoder_h, zout_size, h_params.encoder_l,
#                                         Gaussian.parameter_activations, nheads=4,
#                                         highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_number)
#
#     return {'infer': nn.ModuleList([nn.ModuleList([x_inf, x_to_z, z_inf]),
#                                     ]),
#             'gen':   nn.ModuleList([
#                                     nn.ModuleList([z_gen, z_xprev_to_x, x_gen]),
#                                     nn.ModuleList([x_prev_gen, z_xprev_to_x, x_gen]),
#                                     ])}, None, x_gen
#
#
# def get_non_auto_regressive_disentanglement_graph(h_params, word_embeddings):
#     xin_size, zin_size = h_params.embedding_dim, h_params.z_size
#     xout_size, zout_size = h_params.vocab_size, h_params.z_size
#     z_repnet = nn.LSTM(h_params.z_size, h_params.z_size, h_params.text_rep_l,
#                        batch_first=True,
#                        dropout=h_params.dropout)
#     lv_number = h_params.n_latents
#
#     # Generation
#     x_gen, z_gen, zlstm_gen = XGen(h_params, word_embeddings), ZGen(h_params, z_repnet, allow_prior=True), \
#                    ZlstmGen(h_params, z_repnet, allow_prior=True)
#     z_zlstm_to_x = ConditionalCoattentiveTransformerLink(xin_size, zout_size, xout_size,
#                                                          h_params.decoder_l, Categorical.parameter_activations,
#                                                          word_embeddings, highway=h_params.highway, sbn=None,
#                                                          dropout=h_params.dropout, n_mems=lv_number,
#                                                          memory=['z'], targets=['zlstm'], nheads=4, bidirectional=True)
#     z_to_zlstm = LastStateMLPLink(xin_size, h_params.encoder_h, zout_size, h_params.encoder_l, Gaussian.parameter_activations,
#                      highway=h_params.highway, dropout=h_params.dropout)
#
#
#     # Inference
#     x_inf, z_inf, zlstm_inf = XInfer(h_params, word_embeddings, has_rep=False), ZInfer(h_params, z_repnet), \
#                               ZlstmInfer(h_params, z_repnet)
#     x_to_z = CoattentiveTransformerLink(xin_size, h_params.encoder_h, zout_size, h_params.encoder_l,
#                                         Gaussian.parameter_activations, nheads=4,
#                                         highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_number)
#
#     return {'infer': nn.ModuleList([nn.ModuleList([x_inf, x_to_z, z_inf]),
#                                     ]),
#             'gen':   nn.ModuleList([
#                                     nn.ModuleList([z_gen, z_to_zlstm, zlstm_gen]),
#                                     nn.ModuleList([z_gen, z_zlstm_to_x, x_gen]),
#                                     nn.ModuleList([zlstm_gen, z_zlstm_to_x, x_gen]),
#                                     ])}, None, x_gen
#
#
# def get_non_auto_regressive_lstm_encoder_disentanglement_graph(h_params, word_embeddings):
#     xin_size, zin_size = h_params.embedding_dim, h_params.z_size
#     xout_size, zout_size = h_params.vocab_size, h_params.z_size
#     z_repnet = nn.LSTM(h_params.z_size, h_params.z_size, h_params.text_rep_l,
#                        batch_first=True,
#                        dropout=h_params.dropout)
#     lv_number = h_params.n_latents
#
#     # Generation
#     x_gen, z_gen, zlstm_gen = XGen(h_params, word_embeddings), ZGen(h_params, z_repnet, allow_prior=True), \
#                    ZlstmGen(h_params, z_repnet, allow_prior=True)
#     z_zlstm_to_x = ConditionalCoattentiveTransformerLink(xin_size, zout_size, xout_size,
#                                                          h_params.decoder_l, Categorical.parameter_activations,
#                                                          word_embeddings, highway=h_params.highway, sbn=None,
#                                                          dropout=h_params.dropout, n_mems=lv_number,
#                                                          memory=['z'], targets=['zlstm'], nheads=4, bidirectional=True)
#
#     # Inference
#     x_inf, z_inf, zlstm_inf = XInfer(h_params, word_embeddings, has_rep=True), ZInfer(h_params, z_repnet), \
#                               ZlstmInfer(h_params, z_repnet)
#     x_to_z = LastStateMLPLink(xin_size, h_params.encoder_h, zout_size, h_params.encoder_l,
#                                         Gaussian.parameter_activations, #nheads=4,
#                                         highway=h_params.highway, dropout=h_params.dropout#, n_targets=lv_number
#                               )
#
#     z_to_zlstm = LastStateMLPLink(xin_size, h_params.encoder_h, zout_size, h_params.encoder_l, Gaussian.parameter_activations,
#                      highway=h_params.highway, dropout=h_params.dropout)
#
#     return {'infer': nn.ModuleList([nn.ModuleList([x_inf, x_to_z, z_inf]),
#                                     nn.ModuleList([z_inf, z_to_zlstm, zlstm_inf])
#                                     ]),
#             'gen':   nn.ModuleList([
#                                     nn.ModuleList([z_gen, z_zlstm_to_x, x_gen]),
#                                     nn.ModuleList([zlstm_gen, z_zlstm_to_x, x_gen]),
#                                     ])}, None, x_gen

#
# def get_non_auto_regressive_structured_disentanglement_graph(h_params, word_embeddings):
#     xin_size, zin_size = h_params.embedding_dim, h_params.z_size
#     xout_size, zout_size = h_params.vocab_size, h_params.z_size
#     z_repnet = None
#     #nn.LSTM(h_params.z_size, h_params.z_size, h_params.text_rep_l,
#     # batch_first=True,
#     # dropout=h_params.dropout)
#     lv_number = h_params.n_latents
#
#     # Generation
#     x_gen, z_gen, z_gen1, z_gen2, zlstm_gen = \
#         XGen(h_params, word_embeddings), ZGen(h_params, z_repnet, allow_prior=True), \
#         ZGen1(h_params, z_repnet, allow_prior=True), ZGen2(h_params, z_repnet, allow_prior=True),\
#         ZlstmGen(h_params, z_repnet, allow_prior=True)
#     z_z1_z2_zlstm_to_x = ConditionalCoattentiveTransformerLink(zin_size, zout_size, xout_size,
#                                                                h_params.decoder_l, Categorical.parameter_activations,
#                                                                word_embeddings, highway=h_params.highway, sbn=None,
#                                                                dropout=h_params.dropout, n_mems=lv_number*3,
#                                                                memory=['z1', 'z2'], targets=['zlstm'],
#                                                                nheads=4, bidirectional=True)
#     z_to_z1 = LastStateMLPLink(zin_size, h_params.encoder_h, zout_size, h_params.encoder_l,
#                                         Gaussian.parameter_activations,
#                                         highway=h_params.highway, dropout=h_params.dropout)
#     z1_to_z2 = LastStateMLPLink(zin_size, h_params.encoder_h, zout_size, h_params.encoder_l,
#                                         Gaussian.parameter_activations,
#                                         highway=h_params.highway, dropout=h_params.dropout)
#
#     # Common
#     z_to_zlstm = LastStateMLPLink(zin_size, h_params.encoder_h, zout_size, h_params.encoder_l, Gaussian.parameter_activations,
#                      highway=h_params.highway, dropout=h_params.dropout)
#
#     # Inference
#     x_inf, z_inf, z_inf1, z_inf2, zlstm_inf = XInfer(h_params, word_embeddings, has_rep=False),\
#                                               ZInfer(h_params, z_repnet), \
#                                               ZInfer1(h_params, z_repnet), ZInfer2(h_params, z_repnet), \
#                                               ZlstmInfer(h_params, z_repnet)
#     x_to_z = CoattentiveTransformerLink(xin_size, h_params.encoder_h, zout_size, h_params.encoder_l,
#                                         Gaussian.parameter_activations, nheads=4,
#                                         highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_number)
#
#     x_to_z1 = CoattentiveTransformerLink(xin_size, h_params.encoder_h, zout_size, h_params.encoder_l,
#                                         Gaussian.parameter_activations, nheads=4,
#                                         highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_number)
#
#     x_to_z2 = CoattentiveTransformerLink(xin_size, h_params.encoder_h, zout_size, h_params.encoder_l,
#                                         Gaussian.parameter_activations, nheads=4,
#                                         highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_number)
#
#     return {'infer': nn.ModuleList([nn.ModuleList([x_inf, x_to_z, z_inf]),
#                                     nn.ModuleList([x_inf, x_to_z1, z_inf1]),
#                                     nn.ModuleList([x_inf, x_to_z2, z_inf2]),
#                                     nn.ModuleList([z_inf, z_to_zlstm, zlstm_inf]),
#                                     ]),
#             'gen':   nn.ModuleList([
#                                     nn.ModuleList([z_gen, z_to_zlstm, zlstm_gen]),
#                                     nn.ModuleList([z_gen, z_to_z1, z_gen1]),
#                                     nn.ModuleList([z_gen1, z1_to_z2, z_gen2]),
#                                     # nn.ModuleList([z_gen, z_z1_z2_zlstm_to_x, x_gen]),
#                                     nn.ModuleList([z_gen1, z_z1_z2_zlstm_to_x, x_gen]),
#                                     nn.ModuleList([z_gen2, z_z1_z2_zlstm_to_x, x_gen]),
#                                     nn.ModuleList([zlstm_gen, z_z1_z2_zlstm_to_x, x_gen]),
#                                     ])}, None, x_gen

#
# def get_structured_auto_regressive_disentanglement_graph(h_params, word_embeddings):
#     xin_size, zin_size = h_params.embedding_dim, h_params.z_size
#     xout_size, zout_size = h_params.vocab_size, h_params.z_size
#     z_repnet = None
#     #nn.LSTM(h_params.z_size, h_params.z_size, h_params.text_rep_l,
#     # batch_first=True,
#     # dropout=h_params.dropout)
#     lv_n1, lv_n2, lv_n3 = h_params.n_latents
#     lv_size_prop1, lv_size_prop2, lv_size_prop3 = lv_n1/max(h_params.n_latents), lv_n2/max(h_params.n_latents),\
#                                                      lv_n3/max(h_params.n_latents)
#     z1_size, z2_size, z3_size = int(zin_size*lv_size_prop1), int(zin_size*lv_size_prop2), int(zin_size*lv_size_prop3)
#     # Generation
#     x_gen, z_gen1, z_gen2, z_gen3, xprev_gen = \
#         XGen(h_params, word_embeddings), ZGen1(h_params, z_repnet, allow_prior=True), \
#         ZGen2(h_params, z_repnet, allow_prior=True), ZGen3(h_params, z_repnet, allow_prior=True), \
#         XPrevGen(h_params, word_embeddings, has_rep=False)
#     z1_z2_z3_xprev_to_x = ConditionalCoattentiveTransformerLink(xin_size,
#                                                                 int(zout_size*sum(h_params.n_latents)/max(h_params.n_latents)),
#                                                                 xout_size,h_params.decoder_l, Categorical.parameter_activations,
#                                                                 word_embeddings, highway=h_params.highway, sbn=None,
#                                                                 dropout=h_params.dropout, n_mems=sum(h_params.n_latents),
#                                                                 memory=['z1', 'z2', 'z3'], targets=['x_prev'],
#                                                                 nheads=4, bidirectional=False)
#     z1_to_z2 = CoattentiveTransformerLink(z1_size, int(h_params.decoder_h*lv_size_prop2), z2_size, h_params.decoder_l,
#                                           Gaussian.parameter_activations, nheads=4, sequence=None, memory=['z1'],
#                                           n_mems=h_params.n_latents[0],
#                                           highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n2)
#     z1_z2_to_z3 = CoattentiveTransformerLink(z2_size, # Input size doesn't matter here because there's no input
#                                              int(h_params.decoder_h*lv_size_prop3), z3_size, h_params.decoder_l,
#                                              Gaussian.parameter_activations, nheads=4, sequence=None, memory=['z1', 'z2'],
#                                              n_mems=h_params.n_latents[0]+h_params.n_latents[1],
#                                              highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n3)
#
#     # Inference
#     x_inf, z_inf1, z_inf2, z_inf3 = XInfer(h_params, word_embeddings, has_rep=False),\
#                                           ZInfer1(h_params, z_repnet), \
#                                           ZInfer2(h_params, z_repnet), ZInfer3(h_params, z_repnet)
#
#     x_to_z3 = CoattentiveTransformerLink(xin_size, h_params.encoder_h, z3_size, h_params.encoder_l,
#                                          Gaussian.parameter_activations, nheads=4, sequence=['x'], memory=None,
#                                          highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n3)
#
#     x_z3_to_z2 = CoattentiveTransformerLink(xin_size, int(lv_size_prop2*h_params.encoder_h), z2_size, h_params.encoder_l,
#                                             Gaussian.parameter_activations, nheads=4, sequence=['x'], memory=['z3'],
#                                             n_mems=lv_n3,
#                                             highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n2)
#     x_z2_z3_to_z1 = CoattentiveTransformerLink(xin_size, int(lv_size_prop1*h_params.encoder_h), z1_size, h_params.encoder_l,
#                                         Gaussian.parameter_activations, nheads=4, sequence=['x'], memory=['z2', 'z3'],
#                                         n_mems=lv_n3+lv_n2,
#                                         highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n1)
#
#     return {'infer': nn.ModuleList([nn.ModuleList([x_inf, x_z2_z3_to_z1, z_inf1]),
#                                     nn.ModuleList([z_inf2, x_z2_z3_to_z1, z_inf1]),
#                                     nn.ModuleList([z_inf3, x_z2_z3_to_z1, z_inf1]),
#                                     nn.ModuleList([z_inf3, x_z3_to_z2, z_inf2]),
#                                     nn.ModuleList([x_inf, x_z3_to_z2, z_inf2]),
#                                     nn.ModuleList([x_inf, x_to_z3, z_inf3]),
#                                     ]),
#             'gen':   nn.ModuleList([
#                                     nn.ModuleList([z_gen1, z1_to_z2, z_gen2]),
#                                     nn.ModuleList([z_gen1, z1_z2_to_z3, z_gen3]),
#                                     nn.ModuleList([z_gen2, z1_z2_to_z3, z_gen3]),
#                                     nn.ModuleList([z_gen1, z1_z2_z3_xprev_to_x, x_gen]),
#                                     nn.ModuleList([z_gen2, z1_z2_z3_xprev_to_x, x_gen]),
#                                     nn.ModuleList([z_gen3, z1_z2_z3_xprev_to_x, x_gen]),
#                                     nn.ModuleList([xprev_gen, z1_z2_z3_xprev_to_x, x_gen]),
#                                     ])}, None, x_gen


def get_structured_auto_regressive_disentanglement_graph(h_params, word_embeddings):
    xin_size, zin_size = h_params.embedding_dim, h_params.z_size
    xout_size, zout_size = h_params.vocab_size, h_params.z_size
    z_repnet = None
    #nn.LSTM(h_params.z_size, h_params.z_size, h_params.text_rep_l,
    # batch_first=True,
    # dropout=h_params.dropout)
    lv_n1, lv_n2, lv_n3 = h_params.n_latents
    lv_size_prop1, lv_size_prop2, lv_size_prop3 = lv_n1/max(h_params.n_latents), lv_n2/max(h_params.n_latents),\
                                                     lv_n3/max(h_params.n_latents)
    z1_size, z2_size, z3_size = int(zin_size*lv_size_prop1), int(zin_size*lv_size_prop2), int(zin_size*lv_size_prop3)
    # Generation
    x_gen, z_gen1, z_gen2, z_gen3, xprev_gen = \
        XGen(h_params, word_embeddings), ZGen1(h_params, z_repnet, allow_prior=True), \
        ZGen2(h_params, z_repnet, allow_prior=True), ZGen3(h_params, z_repnet, allow_prior=True), \
        XPrevGen(h_params, word_embeddings, has_rep=False)
    z1_z2_z3_xprev_to_x = ConditionalCoattentiveTransformerLink(xin_size,
                                                                int(zout_size*sum(h_params.n_latents)/max(h_params.n_latents)),
                                                                xout_size,h_params.decoder_l, Categorical.parameter_activations,
                                                                word_embeddings, highway=h_params.highway, sbn=None,
                                                                dropout=h_params.dropout, n_mems=sum(h_params.n_latents),
                                                                memory=['z1', 'z2', 'z3'], targets=['x_prev'],
                                                                nheads=4, bidirectional=False)
    z1_to_z2 = CoattentiveTransformerLink(z1_size, int(h_params.decoder_h*lv_size_prop2), z2_size, h_params.decoder_l,
                                          Gaussian.parameter_activations, nheads=4, sequence=None, memory=['z1'],
                                          n_mems=h_params.n_latents[0],
                                          highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n2)
    z2_to_z3 = CoattentiveTransformerLink(z2_size, # Input size doesn't matter here because there's no input
                                             int(h_params.decoder_h*lv_size_prop3), z3_size, h_params.decoder_l,
                                             Gaussian.parameter_activations, nheads=4, sequence=None, memory=['z2'],
                                             n_mems=h_params.n_latents[1],
                                             highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n3)

    # Inference
    x_inf, z_inf1, z_inf2, z_inf3 = XInfer(h_params, word_embeddings, has_rep=False),\
                                          ZInfer1(h_params, z_repnet), \
                                          ZInfer2(h_params, z_repnet), ZInfer3(h_params, z_repnet)

    x_to_z3 = CoattentiveTransformerLink(xin_size, h_params.encoder_h, z3_size, h_params.encoder_l,
                                         Gaussian.parameter_activations, nheads=4, sequence=['x'], memory=None,
                                         highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n3)

    x_z3_to_z2 = CoattentiveTransformerLink(xin_size, int(lv_size_prop2*h_params.encoder_h), z2_size, h_params.encoder_l,
                                            Gaussian.parameter_activations, nheads=4, sequence=['x'], memory=['z3'],
                                            n_mems=lv_n3,
                                            highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n2)
    x_z2_z3_to_z1 = CoattentiveTransformerLink(xin_size, int(lv_size_prop1*h_params.encoder_h), z1_size, h_params.encoder_l,
                                        Gaussian.parameter_activations, nheads=4, sequence=['x'], memory=['z2', 'z3'],
                                        n_mems=lv_n3+lv_n2,
                                        highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n1)

    return {'infer': nn.ModuleList([nn.ModuleList([x_inf, x_z2_z3_to_z1, z_inf1]),
                                    nn.ModuleList([z_inf2, x_z2_z3_to_z1, z_inf1]),
                                    nn.ModuleList([z_inf3, x_z2_z3_to_z1, z_inf1]),
                                    nn.ModuleList([z_inf3, x_z3_to_z2, z_inf2]),
                                    nn.ModuleList([x_inf, x_z3_to_z2, z_inf2]),
                                    nn.ModuleList([x_inf, x_to_z3, z_inf3]),
                                    ]),
            'gen':   nn.ModuleList([
                                    nn.ModuleList([z_gen1, z1_to_z2, z_gen2]),
                                    nn.ModuleList([z_gen2, z2_to_z3, z_gen3]),
                                    nn.ModuleList([z_gen1, z1_z2_z3_xprev_to_x, x_gen]),
                                    nn.ModuleList([z_gen2, z1_z2_z3_xprev_to_x, x_gen]),
                                    nn.ModuleList([z_gen3, z1_z2_z3_xprev_to_x, x_gen]),
                                    nn.ModuleList([xprev_gen, z1_z2_z3_xprev_to_x, x_gen]),
                                    ])}, None, x_gen


def get_discrete_auto_regressive_disentanglement_graph(h_params, word_embeddings):
    xin_size, zin_size = h_params.embedding_dim, h_params.z_emb_dim
    xout_size, zout_size = h_params.vocab_size, h_params.z_size
    z_repnet = None
    #nn.LSTM(h_params.z_size, h_params.z_size, h_params.text_rep_l,
    # batch_first=True,
    # dropout=h_params.dropout)
    lv_n1, lv_n2, lv_n3 = h_params.n_latents
    lv_size_prop1, lv_size_prop2, lv_size_prop3 = lv_n1/max(h_params.n_latents), lv_n2/max(h_params.n_latents),\
                                                     lv_n3/max(h_params.n_latents)
    z1in_size, z2in_size, z3in_size = int(zin_size*lv_size_prop1), int(zin_size*lv_size_prop2), int(zin_size*lv_size_prop3)
    z1out_size, z2out_size, z3out_size = int(zout_size*lv_size_prop1), int(zout_size*lv_size_prop2), int(zout_size*lv_size_prop3)
    # Generation
    x_gen, z_gen1, z_gen2, z_gen3, xprev_gen = \
        XGen(h_params, word_embeddings), ZGenDisc1(h_params, z_repnet, allow_prior=True), \
        ZGenDisc2(h_params, z_repnet, allow_prior=True), ZGenDisc3(h_params, z_repnet, allow_prior=True), \
        XPrevGen(h_params, word_embeddings, has_rep=False)
    z1_z2_z3_xprev_to_x = ConditionalCoattentiveTransformerLink(xin_size,
                                                                int(zin_size*sum(h_params.n_latents)/max(h_params.n_latents)),
                                                                xout_size,h_params.decoder_l, Categorical.parameter_activations,
                                                                word_embeddings, highway=h_params.highway, sbn=None,
                                                                dropout=h_params.dropout, n_mems=sum(h_params.n_latents),
                                                                memory=['z1', 'z2', 'z3'], targets=['x_prev'],
                                                                nheads=4, bidirectional=False)
    z1_to_z2 = CoattentiveTransformerLink(z1in_size, int(h_params.decoder_h*lv_size_prop2), z2out_size, h_params.decoder_l,
                                          MultiCategorical.parameter_activations, nheads=4, sequence=None, memory=['z1'],
                                          n_mems=h_params.n_latents[0],
                                          highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n2)
    z2_to_z3 = CoattentiveTransformerLink(z2in_size, # Input size doesn't matter here because there's no input
                                             int(h_params.decoder_h*lv_size_prop3), z3out_size, h_params.decoder_l,
                                             MultiCategorical.parameter_activations, nheads=4, sequence=None, memory=['z2'],
                                             n_mems=h_params.n_latents[1],
                                             highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n3)

    # Inference
    x_inf, z_inf1, z_inf2, z_inf3 = XInfer(h_params, word_embeddings, has_rep=False),\
                                          ZInferDisc1(h_params, z_repnet), \
                                          ZInferDisc2(h_params, z_repnet), ZInferDisc3(h_params, z_repnet)

    x_to_z3 = CoattentiveTransformerLink(xin_size, h_params.encoder_h, z3out_size, h_params.encoder_l,
                                         MultiCategorical.parameter_activations, nheads=4, sequence=['x'], memory=None,
                                         highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n3)

    x_z3_to_z2 = CoattentiveTransformerLink(xin_size, int(lv_size_prop2*h_params.encoder_h), z2out_size, h_params.encoder_l,
                                            MultiCategorical.parameter_activations, nheads=4, sequence=['x'], memory=['z3'],
                                            n_mems=lv_n3,
                                            highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n2)
    x_z2_z3_to_z1 = CoattentiveTransformerLink(xin_size, int(lv_size_prop1*h_params.encoder_h), z1out_size, h_params.encoder_l,
                                        MultiCategorical.parameter_activations, nheads=4, sequence=['x'], memory=['z2', 'z3'],
                                        n_mems=lv_n3+lv_n2,
                                        highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n1)

    return {'infer': nn.ModuleList([nn.ModuleList([x_inf, x_z2_z3_to_z1, z_inf1]),
                                    nn.ModuleList([z_inf2, x_z2_z3_to_z1, z_inf1]),
                                    nn.ModuleList([z_inf3, x_z2_z3_to_z1, z_inf1]),
                                    nn.ModuleList([z_inf3, x_z3_to_z2, z_inf2]),
                                    nn.ModuleList([x_inf, x_z3_to_z2, z_inf2]),
                                    nn.ModuleList([x_inf, x_to_z3, z_inf3]),
                                    ]),
            'gen':   nn.ModuleList([
                                    nn.ModuleList([z_gen1, z1_to_z2, z_gen2]),
                                    nn.ModuleList([z_gen2, z2_to_z3, z_gen3]),
                                    nn.ModuleList([z_gen1, z1_z2_z3_xprev_to_x, x_gen]),
                                    nn.ModuleList([z_gen2, z1_z2_z3_xprev_to_x, x_gen]),
                                    nn.ModuleList([z_gen3, z1_z2_z3_xprev_to_x, x_gen]),
                                    nn.ModuleList([xprev_gen, z1_z2_z3_xprev_to_x, x_gen]),
                                    ])}, None, x_gen


def get_structured_auto_regressive_disentanglement_graph2(h_params, word_embeddings):
    # in this one, generation only depends on z3
    xin_size, zin_size = h_params.embedding_dim, h_params.z_size
    xout_size, zout_size = h_params.vocab_size, h_params.z_size
    z_repnet = None
    #nn.LSTM(h_params.z_size, h_params.z_size, h_params.text_rep_l,
    # batch_first=True,
    # dropout=h_params.dropout)
    lv_n1, lv_n2, lv_n3 = h_params.n_latents
    lv_size_prop1, lv_size_prop2, lv_size_prop3 = lv_n1/max(h_params.n_latents), lv_n2/max(h_params.n_latents),\
                                                     lv_n3/max(h_params.n_latents)
    z1_size, z2_size, z3_size = int(zin_size*lv_size_prop1), int(zin_size*lv_size_prop2), int(zin_size*lv_size_prop3)
    # Generation
    x_gen, z_gen1, z_gen2, z_gen3, xprev_gen = \
        XGen(h_params, word_embeddings), ZGen1(h_params, z_repnet, allow_prior=True), \
        ZGen2(h_params, z_repnet, allow_prior=True), ZGen3(h_params, z_repnet, allow_prior=True), \
        XPrevGen(h_params, word_embeddings, has_rep=False)
    z3_xprev_to_x = ConditionalCoattentiveTransformerLink(xin_size,
                                                                int(zout_size*lv_n3/max(h_params.n_latents)),
                                                                xout_size,h_params.decoder_l, Categorical.parameter_activations,
                                                                word_embeddings, highway=h_params.highway, sbn=None,
                                                                dropout=h_params.dropout, n_mems=lv_n3,
                                                                memory=['z3'], targets=['x_prev'],
                                                                nheads=4, bidirectional=False)
    z1_to_z2 = CoattentiveTransformerLink(z1_size, int(h_params.decoder_h*lv_size_prop2), z2_size, h_params.decoder_l,
                                          Gaussian.parameter_activations, nheads=4, sequence=None, memory=['z1'],
                                          n_mems=h_params.n_latents[0],
                                          highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n2)
    z1_z2_to_z3 = CoattentiveTransformerLink(z2_size, # Input size doesn't matter here because there's no input
                                             int(h_params.decoder_h*lv_size_prop3), z3_size, h_params.decoder_l,
                                             Gaussian.parameter_activations, nheads=4, sequence=None, memory=['z1', 'z2'],
                                             n_mems=h_params.n_latents[0]+h_params.n_latents[1],
                                             highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n3)

    # Inference
    x_inf, z_inf1, z_inf2, z_inf3 = XInfer(h_params, word_embeddings, has_rep=False),\
                                          ZInfer1(h_params, z_repnet), \
                                          ZInfer2(h_params, z_repnet), ZInfer3(h_params, z_repnet)

    x_to_z3 = CoattentiveTransformerLink(xin_size, h_params.encoder_h, z3_size, h_params.encoder_l,
                                         Gaussian.parameter_activations, nheads=4, sequence=['x'], memory=None,
                                         highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n3)

    x_z3_to_z2 = CoattentiveTransformerLink(xin_size, int(lv_size_prop2*h_params.encoder_h), z2_size, h_params.encoder_l,
                                            Gaussian.parameter_activations, nheads=4, sequence=['x'], memory=['z3'],
                                            n_mems=lv_n3,
                                            highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n2)
    x_z2_z3_to_z1 = CoattentiveTransformerLink(xin_size, int(lv_size_prop1*h_params.encoder_h), z1_size, h_params.encoder_l,
                                        Gaussian.parameter_activations, nheads=4, sequence=['x'], memory=['z2', 'z3'],
                                        n_mems=lv_n3+lv_n2,
                                        highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_n1)

    return {'infer': nn.ModuleList([nn.ModuleList([x_inf, x_z2_z3_to_z1, z_inf1]),
                                    nn.ModuleList([z_inf2, x_z2_z3_to_z1, z_inf1]),
                                    nn.ModuleList([z_inf3, x_z2_z3_to_z1, z_inf1]),
                                    nn.ModuleList([z_inf3, x_z3_to_z2, z_inf2]),
                                    nn.ModuleList([x_inf, x_z3_to_z2, z_inf2]),
                                    nn.ModuleList([x_inf, x_to_z3, z_inf3]),
                                    ]),
            'gen':   nn.ModuleList([
                                    nn.ModuleList([z_gen1, z1_to_z2, z_gen2]),
                                    nn.ModuleList([z_gen1, z1_z2_to_z3, z_gen3]),
                                    nn.ModuleList([z_gen2, z1_z2_to_z3, z_gen3]),
                                    nn.ModuleList([z_gen3, z3_xprev_to_x, x_gen]),
                                    nn.ModuleList([xprev_gen, z3_xprev_to_x, x_gen]),
                                    ])}, None, x_gen


def get_non_auto_regressive_structured_disentanglement_graph(h_params, word_embeddings):
    xin_size, zin_size = h_params.embedding_dim, h_params.z_size
    xout_size, zout_size = h_params.vocab_size, h_params.z_size
    z_repnet = None
    #nn.LSTM(h_params.z_size, h_params.z_size, h_params.text_rep_l,
    # batch_first=True,
    # dropout=h_params.dropout)
    lv_number = h_params.n_latents

    # Generation
    x_gen, z_gen, z_gen1, z_gen2, zlstm_gen = \
        XGen(h_params, word_embeddings), ZGen(h_params, z_repnet, allow_prior=True), \
        ZGen1(h_params, z_repnet, allow_prior=True), ZGen2(h_params, z_repnet, allow_prior=True),\
        ZlstmGen(h_params, z_repnet, allow_prior=True)
    z_z1_z2_zlstm_to_x = ConditionalCoattentiveTransformerLink(zin_size, zout_size*3, xout_size,
                                                               h_params.decoder_l, Categorical.parameter_activations,
                                                               word_embeddings, highway=h_params.highway, sbn=None,
                                                               dropout=h_params.dropout, n_mems=lv_number*3,
                                                               memory=['z', 'z1', 'z2'], targets=['zlstm'],
                                                               nheads=4, bidirectional=True)
    z_to_z1 = LastStateMLPLink(zin_size, h_params.encoder_h, zout_size, h_params.encoder_l,
                               Gaussian.parameter_activations,
                               highway=h_params.highway, dropout=h_params.dropout)
    z1_to_z2 = LastStateMLPLink(zin_size, h_params.encoder_h, zout_size, h_params.encoder_l,
                                Gaussian.parameter_activations,
                                highway=h_params.highway, dropout=h_params.dropout)

    # Common
    z_z1_z2_to_zlstm = LastStateMLPLink(zin_size*3, h_params.encoder_h, zout_size, h_params.encoder_l,
                                        Gaussian.parameter_activations, highway=h_params.highway,
                                        dropout=h_params.dropout)

    # Inference
    x_inf, z_inf, z_inf1, z_inf2, zlstm_inf = XInfer(h_params, word_embeddings, has_rep=False),\
                                              ZInfer(h_params, z_repnet), \
                                              ZInfer1(h_params, z_repnet), ZInfer2(h_params, z_repnet), \
                                              ZlstmInfer(h_params, z_repnet)

    x_to_z2 = CoattentiveTransformerLink(xin_size, h_params.encoder_h, zout_size, h_params.encoder_l,
                                         Gaussian.parameter_activations, nheads=4, sequence=['x'], memory=None,
                                         highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_number)

    x_z2_to_z1 = CoattentiveTransformerLink(xin_size, h_params.encoder_h, zout_size, h_params.encoder_l,
                                            Gaussian.parameter_activations, nheads=4, sequence=['x'], memory=['z2'],
                                            n_mems=h_params.n_latents,
                                            highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_number)
    x_z1_z2_to_z = CoattentiveTransformerLink(xin_size, h_params.encoder_h, zout_size, h_params.encoder_l,
                                        Gaussian.parameter_activations, nheads=4, sequence=['x'], memory=['z2', 'z1'],
                                        n_mems=h_params.n_latents*2,
                                        highway=h_params.highway, dropout=h_params.dropout, n_targets=lv_number)

    return {'infer': nn.ModuleList([nn.ModuleList([x_inf, x_z1_z2_to_z, z_inf]),
                                    nn.ModuleList([z_inf1, x_z1_z2_to_z, z_inf]),
                                    nn.ModuleList([z_inf2, x_z1_z2_to_z, z_inf]),
                                    nn.ModuleList([z_inf2, x_z2_to_z1, z_inf1]),
                                    nn.ModuleList([x_inf, x_z2_to_z1, z_inf1]),
                                    nn.ModuleList([x_inf, x_to_z2, z_inf2]),
                                    nn.ModuleList([z_inf, z_z1_z2_to_zlstm, zlstm_inf]),
                                    nn.ModuleList([z_inf1, z_z1_z2_to_zlstm, zlstm_inf]),
                                    nn.ModuleList([z_inf2, z_z1_z2_to_zlstm, zlstm_inf]),
                                    ]),
            'gen':   nn.ModuleList([
                                    nn.ModuleList([z_gen, z_to_z1, z_gen1]),
                                    nn.ModuleList([z_gen1, z1_to_z2, z_gen2]),
                                    nn.ModuleList([z_gen, z_z1_z2_zlstm_to_x, x_gen]),
                                    nn.ModuleList([z_gen1, z_z1_z2_zlstm_to_x, x_gen]),
                                    nn.ModuleList([z_gen2, z_z1_z2_zlstm_to_x, x_gen]),
                                    nn.ModuleList([zlstm_gen, z_z1_z2_zlstm_to_x, x_gen]),
                                    nn.ModuleList([z_gen, z_z1_z2_to_zlstm, zlstm_gen]),
                                    nn.ModuleList([z_gen1, z_z1_z2_to_zlstm, zlstm_gen]),
                                    nn.ModuleList([z_gen2, z_z1_z2_to_zlstm, zlstm_gen]),
                                    ])}, None, x_gen
