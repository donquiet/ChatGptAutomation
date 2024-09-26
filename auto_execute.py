import os

def save_and_execute_code(code):
    file_name = "generated_script.py"
    
    # 생성된 코드를 파일로 저장
    with open(file_name, 'w') as file:
        file.write(code)
    
    # 저장된 Python 파일을 python3로 실행
    os.system(f"python3 {file_name}")

# 예시 코드 (여기서 챗GPT가 생성한 코드를 받아옴)
generated_code = """
def hello_world():
    print('Hello, World!')

hello_world()
"""

# 코드 저장 및 실행
save_and_execute_code(generated_code)