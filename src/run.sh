#!/bin/bash

# export CUDA_VISIBLE_DEVICES="1,2,3"

# python zero-shot-eval.py --bs 65 --model_path 'XVERSE-13B'
 python zero-shot-eval.py --bs 60 --model_path 'Baichuan-7B'
# python zero-shot-eval.py --bs 45 --model_path 'Baichuan-13B-Base'
# python zero-shot-eval.py --bs 100 --model_path 'ChatMusician'

# python five-shot.py --bs 40 --model_path 'XVERSE-7B'
# python five-shot.py --bs 20 --model_path 'XVERSE-13B'
# python five-shot.py --bs 60 --model_path 'Baichuan-7B'
# python five-shot.py --bs 40 --model_path 'Baichuan-13B-Base'
#python five-shot.py --bs 30 --model_path 'ChatMusician'