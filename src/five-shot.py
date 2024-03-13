import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm
import os
import torch
import numpy as np
import re
import json
import argparse
import pdb

def make_prompt(question, A, B, C, D):
    prompt = "{} 选项A，{}; 选项B，{}; 选项C，{}; 选项D，{}。请你严格按照以下格式输出：[[答案：]]解析".format(question, A, B, C, D)
    return prompt

def retrieve_answer(prompt, response):
    pattern = r'[A-D]'
    try:
        response = response.replace(prompt, '')
        matches = re.findall(pattern, response)
        matches = list(set(matches))
        if len(matches) == 1:
            response_answer = matches[0]
        elif len(matches) > 1:
            response_answer = matches[-1]
        else:
            response_answer = ''
    except Exception as e:
        # print(e)
        response_answer = ''
    return response_answer

def process_csv(input_csv, output_csv, model, tokenizer, theme):
    df = pd.read_csv(input_csv)

    batch_size = bs
    # batch_size = 2
    # batch_size = 10
    num_batches = len(df) // batch_size + 1
    responses = []
    # pdb.set_trace()
    for i in tqdm(range(num_batches)):
        start_idx = i * batch_size
        end_idx = start_idx + batch_size
        batch_df = df[start_idx:end_idx]

        prompts, subthemes, answers = [], [], [] # 不能列表连等，不然会是一个存储空间！！！
        for index, row in tqdm(batch_df.iterrows()):
            # question = row['question']
            # A, B, C, D = row['A'], row['B'], row['C'], row['D']
            answer = row['answer']
            subtheme = row['subtheme']
            # prompt = make_prompt(question, A, B, C, D)
            prompt = row['question']
            
            prompts.append(prompt)
            subthemes.append(subtheme)
            answers.append(answer)

        try:
            response = generate(prompts, model, tokenizer)
            for ri in range(len(response)):
                predict_answer = retrieve_answer(prompt=prompts[ri], response=response[ri])
                match = 1 if answers[ri] == predict_answer else 0
                responses.append({
                    'prompt': prompts[ri], 
                    # 'response': response[ri].replace('|',''), 
                    'response': response[ri],
                    'theme': theme,
                    'subtheme': subthemes[ri],
                    'right_answer': answers[ri],
                    'predict_answer': predict_answer,
                    'match': match})
        except Exception as e:
            print(e)
            for ri in range(len(prompts)):
                responses.append({
                    'prompt': prompts[ri],
                    'response': ' ',
                    'theme': theme,
                    'subtheme': subthemes[ri],
                    'right_answer': answers[ri],
                    'predict_answer': ' ',
                    'match': 0})

    return responses

def generate(prompt, model, tokenizer):
    # pdb.set_trace()
    input_ids = tokenizer(prompt, return_tensors="pt", padding=True).input_ids.to(model.device)
    outputs = model.generate(input_ids, max_new_tokens=100)
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)

def write_jsonl(responses, output_json):
    with open(output_json, 'w') as file:
        for item in responses:
            json.dump(item, file)
            file.write('\n')
            
def write_csv(responses, output_csv):
    responses = pd.DataFrame(responses)
    responses.to_csv(output_csv, index=False)

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bs', type=int)
    parser.add_argument('--model_path')
    args = parser.parse_args()
    bs = args.bs
    model_path = args.model_path
    return bs, model_path

if __name__ == '__main__':

    # pdb.set_trace()
    bs, pretrained_path = argparser()

    folder_path = "ZIQI-fiveshot/test"
    file_list = os.listdir(folder_path)
    input_csvs = []
    for file_name in file_list:
        if file_name.endswith(".csv"): 
            file_path = os.path.join(folder_path, file_name)  
            input_csvs.append(file_path)

    folder_path = 'evaluations/' 
    output_csv = folder_path + '{}-fiveshot.csv'.format(pretrained_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    model = AutoModelForCausalLM.from_pretrained(
        pretrained_path,
        device_map='auto',
        trust_remote_code=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(
        pretrained_path,
        device_map='auto',
        padding_side='left',
        trust_remote_code=True,
    )
    # tokenizer.pad_token_id = tokenizer.eod_id
    tokenizer.pad_token_id = tokenizer.eos_token_id

    accdict = {}
    accdict['model'] = pretrained_path
    anums = tots = 0
    responsess = []
    for input_csv in input_csvs:
        theme = input_csv.split("/")[-1].split(".")[0]
        responses = process_csv(input_csv, output_csv, model, tokenizer, theme)
        responsess.extend(responses)
        anum = tot = 0
        for response in responses:
            tot += 1
            if response['match'] == 1:
                anum += 1
        acc = anum/tot
        anums += anum
        tots += tot
        accdict[theme] = acc
        # write_jsonl(responsess, output_json=output_json)
        write_csv(responsess, output_csv)

    # write_jsonl(responsess, output_json=output_json)
    write_csv(responsess, output_csv)
    accdict['all'] = anums/tots
    print(output_csv)
    print(accdict)
    result_path = folder_path + '{}-fiveshot-results.json'.format(pretrained_path)
    with open(result_path, "w") as json_file:
        json.dump(accdict, json_file)