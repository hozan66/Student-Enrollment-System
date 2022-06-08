use userDB2

drop table Enrollment;
drop table Student;
drop table Department;
drop table College;
drop table University;
drop table users;

create table users(
userName nvarchar(50),
[password] nvarchar(50)
);

insert into users values ('admin','1234');
insert into users values ('hozan','999');
insert into users values ('osama','1234');
insert into users values ('ali','4321');
insert into users values ('hozan','999999999');


create table University(
Univ_ID int primary key,
Univ_Name nvarchar(50),
Adress nvarchar(50)
)
go

insert into University values(1,'Salahaddin','Erbil-karkuk-street');
insert into University values(2,'Sulaimani','Sulaimani-street');
insert into University values(3,'Duhok','Duho-Zakho-street');

select * from University;

create table College(
College_ID int primary key,
College_Name nvarchar(50),
Dean nvarchar(50),
Univ_ID int foreign key references University(Univ_ID)
)
go

insert into College values(11,'Science','Professor Hauresh',1);
insert into College values(12,'Engineering','Professor Hamdin',1);
insert into College values(13,'Language','Professor Ahmad',1);
insert into College values(14,'Engineering','Professor Ramadan',2);
insert into College values(15,'Medicine','Professor Ali',2);
insert into College values(16,'Language','Professor Sarkheel',3);
insert into College values(17,'Science','Professor Shekhmus',3);
insert into College values(18,'Engineering','Professor Zana',3);
insert into College values(19,'Medicine','Professor Aland',3);

select * from College;

create table Department(
Dep_ID int primary key,
Dep_Name nvarchar(50),
Supervisor nvarchar(50),
College_ID int foreign key references College(College_ID)
)
go

insert into Department values(123,'CS & IT','Dr Dler',11);
insert into Department values(124,'Math','Dr Maria',11);
insert into Department values(125,'Physic','Dr Nushi',11);
insert into Department values(126,'Geology','Dr Mohammed',11);
insert into Department values(127,'Biology','Dr Jose',11);
insert into Department values(128,'chemic','Dr Wei',11);
insert into Department values(129,'Software Engineering','Dr Salar',12);
insert into Department values(130,'Mechanical & Mechatronics','Dr Yan',12);
insert into Department values(131,'Architecture','Dr John',12);
insert into Department values(132,'Civil','Dr David',12);
insert into Department values(133,'Electrical','Dr Li',12);
insert into Department values(134,'Kurdish','Dr Eanoo',13);
insert into Department values(135,'Arabic','Dr Abdul',13);
insert into Department values(136,'English','Dr Ana',13);
insert into Department values(137,'French','Dr Ying',13);
insert into Department values(138,'Germany','Dr Michael',13);
insert into Department values(139,'Turkish','Dr Juan',13);

insert into Department values(140,'Software Engineering','Dr Anna',14);
insert into Department values(141,'Mechanical & Mechatronics','Dr Mary',14);
insert into Department values(142,'Architecture','Dr Jean',14);
insert into Department values(143,'Civil','Dr Robert',14);
insert into Department values(144,'Electrical','Dr Daniel',14);
insert into Department values(145,'General Medicine','Dr Luis',15);
insert into Department values(146,'Dentistry','Dr Carlos',15);
insert into Department values(147,'Pharmacy','Dr James',15);
insert into Department values(148,'Ophthalmology','Dr Antonio',15);

insert into Department values(149,'Kurdish','Dr Joseph',16);
insert into Department values(150,'Arabic','Dr Hui',16);
insert into Department values(151,'English','Dr Elena',16);
insert into Department values(152,'French','Dr Francisco',16);
insert into Department values(153,'Germany','Dr Hong',16);
insert into Department values(154,'Turkish','Dr Marie',16);
insert into Department values(155,'CS & IT','Dr Min',17);
insert into Department values(156,'Math','Dr Lei',17);
insert into Department values(157,'Physic','Dr Yu',17);
insert into Department values(158,'Geology','Dr Ibrahim',17);
insert into Department values(159,'Biology','Dr Peter',17);
insert into Department values(160,'chemic','Dr Fatima',17);
insert into Department values(161,'Software Engineering','Dr Aleksandr',18);
insert into Department values(162,'Mechanical & Mechatronics','Dr Richard',18);
insert into Department values(163,'Architecture','Dr Xin',18);
insert into Department values(164,'Civil','Dr Bin',18);
insert into Department values(165,'Electrical','Dr Paul',18);
insert into Department values(166,'General Medicine','Dr Ping',19);
insert into Department values(167,'Dentistry','Dr Lin',19);
insert into Department values(168,'Pharmacy','Dr Olga',19);
insert into Department values(169,'Ophthalmology','Dr Sri',19);

select * from Department;

create table Student(
Student_ID bigint primary key,
First_Name nvarchar(50),
Last_Name nvarchar(50),
Gender nvarchar(10),
Date_Of_Birth date,
Email nvarchar(50),
Phone_Number nvarchar(50)
)
go

insert into Student values(112200,'James','John','Male','1999-7-1','James@gmail.com','+9647826030525');
insert into Student values(112201,'Mary','Patricia','Female','2000-7-2','Mary@gmail.com','+9647835459526');
insert into Student values(112202,'Robert','Michael','Male','2000-7-3','Robert@gmail.com','+9647507788527');
insert into Student values(112203,'Jennifer','Linda','Female','2000-7-4','Jennifer@gmail.com','+9647835459528');
insert into Student values(112204,'William','David','Male','1999-7-5','William@gmail.com','+9647826030529');
insert into Student values(112205,'Elizabeth','Barbara','Female','2000-7-6','Elizabeth@gmail.com','+9647835459530');
insert into Student values(112206,'Richard','Joseph','Male','2000-7-7','Richard@gmail.com','+9647507788531');
insert into Student values(112207,'Susan','Jessica','Female','2000-7-8','Susan@gmail.com','+9647835459532');
insert into Student values(112208,'Thomas','Charles','Male','1999-7-9','Thomas@gmail.com','+9647826030533');
insert into Student values(112209,'Sarah','Karen','Female','2000-7-10','Sarah@gmail.com','+9647835459534');
insert into Student values(112210,'Christopher','Daniel','Male','2000-7-11','Christopher@gmail.com','+9647507788535');
insert into Student values(112211,'Nancy','Lisa','Female','2000-7-12','Nancy@gmail.com','+9647835459536');
insert into Student values(112212,'Matthew','Anthony','Male','1999-7-13','Matthew@gmail.com','+9647826030537');
insert into Student values(112213,'Margaret','Betty','Female','2000-7-14','Margaret@gmail.com','+9647835459538');
insert into Student values(112214,'Donald','Mark','Male','2000-7-15','Donald@gmail.com','+9647507788539');
insert into Student values(112215,'Sandra','Ashley','Female','2000-7-16','Sandra@gmail.com','+9647835459540');
insert into Student values(112216,'Paul','Steven','Male','1999-7-17','Paul@gmail.com','+9647826030541');
insert into Student values(112217,'Dorothy','Kimberly','Female','2000-7-18','Dorothy@gmail.com','+9647835459542');
insert into Student values(112218,'Andrew','Kenneth','Male','2000-7-19','Andrew@gmail.com','+9647507788543');
insert into Student values(112219,'Emily','Donna','Female','2000-7-20','Emily@gmail.com','+9647835459544');
insert into Student values(112220,'Joshua','Kevin','Male','1999-7-21','Joshua@gmail.com','+9647826030545');
insert into Student values(112221,'Michelle','Carol','Female','2000-7-22','Michelle@gmail.com','+9647835459546');
insert into Student values(112222,'Brian','George','Male','2000-7-23','Brian@gmail.com','+9647507788547');
insert into Student values(112223,'Amanda','Melissa','Female','2000-7-24','Amanda@gmail.com','+9647835459548');
insert into Student values(112224,'Edward','Ronald','Male','1999-7-25','Edward@gmail.com','+9647826030549');
insert into Student values(112225,'Deborah','Stephanie','Female','2000-8-1','Deborah@gmail.com','+9647835459550');
insert into Student values(112226,'Timothy','Jason','Male','2000-8-2','Timothy@gmail.com','+9647507788551');
insert into Student values(112227,'Rebecca','Laura','Female','2000-8-3','Rebecca@gmail.com','+9647835459552');
insert into Student values(112228,'Jeffrey','Ryan','Male','1999-8-4','Jeffrey@gmail.com','+9647826030553');
insert into Student values(112229,'Sharon','Cynthia','Female','2000-8-5','Sharon@gmail.com','+9647835459554');
insert into Student values(112230,'Jacob','Gary','Male','2000-8-6','Jacob@gmail.com','+9647507788555');
insert into Student values(112231,'Kathleen','Amy','Female','2000-8-7','Kathleen@gmail.com','+9647835459556');
insert into Student values(112232,'Nicholas','Eric','Male','1999-8-8','Nicholas@gmail.com','+9647826030557');
insert into Student values(112233,'Shirley','Angela','Female','2000-8-9','Shirley@gmail.com','+9647835459558');
insert into Student values(112234,'Jonathan','Stephen','Male','2000-8-10','Jonathan@gmail.com','+9647507788559');
insert into Student values(112235,'Helen','Anna','Female','2000-8-11','Helen@gmail.com','+9647835459560');
insert into Student values(112236,'Larry','Justin','Male','1999-8-12','Larry@gmail.com','+9647826030561');
insert into Student values(112237,'Brenda','Pamela','Female','2000-8-13','Brenda@gmail.com','+9647835459562');
insert into Student values(112238,'Scott','Brandon','Male','2000-8-14','Scott@gmail.com','+9647507788563');
insert into Student values(112239,'Nicole','Samantha','Female','2000-8-15','Nicole@gmail.com','+9647835459564');
insert into Student values(112240,'Benjamin','Samuel','Male','1999-8-16','Benjamin@gmail.com','+9647826030565');
insert into Student values(112241,'Katherine','Emma','Female','2000-8-17','Katherine@gmail.com','+9647835459566');
insert into Student values(112242,'Frank','Gregory','Male','2000-8-18','Frank@gmail.com','+9647507788567');
insert into Student values(112243,'Ruth','Christine','Female','2000-8-19','Ruth@gmail.com','+9647835459568');
insert into Student values(112244,'Raymond	','Alexander','Male','1999-8-20','Raymond@gmail.com','+9647826030569');
insert into Student values(112245,'Catherine','Debra','Female','2000-8-21','Catherine@gmail.com','+9647835459570');
insert into Student values(112246,'Patrick','Jack','Male','2000-8-22','Patrick@gmail.com','+9647507788571');
insert into Student values(112247,'Rachel','Carolyn','Female','2000-8-23','Rachel@gmail.com','+9647835459572');
insert into Student values(112248,'Dennis','Jerry','Male','1999-8-24','Dennis@gmail.com','+9647826030573');
insert into Student values(112249,'Janet','Virginia','Female','2000-8-25','Janet@gmail.com','+9647835459574');
insert into Student values(112250,'Tyler','Aaron','Male','2000-9-1','Tyler@gmail.com','+9647507788575');
insert into Student values(112251,'Maria','Heather','Female','2000-9-2','Maria@gmail.com','+9647835459576');
insert into Student values(112252,'Jose','Henry','Male','1999-9-3','Jose@gmail.com','+9647826030577');
insert into Student values(112253,'Diane','Julie','Female','2000-9-4','Diane@gmail.com','+9647835459578');
insert into Student values(112254,'Adam','Douglas','Male','2000-9-5','Adam@gmail.com','+9647507788579');
insert into Student values(112255,'Joyce','Victoria','Female','2000-9-6','Joyce@gmail.com','+9647835459580');
insert into Student values(112256,'Nathan','Peter','Male','1999-9-7','Nathan@gmail.com','+9647826030581');
insert into Student values(112257,'Kelly','Christina','Female','2000-9-8','Kelly@gmail.com','+9647835459582');
insert into Student values(112258,'Zachary','Kyle','Male','2000-9-9','Zachary@gmail.com','+9647507788583');
insert into Student values(112259,'Lauren','Joan','Female','2000-9-10','Lauren@gmail.com','+9647835459584');
insert into Student values(112260,'Walter','Harold','Male','1999-9-11','Walter@gmail.com','+9647826030585');
insert into Student values(112261,'Evelyn','Olivia','Female','2000-9-12','Evelyn@gmail.com','+9647835459586');
insert into Student values(112262,'Jeremy','Ethan','Male','2000-9-13','Jeremy@gmail.com','+9647507788587');
insert into Student values(112263,'Judith','Megan','Female','2000-9-14','Judith@gmail.com','+9647835459588');
insert into Student values(112264,'Carl','Keith','Male','1999-9-15','Carl@gmail.com','+9647826030589');
insert into Student values(112265,'Cheryl','Martha','Female','2000-9-16','Cheryl@gmail.com','+9647835459590');
insert into Student values(112266,'Roger','Gerald','Male','2000-9-17','Roger@gmail.com','+9647507788591');
insert into Student values(112267,'Andrea','Frances','Female','2000-9-18','Andrea@gmail.com','+9647835459592');
insert into Student values(112268,'Christian','Terry','Male','1999-9-19','Christian@gmail.com','+9647826030593');
insert into Student values(112269,'Hannah','Jacqueline','Female','2000-9-20','Hannah@gmail.com','+9647835459594');
insert into Student values(112270,'Sean','Arthur','Male','2000-9-21','Sean@gmail.com','+9647507788595');
insert into Student values(112271,'Ann','Gloria','Female','2000-9-22','Ann@gmail.com','+9647835459596');
insert into Student values(112272,'Austin','Noah','Male','1999-9-23','Austin@gmail.com','+9647826030597');
insert into Student values(112273,'Jean','Kathryn','Female','2000-9-24','Jean@gmail.com','+9647835459598');
insert into Student values(112274,'Lawrence','Jesse','Male','2000-9-25','Lawrence@gmail.com','+9647507788599');
insert into Student values(112275,'Alice','Teresa','Female','2000-10-1','Alice@gmail.com','+9647835459600');
insert into Student values(112276,'Joe','Bryan','Male','1999-10-2','Joe@gmail.com','+9647826030601');
insert into Student values(112277,'Sara','Janice','Female','2000-10-3','Sara@gmail.com','+9647835459602');
insert into Student values(112278,'Billy','Jordan','Male','2000-10-4','Billy@gmail.com','+9647507788603');
insert into Student values(112279,'Doris','Madison','Female','2000-10-5','Doris@gmail.com','+9647835459604');
insert into Student values(112280,'Albert','Dylan','Male','1999-10-6','Albert@gmail.com','+9647826030605');
insert into Student values(112281,'Julia','Grace','Female','2000-10-7','Julia@gmail.com','+9647835459607');
insert into Student values(112282,'Bruce','Willie','Male','2000-10-8','Bruce@gmail.com','+9647507788608');
insert into Student values(112283,'Judy','Abigail','Female','2000-10-9','Judy@gmail.com','+9647835459609');
insert into Student values(112284,'Gabriel','Alan','Male','1999-10-10','Gabriel@gmail.com','+9647826030610');
insert into Student values(112285,'Marie','Denise','Female','2000-10-11','Marie@gmail.com','+9647835459611');
insert into Student values(112286,'Juan','Logan','Male','2000-10-12','Juan@gmail.com','+9647507788612');
insert into Student values(112287,'Beverly','Amber','Female','2000-10-13','Beverly@gmail.com','+9647835459613');
insert into Student values(112288,'Wayne','Ralph','Male','1999-10-14','Wayne@gmail.com','+9647826030614');
insert into Student values(112289,'Theresa','Marilyn','Female','2000-10-15','Theresa@gmail.com','+9647835459615');
insert into Student values(112290,'Roy','Eugene','Male','2000-10-16','Roy@gmail.com','+9647507788616');
insert into Student values(112291,'Danielle','Diana','Female','2000-10-17','Danielle@gmail.com','+9647835459617');
insert into Student values(112292,'Randy','Vincent','Male','1999-10-18','Randy@gmail.com','+9647826030618');
insert into Student values(112293,'Brittany','Natalie','Female','2000-10-19','Brittany@gmail.com','+9647835459619');
insert into Student values(112294,'Russell','Louis','Male','2000-10-20','Russell@gmail.com','+9647507788620');
insert into Student values(112295,'Sophia','Rose','Female','2000-10-21','Sophia@gmail.com','+9647835459621');
insert into Student values(112296,'Philip','Bobby','Male','1999-10-22','Philip@gmail.com','+9647826030622');
insert into Student values(112297,'Isabella','Alexis','Female','2000-10-23','Isabella@gmail.com','+9647835459623');
insert into Student values(112298,'Kayla','Charlotte','Male','2000-10-24','Kayla@gmail.com','+9647507788624');
insert into Student values(112299,'shereen','sulaiman','Female','2000-10-25','shirin2021@gmail.com','+9647835459625');

select * from Student;

create table Enrollment(
Enrol_ID bigint primary key,
Enrollment_Date date,
Grade float,
Image_Certificate nvarchar(max),
Student_ID bigint unique foreign key references Student(Student_ID),
Dep_ID int foreign key references Department(Dep_ID)
)
go

insert into Enrollment values(998800,'2016-8-1',65.2,'images (1).jpg',112200,123);
insert into Enrollment values(998801,'2017-9-1',70.9,'images (2).jpg',112201,123);
insert into Enrollment values(998802,'2018-10-1',80.7,'images (3).jpg',112202,124);
insert into Enrollment values(998803,'2019-11-1',90.4,'images (4).jpg',112203,124);
insert into Enrollment values(998804,'2020-12-1',92.6,'images (5).jpg',112204,125);
insert into Enrollment values(998805,'2016-8-2',86.7,'images (6).jpg',112205,125);
insert into Enrollment values(998806,'2017-9-2',80.2,'images (7).jpg',112206,126);
insert into Enrollment values(998807,'2018-10-2',60.5,'images (8).jpg',112207,126);
insert into Enrollment values(998808,'2019-11-2',50.5,'images (9).jpg',112208,127);
insert into Enrollment values(998809,'2020-12-2',55.5,'images (10).jpg',112209,127);
insert into Enrollment values(998810,'2016-8-3',66.7,'images (11).jpg',112210,128);
insert into Enrollment values(998811,'2017-9-3',77.2,'images (12).jpg',112211,128);
insert into Enrollment values(998812,'2018-10-3',90.5,'images (13).jpg',112212,129);
insert into Enrollment values(998813,'2019-11-3',88.5,'images (14).jpg',112213,129);
insert into Enrollment values(998814,'2020-12-3',99.0,'images (15).jpg',112214,130);
insert into Enrollment values(998815,'2016-8-4',81.4,'images (16).jpg',112215,130);
insert into Enrollment values(998816,'2017-9-4',74.3,'images (17).jpg',112216,131);
insert into Enrollment values(998817,'2018-10-4',91.8,'images (18).jpg',112217,131);
insert into Enrollment values(998818,'2019-11-4',92.8,'images (19).jpg',112218,132);
insert into Enrollment values(998819,'2020-12-4',93.8,'images (20).jpg',112219,132);
insert into Enrollment values(998820,'2016-8-5',70.1,'images (21).jpg',112220,133);
insert into Enrollment values(998821,'2017-9-5',75.1,'images (22).jpg',112221,133);
insert into Enrollment values(998822,'2018-10-5',78.1,'images (23).jpg',112222,134);
insert into Enrollment values(998823,'2019-11-5',67.3,'images (24).jpg',112223,134);
insert into Enrollment values(998824,'2020-12-5',69.3,'images (25).jpg',112224,135);
insert into Enrollment values(998825,'2016-8-6',92.3,'images (26).jpg',112225,135);
insert into Enrollment values(998826,'2017-9-6',68.3,'images (27).jpg',112226,136);
insert into Enrollment values(998827,'2018-10-6',79.3,'images (28).jpg',112227,136);
insert into Enrollment values(998828,'2019-11-6',86.9,'images (29).jpg',112228,137);
insert into Enrollment values(998829,'2020-12-6',65.0,'images (30).jpg',112229,137);
insert into Enrollment values(998830,'2016-8-7',66.0,'images (31).jpg',112230,138);
insert into Enrollment values(998831,'2017-9-7',67.0,'images (32).jpg',112231,138);
insert into Enrollment values(998832,'2018-10-7',68.0,'images (33).jpg',112232,139);
insert into Enrollment values(998833,'2019-11-7',69.0,'images (34).jpg',112233,139);
insert into Enrollment values(998834,'2020-12-7',70.2,'images (35).jpg',112234,140);
insert into Enrollment values(998835,'2016-8-8',71.2,'images (36).jpg',112235,140);
insert into Enrollment values(998836,'2017-9-8',72.2,'images (37).jpg',112236,141);
insert into Enrollment values(998837,'2018-10-8',73.2,'images (38).jpg',112237,141);
insert into Enrollment values(998838,'2019-11-8',74.2,'images (39).jpg',112238,142);
insert into Enrollment values(998839,'2020-12-8',75.5,'images (40).jpg',112239,142);
insert into Enrollment values(998840,'2016-8-9',76.7,'images (41).jpg',112240,143);
insert into Enrollment values(998841,'2017-9-9',77.2,'images (42).jpg',112241,143);
insert into Enrollment values(998842,'2018-10-9',78.5,'images (43).jpg',112242,144);
insert into Enrollment values(998843,'2019-11-9',79.5,'images (44).jpg',112243,144);
insert into Enrollment values(998844,'2020-12-9',99.4,'images (45).jpg',112244,145);
insert into Enrollment values(998845,'2016-8-10',91.4,'images (46).jpg',112245,145);
insert into Enrollment values(998846,'2017-9-10',92.4,'images (47).jpg',112246,146);
insert into Enrollment values(998847,'2018-10-10',93.4,'images (48).jpg',112247,146);
insert into Enrollment values(998848,'2019-11-10',94.4,'images (49).jpg',112248,147);
insert into Enrollment values(998849,'2020-12-10',95.6,'images (50).jpg',112249,147);
insert into Enrollment values(998850,'2016-8-11',96.6,'images (51).jpg',112250,148);
insert into Enrollment values(998851,'2017-9-11',97.6,'images (52).jpg',112251,148);
insert into Enrollment values(998852,'2018-10-11',88.6,'images (53).jpg',112252,149);
insert into Enrollment values(998853,'2019-11-11',89.6,'images (54).jpg',112253,149);
insert into Enrollment values(998854,'2020-12-11',90.6,'images (55).jpg',112254,150);
insert into Enrollment values(998855,'2016-8-12',91.7,'images (56).jpg',112255,150);
insert into Enrollment values(998856,'2017-9-12',92.2,'images (57).jpg',112256,151);
insert into Enrollment values(998857,'2018-10-12',93.5,'images (58).jpg',112257,151);
insert into Enrollment values(998858,'2019-11-12',94.5,'images (59).jpg',112258,152);
insert into Enrollment values(998859,'2020-12-12',95.5,'images (60).jpg',112259,152);
insert into Enrollment values(998860,'2016-8-13',96.7,'images (61).jpg',112260,153);
insert into Enrollment values(998861,'2017-9-13',97.2,'images (62).jpg',112261,153);
insert into Enrollment values(998862,'2018-10-13',98.5,'images (63).jpg',112262,154);
insert into Enrollment values(998863,'2019-11-13',99.5,'images (64).jpg',112263,154);
insert into Enrollment values(998864,'2020-12-13',99.1,'images (65).jpg',112264,155);
insert into Enrollment values(998865,'2016-8-14',85.9,'images (66).jpg',112265,155);
insert into Enrollment values(998866,'2017-9-14',80.9,'images (67).jpg',112266,156);
insert into Enrollment values(998867,'2018-10-14',90.9,'images (68).jpg',112267,156);
insert into Enrollment values(998868,'2019-11-14',91.9,'images (69).jpg',112268,157);
insert into Enrollment values(998869,'2020-12-14',80.9,'images (70).jpg',112269,157);
insert into Enrollment values(998870,'2016-8-15',73.9,'images (71).jpg',112270,158);
insert into Enrollment values(998871,'2017-9-15',82.9,'images (72).jpg',112271,158);
insert into Enrollment values(998872,'2018-10-15',95.9,'images (73).jpg',112272,159);
insert into Enrollment values(998873,'2019-11-15',66.9,'images (74).jpg',112273,159);
insert into Enrollment values(998874,'2020-12-15',89.9,'images (75).jpg',112274,160);
insert into Enrollment values(998875,'2016-8-16',78.9,'images (76).jpg',112275,160);
insert into Enrollment values(998876,'2017-9-16',99.9,'images (77).jpg',112276,161);
insert into Enrollment values(998877,'2018-10-16',64.9,'images (78).jpg',112277,161);
insert into Enrollment values(998878,'2019-11-16',68.9,'images (79).jpg',112278,162);
insert into Enrollment values(998879,'2020-12-16',86.9,'images (80).jpg',112279,162);
insert into Enrollment values(998880,'2016-8-17',84.7,'images (81).jpg',112280,163);
insert into Enrollment values(998881,'2017-9-17',80.2,'images (82).jpg',112281,163);
insert into Enrollment values(998882,'2018-10-17',93.5,'images (83).jpg',112282,164);
insert into Enrollment values(998883,'2019-11-17',95.5,'images (84).jpg',112283,164);
insert into Enrollment values(998884,'2020-12-17',99.5,'images (85).jpg',112284,165);
insert into Enrollment values(998885,'2016-8-18',8.7,'images (86).jpg',112285,165);
insert into Enrollment values(998886,'2017-9-18',83.2,'images (87).jpg',112286,165);
insert into Enrollment values(998887,'2018-10-18',99.5,'images (88).jpg',112287,166);
insert into Enrollment values(998888,'2019-11-18',97.5,'images (89).jpg',112288,166);
insert into Enrollment values(998889,'2020-12-18',93.5,'images (90).jpg',112289,166);
insert into Enrollment values(998890,'2016-8-19',91.7,'images (91).jpg',112290,167);
insert into Enrollment values(998891,'2017-9-19',92.2,'images (92).jpg',112291,167);
insert into Enrollment values(998892,'2018-10-19',93.5,'images (93).jpg',112292,167);
insert into Enrollment values(998893,'2019-11-19',94.5,'images (94).jpg',112293,168);
insert into Enrollment values(998894,'2020-12-19',95.5,'images (95).jpg',112294,168);
insert into Enrollment values(998895,'2016-8-20',96.7,'images (96).jpg',112295,168);
insert into Enrollment values(998896,'2017-9-20',91.2,'images (97).jpg',112296,169);
insert into Enrollment values(998897,'2018-10-20',93.5,'images (98).jpg',112297,169);
insert into Enrollment values(998898,'2019-11-20',96.5,'images (99).jpg',112298,169);
insert into Enrollment values(998899,'2020-12-20',91.5,'images (100).jpg',112299,169);

select * from Enrollment;

SELECT * FROM University u
join College c
on u.Univ_ID=c.Univ_ID
join Department d
on c.College_ID=d.College_ID
join Enrollment e
on d.Dep_ID=e.Dep_ID
join Student s
on e.Student_ID=s.Student_ID;

------------------------------------------------------------------
--SELECT s.First_Name, s.Last_Name, c.College_Name, e.Grade
--FROM University u
--join College c
--on u.Univ_ID=c.Univ_ID
--join Department d
--on c.College_ID=d.College_ID
--join Enrollment e
--on d.Dep_ID=e.Dep_ID
--join Student s
--on e.Student_ID=s.Student_ID
--where u.Univ_Name='Salahaddin';

--update Student
--set First_Name='hahahaha', Last_Name='hohohho' where Student_ID=112233;

--SELECT e.Dep_ID, d.Dep_ID, d.Dep_Name, d.Supervisor, d.College_ID, 
--    c.College_ID, c.College_Name, c.Dean, c.Univ_ID
--    FROM University u
--    join College c
--    on u.Univ_ID=c.Univ_ID
--    join Department d
--    on c.College_ID=d.College_ID
--    join Enrollment e
--    on d.Dep_ID=e.Dep_ID
--    join Student s
--    on e.Student_ID=s.Student_ID
--    where u.Univ_Name='Salahaddin' and c.College_Name='Science' and d.Dep_Name='CS & IT'; 