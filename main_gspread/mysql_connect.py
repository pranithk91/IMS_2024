

import mysql.connector
from mysql.connector import Error

query = """Insert into DeliveryBills values ('YMAS5183','2023-12-01','Yathiraja Medical and Surgical Agencies',3018,'1',5.00141043723554,'0','Paid','Cash','2023-12-27','','');
Insert into DeliveryBills values ('RD17320','2023-12-04','Shanmukha Medical Agencies',7334,'1',5,'1','Paid','Cash','2024-01-27','','');
Insert into DeliveryBills values ('CD1344','2023-12-04','Shanmukha Medical Agencies',703,'0',100,'1','Done','',NULL,'','');
Insert into DeliveryBills values ('CD1343','2023-12-04','Shanmukha Medical Agencies',266,'0',100,'1','Done','',NULL,'','');
Insert into DeliveryBills values ('RD17319','2023-12-04','Shanmukha Medical Agencies',1990,'1',5,'1','Paid','Cash','2024-01-27','','');
Insert into DeliveryBills values ('A01396','2023-12-05','Medicure Medical and Surgical Agencies',6514,'0',4,'1','Paid','Cash','2024-01-09','','');
Insert into DeliveryBills values ('YMAS5259','2023-12-05','Yathiraja Medical and Surgical Agencies',3018,'1',5,'1','Paid','Cash','2023-12-27','','');
Insert into DeliveryBills values ('SMA006765','2023-12-05','Siddartha Medical Agencies',2569,'1',5.0002115148695,'1','Paid','Cash','2024-01-08','','');
Insert into DeliveryBills values ('RK05222','2023-12-05','Siddartha Medical & Surgical Agencies',3572,'1',5,'0','Paid','UPI','2024-01-26','402632646472','');
Insert into DeliveryBills values ('RK05259','2023-12-06','Siddartha Medical & Surgical Agencies',0,'1',0,'0','Paid','UPI','2024-01-26','402632646472','');
Insert into DeliveryBills values ('XF20749','2023-12-06','Sree Saptagiri Pharma Distributors',5760,'0',4,'1','Paid','Cash','2024-01-10','','');
Insert into DeliveryBills values ('CIA000708','2023-12-06','M S S Pharmaceuticals',2453,'1',2,'1','Paid','Cash','2024-01-24','','');
Insert into DeliveryBills values ('RLF34535','2023-12-07','Sri Jaya Krishna Medical Agencies',3010,'1',5.00012372168983,'0','Paid','Cash','2024-01-03','','');
Insert into DeliveryBills values ('NMA1134','2023-12-08','Neelakanteswara Medical Agency',1079,'1',5,'1','Paid','Cash','2024-01-23','','');
Insert into DeliveryBills values ('A01436','2023-12-12','Medicure Medical and Surgical Agencies',3657,'0',4,'1','Paid','Cash','2024-01-09','','');
Insert into DeliveryBills values ('A01444','2023-12-13','Medicure Medical and Surgical Agencies',3675,'0',4,'1','Paid','Cash','2024-01-09','','');
Insert into DeliveryBills values ('NMA1153','2023-12-14','Neelakanteswara Medical Agency',2880,'1',5,'1','Paid','Cash','2024-01-23','','');
Insert into DeliveryBills values ('A01458','2023-12-14','Medicure Medical and Surgical Agencies',2303,'0',4,'1','Paid','Cash','2024-01-09','','');
Insert into DeliveryBills values ('RK05451','2023-12-14','Siddartha Medical & Surgical Agencies',9031,'1',5,'1','Paid','UPI','2024-01-26','402632646472','');
Insert into DeliveryBills values ('AB07001','2023-12-14','Maheswari Agencies',4472,'1',5,'1','Paid','Cash','2024-01-11','','');
Insert into DeliveryBills values ('23-24/014768','2023-12-15','Sri Lakshmi Venkateswara Agencies',4431,'1',5.00012649581299,'1','Paid','UPI','2024-01-19','T2401191918191305204251','');
Insert into DeliveryBills values ('RI20529','2023-12-15','Sri Sujit Pharma',4456,'1',5,'1','Paid','Cash','2024-01-24','','');
Insert into DeliveryBills values ('RK05484','2023-12-15','Siddartha Medical & Surgical Agencies',0,'0',0,'0','Paid','UPI','2024-01-26','402632646472','');
Insert into DeliveryBills values ('AB07063','2023-12-16','Maheswari Agencies',3101,'1',5,'1','Paid','Cash','2024-01-11','','');
Insert into DeliveryBills values ('RK05543','2023-12-18','Siddartha Medical & Surgical Agencies',3648,'1',5,'0','Paid','UPI','2024-02-05','403690325618','');
Insert into DeliveryBills values ('','2023-12-18','Rajesh Medical Agencies',1406,'1',5,'1','Paid','',NULL,'','');
Insert into DeliveryBills values ('RD18659','2023-12-22','Shanmukha Medical Agencies',1668,'1',5,'1','Paid','Cash','2024-01-27','','');
Insert into DeliveryBills values ('C000712','2023-12-23','M R Medical Agencies',5658,'0',4,'1','Paid','Cash','2024-01-09','','');
Insert into DeliveryBills values ('RK05662','2023-12-23','Siddartha Medical & Surgical Agencies',3595,'1',5,'0','Paid','UPI','2024-01-26','402632646472','');
Insert into DeliveryBills values ('NMA1195','2023-12-23','Neelakanteswara Medical Agency',5092,'1',4,'0','Paid','Cash','2024-01-23','','');
Insert into DeliveryBills values ('RLF36794','2023-12-23','Sri Jaya Krishna Medical Agencies',3216,'0',5,'0','Paid','Cash','2024-01-03','','');
Insert into DeliveryBills values ('A01519','2023-12-25','Medicure Medical and Surgical Agencies',4696,'0',4,'1','Paid','Cash','2024-01-09','','');
Insert into DeliveryBills values ('NMA1200','2023-12-25','Neelakanteswara Medical Agency',10488,'1',5,'1','Paid','Cash','2024-01-23','','');
Insert into DeliveryBills values ('YMAS5643','2023-12-25','Yathiraja Medical and Surgical Agencies',5490,'1',5,'1','Paid','Cash','2024-01-18','','');
Insert into DeliveryBills values ('XF22245','2023-12-25','Sree Saptagiri Pharma Distributors',6240,'0',4,'0','Paid','Cash','2024-03-30','','');
Insert into DeliveryBills values ('RK05685','2023-12-25','Siddartha Medical & Surgical Agencies',3553,'1',5,'0','Paid','UPI','2024-01-26','402632646472','');
Insert into DeliveryBills values ('RD18923','2023-12-26','Shanmukha Medical Agencies',2850,'1',5,'1','Paid','Cash','2024-01-27','','');
Insert into DeliveryBills values ('23R7359','2023-12-26','AR Medical Agencies',7835,'0',3,'1','Paid','UPI','2024-01-30','T2401301506409730035253','');
Insert into DeliveryBills values ('RI21303','2023-12-26','Sri Sujit Pharma',1882,'1',5,'1','Paid','Cash','2024-01-24','','');
Insert into DeliveryBills values ('YMAS5677','2023-12-26','Yathiraja Medical and Surgical Agencies',4191,'1',5,'1','Paid','Cash','2024-01-18','','');
Insert into DeliveryBills values ('CF28032','2023-12-26','Vasu Medical Enterprises',11696,'1',3.99996766105915,'0','Paid','Cash','2024-02-10','','1956 also paid on same date for 16 nov bill-23935');
Insert into DeliveryBills values ('RLF36875','2023-12-26','Sri Jaya Krishna Medical Agencies',3572,'1',5.00008936177818,'0','Paid','Cash','2024-01-18','','');
Insert into DeliveryBills values ('RK05696','2023-12-26','Siddartha Medical & Surgical Agencies',5937,'1',5,'0','Paid','UPI','2024-01-26','402632646472','');
Insert into DeliveryBills values ('A01528','2023-12-27','Medicure Medical and Surgical Agencies',6022,'0',4,'1','Paid','Cash','2024-01-09','','');
Insert into DeliveryBills values ('A004695','2023-12-27','Sri Lakshmi Balaji Medi Needs',2712,'0',4,'1','Paid','Cash','2024-01-19','','');
Insert into DeliveryBills values ('RC10793','2023-12-27','Janardhan Medical Agencies',2964,'1',5,'0','Paid','Cash','2024-02-26','','');
Insert into DeliveryBills values ('AB07311','2023-12-27','Maheswari Agencies',9769,'1',4.00004073706938,'0','Paid','Cash','2024-03-11','','');
Insert into DeliveryBills values ('CI00487','2023-12-27','Madeena Medical & Surgical Agencies',2014,'0',0,'1','Paid','Cash','2024-01-18','','');
Insert into DeliveryBills values ('AB07353','2023-12-28','Maheswari Agencies',3410,'1',4,'1','Paid','Cash','2024-03-11','','');
Insert into DeliveryBills values ('RK05752','2023-12-28','Siddartha Medical & Surgical Agencies',6900,'1',5,'0','Paid','UPI','2024-01-26','402632646472','');
Insert into DeliveryBills values ('23-24/015402','2023-12-28','Sri Lakshmi Venkateswara Agencies',2987,'1',5,'0','Paid','Cash','2024-02-10','','');
Insert into DeliveryBills values ('CI00492','2023-12-29','Madeena Medical & Surgical Agencies',941,'0',0,'1','Paid','Cash','2024-01-18','','');
Insert into DeliveryBills values ('NMA1236','2023-12-30','Neelakanteswara Medical Agency',4280,'0',5,'1','Paid','Cash','2024-01-23','','');
Insert into DeliveryBills values ('RK05815','2023-12-30','Siddartha Medical & Surgical Agencies',2242,'1',5,'0','Paid','UPI','2024-01-26','402632646472','');
Insert into DeliveryBills values ('SMA007471','2023-12-30','Siddartha Medical Agencies',2220,'1',4.99976038721426,'0','Paid','',NULL,'','');
Insert into DeliveryBills values ('YMAS5802','2024-01-02','Yathiraja Medical and Surgical Agencies',3283,'1',4.99189627228525,'1','Paid','Cash','2024-01-30','','');
Insert into DeliveryBills values ('AB07481','2024-01-02','Maheswari Agencies',2304,'1',3.99983199865599,'1','Paid','Cash','2024-03-11','','');
Insert into DeliveryBills values ('RD19425','2024-01-03','Shanmukha Medical Agencies',10267,'1',5,'1','Paid','Cash','2024-01-27','','');
Insert into DeliveryBills values ('CD1471','2024-01-04','Shanmukha Medical Agencies',5134,'0',100,'1','Done','',NULL,'','Do Not Pay. Discounts bill');
Insert into DeliveryBills values ('YMAS5840','2024-01-04','Yathiraja Medical and Surgical Agencies',814,'1',5.00052265718915,'1','Paid','Cash','2024-01-30','','');
Insert into DeliveryBills values ('AR2324/04875','2024-01-08','Ascent Therapeutics',14535,'1',2,'1','Paid','Cash','2024-04-05','','no offer salex l');
Insert into DeliveryBills values ('YMAS5918','2024-01-09','Yathiraja Medical and Surgical Agencies',488,'1',5,'1','Paid','Cash','2024-01-30','','');
Insert into DeliveryBills values ('XF23471','2024-01-09','Sree Saptagiri Pharma Distributors',12192,'1',4,'1','Paid','Cash','2024-02-08','','');
Insert into DeliveryBills values ('CD1512','2024-01-10','Shanmukha Medical Agencies',1557,'0',100,'1','Done','',NULL,'','');
Insert into DeliveryBills values ('RD19990','2024-01-10','Shanmukha Medical Agencies',12674,'1',5,'1','Paid','Cash','2024-03-02','','');
Insert into DeliveryBills values ('SMA007793','2024-01-10','Siddartha Medical Agencies',3744,'1',5,'1','Paid','Cash','2024-02-06','','');
Insert into DeliveryBills values ('CH17113','2024-01-10','Rajesh Medical Agencies',9383,'0',3.5,'1','Paid','Cash','2024-02-03','','');
Insert into DeliveryBills values ('YMAS5995','2024-01-11','Yathiraja Medical and Surgical Agencies',2520,'1',5,'1','Paid','Cash','2024-01-30','','');
Insert into DeliveryBills values ('A01638','2024-01-11','Medicure Medical and Surgical Agencies',6169,'0',4,'1','Paid','Cash','2024-02-06','','');
Insert into DeliveryBills values ('R122636','2024-01-11','Sri Sujit Pharma',3962,'0',4,'1','Paid','Cash','2024-03-06','','');
Insert into DeliveryBills values ('AB07745','2024-01-12','Maheswari Agencies',11216,'1',4.00001974197242,'1','Paid','Cash','2024-03-11','','');
Insert into DeliveryBills values ('RK06111','2024-01-12','Siddartha Medical & Surgical Agencies',2530,'0',4,'1','Paid','UPI','2024-02-27','405831641756','');
Insert into DeliveryBills values ('23R7856','2024-01-12','AR Medical Agencies',6944,'0',4,'1','Paid','UPI','2024-02-05','403690311007','');
Insert into DeliveryBills values ('RK06138','2024-01-13','Siddartha Medical & Surgical Agencies',5176,'0',4,'1','Paid','UPI','2024-02-27','405831641756','');
Insert into DeliveryBills values ('RK06197','2024-01-17','Siddartha Medical & Surgical Agencies',5580,'0',4,'1','Paid','UPI','2024-02-27','405831641756','');
Insert into DeliveryBills values ('CD1537','2024-01-17','Shanmukha Medical Agencies',2220,'0',100,'1','Done','',NULL,'','Do Not Pay. Discount Bill');
Insert into DeliveryBills values ('RD20413','2024-01-17','Shanmukha Medical Agencies',3306,'1',5,'1','Paid','Cash','2024-03-02','','');
Insert into DeliveryBills values ('A01673','2024-01-17','Medicure Medical and Surgical Agencies',7698,'0',4,'1','Paid','Cash','2024-02-06','','');
Insert into DeliveryBills values ('RK06232','2024-01-18','Siddartha Medical & Surgical Agencies',3840,'0',4,'1','Paid','UPI','2024-02-27','405831641756','');
Insert into DeliveryBills values ('AB07907','2024-01-18','Maheswari Agencies',5929,'1',3.72018890200708,'1','Paid','Cash','2024-03-11','','');
Insert into DeliveryBills values ('A005068','2024-01-19','Sri Lakshmi Balaji Medi Needs',3426,'0',4,'1','Paid','Cash','2024-02-27','','');
Insert into DeliveryBills values ('23-24/016706','2024-01-19','Sri Lakshmi Venkateswara Agencies',3120,'0',4,'1','Paid','Cash','2024-02-10','','');
Insert into DeliveryBills values ('23R8003','2024-01-19','AR Medical Agencies',2171,'0',4,'1','Paid','UPI','2024-02-05','403690311007','');
Insert into DeliveryBills values ('RK06308','2024-01-20','Siddartha Medical & Surgical Agencies',3260,'0',4,'1','Paid','UPI','2024-02-27','405831641756','');
Insert into DeliveryBills values ('NMA1352','2024-01-22','Neelakanteswara Medical Agency',7227,'0',4,'1','Paid','Cash','2024-02-13','','');
Insert into DeliveryBills values ('SMA008134','2024-01-23','Siddartha Medical Agencies',1112,'0',5,'1','Paid','Cash','2024-02-06','','');
Insert into DeliveryBills values ('CH17883','2024-01-23','Rajesh Medical Agencies',9472,'0',4,'1','Paid','Cash','2024-03-02','','');
Insert into DeliveryBills values ('RK06379','2024-01-23','Siddartha Medical & Surgical Agencies',13713,'1',3.59461824546051,'1','Paid','UPI','2024-02-27','405831641756','');
Insert into DeliveryBills values ('A01714','2024-01-23','Medicure Medical and Surgical Agencies',5818,'0',4,'1','Paid','UPI','2024-03-19','T2403191321277877026763','');
Insert into DeliveryBills values ('MR02065','2024-01-23','Aruna Medical Agencies',7367,'0',4,'1','Paid','Cash','2024-01-31','','');
Insert into DeliveryBills values ('RD20928','2024-01-24','Shanmukha Medical Agencies',1406,'1',5,'1','Paid','Cash','2024-03-02','','');
Insert into DeliveryBills values ('CD1561','2024-01-24','Shanmukha Medical Agencies',740,'0',100,'1','Done','',NULL,'','Do Not Pay. Discount Bill');
Insert into DeliveryBills values ('RK06399','2024-01-24','Siddartha Medical & Surgical Agencies',4126,'1',4,'1','Paid','UPI','2024-02-27','405831641756','');
Insert into DeliveryBills values ('FR09516','2024-01-24','Arogya Medical & Surgical Agencies',4608,'0',4,'1','Paid','Cash','2024-03-21','','');
Insert into DeliveryBills values ('SK00470','2024-01-24','Skinova Health Care Pvt Ltd.',1040,'0',5,'1','Paid','UPI','2024-03-27','T2403271321151413538095','In the name of the clinic');
Insert into DeliveryBills values ('RC11982','2024-01-25','Janardhan Medical Agencies',6584,'0',5,'1','Paid','Cash','2024-02-26','','');
Insert into DeliveryBills values ('A808064','2024-01-25','Maheswari Agencies',3871,'1',4.00004444493828,'1','Paid','Cash','2024-03-11','','');
Insert into DeliveryBills values ('A001454','2024-01-27','M R Medical Agencies',6451,'1',3.531080452643,'1','Paid','Cash','2024-02-27','','');
Insert into DeliveryBills values ('A3360976','2024-01-31','Maruti Agencies',8710,'0',4,'1','Paid','Cash','2024-03-05','','');
Insert into DeliveryBills values ('R124288','2024-02-01','Sri Sujit Pharma',7924,'0',4,'1','Paid','Cash','2024-03-06','','');
Insert into DeliveryBills values ('A01778','2024-02-01','Medicure Medical and Surgical Agencies',7112,'0',4,'1','Paid','UPI','2024-03-19','T2403191321277877026763','');
Insert into DeliveryBills values ('R124294','2024-02-01','Sri Sujit Pharma',3899,'0',4,'1','Paid','Cash','2024-03-06','','');
Insert into DeliveryBills values ('RD21556','2024-02-02','Shanmukha Medical Agencies',4674,'1',5,'1','Paid','Cash','2024-03-02','','');
Insert into DeliveryBills values ('CD1603','2024-02-02','Shanmukha Medical Agencies',2160,'0',100,'1','Done','',NULL,'','');
Insert into DeliveryBills values ('RD21557','2024-02-02','Shanmukha Medical Agencies',5928,'1',5,'1','Paid','Cash','2024-03-02','','');
Insert into DeliveryBills values ('A01782','2024-02-02','Medicure Medical and Surgical Agencies',7184,'0',4,'1','Paid','UPI','2024-03-19','T2403191321277877026763','');
Insert into DeliveryBills values ('CH18588','2024-02-02','Rajesh Medical Agencies',3960,'0',4,'1','Paid','Cash','2024-03-02','','');
Insert into DeliveryBills values ('RK06618','2024-02-02','Siddartha Medical & Surgical Agencies',7123,'1',4,'1','Paid','UPI','2024-03-21','408171937779','');
Insert into DeliveryBills values ('A005288','2024-02-03','Sri Lakshmi Balaji Medi Needs',4832,'0',4,'1','Paid','Cash','2024-02-10','','');
Insert into DeliveryBills values ('R124529','2024-02-05','Sri Sujit Pharma',9381,'0',4,'1','Paid','Cash','2024-03-06','','');
Insert into DeliveryBills values ('AB08338','2024-02-05','Maheswari Agencies',15760,'1',3.72005076142132,'1','Paid','Cash','2024-03-11','','');
Insert into DeliveryBills values ('XF25696','2024-02-06','Sree Saptagiri Pharma Distributors',5760,'0',4,'1','Paid','Cash','2024-03-30','','');
Insert into DeliveryBills values ('RD21959','2024-02-07','Shanmukha Medical Agencies',5820,'1',5,'1','Paid','Cash','2024-03-02','','');
Insert into DeliveryBills values ('SK00517','2024-02-07','Skinova Health Care Pvt Ltd.',4816,'0',5,'1','Paid','UPI','2024-03-27','T2403271321151413538095','');
Insert into DeliveryBills values ('RLF43202','2024-02-07','Sri Jaya Krishna Medical Agencies',6202,'1',5,'1','Paid','Cash','2024-02-28','','');
Insert into DeliveryBills values ('RD21983','2024-02-08','Shanmukha Medical Agencies',3085,'1',5,'1','Paid','Cash','2024-03-02','','');
Insert into DeliveryBills values ('YMAS6506','2024-02-08','Yathiraja Medical and Surgical Agencies',5064,'1',5,'1','Paid','Cash','2024-03-11','','');
Insert into DeliveryBills values ('NMA1454','2024-02-09','Neelakanteswara Medical Agency',452,'1',3.71681415929204,'1','Paid','Cash','2024-02-13','','');
Insert into DeliveryBills values ('RK06783','2024-02-09','Siddartha Medical & Surgical Agencies',2770,'1',4,'1','Paid','UPI','2024-03-21','408171937779','');
Insert into DeliveryBills values ('RK06841','2024-02-12','Siddartha Medical & Surgical Agencies',5799,'1',4,'1','Paid','UPI','2024-03-21','408171937779','');
Insert into DeliveryBills values ('ANHVA12773','2024-02-13','Laxmi Sai Santhosh Medical & Surgical Agencies',996,'0',2,'1','Paid','Cash','2024-04-05','','');
Insert into DeliveryBills values ('RK07085','2024-02-22','Siddartha Medical & Surgical Agencies',5666,'1',4,'1','Paid','UPI','2024-03-21','408171937779','');
Insert into DeliveryBills values ('RK07105','2024-02-23','Siddartha Medical & Surgical Agencies',1037,'1',4,'1','Paid','UPI','2024-03-21','408171937779','');
Insert into DeliveryBills values ('AH021168','2024-02-23','Pavan Sai Medical & Surgicals',1564,'0',5,'1','','',NULL,'','');
Insert into DeliveryBills values ('SMA008979','2024-02-23','Siddartha Medical Agencies',2596,'1',4.0001692118956,'1','Paid','Cash','2024-03-19','','');
Insert into DeliveryBills values ('AB08839','2024-02-23','Maheswari Agencies',4148,'1',4.00004370438355,'1','Paid','NEFT','2024-04-19','N110242995555755','');
Insert into DeliveryBills values ('CH19949','2024-02-23','Rajesh Medical Agencies',3121,'0',4,'1','Paid','NEFT','2024-04-22','N113242999697215','');
Insert into DeliveryBills values ('A01927','2024-02-23','Medicure Medical and Surgical Agencies',5456,'0',4,'1','Paid','UPI','2024-03-19','T2403191321277877026763','');
Insert into DeliveryBills values ('RLF45711','2024-02-26','Sri Jaya Krishna Medical Agencies',2329,'1',5,'1','Paid','Cash','2024-03-13','','');
Insert into DeliveryBills values ('RK07156','2024-02-26','Siddartha Medical & Surgical Agencies',5258,'1',4,'1','Paid','UPI','2024-03-21','408171937779','');
Insert into DeliveryBills values ('A01929','2024-02-26','Medicure Medical and Surgical Agencies',3125,'0',4,'1','Paid','UPI','2024-03-19','T2403191321277877026763','');
Insert into DeliveryBills values ('DRT016144','2024-02-26','Sri Chennakesava Medical Agencies',4040,'0',4,'1','Paid','UPI','2024-03-30','T2403301124147468116138','');
Insert into DeliveryBills values ('NMA1547','2024-02-26','Neelakanteswara Medical Agency',7389,'1',4.01090117385545,'1','Paid','Cash','2024-02-13','','');
Insert into DeliveryBills values ('A003660','2024-02-26','Sai Leela Medical Agencies',10716,'0',4,'1','Paid','NEFT','2024-04-15','N106242989435690','');
Insert into DeliveryBills values ('AB08930','2024-02-27','Maheswari Agencies',7496,'1',3.99995983544006,'1','Paid','NEFT','2024-04-19','N110242995555755','');
Insert into DeliveryBills values ('RK07229','2024-02-28','Siddartha Medical & Surgical Agencies',3686,'1',4,'1','Paid','UPI','2024-03-21','408171937779','');
Insert into DeliveryBills values ('23R9141','2024-02-28','AR Medical Agencies',7331,'0',4,'1','Paid','NEFT','2024-04-17','N108242992684554','');
Insert into DeliveryBills values ('A01941','2024-02-28','Medicure Medical and Surgical Agencies',1604,'0',4,'1','Paid','UPI','2024-03-19','T2403191321277877026763','');
Insert into DeliveryBills values ('RK07237','2024-02-29','Siddartha Medical & Surgical Agencies',4301,'1',4,'1','Paid','UPI','2024-03-21','408171937779','');
Insert into DeliveryBills values ('RK07281','2024-03-02','Siddartha Medical & Surgical Agencies',8187,'1',4,'1','Paid','NEFT','2024-04-19','N110242995548543','');
Insert into DeliveryBills values ('AB09083','2024-03-04','Maheswari Agencies',7250,'1',3.99995097348278,'1','Paid','NEFT','2024-04-19','N110242995555755','');
Insert into DeliveryBills values ('RLF46608','2024-03-04','Sri Jaya Krishna Medical Agencies',7731,'1',5.00006881649394,'1','Paid','Cash','2024-03-13','','');
Insert into DeliveryBills values ('A01978','2024-03-04','Medicure Medical and Surgical Agencies',7984,'1',4,'1','Paid','UPI','2024-04-20','T2404201126538155626755','');
Insert into DeliveryBills values ('RK07354','2024-03-05','Siddartha Medical & Surgical Agencies',5507,'1',4,'1','Paid','NEFT','2024-04-19','N110242995548543','');
Insert into DeliveryBills values ('NMA1585','2024-03-05','Neelakanteswara Medical Agency',3878,'1',4.00005544466622,'1','Paid','NEFT','2024-05-15','1568087255','');
Insert into DeliveryBills values ('A003797','2024-03-05','Sai Leela Medical Agencies',10030,'0',4,'1','Paid','NEFT','2024-04-15','N106242989435690','');
Insert into DeliveryBills values ('RK07369','2024-03-06','Siddartha Medical & Surgical Agencies',5290,'1',4,'1','Paid','NEFT','2024-04-19','N110242995548543','');
Insert into DeliveryBills values ('CH20684','2024-03-06','Rajesh Medical Agencies',8003,'1',4.00002760829353,'1','Paid','NEFT','2024-04-22','N113242999697215','');
Insert into DeliveryBills values ('NMA1589','2024-03-06','Neelakanteswara Medical Agency',9050,'1',3.99997554952444,'1','Paid','NEFT','2024-05-15','1568087255','');
Insert into DeliveryBills values ('RD23985','2024-03-07','Shanmukha Medical Agencies',5928,'1',5,'1','Paid','NEFT','2024-05-06','1557511407','');
Insert into DeliveryBills values ('23-24/019362','2024-03-07','Sri Lakshmi Venkateswara Agencies',5464,'0',4,'1','Paid','UPI','2024-03-22','444880538088','');
Insert into DeliveryBills values ('CH20748','2024-03-07','Rajesh Medical Agencies',3802,'1',4.00005656588511,'1','Paid','NEFT','2024-04-22','N113242999697215','');
Insert into DeliveryBills values ('XF28102','2024-03-07','Sree Saptagiri Pharma Distributors',5760,'0',5,'1','','',NULL,'','');
Insert into DeliveryBills values ('RK07432','2024-03-08','Siddartha Medical & Surgical Agencies',2765,'1',4,'1','Paid','NEFT','2024-04-19','N110242995548543','');
Insert into DeliveryBills values ('MR02379','2024-03-09','Aruna Medical Agencies',3660,'0',4,'1','Paid','Cash','2024-04-24','','');
Insert into DeliveryBills values ('RC13851','2024-03-09','Janardhan Medical Agencies',3240,'0',5,'1','Paid','Cash','2024-06-20','','');
Insert into DeliveryBills values ('RK07535','2024-03-13','Siddartha Medical & Surgical Agencies',4172,'1',4,'1','Paid','NEFT','2024-04-19','N110242995548543','');
Insert into DeliveryBills values ('CR321324','2024-03-14','Sri Anjani Agencies',19728,'0',4,'1','Paid','NEFT','2024-06-01','1585887166','');
Insert into DeliveryBills values ('AB09357','2024-03-15','Maheswari Agencies',17557,'1',4.00017721070353,'1','Paid','NEFT','2024-04-19','N110242995555755','');
Insert into DeliveryBills values ('RD24526','2024-03-15','Shanmukha Medical Agencies',12659,'1',5,'1','Paid','NEFT','2024-05-06','1557511407','');
Insert into DeliveryBills values ('SD00249','2024-03-15','Shanmukha Medical Agencies',646.08,'0',0,'1','Paid','NEFT','2024-05-06','1557511407','');
Insert into DeliveryBills values ('A006047','2024-03-16','Sri Lakshmi Balaji Medi Needs',6452,'0',4,'1','Paid','Cash','2024-04-04','','');
Insert into DeliveryBills values ('RK07608','2024-03-16','Siddartha Medical & Surgical Agencies',2106,'1',4,'1','Paid','NEFT','2024-04-19','N110242995548543','');
Insert into DeliveryBills values ('RD24677','2024-03-18','Shanmukha Medical Agencies',1088,'1',5,'1','Paid','NEFT','2024-05-06','1557511407','');
Insert into DeliveryBills values ('CH21478','2024-03-19','Rajesh Medical Agencies',2304,'1',4.00140056022409,'1','Paid','NEFT','2024-04-22','N113242999697215','');
Insert into DeliveryBills values ('SMA009681','2024-03-19','Siddartha Medical Agencies',2596,'1',4.0001692118956,'1','Paid','Cash','2024-03-30','','');
Insert into DeliveryBills values ('SKR02603','2024-03-20','Challa Pharma and Surgicals',4195,'0',4,'1','Paid','NEFT','2024-05-06','412713678132','');
Insert into DeliveryBills values ('AB09487','2024-03-20','Maheswari Agencies',3019,'1',4,'1','Paid','NEFT','2024-04-19','N110242995555755','');
Insert into DeliveryBills values ('RK07782','2024-03-25','Siddartha Medical & Surgical Agencies',7550,'1',4,'1','Paid','NEFT','2024-04-19','N110242995548543','');
Insert into DeliveryBills values ('AF30402','2024-03-25','Jyothi Agencies',98490,'1',2,'1','Paid','Cash','2024-03-25','Clinic Name','');
Insert into DeliveryBills values ('A02109','2024-03-25','Medicure Medical and Surgical Agencies',1942,'0',4,'1','Paid','UPI','2024-04-20','T2404201126538155626755','');
Insert into DeliveryBills values ('CH21929','2024-03-27','Rajesh Medical Agencies',8253,'1',3.99994788681015,'1','Paid','NEFT','2024-04-22','N113242999697215','');
Insert into DeliveryBills values ('A006214','2024-03-27','Sri Lakshmi Balaji Medi Needs',3032,'0',4,'1','Paid','NEFT','2024-05-07','412813433775','');
Insert into DeliveryBills values ('NMA1689','2024-03-27','Neelakanteswara Medical Agency',12278,'1',3.99995940345218,'1','Paid','NEFT','2024-05-15','1568087255','');
Insert into DeliveryBills values ('AB09644','2024-03-28','Maheswari Agencies',13525,'1',4.00033233632436,'1','Paid','NEFT','2024-04-19','N110242995555755','');
Insert into DeliveryBills values ('RK07830','2024-03-28','Siddartha Medical & Surgical Agencies',7373,'1',4,'1','Paid','NEFT','2024-04-19','N110242995548543','');
Insert into DeliveryBills values ('23R9810','2024-03-28','AR Medical Agencies',2835,'0',4,'1','Paid','NEFT','2024-04-17','N108242992684554','');
Insert into DeliveryBills values ('UVD23586','2024-03-29','Brinton Pharmaceuticals LTD',1,'0',0,'1','Paid','Cash','2024-03-30','','');
Insert into DeliveryBills values ('RK07861','2024-03-30','Siddartha Medical & Surgical Agencies',1609,'1',4,'1','Paid','NEFT','2024-04-19','N110242995548543','');
Insert into DeliveryBills values ('DRU0172','2024-04-03','Sri Chennakesava Medical Agencies',2808,'0',4,'1','Paid','UPI','2024-05-13','106858182264','');
Insert into DeliveryBills values ('RL00105','2024-04-03','Siddartha Medical & Surgical Agencies',9322,'1',4,'1','Paid','NEFT','2024-05-11','1564217051','');
Insert into DeliveryBills values ('RE00209','2024-04-03','Shanmukha Medical Agencies',3002,'1',5,'1','Paid','NEFT','2024-05-06','1557511407','');
Insert into DeliveryBills values ('CE0015','2024-04-03','Shanmukha Medical Agencies',1501,'0',100,'1','Paid','NEFT','2024-05-06','1557511407','');
Insert into DeliveryBills values ('RE00210','2024-04-03','Shanmukha Medical Agencies',5928,'1',5,'1','Paid','NEFT','2024-05-06','1557511407','');
Insert into DeliveryBills values ('B000067','2024-04-04','Sri Lakshmi Balaji Medi Needs',1434,'0',4,'1','Paid','NEFT','2024-05-07','412813433775','');
Insert into DeliveryBills values ('7VB0123','2024-04-05','Sri Veerabrahmendra Phrama',7607,'0',5,'1','Paid','NEFT','2024-06-06','415813931757','');
Insert into DeliveryBills values ('RE00481','2024-04-06','Shanmukha Medical Agencies',6726,'1',5,'1','Paid','NEFT','2024-05-06','1557511407','');
Insert into DeliveryBills values ('CE0035','2024-04-06','Shanmukha Medical Agencies',3363,'0',100,'1','Paid','NEFT','2024-05-06','1557511407','');
Insert into DeliveryBills values ('S00053','2024-04-06','Medicure Medical and Surgical Agencies',7086,'0',4,'1','Paid','NEFT','2024-05-23','1576425706','');
Insert into DeliveryBills values ('RL00170','2024-04-06','Siddartha Medical & Surgical Agencies',5952,'1',4,'1','Paid','NEFT','2024-05-11','1564217051','');
Insert into DeliveryBills values ('7VB0168','2024-04-08','Sri Veerabrahmendra Phrama',6048,'0',5,'1','Paid','NEFT','2024-06-06','415813931757','');
Insert into DeliveryBills values ('CJ00464','2024-04-08','Rajesh Medical Agencies',6524,'1',4.00006605128883,'1','Paid','NEFT','2024-05-11','1564219047','');
Insert into DeliveryBills values ('RL00198','2024-04-08','Siddartha Medical & Surgical Agencies',3291,'1',4,'1','Paid','NEFT','2024-05-11','1564217051','');
Insert into DeliveryBills values ('RL00179','2024-04-08','Siddartha Medical & Surgical Agencies',14796,'1',4,'1','Paid','NEFT','2024-05-11','1564217051','');
Insert into DeliveryBills values ('RE00694','2024-04-10','Shanmukha Medical Agencies',1718,'0',5,'1','Paid','NEFT','2024-05-06','1557511407','');
Insert into DeliveryBills values ('SMA00187','2024-04-10','Siddartha Medical Agencies',4585,'1',4.00074128984433,'1','Paid','UPI','2024-05-11','106692965034','');
Insert into DeliveryBills values ('D000025','2024-04-10','M R Medical Agencies',3239,'0',4,'1','Paid','NEFT','2024-05-20','1573990581','');
Insert into DeliveryBills values ('RL00214','2024-04-10','Siddartha Medical & Surgical Agencies',3057,'1',4,'1','Paid','NEFT','2024-05-11','1564217051','');
Insert into DeliveryBills values ('S00075','2024-04-10','Medicure Medical and Surgical Agencies',1926,'0',4,'1','Paid','NEFT','2024-05-23','1576425706','');
Insert into DeliveryBills values ('S00072','2024-04-10','Medicure Medical and Surgical Agencies',2846,'0',4,'1','Paid','NEFT','2024-05-23','1576425706','');
Insert into DeliveryBills values ('GR00245','2024-04-10','Maheswari Agencies',9432,'1',4.00022802417056,'1','Paid','NEFT','2024-05-22','1575604072','');
Insert into DeliveryBills values ('NMA2400041','2024-04-10','Neelakanteswara Medical Agency',8065,'1',4.05407231259796,'1','Paid','NEFT','2024-05-15','1568087255','');
Insert into DeliveryBills values ('RL00244','2024-04-12','Siddartha Medical & Surgical Agencies',13478,'1',4,'1','Paid','NEFT','2024-05-11','1564217051','');
Insert into DeliveryBills values ('YF01326','2024-04-15','Sree Saptagiri Pharma Distributors',10600,'0',4,'1','Paid','NEFT','2024-05-06','412713688458','');
Insert into DeliveryBills values ('NMA2400072','2024-04-15','Neelakanteswara Medical Agency',3379,'1',3.999933999934,'1','Paid','NEFT','2024-05-15','1568087255','');
Insert into DeliveryBills values ('SMA00335','2024-04-16','Siddartha Medical Agencies',2296,'1',4.00009865824783,'1','Paid','UPI','2024-05-11','106692965034','');
Insert into DeliveryBills values ('YMAS268','2024-04-16','Yathiraja Medical and Surgical Agencies',2534,'1',3.9998268098372,'1','Paid','UPI','2024-05-07','106414963695','');
Insert into DeliveryBills values ('RL00389','2024-04-18','Siddartha Medical & Surgical Agencies',2112,'1',4,'1','Paid','NEFT','2024-05-11','1564217051','');
Insert into DeliveryBills values ('AS00191','2024-04-19','Sree Challa Pharma and Surgicals',5631,'0',4,'1','Paid','UPI','2024-05-20','414128124582','');
Insert into DeliveryBills values ('RL00447','2024-04-20','Siddartha Medical & Surgical Agencies',6057,'1',4,'1','Paid','NEFT','2024-05-11','1564217051','');
Insert into DeliveryBills values ('S00134','2024-04-20','Medicure Medical and Surgical Agencies',1457,'0',4,'1','Paid','NEFT','2024-05-23','1576425706','');
Insert into DeliveryBills values ('NMA2400101','2024-04-22','Neelakanteswara Medical Agency',6059,'1',3.99985676430567,'1','Paid','NEFT','2024-05-15','1568087255','');
Insert into DeliveryBills values ('CJ01261','2024-04-22','Rajesh Medical Agencies',12753,'1',4.00008502678344,'1','Paid','NEFT','2024-05-11','1564219047','');
Insert into DeliveryBills values ('RLG03425','2024-04-25','Sri Jaya Krishna Medical Agencies',5335,'1',5,'1','Paid','UPI','2024-05-08','106462453668','');
Insert into DeliveryBills values ('A000101','2024-04-26','M R Medical Agencies',2227,'1',3.99979655154875,'1','Paid','NEFT','2024-06-07','1592481424','');
Insert into DeliveryBills values ('S00174','2024-04-26','Medicure Medical and Surgical Agencies',3013,'0',4,'1','Paid','NEFT','2024-05-23','1576425706','');
Insert into DeliveryBills values ('RL00566','2024-04-26','Siddartha Medical & Surgical Agencies',7987,'1',4,'1','Paid','NEFT','2024-05-11','1564217051','');
Insert into DeliveryBills values ('RL00581','2024-04-26','Siddartha Medical & Surgical Agencies',8987,'1',4,'1','Paid','NEFT','2024-05-11','1564217051','');
Insert into DeliveryBills values ('CJ01530','2024-04-27','Rajesh Medical Agencies',3802,'1',4.00005656588511,'1','Paid','NEFT','2024-05-11','1564219047','');
Insert into DeliveryBills values ('GR00657','2024-04-27','Maheswari Agencies',9539,'1',3.99995378714358,'1','Paid','NEFT','2024-05-22','1575604072','');
Insert into DeliveryBills values ('RD00029','2024-04-27','Uma Maheswara Medical Agencies',10512,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RG00182','2024-04-27','Gopala Krishna Agencies',10456,'0',4,'1','Paid','NEFT','2024-06-21','1608039688','');
Insert into DeliveryBills values ('RG00183','2024-04-27','Gopala Krishna Agencies',5228,'0',100,'1','Done','',NULL,'','');
Insert into DeliveryBills values ('RG00184','2024-04-27','Gopala Krishna Agencies',6240,'0',4,'1','Paid','NEFT','2024-06-21','1608039688','');
Insert into DeliveryBills values ('RL00616','2024-04-29','Siddartha Medical & Surgical Agencies',4915,'1',4,'1','Paid','NEFT','2024-05-11','1564217051','');
Insert into DeliveryBills values ('S00192','2024-04-29','Medicure Medical and Surgical Agencies',3885,'0',4,'1','Paid','NEFT','2024-05-23','1576425706','');
Insert into DeliveryBills values ('AR001083','2024-05-01','Visweswara Medical & Surgical Agencies',6000,'0',3.8,'1','Paid','NEFT','2024-06-01','1585600458','');
Insert into DeliveryBills values ('SM000012','2024-05-01','Sree Challa Pharma and Surgicals',3964,'0',4,'1','Paid','UPI','2024-06-07','108853182248','');
Insert into DeliveryBills values ('RL00741','2024-05-04','Siddartha Medical & Surgical Agencies',6566,'1',4,'1','Paid','IMPS','2024-06-18','1604601571','');
Insert into DeliveryBills values ('RJ02957','2024-05-07','Sri Sujit Pharma',3962,'0',4,'1','Paid','NEFT','2024-06-01','1585595049','');
Insert into DeliveryBills values ('RL00814','2024-05-07','Siddartha Medical & Surgical Agencies',6758,'1',4,'1','Paid','IMPS','2024-06-18','1604601571','');
Insert into DeliveryBills values ('GR00904','2024-05-07','Maheswari Agencies',5960,'1',3.99993505134552,'1','','',NULL,'','');
Insert into DeliveryBills values ('YF03379','2024-05-08','Sree Saptagiri Pharma Distributors',7880,'0',4,'1','Paid','NEFT','2024-06-03','1587325979','');
Insert into DeliveryBills values ('RL00846','2024-05-08','Siddartha Medical & Surgical Agencies',3232,'1',4,'1','Paid','IMPS','2024-06-18','1604601571','');
Insert into DeliveryBills values ('B000652','2024-05-08','Sri Lakshmi Balaji Medi Needs',4832,'0',4,'1','Paid','NEFT','2024-06-14','1601355141','');
Insert into DeliveryBills values ('CJ02178','2024-05-08','Rajesh Medical Agencies',2289,'1',3.99981208305929,'1','Paid','NEFT','2024-06-10','1595614217','');
Insert into DeliveryBills values ('RL00861','2024-05-09','Siddartha Medical & Surgical Agencies',4101,'1',4,'1','Paid','IMPS','2024-06-18','1604601571','');
Insert into DeliveryBills values ('CG03894','2024-05-09','Vasu Medical Enterprises',10340,'0',5,'1','','',NULL,'','');
Insert into DeliveryBills values ('CJ02213','2024-05-09','Rajesh Medical Agencies',2304,'1',4.00140056022409,'1','Paid','NEFT','2024-06-10','1595614217','');
Insert into DeliveryBills values ('NR00210','2024-05-10','Aruna Medical Agencies',3600,'0',4,'1','Paid','UPI','2024-05-23','107634297413','');
Insert into DeliveryBills values ('CJ02302','2024-05-10','Rajesh Medical Agencies',12719,'1',4,'1','Paid','NEFT','2024-06-10','1595614217','');
Insert into DeliveryBills values ('RJ03407','2024-05-14','Sri Sujit Pharma',10033,'0',4,'1','Paid','NEFT','2024-06-01','1585595049','');
Insert into DeliveryBills values ('GR01063','2024-05-15','Maheswari Agencies',8178,'1',4.00002165099676,'1','','',NULL,'','');
Insert into DeliveryBills values ('NMA2400215','2024-05-15','Neelakanteswara Medical Agency',4338,'1',3.99990598902161,'1','','',NULL,'','');
Insert into DeliveryBills values ('RL00983','2024-05-15','Siddartha Medical & Surgical Agencies',9216,'1',4,'1','Paid','IMPS','2024-06-18','1604601571','');
Insert into DeliveryBills values ('YF03942','2024-05-15','Sree Saptagiri Pharma Distributors',7120,'0',4,'1','Paid','NEFT','2024-06-03','1587325979','');
Insert into DeliveryBills values ('S00305','2024-05-15','Medicure Medical and Surgical Agencies',5376,'0',4,'1','Paid','NEFT','2024-06-27','1613663384','');
Insert into DeliveryBills values ('CJ02609','2024-05-16','Rajesh Medical Agencies',6336,'1',3.99996606027695,'1','Paid','NEFT','2024-06-10','1595614217','');
Insert into DeliveryBills values ('RE02849','2024-05-16','Shanmukha Medical Agencies',2280,'1',5,'1','Paid','NEFT','2024-06-10','1595606720','');
Insert into DeliveryBills values ('RG00294','2024-05-16','Gopala Krishna Agencies',6240,'0',4,'1','Paid','NEFT','2024-06-21','1608039688','');
Insert into DeliveryBills values ('RG00295','2024-05-16','Gopala Krishna Agencies',1320,'0',4,'1','Paid','NEFT','2024-06-21','1608039688','');
Insert into DeliveryBills values ('RG00296','2024-05-16','Gopala Krishna Agencies',1860,'0',100,'1','Done','',NULL,'','');
Insert into DeliveryBills values ('SMA01006','2024-05-16','Siddartha Medical Agencies',4601,'1',4.00004924652812,'1','','',NULL,'','');
Insert into DeliveryBills values ('RL01038','2024-05-17','Siddartha Medical & Surgical Agencies',1613,'1',4,'1','Paid','IMPS','2024-06-18','1604601571','');
Insert into DeliveryBills values ('S00338','2024-05-18','Medicure Medical and Surgical Agencies',4029,'0',4,'1','Paid','NEFT','2024-06-27','1613663384','');
Insert into DeliveryBills values ('GR01187','2024-05-20','Maheswari Agencies',6083,'1',3.99997171665747,'1','','',NULL,'','');
Insert into DeliveryBills values ('RL01131','2024-05-20','Siddartha Medical & Surgical Agencies',2291,'1',4,'1','Paid','IMPS','2024-06-18','1604601571','');
Insert into DeliveryBills values ('A000598','2024-05-20','Sai Leela Medical Agencies',5358,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RE03170','2024-05-21','Shanmukha Medical Agencies',4366,'1',5,'1','Paid','NEFT','2024-06-10','1595606720','');
Insert into DeliveryBills values ('A000207','2024-05-21','M R Medical Agencies',6036,'1',4.00056306306306,'1','Paid','NEFT','2024-06-07','1592481424','');
Insert into DeliveryBills values ('YF04504','2024-05-21','Sree Saptagiri Pharma Distributors',6320,'0',4,'1','Paid','NEFT','2024-06-03','1587325979','');
Insert into DeliveryBills values ('RJ03971','2024-05-21','Sri Sujit Pharma',2392,'0',4,'1','Paid','NEFT','2024-06-01','1585595049','');
Insert into DeliveryBills values ('24-25/002809','2024-05-22','Sri Lakshmi Venkateswara Agencies',3096,'0',4,'1','Paid','UPI','2024-06-20','109898968999','');
Insert into DeliveryBills values ('RL01211','2024-05-23','Siddartha Medical & Surgical Agencies',4838,'1',4,'1','Paid','IMPS','2024-06-18','1604601571','');
Insert into DeliveryBills values ('CE0203','2024-05-23','Shanmukha Medical Agencies',3972,'0',100,'1','Done','',NULL,'','');
Insert into DeliveryBills values ('RE03300','2024-05-23','Shanmukha Medical Agencies',7547,'1',5,'1','Paid','NEFT','2024-06-10','1595606720','');
Insert into DeliveryBills values ('RZ009319','2024-05-23','Balaji Medical & Surgical Agencies',3792,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('CJ03040','2024-05-23','Rajesh Medical Agencies',2304,'1',4.00140056022409,'1','Paid','NEFT','2024-06-10','1595614217','');
Insert into DeliveryBills values ('RL01243','2024-05-24','Siddartha Medical & Surgical Agencies',8047,'1',4,'1','Paid','IMPS','2024-06-18','1604601571','');
Insert into DeliveryBills values ('RLG07371','2024-05-24','Sri Jaya Krishna Medical Agencies',7311,'1',5,'1','Paid','Cash','2024-06-19','','');
Insert into DeliveryBills values ('YMAS825','2024-05-24','Yathiraja Medical and Surgical Agencies',4474,'1',5.00095147478592,'1','','',NULL,'','');
Insert into DeliveryBills values ('YMAS835','2024-05-24','Yathiraja Medical and Surgical Agencies',1839,'1',5,'1','','',NULL,'','');
Insert into DeliveryBills values ('RD01930','2024-05-25','Janardhan Medical Agencies',5272,'0',5,'1','Paid','Cash','2024-06-20','','');
Insert into DeliveryBills values ('RG00364','2024-05-25','Gopala Krishna Agencies',2864,'0',4,'1','Paid','NEFT','2024-06-21','1608039688','');
Insert into DeliveryBills values ('RG00365','2024-05-25','Gopala Krishna Agencies',1432,'0',100,'1','Done','',NULL,'','');
Insert into DeliveryBills values ('RL01254','2024-05-25','Siddartha Medical & Surgical Agencies',7219,'1',4,'1','Paid','IMPS','2024-06-18','1604601571','');
Insert into DeliveryBills values ('S00379','2024-05-25','Medicure Medical and Surgical Agencies',3532,'0',4,'1','Paid','NEFT','2024-06-27','1613663384','');
Insert into DeliveryBills values ('CJ03281','2024-05-28','Rajesh Medical Agencies',6883,'1',3.99993551091478,'1','Paid','NEFT','2024-06-10','1595614217','');
Insert into DeliveryBills values ('RL01338','2024-05-28','Siddartha Medical & Surgical Agencies',7680,'1',4,'1','Paid','IMPS','2024-06-18','1604601571','');
Insert into DeliveryBills values ('C001641','2024-05-28','S.R. Medical And Surgicals',3664,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RL01355','2024-05-29','Siddartha Medical & Surgical Agencies',7587,'1',4,'1','Paid','IMPS','2024-06-18','1604601571','');
Insert into DeliveryBills values ('RE004030','2024-05-30','Jyothi Medical Agencies',1320,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('CJ03391','2024-05-30','Rajesh Medical Agencies',4578,'1',4.00023490721165,'1','Paid','NEFT','2024-06-10','1595614217','');
Insert into DeliveryBills values ('NMA2400298','2024-05-31','Neelakanteswara Medical Agency',4701,'1',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('CJ03529','2024-06-01','Rajesh Medical Agencies',6068,'1',4.00007468399335,'1','','',NULL,'','');
Insert into DeliveryBills values ('CJ03711','2024-06-04','Rajesh Medical Agencies',6496,'1',4.00034002040122,'1','','',NULL,'','Modified Bill');
Insert into DeliveryBills values ('SVS2379','2024-06-04','Rainbow Vaccine House - Nandyal',1498,'1',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('YF05870','2024-06-05','Sree Saptagiri Pharma Distributors',6320,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('B001093','2024-06-03','Sri Lakshmi Balaji Medi Needs',3394,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RL01554','2024-06-06','Siddartha Medical & Surgical Agencies',6451,'1',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('A000271','2024-06-07','M R Medical Agencies',2719,'1',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('GR02265','2024-06-07','Arogya Medical & Surgical Agencies',4160,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RD02388','2024-06-07','Janardhan Medical Agencies',2992,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RL01614','2024-06-08','Siddartha Medical & Surgical Agencies',15268,'1',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RL01595','2024-06-07','Siddartha Medical & Surgical Agencies',5009,'1',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('S00475','2024-06-08','Medicure Medical and Surgical Agencies',22832,'0',5,'1','','',NULL,'','');
Insert into DeliveryBills values ('24-25/003728','2024-06-08','Sri Lakshmi Venkateswara Agencies',2299,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RG00443','2024-06-08','Gopala Krishna Agencies',6240,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RG00444','2024-06-08','Gopala Krishna Agencies',6272,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RG00445','2024-06-08','Gopala Krishna Agencies',3136,'0',100,'1','','',NULL,'','');
Insert into DeliveryBills values ('B001167','2024-06-08','Sri Lakshmi Balaji Medi Needs',1432,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('CJ04052','2024-06-10','Rajesh Medical Agencies',11338,'1',4.00018968133536,'1','','',NULL,'','');
Insert into DeliveryBills values ('GR01688','2024-06-10','Maheswari Agencies',16663,'1',4.0000206492645,'1','','',NULL,'','');
Insert into DeliveryBills values ('RJ05479','2024-06-10','Sri Sujit Pharma',8145,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RL01644','2024-06-10','Siddartha Medical & Surgical Agencies',5967,'1',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RZ012458','2024-06-11','Balaji Medical & Surgical Agencies',3960,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('AS000770','2024-06-11','Sree Challa Pharma and Surgicals',4040,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('24-25/003959','2024-06-12','Sri Lakshmi Venkateswara Agencies',6529,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('D000214','2024-06-12','M R Medical Agencies',3321,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RL01697','2024-06-12','Siddartha Medical & Surgical Agencies',9139,'1',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('CJ04403','2024-06-15','Rajesh Medical Agencies',2831,'1',4.00037993920973,'1','','',NULL,'','');
Insert into DeliveryBills values ('NMA2400369','2024-06-15','Neelakanteswara Medical Agency',1920,'1',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('GR01952','2024-06-21','Maheswari Agencies',9447,'1',4.00046679892636,'1','','',NULL,'','');
Insert into DeliveryBills values ('RG00535','2024-06-19','Gopala Krishna Agencies',3192,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RG00536','2024-06-19','Gopala Krishna Agencies',1596,'0',100,'1','Done','',NULL,'','');
Insert into DeliveryBills values ('RL01907','2024-06-20','Siddartha Medical & Surgical Agencies',5146,'1',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('NP583','2024-06-15','Nemus Pharmaceuticals Pvt Ltd, Dharwad',23512,'0',5,'1','','',NULL,'','Bill under Dr.Preethis name. SLC SCalp returned');
Insert into DeliveryBills values ('RE05411','2024-06-24','Shanmukha Medical Agencies',6308,'1',5,'1','','',NULL,'','');
Insert into DeliveryBills values ('S00554','2024-06-21','Medicure Medical and Surgical Agencies',1455,'0',5,'1','','',NULL,'','');
Insert into DeliveryBills values ('YF07648','2024-06-24','Sree Saptagiri Pharma Distributors',6672,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('SMA01925','2024-06-25','Siddartha Medical Agencies',3755,'1',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('A001012','2024-06-22','Sai Leela Medical Agencies',7611,'0',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RL02057','2024-06-26','Siddartha Medical & Surgical Agencies',3840,'1',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RL02090','2024-06-27','Siddartha Medical & Surgical Agencies',12839,'1',4,'1','','',NULL,'','');
Insert into DeliveryBills values ('RLG11999','2024-06-27','Sri Jaya Krishna Medical Agencies',5426,'1',5,'1','','',NULL,'','');"""


try:
    conn = mysql.connector.connect(
        host="193.203.184.152",
        port='3306',
        user="u885517842_AdminUser",
        password="MdP@ssword!!1",
        database="u885517842_MedicalStore"
    )

    query2 = 'Drop table MedicineList;'
    query3 = """CREATE TABLE MedicineList (
  MId varchar(255) DEFAULT NULL,
  MName varchar(255) DEFAULT NULL,
  MCompany varchar(255) DEFAULT NULL,
  CurrentStock int(11) DEFAULT NULL,
  MType varchar(255) DEFAULT NULL,
  MRP decimal(10,0) DEFAULT NULL,
  PTR decimal(10,0) DEFAULT NULL,
  GST int(11) DEFAULT NULL,
  HSN varchar(255) DEFAULT NULL,
  Offer1 int(11) DEFAULT NULL,
  Offer2 int(11) DEFAULT NULL,
  Weight varchar(255) DEFAULT NULL,
  Composition varchar(255) DEFAULT NULL,
  Alternative varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;"""    
    record = ('RLG11999','2024-06-27','Sri Jaya Krishna Medical Agencies',5426,'1',5,'1','','','NULL','','')                                      
    if conn.is_connected():
        print("Connected to MySQL database")
        cursor = conn.cursor()
        cursor.execute(query2, multi= True)

        #print(f"Line {line_number}: {word_count} words")
        
        # You can do more processing here
        # For example, print lines with more than 10 words

        
        
        #results = cursor.fetchall()
        
        #for row in results:
            #print(row)

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")