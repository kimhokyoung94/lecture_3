Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@kimhokyoung94 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


TaeKyoungKim
/
lecture_3
0
05
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
lecture_3/README.md
@TaeKyoungKim
TaeKyoungKim README.md
Latest commit d0bf244 2 minutes ago
 History
 1 contributor
68 lines (32 sloc)  989 Bytes
  
python 라이브러리 설치 명령어
pip install virtualenv
virtualenv 명령어를 이용해서 가상환경을 만드는 방법
virtualenv [원하고자하는 프로젝트명]
virtualenv lecture_3 && cd lecture_3
1

가상환경 활성화
가상환경 할성화 명령어 activate.bat

Scripts 폴더내에 존재

cd Scripts && activate
가상환경 비활성화
가상환경 비할성화 명령어 deactivate.bat

Scripts 폴더내에 존재

cd Scripts && deactivate
설치한 라이브러리 관리는 requirements.txt에서 관리된다.
freeze 명령어를 이용해서 생성
생성방법

pip freeze > requirements.txt
requirements.txt 를 활용해서 라브러리 설치
pip install -r requirements.txt
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
