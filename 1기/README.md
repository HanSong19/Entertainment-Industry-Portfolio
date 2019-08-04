# kgitbank_bigdata
> 1. os : windows 10
> 2. 아나콘다 (python 3.65)
> 3. git, github
> 4. edit : vs code
> 5. 웹 : flask,html,css,jqeury,bootstrap,json,ajax 
          pandas, ...
> 6. DB : mariaDB
> 7. 기타 : data(네이버 api, 공공데이터포탈)


DB root계정 비밀번호 변경  
use mysql;  
update user set password=password('1234') where user='root';  
describe user;  
flush privileges;  

update user set authentication_string=password('1234') where user='root';  
  
mysql의 root 비밀번호를 변경할 때 update user set password=password('1234') where user='root';   
명령을 입력했는데 ERROR 1054 (42S22): Unknown column 'password' in 'field list' 오류가 발생했다면   
user table에 password 필드가 존재하지 않기 때문이다.   
password 대신 authentication_string 필드가 존재할 것이므로   
update user set authentication_string=password('1234') where user='root'; 을 이용하면 된다.  
