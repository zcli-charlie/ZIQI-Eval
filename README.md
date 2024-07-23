# ZIQI-Eval: A Music Evaluation Benchmark for Large Language Models


<h4 align="center">
    <p>
        <b>简体中文</b> |
        <a href="https://github.com/zcli-charlie/ZIQI-Eval/blob/main/README_EN.md">English</a> 
    <p>
</h4>

<p align="center" style="display: flex; flex-direction: row; justify-content: center; align-items: center">
📄 <a href="https://arxiv.org/abs/xxx" target="_blank" style="margin-right: 15px; margin-left: 10px">论文</a> •
🏆 <a href="#排行榜" target="_blank"  style="margin-left: 10px">排行榜</a> • 
🤗 <a href="https://huggingface.co/datasets/MYTH-Lab/ZIQI-Eval" target="_blank" style="margin-left: 10px">数据集</a>
</p>


## 简介
ZIQI-Eval是一个评估大语言模型综合音乐能力的测试基准，旨在填补当前LLM音乐能力评估的空白,为全面评估LLM的能力提供新的维度。
数据集包括两部分:音乐理解题库和音乐生成题库。
音乐理解题库以多选题形式呈现，涵盖10大类56个子类，共14244条数据条目。其中不仅包括音乐表演、作曲理论、世界民族音乐等传统分类，还涵盖流行音乐、西方音乐史、中国音乐史、中国传统音乐、音乐美学、音乐教育等内容。题目涉及流行音乐、摇滚音乐、节奏布鲁斯等各类型，并采用去中心化的设计理念，全面展现了全球音乐文化的多样性和包容性。
音乐生成题库包括200个问题,测试模型的音乐延续能力。考虑到音乐生成结果评估的困难性,这部分也采用多选题的形式。
特别地，我们还关注了大语言模型在黑人音乐、女性作曲家和欧洲地域中心化这三方面是否存在偏见。


## 排行榜

以下表格显示了模型在 zero-shot 和 five-shot 下的表现。如果您想贡献您的模型结果，请与我们联系或直接提交拉取请求。

### Zero-shot


| 模型                                                                          | 作曲理论  | 世界民族音乐 | 流行音乐 | 西方音乐史 | 中国音乐史 | 中国传统音乐 | 音乐美学 | 音乐教育 | 音乐表演 | 女性音乐 | 平均分 |
|-------------------------------------------------------------------------------|--------|-----------|--------|---------|---------|-----------|-------|-------|-------|-------|-------|
| GPT4 (gpt-4)                                                                  | 50.00  | 64.80     | 89.15  | 77.51   | 55.33   | 55.57     | 38.92 | 73.35 | 67.23 | 66.67 | 62.93 |
| ChatGPT (gpt-3.5-turbo)                                                       | 34.36  | 50.14     | 67.49  | 49.04   | 36.22   | 37.70     | 38.67 | 47.30 | 48.61 | 42.48 | 44.86 |
| [ChatMusician-Base](https://github.com/hf-lin/ChatMusician)                   | 22.40  | 21.94     | 25.02  | 26.26   | 25.19   | 25.63     | 31.31 | 23.45 | 22.52 | 33.43 | 24.61 |
| [ChatGLM2-6B](https://github.com/THUDM/ChatGLM2-6B)                           | 18.08  | 24.77     | 32.43  | 21.40   | 24.10   | 26.35     | 16.47 | 25.55 | 26.72 | 19.47 | 24.12 |
| [Ziya-LLaMA-13B-v1.1](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1.1)   | 27.21  | 25.15     | 21.84  | 22.09   | 23.29   | 26.11     | 19.91 | 23.62 | 22.52 | 22.09 | 23.69 |
| [Qwen-7B-base](https://github.com/QwenLM/Qwen)                                | 18.97  | 19.61     | 24.71  | 19.28   | 19.83   | 19.46     | 17.78 | 21.68 | 22.40 | 24.48 | 20.36 |
| [Qwen-14B-Base](https://github.com/QwenLM/Qwen)                               | 15.28  | 24.04     | 25.79  | 16.34   | 16.19   | 17.67     | 18.39 | 20.32 | 18.28 | 20.90 | 18.90 |
| [XVERSE-13B](https://github.com/xverse-ai/XVERSE-13B)                         | 12.79  | 16.84     | 19.29  | 23.57   | 17.17   | 16.93     | 19.91 | 21.00 | 18.89 | 20.90 | 18.38 |
| [XVERSE-7B](https://github.com/xverse-ai/XVERSE-7B)                           | 12.79  | 12.35     | 16.81  | 19.06   | 17.40   | 16.35     | 12.92 | 15.83 | 16.22 | 13.73 | 15.75 |
| [Baichuan2-7B-Base](https://github.com/baichuan-inc/Baichuan2)                | 9.36   | 11.41     | 13.63  | 12.85   | 11.55   | 11.29     | 11.70 | 12.53 | 13.44 | 10.15 | 11.79 |
| [Baichuan-13B-Base](https://github.com/baichuan-inc/Baichuan-13B)             | 9.70   | 11.30     | 15.65  | 10.26   | 12.42   | 10.60     | 9.27  | 14.39 | 8.84  | 11.94 | 11.46 |
| [InternLM-7B](https://github.com/InternLM/InternLM)                           | 8.67   | 8.09      | 9.99   | 10.34   | 6.31    | 7.44      | 6.08  | 9.57  | 7.38  | 5.97  | 8.22  |
| [InternLM-20B](https://github.com/InternLM/InternLM)                          | 6.78   | 6.20      | 12.86  | 9.19    | 5.47    | 6.59      | 7.45  | 4.40  | 7.75  | 9.25  | 7.43  |
| [Baichuan-7B-Base](https://github.com/baichuan-inc/Baichuan-7B)               | 7.64   | 6.15      | 10.53  | 7.02    | 6.31    | 6.86      | 5.93  | 5.25  | 7.02  | 7.46  | 6.90  |
| [Baichuan2-13B-Base](https://github.com/baichuan-inc/Baichuan2)               | 6.27   | 3.49      | 8.60   | 6.51    | 5.47    | 3.59      | 3.80  | 3.47  | 3.87  | 8.96  | 5.23  |
| [educhat-base-002-13B](https://github.com/icalk-nlp/EduChat)                  | 0.00   | 0.00      | 0.00   | 0.00    | 0.00    | 0.00      | 0.00  | 0.00  | 0.00  | 0.00  | 0.00  |




| 模型                                                                          | 作曲理论  | 世界民族音乐 | 流行音乐 | 西方音乐史 | 中国音乐史 | 中国传统音乐 | 音乐美学 | 音乐教育 | 音乐表演 | 女性音乐 | 平均分 |
|-------------------------------------------------------------------------------|-------|---------|---------|-------|-------|-------|---------|---------|-------|-------|-------|
| GPT4 (gpt-4)                                                                  | 62.93 | 65.19  | 75.97   | 78.57 | 57.44 | 63.16 | 56.06   | 77.12   | 76.83 | 60.61 | 67.27 |
| ChatGPT (gpt-3.5-turbo)                                                       | 37.07 | 53.59   | 66.67   | 47.62 | 34.2  | 39.47 | 46.97   | 55.93   | 53.66 | 33.33 | 45.64 |
| [ChatGLM2-6B](https://github.com/THUDM/ChatGLM2-6B)                           | 18.10 | 16.57   | 27.13   | 30.00 | 24.57 | 28.42 | 36.36   | 31.36   | 28.05 | 33.33 | 26.10 |
| [XVERSE-13B](https://github.com/xverse-ai/XVERSE-13B)                         | 20.00 | 19.28   | 20.84   | 24.00 | 16.19 | 23.36 | 19.15   | 22.27   | 15.86 | 7.16  | 19.72 |
| [Ziya-LLaMA-13B-v1.1](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1.1)   | 26.44 | 25.26   | 17.35   | 22.85 | 23.82 | 20.68 | 20.67   | 27.52   | 24.58 | 19.70 | 22.84 |
| [Qwen-14B-Base](https://github.com/QwenLM/Qwen)                               | 13.13 | 16.34   | 15.34   | 17.79 | 24.73 | 19.25 | 17.02   | 14.65   | 14.04 | 15.82 | 17.68 |
| [Baichuan2-7B-Base](https://github.com/baichuan-inc/Baichuan2)                | 7.98  | 6.81    | 12.01   | 7.83  | 11.59 | 9.86  | 9.88    | 9.14    | 12.35 | 9.25  | 9.48  |
| [XVERSE-7B](https://github.com/xverse-ai/XVERSE-7B)                           | 16.39 | 3.77    | 8.91    | 15.19 | 2.77  | 16.67 | 17.02   | 7.03    | 14.16 | 6.57  | 10.14 |
| [Baichuan2-13B-Base](https://github.com/baichuan-inc/Baichuan2)               | 6.44  | 6.87    | 12.39   | 7.79  | 9.80  | 6.59  | 6.69    | 7.87    | 8.23  | 5.37  | 8.01  |
| [InternLM-20B](https://github.com/InternLM/InternLM)                          | 3.35  | 12.63   | 10.07   | 6.64  | 4.41  | 9.34  | 5.47    | 4.91    | 19.25 | 16.42 | 8.06  |
| [InternLM-7B](https://github.com/InternLM/InternLM)                           | 6.52  | 6.81    | 11.93   | 6.09  | 6.53  | 6.49  | 9.12    | 6.86    | 9.20  | 8.06  | 7.22  |
| [Baichuan-13B-Base](https://github.com/baichuan-inc/Baichuan-13B)             | 5.92  | 4.93    | 9.22    | 5.32  | 5.28  | 6.22  | 6.23    | 5.67    | 5.81  | 6.57  | 5.84  |
| [Baichuan-7B-Base](https://github.com/baichuan-inc/Baichuan-7B)               | 7.21  | 4.99    | 8.37    | 4.64  | 5.09  | 4.43  | 6.23    | 6.18    | 6.30  | 6.87  | 5.60  |
| [Qwen-7B-Base](https://github.com/QwenLM/Qwen)                                | 5.41  | 6.20    | 5.89    | 5.57  | 5.05  | 4.96  | 6.53    | 5.67    | 4.96  | 5.97  | 5.48  |
| [ChatMusician](https://github.com/hf-lin/ChatMusician)                        | 2.32  | 4.88    | 2.01    | 5.40  | 4.14  | 4.85  | 1.22    | 6.52    | 3.39  | 4.48  | 4.16  |
| [educhat-base-002-13B](https://github.com/icalk-nlp/EduChat)                  | 0.00  | 0.00    | 0.00    | 0.00  | 0.00  | 0.00  | 0.00    | 0.00    | 0.00  | 0.00  | 0.00  |




## 数据示例

数据集内的每个问题均为四选一的选择题，其中仅有一个选项为正确答案。数据采用逗号分隔，并保存为.csv文件格式。以下是数据样例：

```bash
# 西方音乐史
问题: 迪斯康特声部附加在格里高利圣咏的（ ）。
A.上方
B.下方
C.上下方皆有
D.与奥尔加农声部相同
答案: A

# 中国音乐史
问题: 《阳关三叠》是现存唐诗与音乐巧妙融合的典范，源于唐朝诗人王维的七言律诗《送元二使安西》。全诗纯净秀美，满怀依依惜别之情；唐宋时用一个曲调变化反复，叠唱三次，故称“三叠”。歌曲情深意切地表达了对即将远行友人的无限关怀和诚挚的感情。这种我国古代诗歌与音乐结合的活化石，音乐类型被称作____。
A.琴歌 
B.京韵大鼓
C.山东琴书
D.四川清音
答案: A

# 中国民族民间音乐
问题: 十二木卡姆已被列入联合国教科文组织非物质文化遗产名录，它是属于____。
A.新疆维吾尔族
B.藏族
C.苗族
D.满族
答案: A

```

## 使用方法

要在您的项目中使用我们的代码，请将存储库克隆到本地计算机：

```bash
git clone https://github.com/zcli-charlie/ZIQI-Eval.git
cd ZIQI-Eval/src
```

## 数据

我们根据每个评测维度在 data/dev 和 data/test 目录中提供了开发和测试数据集。

## 引用

```
@misc{li2023ziqieval,
      title={ZIQI-Eval: A Library and Information Science Benchmark for Large Language Models}, 
      author={XXXXX},
      year={2024},
      eprint={xxx},
      archivePrefix={xxxx},
      primaryClass={cs.CL}
}
```
## 许可证

ZIQI-Eval数据集采用
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).
