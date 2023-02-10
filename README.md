# rs - study

---

ECONOVATION에서 코딩테스트를 준비하는 학생들이 모인 스터디 rs-study 입니다.  

스터디를 함께하는 사람들 : 김가연, 이승건 ,이시현, 임수미, 장현지, 황대선   

- 자료구조/알고리즘 이론 공부  
  - 누구나 자료 구조와 알고리즘   
- 코딩테스트 문제 풀이
  - code-up
  - 이것이 취업을 위한 코딩테스트다 with 파이썬

<br>

# Rule 

---

- 스터디 진행 전에 답안을 확인하지 말 것
  - 만약, 답안을 확인한다면 스터디 이후에 확인할 것
- 스터디 결과로 나오는 산출물은 아래와 같습니다.
  - 자료구조/알고리즘 이론 공부 : 해당 주차의 공부 내역을 md 파일로 업로드할 것
  - 코딩 테스트 문제 풀이 : .py
- 스터디 진행 일정 : 매주 금요일 오전 10시   


<br>

#  교재 스터디 진행 방법

---

1. 프로젝트를 자신의 계정으로 fork합니다
   - fork는 알고리즘 스터디 저장소를 자신의 계정으로 복사하는 기능입니다.   

<img width="1414" alt="1" src="https://user-images.githubusercontent.com/91835827/218129133-6f00f501-6d2d-4e5a-ace4-a242ac4df002.png">

2. fork한 저장소를 자신의 컴퓨터로 clone하고 폴더로 이동합니다.
   - clone 명령은 github.com에 존재하는 저장소를 자신의 노트북 또는 PC로 복사하는 과정입니다.
   

   `git clone https://github.com/{본인 아이디}/{저장소 아이디}.git`

<img width="648" alt="2" src="https://user-images.githubusercontent.com/91835827/218129329-7d4506f8-ba16-4809-8796-44bebf3ef959.png">


3. 자신의 브랜치를 생성하고 이동합니다.  

`   git checkout -b {본인 아이디}` 

<img width="655" alt="3" src="https://user-images.githubusercontent.com/91835827/218129398-4dd44ae7-a47d-4896-a92c-ac8c745b0969.png">


4. JNU-econovation/rs-study/ 디렉토리 아래에 현재 진행중인 책의 제목에 맞는 패키지를 선택하신 후, 패키지 아래에 본인 깃허브 아이디에 맞는 폴더를 만들어주세요. 그 아래에 현재 진행중인 n주차 폴더를 만드신 후 결과물들을 넣어주세요.   

    - JNU-econovation/rs-study/nuguna/{본인 아이디}/n주차/정리.md
    - JNU-econovation/rs-study/code-up/{본인 아이디}/n주차/과자만들기.py   

<img width="652" alt="4" src="https://user-images.githubusercontent.com/91835827/218129526-55261a1b-4398-49e8-ad02-93d49b069b26.png">
<img width="876" alt="5" src="https://user-images.githubusercontent.com/91835827/218129616-b4372e91-60be-4fa9-b3a9-7365a5a5a78a.png">
<img width="1440" alt="6" src="https://user-images.githubusercontent.com/91835827/218129711-5c92a345-1ffc-4691-942e-1270303b5ec7.png">


5. 기능 구현 후 add, commit 합니다.   
    - 기능 구현을 완료한 후 로컬 저장소에 변경된 부분을 반영하기 위해 add, commit 명령어를 사용합니다.   

    `git status `   

    `git add .`   

   ` git commit -m "메시지"`   

<img width="1440" alt="7" src="https://user-images.githubusercontent.com/91835827/218129801-dc9548ac-e451-4612-83e3-cd7a189471e7.png">

6. 본인 원격 저장소에 올립니다.   
    - 로컬에서 commit 명령을 실행하는 것은 로컬 저장소에 반영될 뿐, 원격 github.com의 저장소에는 반영되지 않습니다.  

   `git push origin 브랜치이름`   

<img width="1440" alt="8" src="https://user-images.githubusercontent.com/91835827/218129875-7bb41327-2a14-4d6d-b031-14f091e83fc2.png">

7. github 서비스에서 pull request를 보냅니다.   
    - pull request는 github에서 제공하는 기능으로 코드리뷰를 요청할 때 사용합니다.  

   `{자신의 github id}/rs-study/{자신의 브랜치}에서 JNU-econovation/rs-study/{자신의 브랜치}로 pull request를 보냅니다.`   

<img width="1424" alt="9" src="https://user-images.githubusercontent.com/91835827/218129970-e7bc33af-f255-4c14-bf6d-6b8be8aed0b0.png">

8. Create pull request 버튼을 클릭해 PR 내용을 작성한 후, Create pull request를 눌러 제출합니다.   
    - title : [{미션이름}] {자신 이름} 미션 제출합니다 
    - decription : 알게된 내용, 고민한 점등을 자유롭게 작성합니다.

<img width="1438" alt="10" src="https://user-images.githubusercontent.com/91835827/218130131-299cb42d-8007-44cf-97df-ebd6cf01255f.png">