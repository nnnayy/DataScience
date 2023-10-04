# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # 주피터 노트북 사용법
# * Shift + Enter 키를 누르면 셀이 실행되고 커서가 다음 셀로 이동함
# * Enter 키를 누르면 다시 편집상태로 돌아옴
# * ESC 키를 누르고
#     * a 키를 누르면 위에 셀이 추가됨
#     * b 키를 누르면 아래에 셀이 추가됨
#     * dd 키를 누르면 셀이 삭제됨
#     * m 키를 누르면 문서 셀로 변경됨
#     * y 키를 누르면 코드 셀로 변경됨
#     
# ## 마크다운이란
# * 코드와 함께 문서화할 수 있음
# * 문서화할 수 있는 `문법`
#
# ```
# 여러 줄의 설명을 
# 줄바꿈으로 쓰고자 할 때
# ```

print("Hello World!")

a = 1
b = 2
a + b

for i in range(10000):
    print(i)

# !pip install jupyter_nbextensions_configurator jupyter_contrib_nbextensions
# !jupyter contrib nbextension install --user
# !jupyter nbextensions_configurator enable --user


