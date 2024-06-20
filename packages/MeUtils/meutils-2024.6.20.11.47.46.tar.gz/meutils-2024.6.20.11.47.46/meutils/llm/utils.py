#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : utils
# @Time         : 2024/6/20 09:08
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.pipe import *

messages = [
    {"role": "system", "content": "U1"},
    {"role": "user", "content": "U1"},
    {"role": "assistant", "content": "A1"},
    {"role": "user", "content": "U2"},
    {"role": "assistant", "content": "A2"},
]


# 多轮对话合并
# user_prompt = "<|User|>:{user}<eoh>\n"
# robot_prompt = "<|Bot|>:{robot}<eoa>\n"
# cur_query_prompt = "<|User|>:{user}<eoh>\n<|Bot|>:"
#
#
# def combine_history(prompt):
#     messages = st.session_state.messages
#     total_prompt = ""
#     for message in messages:
#         cur_content = message["content"]
#         if message["role"] == "user":
#             cur_prompt = user_prompt.replace("{user}", cur_content)
#         elif message["role"] == "robot":
#             cur_prompt = robot_prompt.replace("{robot}", cur_content)
#         else:
#             raise RuntimeError
#         total_prompt += cur_prompt
#     total_prompt = total_prompt + cur_query_prompt.replace("{user}", prompt)
#     return total_prompt

def oneturn2multiturn(messages, template: Optional[str] = None):
    """todo: https://github.com/hiyouga/LLaMA-Factory/blob/e898fabbe3efcd8b44d0e119e7afaed4542a9f39/src/llmtuner/data/template.py#L423-L427

    _register_template(
    name="qwen",
    format_user=StringFormatter(slots=["<|im_start|>user\n{{content}}<|im_end|>\n<|im_start|>assistant\n"]),
    format_system=StringFormatter(slots=["<|im_start|>system\n{{content}}<|im_end|>\n"]),
    format_observation=StringFormatter(slots=["<|im_start|>tool\n{{content}}<|im_end|>\n<|im_start|>assistant\n"]),
    format_separator=EmptyFormatter(slots=["\n"]),
    default_system="You are a helpful assistant.",
    stop_words=["<|im_end|>"],
    replace_eos=True,
)
    :return:
    """
    # from jinja2 import Template, Environment, PackageLoader, FileSystemLoader
    #
    # system_template = Template("<|im_start|>system\n{{content}}<|im_end|>\n")  # .render(content='xxxx')
    # user_template = Template("<|im_start|>user\n{{content}}<|im_end|>\n")  # 最后<|im_start|>assistant\n
    # assistant_template = Template("<|im_start|>assistant\n{{content}}<|im_end|>\n")

    # todo: [{"type": "image_url", "image_url": {"url": ""}}]] 单独处理
    # 混元不是很感冒
    # context = "\n"
    # for message in messages:
    #     role, content = message.get("role"), message.get("content")
    #     context += f"<|im_start|>{role}\n{content}<|im_end|>\n"
    # context += "<|im_start|>assistant\n"

    context = "\n"
    for message in messages:
        role, content = message.get("role"), message.get("content")
        context += f"{role}:\n{content}\n"
    context += "assistant:\n"
    return context
