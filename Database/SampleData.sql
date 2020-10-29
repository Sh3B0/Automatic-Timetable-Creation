INSERT INTO Instructor (Iid, Iname) VALUES
	(1, 'Evgenii Bobrov'),
	(2, 'Giancarlo Succi'),
	(3, 'Igor Gaponov'),
	(4, 'Sergey Gorodetskiy'),
	(5, 'Nickolay Shilov');

INSERT INTO Student (Sid, Eyear, Master, Grp, Email, Fname, Mname, Lname) VALUES
	(1, 2019, FALSE, 2, 'a.shaaban@innopolis.university', 'Ahmed', 'Shaaban', 'Nouralla'),
	(2, 2019, FALSE, 2, 'd.danko@innopolis.university', 'Danila', 'Konstantinovich', 'Danko'),
	(3, 2019, FALSE, 2, 'h.khadra@innopolis.university', 'Hasan', NULL, 'Khadra'),
	(4, 2019, FALSE, 2, 'k.sabbagh@innopolis.university', 'Kamil', 'Nishan', 'Sabbagh'),
	(5, 2019, FALSE, 2, 'v.bazilevich@innopolis.university', 'Vladimir', 'Alexandrovich', 'Bazilevich');

INSERT INTO Course(Cid, Cname, Iid) VALUES
	(1, 'FSE', 1),
	(2, 'OS', 2),
	(3, 'P(M)', 3),
	(4, 'PS', 4),
	(5, 'DE', 5);

INSERT INTO Grp(Gid, Rep) VALUES
	(1, 1), (2, 2), (3, 3), (4, 4), (5, 5);

SET datestyle TO DMY

INSERT INTO Dependent(Iid, Dname, Bdate, Relationship) VALUES
	(1, 'Vladimir', '02-06-2015', 'Son'),
	(2, 'Igor', '10-05-2020', 'Son'),
	(3, 'Tatiana', '23-01-2019', 'Daughter'),
	(4, 'Alexandr', '17-04-2014', 'Son'),
	(5, 'Dmitriy', '01-09-1960', 'Father');

INSERT INTO Student_Electives(Sid, Elective) VALUES
	(1, 1), (5, 2), (2, 3), (3, 4), (4, 5);

INSERT INTO Enrolled_In(Sid, Cid) VALUES
	(1, 1), (1, 2), (1, 3), (1, 4), (1, 5);

