# rocat/language_model.py

from openai import OpenAI
from rocat.config import get_api_key
import requests
import json
import uuid
import anthropic
from .config import get_api_key
from .language_utils import _convert_language_code

MODEL_MAP = {
    "gpt3": "gpt-3.5-turbo",
    "gpt4o": "gpt-4o",
    "opus": "claude-3-opus-20240229",
    "haiku": "claude-3-haiku-20240307",
    "sonnet": "claude-3-sonnet-20240229",
    "clova": "HCX-003"
}

def run_model(model, prompt, system_prompt="", temperature=0.7, top_p=1, max_tokens=1024, output="default", lang="", tools=[]):
    """
    주어진 모델을 사용하여 프롬프트에 대한 응답을 생성합니다.
    
    Parameters:
        model (str): 사용할 모델의 이름.
        prompt (str or list): 모델에 입력할 프롬프트. 문자열 또는 리스트 형태로 전달 가능.
        system_prompt (str): 시스템 프롬프트, 대화의 맥락을 설정하는 데 사용됩니다 (옵션).
        temperature (float): 생성의 무작위성을 결정하는 값.
        top_p (float): 토큰 확률의 누적 분포 임곗값.
        max_tokens (int): 생성할 최대 토큰 수.
        output (str): 응답의 출력 형식 (default, word, sentence, bullet, json).
        lang (str): 응답 언어 코드 (ISO 639-1).
        tools (list): 사용할 도구 목록.
    
    Returns:
        list: 생성된 메시지 리스트 (각 메시지는 {"role": "user" 또는 "assistant", "content": 메시지 내용} 형태의 딕셔너리).
    """
    full_model_name = MODEL_MAP.get(model.lower())
    if not full_model_name:
        raise ValueError(f"Unknown model: {model}")
    
    messages = [{"role": "system", "content": system_prompt}] if system_prompt else []
    
    if isinstance(prompt, str):
        messages.append({"role": "user", "content": prompt})
    elif isinstance(prompt, list):
        for i, p in enumerate(prompt):
            role = "user" if i % 2 == 0 else "assistant"
            messages.append({"role": role, "content": p})
    else:
        raise ValueError("prompt should be either a string or a list")
    
    if "gpt" in model.lower():
        messages = _run_openai(full_model_name, messages, temperature, top_p, max_tokens)
    elif "claude" in full_model_name or "opus" in full_model_name or "haiku" in full_model_name or "sonnet" in full_model_name:
        messages = _run_anthropic(full_model_name, messages, temperature, top_p, max_tokens, output, lang, tools)
    elif "clova" in model.lower():
        messages = _run_clova(full_model_name, messages, temperature, top_p, max_tokens)
    else:
        raise ValueError(f"Unknown model: {model}")

    return messages[-1]["content"]

def _run_openai(model, messages, temperature=0.7, top_p=1, max_tokens=1024):
    key = get_api_key("openai")
    client = OpenAI(api_key=key)
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens
    )
    
    messages.append({"role": "assistant", "content": response.choices[0].message.content})
    
    return messages


def _run_anthropic(model_name, messages, temperature=0.7, top_p=1, max_tokens=1024, output="default", lang="", tools=[]):
    key = get_api_key("anthropic")
    anth_client = anthropic.Anthropic(api_key=key)
    output_format = {
        "default": "",
        "word": " Don't explain, keep your output to very short one word.",
        "sentence": " Keep your output to very short one sentence.",
        "bullet": " Don't explain, keep your output in bullet points. Don't say anything else.",
        "json": " Don't explain, keep your output in json format. Don't say anything else."
    }
    lang_output = ""
    if lang:
        language = _convert_language_code(lang)
        if language is not None:
            lang_output = f" Please Write in {language} without any additional explanations."

    system_prompt = messages[0]["content"] if messages and messages[0]["role"] == "system" else ""
    system_prompt += output_format.get(output, "") + lang_output

    if system_prompt:
        messages = messages[1:]  # Remove the system message from the messages list

    response = anth_client.messages.create(
        model=model_name,
        max_tokens=max_tokens,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        system=system_prompt  # Pass the system prompt as a separate parameter
    )
    content = response.content
    messages.append({"role": "assistant", "content": "\n".join([block.text for block in content if hasattr(block, 'text')])})

    return messages


def _run_clova(model, messages, temperature=0.7, top_p=0.8, max_tokens=256):
    host = 'https://clovastudio.stream.ntruss.com'
    
    api_key = get_api_key("naver_clovastudio")
    api_key_primary_val = get_api_key("naver_apigw")
    
    request_id = str(uuid.uuid4())

    headers = {
        'X-NCP-CLOVASTUDIO-API-KEY': api_key,
        'X-NCP-APIGW-API-KEY': api_key_primary_val,
        'X-NCP-CLOVASTUDIO-REQUEST-ID': request_id,
        'Content-Type': 'application/json; charset=utf-8',
        'Accept': 'text/event-stream'
    }

    request_data = {
        'messages': messages,
        'topP': top_p,
        'topK': 0,
        'maxTokens': max_tokens,
        'temperature': temperature,
        'repeatPenalty': 5.0,
        'stopBefore': [],
        'includeAiFilters': True,
        'seed': 0
    }

    with requests.post(host + f'/testapp/v1/chat-completions/{model}',
                       headers=headers, json=request_data, stream=True) as r:
        content = ""
        for line in r.iter_lines():
            if line:
                decoded_line = line.decode("utf-8")
                if "data:" in decoded_line:
                    _, data = decoded_line.split("data:")
                    data = data.strip()
                    if data != "[DONE]":
                        event_data = json.loads(data)
                        if "message" in event_data:
                            content += event_data["message"]["content"]
        messages.append({"role": "assistant", "content": content.strip()})
        
    return messages