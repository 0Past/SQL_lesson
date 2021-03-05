--Задание 1
SELECT student_id||';'|| Upper(surname)||';'||upper(name)||';'||stipend||';'||upper(city)||';'||TO_CHAR(birthday, 'DD/MM/YY')||';'||univ_id
	FROM student;
--Задание 2
SELECT substr(name,1,1)||'.'|| Upper(surname)|| '; место жителсва-'||Upper(city)||'; родился - '|| TO_CHAR(birthday, 'DD.MM.YY')|| '.'
	FROM student;
--Задание 3
SELECT lower(substr(name,1,1))||'.'|| lower(surname)|| '; место жителсва-'||lower(city)||'; родился - '|| TO_CHAR(birthday, 'DD-MM-YY')||'.'
	FROM student;
--Задание 4
SELECT name||' '|| surname ||' родился в '|| TO_CHAR(birthday,'YYYY')||' году.'
	FROM student;
--Задание 5
SELECT surname, name, stipend*100
	FROM student
--Задание 6
SELECT upper(name)||' '|| upper(surname) ||' родился в '|| TO_CHAR(birthday,'YYYY')||' году.'
	FROM student
	WHERE kurs != 3 and kurs !=5;
--Задание 7
SELECT 'Код-'|| univ_id ||';' || univ_name||'-г.'|| city|| '; '||'Рейтинг='|| rating||'.'
	FROM university;
	
--Задание 8
SELECT 'Код-'|| univ_id ||';' || univ_name||'-г.'|| city|| '; '||'Рейтинг='|| round(rating,-1)||'.'
FROM university;
--Задание 9
SELECT count(student_id)
	FROM exam_marks
	WHERE subj_id = 20;
--Задание 10
SELECT count(Distinct subj_id)
	FROM exam_marks;
--Задание 11
SELECT student_id, min(mark)
	FROM exam_marks
	GROUP BY student_id;
--Задание 12
SELECT student_id, max(mark)
	FROM exam_marks
	GROUP BY student_id;
--Задание 13
SELECT surname, min(surname)
	FROM student 
	WHERE substr(surname,1,1) = 'И';
--Задание 14
SELECT subj_id, subj_name, max(semester)
	FROM subject
	GROUP BY subj_name;
--Задание 15
SELECT count(student_id)
	FROM exam_marks
	GROUP BY exam_date;
--Задание 16
SELECT AVG(mark)
	FROM exam_marks
	GROUP BY kurs;
--Задание 17
SELECT avg(mark)
	FROM exam_marks
	GROUP BY student_id;
--Задание 18
SELECT avg(mark)
	FROM exam_marks
	GROUP BY exam_id;
--Задание 19
SELECT subj_id, count(student_id)
	FROM exam_marks
	GROUP BY subj_id;
--Задание 20
SELECT count(subj_id)
	FROM subject
	GROUP BY semester;
