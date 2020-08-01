
# <font color="red"> Travel Community 여행 커뮤니티 관리 프로그램 구현 </font>

## Introduction
#### [ SK인포섹 클라우드 AI 융합 교육과정 MODULE PROJECT 1 ]
 
   - Python, MySQL, Docker 활용한 여행커뮤니티 관리 프로그램 구현
   - Tkinter 기반의 Graphic User Interface 구성 
    
```
활용 툴 (Used Tool)
 - Docker Toolbox : https://github.com/docker/toolbox/releases
 - DBeaver Community: https://dbeaver.io/download/

사용 추가 라이브러리 (pip install 통해 설치 가능)
 - webbrowser
 - PIL (pillow)
 - pymysql
```
## Demo 
#### *아래 화면 클릭 시, 동영상 링크로 이동
[<img src="https://j.gifs.com/nx4OWp.gif" width="70%">](https://youtu.be/mKtKysbJzJg)


## Docker & DB setting
#### 도커 설정 및 DB연결 
**Docker 실행환경 (Docker QuickStart Shell**
```
docker pull mysql:5.7  # MYSQL이미지 다운로드 (mysql버전 = 5.7)
docker images # 설치한 이미지 확인
docker run --name mysql5 -e MYSQL_ROOT_PASSWORD=password -d -p 3306:3306 mysql:5.7 #컨테이너 생성/실행
docker exec -it mysql5 bash #컨테이너 명령실행
```  
  @root#mysql -u root -p
  Enter Password : password
  
  mysql>create database aidb default character set 'utf8'; #'aidb'이름의 데이터베이스 생성
  mysql>use aidb
  mysql>grant all privileges on *.* to 'admin'@'%' identified by 'password'; #유저생성 및 권한설정
  myslq>grant select,insert,update,delete on aidb.* to 'admin'@'%';  
  mysql>flush privileges;  
  mysql>quit;              //mysql shell 종료
  
 
 VM VirtualBoX 설정
 
 DBeaver 연결
 
  ---
 기능설명 (Options)
 
 
 
 
 ----
 기타정보 (Additional Info)
 
 
 
 
