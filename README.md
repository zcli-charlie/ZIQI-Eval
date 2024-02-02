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
🤗 <a href="https://huggingface.co/datasets/myth/ZIQI-Eval" target="_blank" style="margin-left: 10px">数据集</a>
</p>


## 简介





## 排行榜

以下表格显示了模型在 zero-shot 和 five-shot 下的表现。如果您想贡献您的模型结果，请与我们联系或直接提交拉取请求。

### Zero-shot


| 模型                                                                          | 作曲理论  | 世界民族音乐 | 流行音乐 | 西方音乐史 | 中国音乐史 | 中国传统音乐 | 音乐美学 | 音乐教育 | 音乐表演 | 女性音乐 | 平均分 |
|-------------------------------------------------------------------------------|-------|---------|---------|-------|-------|-------|---------|---------|-------|-------|-------|
| GPT4 (gpt-4-0613)                                                             | 
| [Qwen-14B](https://github.com/QwenLM/Qwen)                                    | 
| [Baichuan2-13B](https://github.com/baichuan-inc/Baichuan2)                    | 
| [XVERSE-7B](https://github.com/xverse-ai/XVERSE-7B)                           | 
| [Qwen-7B](https://github.com/QwenLM/Qwen)                                     | 
| ChatGPT (gpt-3.5-turbo)                                                       | 
| [InternLM-20B](https://github.com/InternLM/InternLM)                          | 
| [Baichuan2-7B](https://github.com/baichuan-inc/Baichuan2)                     | 
| [Baichuan-13B](https://github.com/baichuan-inc/Baichuan-13B)                  | 
| [XVERSE-13B](https://github.com/xverse-ai/XVERSE-13B)                         | 
| [InternLM-7B](https://github.com/InternLM/InternLM)                           | 
| [ChatGLM2-6B](https://github.com/THUDM/ChatGLM2-6B)                           | 
| [educhat-base-002-13b](https://github.com/icalk-nlp/EduChat)                  | 
| [Baichuan-7B](https://github.com/baichuan-inc/Baichuan-7B)                    | 
| [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)                             | 
| [Ziya-LLaMA-13B-v1.1](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1.1)   | 


### Five-shot

| 模型                                                                          | 作曲理论  | 世界民族音乐 | 流行音乐 | 西方音乐史 | 中国音乐史 | 中国传统音乐 | 音乐美学 | 音乐教育 | 音乐表演 | 女性音乐 | 平均分 |
|-------------------------------------------------------------------------------|-------|---------|---------|-------|-------|-------|---------|---------|-------|-------|-------|
| GPT4 (gpt-4-0613)                                                             | 
| [Qwen-14B](https://github.com/QwenLM/Qwen)                                    | 
| [Baichuan2-13B](https://github.com/baichuan-inc/Baichuan2)                    | 
| [XVERSE-7B](https://github.com/xverse-ai/XVERSE-7B)                           |
| [XVERSE-13B](https://github.com/xverse-ai/XVERSE-13B)                         | 
| [Qwen-7B](https://github.com/QwenLM/Qwen)                                     | 
| [Baichuan2-7B](https://github.com/baichuan-inc/Baichuan2)                     | 
| ChatGPT (gpt-3.5-turbo)                                                       | 
| [Baichuan-13B](https://github.com/baichuan-inc/Baichuan-13B)                  | 
| [InternLM-20B](https://github.com/InternLM/InternLM)                          | 
| [InternLM-7B](https://github.com/InternLM/InternLM)                           | 
| [ChatGLM2-6B](https://github.com/THUDM/ChatGLM2-6B)                           | 
| [Baichuan-7B](https://github.com/baichuan-inc/Baichuan-7B)                    | 
| [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)                             | 



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
      author={Jiajia Li and Lu Yang and Mingni Tang and Cong Chen and Zuchao Li* and Ping Wang*},
      year={2024},
      eprint={xxx},
      archivePrefix={xxxx},
      primaryClass={cs.CL}
}
```
## 许可证

ZIQI-Eval数据集采用
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).
