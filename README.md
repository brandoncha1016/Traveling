
# <font color="red"> __Travel Community__ 여행 커뮤니티 관리 프로그램 구현 </font>

## 1. Introduction
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
## 2. Demo 
#### *아래 화면 클릭 시, 동영상 링크로 이동
[<img src="https://j.gifs.com/nx4OWp.gif" width="70%">](https://youtu.be/mKtKysbJzJg)


## 3. Docker & DB setting
#### 도커 설정 및 DB연결 
**Docker 실행환경 (Docker QuickStart Shell)**
- **MySQL 이미지 설치(ver 5.7)**
```
docker pull mysql:5.7 
docker images 
```
- **컨테이너 생성/실행**
```
docker run --name mysql5 -e MYSQL_ROOT_PASSWORD=password -d -p 3306:3306 mysql:5.7 
docker exec -it mysql5 bash 
```  
- **데이터베이스 생성 및 유저설정**
```
  @root#mysql -u root -p
  Enter Password : password
        mysql>create database 'db_name' default character set 'utf8'; 
        mysql>use aidb
        mysql>grant all privileges on *.* to 'admin'@'%' identified by 'password'; 
        myslq>grant select,insert,update,delete on aidb.* to 'admin'@'%';  
        mysql>flush privileges;  
        mysql>quit;            
  ```
 - **VM VirtualBoX 설정**

 ![alt text](https://github.com/Cha-Euy-Sung/traveling_communities/blob/master/README/docker3.png "VM 셋팅")
 
 - **DBeaver 연결**
 
 ![alt text](https://github.com/Cha-Euy-Sung/traveling_communities/blob/master/README/docker4.png "DB 연결확인")
  ---
 ## 4.기능설명 (Options)
 
### 1) 로그인
 
  ![alt text](https://github.com/Cha-Euy-Sung/traveling_communities/blob/master/README/login1.png "로그인")
  
  ![alt text](https://github.com/Cha-Euy-Sung/traveling_communities/blob/master/README/login_error.png "로그인에러")



### 2) 메인메뉴
![alt text](https://github.com/Cha-Euy-Sung/traveling_communities/blob/master/README/main_interface.png "메인메뉴")

 
 ![alt text](https://github.com/Cha-Euy-Sung/traveling_communities/blob/master/README/member_info.png "멤버목록")
 
 ![alt text]( https://github.com/Cha-Euy-Sung/traveling_communities/blob/master/README/member_list_save.png "목록저장")


 ----
 ## 5. 기타정보 (Additional Info)
 
 
 
 
