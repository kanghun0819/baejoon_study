select MEMBER_ID,MEMBER_NAME,GENDER,DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d') as DATE_OF_BIRTH
FROM MEMBER_PROFILE
where MONTH(DATE_OF_BIRTH) = 3 and GENDER = 'W' and TLNO is not null
order by MEMBER_ID;