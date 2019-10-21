#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SellMyBook.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


'''


create TRIGGER tr_insert_charater
befor insert on charater
for each row
set new.charater_name = UPPER(NEW.charater_name)

/////////

dilimeter $

create procedure pro(in rollno tinyint, in name varchar(20), in marks int)
begin
declare class varchar(25);
if marks >= 990 and marks <= 1500 
then set class = "Distintion";
if marks >= 900 and marks <= 989
then set class = "First Class";
if marks >= 825 and marks <= 899 
then set class = "Second Class";
else 
set class = "Fail";
end if;
insert into studmarks values(name,marks);
insert into result values(rollno,name,class);
endl;$

delimeter ;

create procedure totalcount( in classname varchar(25))
return int
begin
declare totalcount int(20);
select count(*) into totalcount where class=classname;
return total;
end;

delimeter ;

//////////
trigger queries to be executed in mock practicals

create trigger achavala_triggerName
BEFORE update on library on each row
begin
declare a varchar(10);
set a = "updated";
insert into lib_audit values( old.name, old.id, a, curdate(), current_user);
end$

delimeter ;

2) Changes the no of copies when issuing copies is greater than aval copies

delimeter $

create trigger changeCopies
BEFORE insert on transection on each row
begin
declare no int;
if new.I_R = "I"
then 
select no_of_copies into no from library where B_id = new.B_id;
if no > new.no_of_c
then new.no_of_copies = no;
end if;
end if;
end$

delimerter ;

3) update no_of_c

delimeter $

create trigger updateNoOfCopies
After insert on transaction on each row
begin 
if new.I_R = "I"
then update library set no_of_c = no_of_c - new.no_of_c where B_id = new.B_id;
end if;
if new.I_R = "R"
then update library set no_of_c = no_of_c + new.no_of_c where B_id = new.B_id;
end if;

delimeter ;


///////// 

Time for the cursor

1) Don't fail all students

begin 
update student set stud_marks = 40 where marks between 35 and 39;
if SQL%notfound 
then dbms_output.put_line('No record updated!)
else
dbms_output.put_line('No of student that are pushed : '||SQL%rowcount);
endif;
end;
10 /

2)

begin
cursor cur_s is select * from student;
cursor cur_new(roll_var int) select * from newstudent where roll_no = roll_var;
new_row newstudent%rowtype;
begin
for student_record in cur_s
loop
open cur_new(student_record.rollno);
fetch cur_new into already_present;
if already_present%notfound 
then 
insert into newstudent values( student_record.rollno, student_record.name, student_record.marks);
end if;
close cur_new;
end loop;

17/


//////////////////

Exception

1)

delimeter $

declare 
roll int := &roll_number;
b_name varchar(20) := '&bookname';
penalty_days int := 0;
start_date date;
total_fine int := 0;
begin
select date_of_relese into start_date
where
roll_no = roll and book_name = b_name;
penalty_days = sysdate - start_date;






'''
