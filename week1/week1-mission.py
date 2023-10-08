# +
# Week1 Q1
# -

question = ['Q2', 'Q3', 'Q4', 'Q5', 'Q6_1', 'Q6_2', 'Q6_3', 'Q6_4', 'Q6_5', 'Q6_6',
       'Q6_7', 'Q6_8', 'Q6_9', 'Q6_10', 'Q6_11', 'Q6_12', 'Q7_1', 'Q7_2',
       'Q7_3', 'Q7_4', 'Q7_5', 'Q7_6', 'Q7_7', 'Q8', 'Q9', 'Q10_1', 'Q10_2',
       'Q10_3']

# +
single_choice_list = []

for single_choice in question:
    if len(single_choice) == 2:
        single_choice_list.append(single_choice)

single_choice_list

# +
# Week1 Q2

# +
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/healthexp.csv")
df
# -

country_list = pd.pivot_table(df[214:], values="Life_Expectancy", index = "Year", columns = "Country")
country_list

# +
# Week1 Q3
# -

# # 1. 데이터 분석 환경 구성
#
# ## 1.1 무엇을 분석할 것인가? 데이터 분석을 위한 환경 만들기
#
# ## 1.2 아나콘다 소개 및 주피터 노트북 사용법
#
# ### 1) 아나콘다 설치
#
# - 아나콘다 공식 사이트에서 설치
#     
#     [Free Download | Anaconda](https://www.anaconda.com/download)
#
# ⇒ 설치 완료되면 응용 프로그램이 생성됨
#
# - 아나콘다에서 주피터 노트북 실행
#     - Launch 버튼 누르면 주피터 노트북 실행
#     - 온라인에서 주피터 노트북 실행
#
# ### 2) 주피터 노트북 활용
#
# - /(root)/DateScience 디렉토리 생성
#     - 주차마다 디렉토리 생성
#     
#
# ### 3) 실습: 주피터 노트북 사용법 및 마크다운
#
# - ***마크다운 코드***
#     
#     ```markdown
#     # 주피터 노트북 사용법
#     * Shift + Enter 키를 누르면 셀이 실행되고 커서가 다음 셀로 이동함
#     * Enter 키를 누르면 다시 편집상태로 돌아옴
#     * ESC 키를 누르고
#         * a 키를 누르면 위에 셀이 추가됨
#         * b 키를 누르면 아래에 셀이 추가됨
#         * dd 키를 누르면 셀이 삭제됨
#         * m 키를 누르면 문서 셀로 변경됨
#         * y 키를 누르면 코드 셀로 변경됨
#         
#     ## 마크다운이란
#     * 코드와 함께 문서화할 수 있음
#     * 문서화할 수 있는 `문법`
#     
#     ```
#     여러 줄의 설명을 
#     줄바꿈으로 쓰고자 할 때
#     ```
#     ```
#     
# - ***파이썬 코드***
#     
#     ```python
#     print("Hello World!")
#     ```
#     
#     ```python
#     a = 1
#     b = 2
#     a + b
#     ```
#     
#     
#     ```python
#     for i in range(10000):
#         print(i)
#     ```
#     
#
# ### 4) 라이브러리 설치
#
# - Nbextension : 마크다운에서 목차 번호가 자동으로 생성되는 라이브러리
#
# - !로 명령어 수행
#     
#     ```python
#     # !pip install jupyter_nbextensions_configurator jupyter_contrib_nbextensions
#     # !jupyter contrib nbextension install --user
#     # !jupyter nbextensions_configurator enable --user
#     ```
#     
#     ⇒ 실행 결과 : Nbextensions 탭 생성
#     
# - 주피터 노트북 다시 실행 후 라이브러리 추가 설정하기
#     - Jupytext : .ipynb 파일과 .py 파일을 자동으로 만드는 라이브러리
#     - Table of Contents : 마크다운에 목차 번호가 자동으로 생성되는 라이브러리
#     
#
# ### 5) 깃허브 연동
#
# - jupytext 설치
#     
#     ```markdown
#     pip install jupytext
#     ```
#     
#
# - config 파일 생성
#     
#     ```markdown
#     jupyter notebook --generate-config
#     ```
#     
# - config 파일 설정 변경 - vi 에디터로 config 파일을 열기
#     
#     ```markdown
#     sudo vi /경로/jupyter_notebook_config.py
#     ```
#     
#
# - c.NotebookApp.contents_manager_class 검색해(/ 입력) 설정 변경하기
#     
#     ```markdown
#     c.NotebookApp.contents_manager_class = 'jupytext.TextFileContentsManager'
#     ```
#     
#     - `i` 입력
#     - `:wq` vi 에디터 나오기
#     
#     ⇒ 실행 결과 : ipynb를 저장할때 py파일도 함께 생성됨
#
# - 내 컴퓨터에 로컬 저장소 만들기 → 아나콘다를 통해 로컬 저장소 경로 설정 완료
#
# - git config 설정하기
#     
#     ```markdown
#     git config --global user.name "깃허브 아이디"
#     ```
#     
#
# - git init
#     
#     ```markdown
#     git init
#     ```
#     
#
# - 깃허브에서 레파지토리 생성하기
#
# - 로컬 저장소와 깃허브 레파지토리 연결하기
#     
#     ```markdown
#     git remote add origin 레파지토리 주소
#     ```
#     
# - git ignore 설정
#     - .gitignore 파일 생성 후 깃허브에 업로드하고 싶지 않은 확장자명 작성
#         
#     - git add .
#     - git commit -m “커밋 메시지 작성”
#     - git push origin master
#
# - 로컬 저장소 master 브랜치와 깃허브 레파지토리 브랜치 main 충돌 발생
#     - 다음 코드로 문제 해결
#     
#     ```markdown
#     git branch main master -f
#     git checkout main
#     git push origin main -f
#     ```


