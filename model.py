import pymysql.cursors
from domain import userEntity
import json

class datum:
    connection=None  
    #Connection Pool 사용시 : method단위로 connection/close
    #db 연결
    def __init__(self):
        #Connection Pool객체얻기
        datum.connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='admin',
                             password='password',
                             db='aidb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
    #db 연결 종료
    def close(self):
        datum.connection.close()
    
    def all_club(self):
        try:
            with datum.connection.cursor() as cursor:
                sql="SELECT * FROM `TravelClub`"
                cursor.execute(sql)
                result = cursor.fetchall()                
        finally:
            pass
        return result


    def insert_userInfo(self, user_entity):
        #Connection Pool로부터 connection객체 얻기
        try:
             with datum.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `CommunityMember` (`id_`, `password_`,`name`, `contact`,`gender`, `area`) VALUES (%s, %s,%s, %s, %s, %s)"
                cursor.execute(sql,(user_entity.id_,user_entity.password_,user_entity.name, user_entity.contact, user_entity.gender, user_entity.area))
                datum.connection.commit()
                sql2 = "UPDATE `CommunityMember` SET `membership` = JSON_ARRAY() WHERE `id_` = %s"
                cursor.execute(sql2, user_entity.id_)
                datum.connection.commit()
        finally:
            #Connection Pool에 자원반납하기
            pass


    def select_all(self):
        try:
            with datum.connection.cursor() as cursor:
                sql="SELECT * FROM `CommunityMember`"
                cursor.execute(sql)
                result = cursor.fetchall()                
        finally:
            pass
        return result


    def login(self, id_, pw_):
        try:
            with datum.connection.cursor() as cursor:
                sql="SELECT * FROM `CommunityMember` WHERE `id_`=%s"
                cursor.execute(sql, id_)
                result = cursor.fetchone()
        finally:
            pass
        
        try:
            if result["password_"] == pw_:
                return True
            else:
                return False
        except TypeError:
            print("계정 정보가 없습니다. 등록 후 사용하세요.")         
        finally:
            pass    

    def get_ownership(self,id_):
        with datum.connection.cursor() as cursor:
                sql0 = "SELECT `leader` FROM `CommunityMember` WHERE `id_` = %s"
                cursor.execute(sql0,id_)
                result = cursor.fetchone()
                if result == None:
                    pass



    def get_id(self,id_):
        try:
            with datum.connection.cursor() as cursor:
                sql="SELECT * FROM `CommunityMember` WHERE `id_`=%s"
                cursor.execute(sql, id_)
                result = cursor.fetchone()
        finally:
            pass
        if result != None:
            return False
        else:
            return True

    def get_userName(self,id_):
        try:
            with datum.connection.cursor() as cursor:
                sql="SELECT `name` FROM `CommunityMember` WHERE `id_`=%s"
                cursor.execute(sql, id_)
                result = cursor.fetchone()
                userName = result['name']
                return userName
        finally:
            pass

    def get_clubName(self,id_):
        try:
            with datum.connection.cursor() as cursor:
                sql="SELECT `leader` FROM `CommunityMember` WHERE `id_`=%s"
                cursor.execute(sql, id_)
                result = cursor.fetchone()
                clubName = result['leader']
                return clubName
        finally:
            pass

    def get_Areas(self,area_):
        try:
            with datum.connection.cursor() as cursor:
                sql="SELECT * FROM `TravelClub` WHERE `area`=%s"
                cursor.execute(sql, area_)
                result = cursor.fetchall()
                return result
        finally:
            pass
 
    def get_clubs(self,clubName_):
        try:
            with datum.connection.cursor() as cursor:
                sql="SELECT * FROM `TravelClub` WHERE `clubName` LIKE '%{}%'".format(clubName_)
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        finally:
            pass

    def get_Content(self,id_):
        try:
            with datum.connection.cursor() as cursor:
                sql="SELECT `content` FROM `TravelClub` WHERE `owner`=%s"
                cursor.execute(sql, id_)
                result = cursor.fetchone()
                content = result['content']
                return content
        finally:
            pass

    def add_user(self, id_,pw_):
        try:
             with datum.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `CommunityMember` (`id_`, `password_`) VALUES (%s, %s)"
                cursor.execute(sql, (id_, pw_))
                datum.connection.commit()
        finally:
            #Connection Pool에 자원반납하기
            pass

    
    def add_club(self, id_, clubName, content, area):
        try:
             with datum.connection.cursor() as cursor:

                sql="SELECT `leader` FROM `CommunityMember` WHERE `id_`=%s"
                cursor.execute(sql, id_)
                result = cursor.fetchone()
                
                if result['leader'] == None:
                    # Create a new record
                    try:
                        sql = "INSERT INTO `TravelClub` (`clubName`, `owner`,`area`,`content`) VALUES (%s, %s,%s,%s)"
                        cursor.execute(sql, (clubName, id_, area, content))
                        datum.connection.commit()
                        sql2 = "UPDATE `CommunityMember` SET `leader` = %s WHERE `id_` = %s"
                        cursor.execute(sql2, (clubName,id_))
                        datum.connection.commit()
                        sql3 = "UPDATE `CommunityMember` SET `membership` = JSON_ARRAY_APPEND(`membership`,'$', %s) WHERE `id_` = %s"
                        cursor.execute(sql3, (clubName, id_))
                        datum.connection.commit()
                        sql4 = "UPDATE `TravelClub` SET `members` = JSON_ARRAY(%s) WHERE `clubName` = %s"
                        cursor.execute(sql4, (id_,clubName))
                        datum.connection.commit()
                        return 2
                    except pymysql.err.IntegrityError:
                        print("이미 등록된 클럽명")
                        return 0
                    finally:
                        pass
                else:
                    print("이미 개설한 클럽이 있습니다.")
                    return 1
        finally:
            pass

    def update_club(self, id_, content, area):
        try:
             with datum.connection.cursor() as cursor:
                sql="SELECT `leader` FROM `CommunityMember` WHERE `id_`=%s"
                cursor.execute(sql, id_)
                result = cursor.fetchone()
                clubName = result["leader"]
                sql1 = "UPDATE `TravelClub` SET `area` = %s, `content`=%s WHERE `owner` = %s"
                cursor.execute(sql1, (area, content, id_))
                datum.connection.commit()
                print("record updated")
        finally:
            pass

    def update_user(self, id_, contact, gender, area):
        try:
             with datum.connection.cursor() as cursor:
                sql1 = "UPDATE `CommunityMember` SET `contact` = %s, `gender`=%s, `area`=%s WHERE `id_` = %s"
                cursor.execute(sql1, (contact, gender, area, id_))
                datum.connection.commit()
                print("record updated")
        finally:
            pass

    def delete_club(self, id_):
        try:
             with datum.connection.cursor() as cursor:
                sql="SELECT `leader` FROM `CommunityMember` WHERE `id_`=%s"
                cursor.execute(sql, id_)
                result = cursor.fetchone()
                clubName = result['leader']
                print(clubName)
                sql1="SELECT `membership` FROM `CommunityMember` WHERE `id_` = %s"
                cursor.execute(sql1,id_)
                membership_list = cursor.fetchone()
                club_list = json.loads(membership_list["membership"])
                idx_club = int(club_list.index(clubName))
                sql2="SELECT `members` FROM `TravelClub` WHERE `clubName` = %s"
                cursor.execute(sql2,clubName)
                members_list = cursor.fetchone()
                
                members = json.loads(members_list['members'])
                
                if (clubName != None) and (len(members)==1) and (members[0] == id_):
                    # Create a new record
                    try:
                        sql = "DELETE FROM `TravelClub` WHERE `clubName`=%s"
                        cursor.execute(sql,clubName)
                        datum.connection.commit()
                        sql2 = "UPDATE `CommunityMember` SET `leader` = NULL WHERE `id_`=%s"                
                        cursor.execute(sql2, id_)
                        datum.connection.commit()
                        sql3 = "UPDATE  `CommunityMember` SET `membership` = JSON_REMOVE(`membership`,'$[%s]') WHERE id_ = %s"
                        cursor.execute(sql3,(int(idx_club),id_))
                        datum.connection.commit()
                        return 2
                    finally:
                        pass
                elif len(members) >=1 or (members[0] != id_):
                    return 3
                else:
                    print("소유한 클럽이 없습니다.")
                    return 1
        except ValueError:
            return 1
        except TypeError:
            return 1
        finally:
            pass
       

    def get_clubList(self):
        try:
            with datum.connection.cursor() as cursor:
                sql="SELECT * FROM `TravelClub`"
                cursor.execute(sql)
                club_list = cursor.fetchall()
                
        finally:
            pass
        return club_list 

    def get_clubList_joined(self,id_):
        try:
            with datum.connection.cursor() as cursor:
                sql="SELECT * FROM `TravelClub` WHERE JSON_SEARCH(`members`,'one', %s) IS NOT NULL"
                cursor.execute(sql,id_)
                club_list = cursor.fetchall()  
        finally:
            pass
        return club_list 

    def get_members_joined(self,id_):
        try:
            with datum.connection.cursor() as cursor:
                sql0 = "SELECT `leader` FROM `CommunityMember` WHERE `id_` = %s"
                cursor.execute(sql0,id_)
                clubName = cursor.fetchone()
                sql ="SELECT * FROM `CommunityMember` WHERE JSON_SEARCH(`membership`,'one', %s) IS NOT NULL"
                cursor.execute(sql,clubName["leader"])
                member_list = cursor.fetchall()
        except pymysql.err.ProgrammingError:
            print("당신은 모임장이 아닙니다.")
            return False
        finally:
            pass
        return member_list


    def get_user(self,id_):
        try:
            with datum.connection.cursor() as cursor:
                sql ="SELECT * FROM `CommunityMember` WHERE `id_`=%s"
                cursor.execute(sql,id_)
                user = cursor.fetchone()
                
        finally:
            pass
        return user


    def join_club(self, id_, clubName):
        try:
            with datum.connection.cursor() as cursor:
                sql="SELECT `members` FROM `TravelClub` WHERE `clubName` = %s"
                cursor.execute(sql,clubName)
                club_list = cursor.fetchone()
                member_list = json.loads(club_list["members"])
                
                if id_ not in member_list:
                    print("join club: ",id_,clubName)
                    sql1 = "UPDATE `TravelClub` SET `members` = JSON_ARRAY_APPEND(`members`,'$',%s) WHERE `clubName` = %s"
                    cursor.execute(sql1,(id_, clubName))
                    datum.connection.commit()
                    print("adding TravelClub")
                    sql2 = "UPDATE `CommunityMember` SET `membership` = JSON_ARRAY_APPEND(`membership`,'$', %s) WHERE `id_` = %s"
                    cursor.execute(sql2,(clubName, id_))
                    datum.connection.commit()
                    print("adding CommunityMember")
                    result = True 
                else:
                    print(":: 이미 가입한 커뮤니티 입니다.")
                    result = False
        finally:
            pass
        return result



    def get_clubMember(self,clubName):
        try:
            with datum.connection.cursor() as cursor:
                sql="SELECT `members` FROM `TravelClub` WHERE `clubName` = %s"
                cursor.execute(sql,clubName)
                club_list = cursor.fetchone()
                member_list = json.loads(club_list["members"])
                
        finally:
            pass
        

    def remove_member(self,id_,clubName):
        try:
            with datum.connection.cursor() as cursor:
                sql="SELECT `owner` FROM `TravelClub` WHERE `clubName` = %s"
                cursor.execute(sql,clubName)
                leader_dict = cursor.fetchone()
                leader = leader_dict["owner"]
                sql1="SELECT `membership` FROM `CommunityMember` WHERE `id_` = %s"
                cursor.execute(sql1,id_)
                membership_list = cursor.fetchone()
                club_list = json.loads(membership_list["membership"])
                idx_club = int(club_list.index(clubName))
                sql2="SELECT `members` FROM `TravelClub` WHERE `clubName` = %s"
                cursor.execute(sql2,clubName)
                members_list = cursor.fetchone()
                member_list = json.loads(members_list['members'])
                idx_id_ = int(member_list.index(id_))

                if id_ in member_list and leader != id_ :
                    sql3 = "UPDATE  `CommunityMember` SET `membership` = JSON_REMOVE(`membership`,'$[%s]') WHERE id_ = %s"
                    cursor.execute(sql3,(int(idx_club),id_))
                    datum.connection.commit()
                    sql4 = "UPDATE  `TravelClub` SET `members` = JSON_REMOVE(`members`,'$[%s]') WHERE clubName = %s"
                    cursor.execute(sql4,(int(idx_id_),clubName))
                    datum.connection.commit()
                    result = True
                else:
                    print(":: 가입되지 않은 커뮤니티입니다.")
                    result = False

        except ValueError:
            result = False
        except TypeError: 
            result = False
        finally:
            pass
        return result



