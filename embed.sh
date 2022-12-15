# -*- coding: utf-8 -*-
#!/usr/bin/env bash

python embed.py --gpu 0 --csv_input_file train_clean.csv --csv_output_file train_esm1v_t33_650M_UR90S_1.csv --batch_size 4 --model esm1v_t33_650M_UR90S_1
python embed.py --gpu 0 --csv_input_file test_clean.csv --csv_output_file test_esm1v_t33_650M_UR90S_1.csv --batch_size 4 --model esm1v_t33_650M_UR90S_1 --test_mode
python embed.py --gpu 0 --csv_input_file train_clean.csv --csv_output_file train_esm1v_t33_650M_UR90S_5.csv --batch_size 4 --model esm1v_t33_650M_UR90S_5
python embed.py --gpu 0 --csv_input_file test_clean.csv --csv_output_file test_esm1v_t33_650M_UR90S_5.csv --batch_size 4 --model esm1v_t33_650M_UR90S_5 --test_mode
python embed.py --gpu 0 --csv_input_file train_clean.csv --csv_output_file train_esm2_t33_650M_UR50D.csv --batch_size 4 --model esm2_t33_650M_UR50D
python embed.py --gpu 0 --csv_input_file test_clean.csv --csv_output_file test_esm2_t33_650M_UR50D.csv --batch_size 4 --model esm2_t33_650M_UR50D --test_mode