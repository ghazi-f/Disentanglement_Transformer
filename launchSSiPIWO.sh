#!/usr/bin/env bash
python sent_train.py --losses "SSiPIWO" --test_name "IMDB/SSiPIWO/0.001small" --supervision_proportion 0.001 ---testing_iw_samples 10 --device "cuda:2" --embedding_dim 200 --z_size 100 --text_rep_h 200 --encoder_h 200 --decoder_h 200 --pos_embedding_dim 100 --pos_h 100
python sent_train.py --losses "SSiPIWO" --test_name "IMDB/SSiPIWO/0.003small" --supervision_proportion 0.003 --testing_iw_samples 10 --device "cuda:2" --embedding_dim 200 --z_size 100 --text_rep_h 200 --encoder_h 200 --decoder_h 200 --pos_embedding_dim 100 --pos_h 100
python sent_train.py --losses "SSiPIWO" --test_name "IMDB/SSiPIWO/0.01small" --supervision_proportion 0.01 --testing_iw_samples 10 --device "cuda:2" --embedding_dim 200 --z_size 100 --text_rep_h 200 --encoder_h 200 --decoder_h 200 --pos_embedding_dim 100 --pos_h 100
python sent_train.py --losses "SSiPIWO" --test_name "IMDB/SSiPIWO/0.03small" --supervision_proportion 0.03 --testing_iw_samples 10 --device "cuda:2" --embedding_dim 200 --z_size 100 --text_rep_h 200 --encoder_h 200 --decoder_h 200 --pos_embedding_dim 100 --pos_h 100
python sent_train.py --losses "SSiPIWO" --test_name "IMDB/SSiPIWO/0.1small" --supervision_proportion 0.1 --testing_iw_samples 10 --device "cuda:2" --embedding_dim 200 --z_size 100 --text_rep_h 200 --encoder_h 200 --decoder_h 200 --pos_embedding_dim 100 --pos_h 100
python sent_train.py --losses "SSiPIWO" --test_name "IMDB/SSiPIWO/0.3small" --supervision_proportion 0.3 --testing_iw_samples 10 --device "cuda:2" --embedding_dim 200 --z_size 100 --text_rep_h 200 --encoder_h 200 --decoder_h 200 --pos_embedding_dim 100 --pos_h 100
python sent_train.py --losses "SSiPIWO" --test_name "IMDB/SSiPIWO/1.0small" --supervision_proportion 1.0 --testing_iw_samples 10 --device "cuda:2" --embedding_dim 200 --z_size 100 --text_rep_h 200 --encoder_h 200 --decoder_h 200 --pos_embedding_dim 100 --pos_h 100