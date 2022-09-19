
# <font color="red"> __Travel Community__ 여행 커뮤니티 관리 프로그램 구현 </font>

## 1. Introduction
 
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
 
 - **프로그램 실행을 위한 테이블 생성 및 샘플데이터 입력**
 ```
 ## Creating Table

CREATE TABLE CommunityMember (
	id_ varchar(30) NOT NULL,
	password_ varchar(25) Not NULL,
	name varchar(20),
	gender enum('남자','여자'),
	contact varchar(30),
	area varchar(12),
	leader varchar(20) DEFAULT NULL,
	membership json DEFAULT NULL,
	PRIMARY KEY(id_)
) CHARSET=utf8mb4;


CREATE TABLE TravelClub (
	clubName varchar(30) NOT NULL,
	owner varchar(30) NOT NULL,
	area varchar(12),
	content varchar(100) DEFAULT NULL,
	members json DEFAULT NULL,
	PRIMARY KEY(clubName)
)CHARSET=utf8mb4 ;

## Inserting sample datum

INSERT INTO CommunityMember(`id_`,`password_`,`name`,`gender`,`contact`,`area`,`leader`,`membership`) VALUES ('admin','password','차의성','남자','010-1111-1111','서울','SK인포섹',JSON_ARRAY('SK인포섹'));
INSERT INTO TravelClub(clubName,owner,area,content,members) VALUES ("SK인포섹","admin","서울","인공지능반 화이팅 입니다",JSON_ARRAY('admin','kanga','songsong','bonobono','joohyun'));

INSERT INTO CommunityMember(`id_`,`password_`,`name`,`gender`,`contact`,`area`,`leader`,`membership`) VALUES ('kanga','1234','강가연','여자','010-1234-1234','서울','제주도푸른밤',JSON_ARRAY('제주도푸른밤','SK인포섹'));
INSERT INTO TravelClub(clubName,owner,area,content,members) VALUES ("제주도푸른밤","kanga","제주","이번 여름 제주바다로 떠나요",JSON_ARRAY('kanga','bonobono'));

INSERT INTO CommunityMember(`id_`,`password_`,`name`,`gender`,`contact`,`area`,`leader`,`membership`) VALUES ('songsong','1234','송태경','남자','010-5678-5678','경북','부산갈매기',JSON_ARRAY('부산갈매기','SK인포섹'));
INSERT INTO TravelClub(clubName,owner,area,content,members) VALUES ("부산갈매기","songsong","경북","다같이 해운대로 GOGO!",JSON_ARRAY('songsong'));

INSERT INTO CommunityMember(`id_`,`password_`,`name`,`gender`,`contact`,`area`,`membership`) VALUES ('bonobono','1234','최보원','여자','02-331-2913','서울',JSON_ARRAY('제주도푸른밤','SK인포섹'));

INSERT INTO CommunityMember(`id_`,`password_`,`name`,`gender`,`contact`,`area`,`leader`,`membership`) VALUES ('joohyun','1234','강주현','남자','010-1588-1588','충북','맛집을찾아서',JSON_ARRAY('맛집을찾아서','SK인포섹'));
INSERT INTO TravelClub(clubName,owner,area,content,members) VALUES ('맛집을찾아서',"joohyun","서울","이번주는 삽겹살 먹으러갑니다",JSON_ARRAY("joohyun"));
```


  ---
 ## 4.기능설명 (Options)
 
### 1) 로그인
 
  ![alt text](https://github.com/Cha-Euy-Sung/traveling_communities/blob/master/README/login1.png "로그인")
  
   신규계정 생성방법
   - 사용할 아이디/비밀번호를 입력 후, '등록하기' 버튼 클릭
   - 전화번호 항목은 양식에 맞게 입력하지 않을 시, 등록 불가 (ex. 000-0000-0000)
   - 이미 생성된 아이디는 재사용불가 
   
   로그인 방법
   - 등록된 계정 아이디/비밀번호 입력 후, '접속하기' 버튼 클릭
   - 등록된 계정이 아닌 경우, 접속 불가 
   
   

### 2) 메인메뉴
![alt text](https://github.com/Cha-Euy-Sung/traveling_communities/blob/master/README/main_interface.png "메인메뉴")

 **메인메뉴**
 - 내정보보기 : 가입 시 입력한 내 정보 '확인' 및 '수정' 가능 -> 아이디/이름을 제외한 정보 수정가능. 
 - 로그아웃 : 로그인화면으로 이동
 - 종료하기 : 프로그램 종료
 
 **커뮤니티**
 - 만들기 : 커뮤니티 생성 -> 한 계정당 하나의 커뮤니티를 개설 가능 
 - 지우기 : 커뮤니티 삭제 -> 자신이 개설한 커뮤니티 삭제 가능 -> (자신을 제외한)회원이 남아있는 경우는 삭제 불가
 - 내용수정 : 커뮤니티 정보 수정 -> 활동(모임)지역 및 공지사항. 커뮤니티명은 변경 불가.  
 - 멤버정보 : 자신이 개설한 커뮤니티에 속한 멤버들의 정보 확인 가능. 멤보 목록 저장가능. (*모임장만 열람가능. 일반회원 불가). 
 - 게시판생성 : 기능구현예정 
 
 **목록보기**
 - 모든 커뮤니티 : 개설 된 모든 커뮤니티 출력. 타 커뮤니티 가입/탈퇴 가능.
 - 가입한 커뮤니티 : 자신이 가입한 커뮤니티 출력. 탈퇴 가능. 
 
 **찾아보기**
 - 커뮤니티명 : 커뮤니티명으로 검색. 이름의 일부분으로도 검색가능. 커뮤니티 가입/탈퇴 가능.
 - 활동지역: 입력한 지역에서 활동중인 커뮤니티 검색 가능. 커뮤니티 가입/탈퇴 가능.
 
 **도움말**
 - github : 해당 github 링크 띄우기. 
 

---

**부가기능**
 - 멤버정보저장 (.csv format)
 
 ![alt text](https://github.com/Cha-Euy-Sung/traveling_communities/blob/master/README/member_info.png "멤버목록")
 
 ![alt text]( https://github.com/Cha-Euy-Sung/traveling_communities/blob/master/README/member_list_save.png "목록저장")


 ----
 ## 5. 기타사항 (Additional Info a.k.a TMI)
 
  **DB 관련**
  - 회원정보(CommunityMember), 커뮤니티(TravelClub) 두개의 테이블로 구성
  - MySQL 5.x 버전부터 사용가능한 JSON 타입 field 활용
  - 해당 필드를 사용하기 위해서, 테이블 생성시 "CHARSET=utf8mb4" 필수. 
  - JSON ARRAY 를 사용함으로 인해서, 불필요한 field 확장을 해소. (membership, members)
  - JSON ARRAY와 관련된 query는 위에 첨부.
  
  **GUI관련**
  - TKinter는 Python 내부에 포함되어있다는 장점이 있지만, 그게 전부임.
  - 페이지(프레임)이 적은 경우는 활용하기 편하나, 그 외에는 PyQT 추천.
  - root.destroy()시, root.mainloop() 아래 문으로 넘어감. (return과 다른 개념)
  - TopLevel보다는, 새로운 window를 생성하는 것이 오류가 적음.
  
  **Pattern**
  - Model-View-Controller 패턴을 염두해두고 작성.
  - 하지만 프로그램 특성 상, View와 Controller가 혼합되는 경우가 많아짐.
  - MVC에서 컨트롤러가 뷰모델로 교체된 형태인 MVVM(Model-View-ViewModel)에 가까워짐.
  - ViewModel은 View가 필요로 하는 data와 command객체를 노출해 주기 때문에, <br> view에 필요한 data와 action을 담고 있는 컨테이너 객체로 볼 수 있음. 
  - MVVM이 MVC와 다른 점은 ViewModel은 View를 지원하고, 거기에 필요한 Data와 Command를 제공함.
  
  
 ----
 
  
  
 
 
 
