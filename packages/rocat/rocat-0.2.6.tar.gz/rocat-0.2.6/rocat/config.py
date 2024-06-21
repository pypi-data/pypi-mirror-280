# rocat/config.py
import configparser
import os

_config_instance = None

def load_config(config_file="config.ini"):
    """ 
    설정 파일을 로드하고, 설정 인스턴스를 반환합니다.
    
    Args:
        config_file (str): 설정 파일의 경로. 기본값은 "config.ini"입니다.
    
    Returns:
        ConfigParser: 설정 인스턴스. 에러 발생 시 None을 반환합니다.
    """
    global _config_instance
    if _config_instance is None:
        _config_instance = configparser.ConfigParser()
        try:
            _config_instance.read(config_file)
        except Exception as e:
            print(f"Error loading config file: {e}")
            _config_instance = None
    return _config_instance

def get_api_key(service_name):
    """
    지정된 서비스 이름에 대한 API 키를 설정에서 가져옵니다.
    
    Args:
        service_name (str): 서비스 이름.
    
    Returns:
        str: API 키. 환경변수에서 가져오며, 설정 파일에도 없을 경우 빈 문자열을 반환합니다.
    """
    env_var_name = f"{service_name.upper()}_API_KEY"
    api_key = os.getenv(env_var_name)
    
    if not api_key:
        config = load_config()
        if config and "API_KEYS" in config:
            if service_name in ["openai", "anthropic", "serpapi", "naver_clovastudio", "naver_apigw"]:
                return config["API_KEYS"].get(service_name, "")
    return api_key or ""

def save_config(config, config_file="config.ini"):
    """ 
    주어진 설정 객체를 파일에 저장합니다.
    
    Args:
        config (ConfigParser): 설정 객체.
        config_file (str): 설정 파일의 경로. 기본값은 "config.ini"입니다.
    """
    try:
        with open(config_file, "w") as file:
            config.write(file)
    except Exception as e:
        print(f"Error saving config file: {e}")

def create_default_config(config_file="config.ini"):
    """ 
    기본 설정 파일을 생성합니다.
    
    Args:
        config_file (str): 설정 파일의 경로. 기본값은 "config.ini"입니다.
    """
    config = configparser.ConfigParser()
    config["API_KEYS"] = {
        "openai": "",
        "anthropic": "",
        "serpapi": "",
        "naver_clovastudio": "",
        "naver_apigw": ""  
    }
    save_config(config, config_file)