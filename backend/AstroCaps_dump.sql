PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "MessierObjects" (
	"Number" BIGINT, 
	"Messier" TEXT, 
	"NGC" TEXT, 
	"Name" TEXT, 
	"Type" TEXT, 
	"Season" TEXT, 
	"Magnitude" FLOAT, 
	"Const" TEXT, 
	"ConstEnglish" TEXT, 
	"Constellation" TEXT, 
	"RA" TEXT, 
	"Dec" TEXT, 
	"Distance" TEXT, 
	"Size" TEXT, 
	"Discoverer" TEXT, 
	"Year" FLOAT, 
	"Captured" BIGINT, 
	"CapYear" FLOAT
);
INSERT INTO MessierObjects VALUES(1,'M1','NGC 1952','Crab Nebula','Supernova remnant','Winter',8.40000000000000035,'Tau','Bull','Taurus','05:34:31.97','+22:00:52.1','6,500','6,0'' x 4,0''','Bévis',1731.0,0,NULL);
INSERT INTO MessierObjects VALUES(2,'M2','NGC 7089','–','Globular cluster','Autumn',6.5,'Aqr','Water Bearer','Aquarius','21:33:27.01','-00:49:23.9','55,000','11,7''','Maraldi',1746.0,0,NULL);
INSERT INTO MessierObjects VALUES(3,'M3','NGC 5272','–','Globular cluster','Spring',6.20000000000000017,'CVn','Hound Dogs','Canes Venatici','13:42:11.23','+28:22:31.6','48,500','18,6''','Messier',1764.0,1,2024.0);
INSERT INTO MessierObjects VALUES(4,'M4','NGC 6121','Spider Globular','Globular cluster','Summer',5.59999999999999964,'Sco','Scorpion','Scorpius','16:23:35.40','-26:31:31.9','9,900','22,8''','Chéseaux',1746.0,0,NULL);
INSERT INTO MessierObjects VALUES(5,'M5','NGC 5904','Rose Cluster','Globular cluster','Spring',5.59999999999999964,'Se1','Snake','Serpens','15:18:33.75','+02:04:57.7','24,800','19,9''','Kirch',1702.0,1,2024.0);
INSERT INTO MessierObjects VALUES(6,'M6','NGC 6504','Butterfly Cluster','Open cluster','Summer',4.20000000000000017,'Sco','Scorpion','Scorpius','17:40:20.75','-32:15:15.0','1,300','15,0''','Hodierna',1654.0,0,NULL);
INSERT INTO MessierObjects VALUES(7,'M7','NGC 6475','Ptolemy''s Cluster','Open cluster','Summer',3.29999999999999982,'Sco','Scorpion','Scorpius','17:53:51.18','-34:47:34.2','780','30,0''','Ptolémée',NULL,0,NULL);
INSERT INTO MessierObjects VALUES(8,'M8','NGC 6523','Lagoon Nebula','Nebula with cluster','Summer',4.59999999999999964,'Sgr','Archer','Sagittarius','18:03:41.27','-24:22:48.6','4,850','90,0'' x 40,0''','Flamsteed',1680.0,0,NULL);
INSERT INTO MessierObjects VALUES(9,'M9','NGC 6333','–','Globular cluster','Summer',7.70000000000000017,'Oph','Serpent Holder','Ophiuchus','17:19:11.78','-18:30:58.5','25,800','5,5''','Messier',1764.0,0,NULL);
INSERT INTO MessierObjects VALUES(10,'M10','NGC 6254','–','Globular cluster','Summer',6.59999999999999964,'Oph','Serpent Holder','Ophiuchus','16:57:08.99','-04:05:57.6','16,300','12,2''','Messier',1764.0,1,2024.0);
INSERT INTO MessierObjects VALUES(11,'M11','NGC 6705','Wild Duck Cluster','Open cluster','Summer',5.79999999999999982,'Sct','Shield','Scutum','18:51:05.99','-06:16:12.1','5,600','14,0''','Kirch',1681.0,0,NULL);
INSERT INTO MessierObjects VALUES(12,'M12','NGC 6218','–','Globular cluster','Summer',6.70000000000000017,'Oph','Serpent Holder','Ophiuchus','16:47:14.52','-01:56:52.2','18,900','12,2''','Messier',1764.0,1,2024.0);
INSERT INTO MessierObjects VALUES(13,'M13','NGC 6205','Great Hercules Cluster','Globular cluster','Summer',5.79999999999999982,'Her','Hercules','Hercules','16:41:41.63','+36:27:40.7','23,500','23,2''','Halley',1714.0,1,2023.0);
INSERT INTO MessierObjects VALUES(14,'M14','NGC 6402','–','Globular cluster','Summer',7.59999999999999964,'Oph','Serpent Holder','Ophiuchus','17:37:36.16','-03:14:45.3','24,000','6,7''','Messier',1764.0,0,NULL);
INSERT INTO MessierObjects VALUES(15,'M15','NGC 7078','Great Pegasus Cluster','Globular cluster','Autumn',6.20000000000000017,'Peg','Winged Horse','Pegasus','21:29:58.38','+12:10:00.6','49,500','12,3''','Maraldi',1746.0,0,NULL);
INSERT INTO MessierObjects VALUES(16,'M16','NGC 6611','Eagle Nebula','H II region nebula with cluster','Summer',6.40000000000000035,'Se2','Snake','Serpens','18:18:48.17','-13:48:26.0','5,870','25,0''','Chéseaux',1746.0,0,NULL);
INSERT INTO MessierObjects VALUES(17,'M17','NGC 6618','Omega',' Horseshoe','Summer',6.0,'Sgr','Archer','Sagittarius','18:20:47.11','-16:10:17.5','5,870','45,0'' x 35,0''','Chéseaux',1746.0,0,NULL);
INSERT INTO MessierObjects VALUES(18,'M18','NGC 6613','Black Swan Cluster','Open cluster','Summer',7.5,'Sgr','Archer','Sagittarius','18:19:58.49','-17:06:07.1','4,900','9,0''','Messier',1764.0,0,NULL);
INSERT INTO MessierObjects VALUES(19,'M19','NGC 6273','–','Globular cluster','Summer',6.79999999999999982,'Oph','Serpent Holder','Ophiuchus','17:02:37.68','-26:16:04.6','22,500','5,3''','Messier',1764.0,0,NULL);
INSERT INTO MessierObjects VALUES(20,'M20','NGC 6514','Trifid Nebula','H II region nebula with cluster','Summer',6.29999999999999982,'Sgr','Archer','Sagittarius','18:02:42.11','-22:58:18.8','2,300','29,0'' x 27,0''','Le Gentil',1749.0,0,NULL);
INSERT INTO MessierObjects VALUES(21,'M21','NGC 6531','Webb''s Cross Cluster','Open cluster','Summer',6.5,'Sgr','Archer','Sagittarius','18:04:13.45','-22:29:24.2','4,200','13,0''','Messier',1764.0,0,NULL);
INSERT INTO MessierObjects VALUES(22,'M22','NGC 6656','Great Sagittarius Cluster','Globular cluster','Summer',5.09999999999999964,'Sgr','Archer','Sagittarius','18:36:24.20','-23:54:12.3','7,800','17,0''','Ihle',1665.0,0,NULL);
INSERT INTO MessierObjects VALUES(23,'M23','NGC 6494','–','Open cluster','Summer',5.5,'Sgr','Archer','Sagittarius','17:57:04.77','-18:59:07.2','2,150','25,0''','Messier',1764.0,0,NULL);
INSERT INTO MessierObjects VALUES(24,'M24','NGC 6603','Small Sagittarius Star Cloud','Milky Way star cloud','Summer',2.5,'Sgr','Archer','Sagittarius','18:16:56.12','-18:30:52.4','16,000','45,0''','Messier',1764.0,0,NULL);
INSERT INTO MessierObjects VALUES(25,'M25','IC4725','–','Open cluster','Summer',4.59999999999999964,'Sgr','Archer','Sagittarius','18:31:46.77','-19:06:53.8','2,060','35,0''','Chéseaux',1746.0,0,NULL);
INSERT INTO MessierObjects VALUES(26,'M26','NGC 6694','–','Open cluster','Summer',8.0,'Sct','Shield','Scutum','18:45:18.66','-09:23:01.0','5,100','15,0''','Le Gentil',1749.0,0,NULL);
INSERT INTO MessierObjects VALUES(27,'M27','NGC 6853','Dumbbell Nebula','Planetary nebula','Summer',7.40000000000000035,'Vul','Little Fox','Vulpecula','19:59:36.38','+22:43:15.7','980','348,0''''','Messier',1764.0,1,2023.0);
INSERT INTO MessierObjects VALUES(28,'M28','NGC 6626','–','Globular cluster','Summer',6.79999999999999982,'Sgr','Archer','Sagittarius','18:24:32.89','-24:52:11.4','19,000','15,0''','Messier',1764.0,0,NULL);
INSERT INTO MessierObjects VALUES(29,'M29','NGC 6913','Cooling Tower','Open cluster','Summer',7.09999999999999964,'Cyg','Swan','Cygnus','20:23:57.77','+38:30:27.6','4,100','7,0''','Messier',1764.0,0,NULL);
INSERT INTO MessierObjects VALUES(30,'M30','NGC 7099','Jellyfish Cluster','Globular cluster','Autumn',7.20000000000000017,'Cap','Goat','Capricornus','21:40:22.02','-23:10:44.7','41,000','8,9''','Messier',1764.0,0,NULL);
INSERT INTO MessierObjects VALUES(31,'M31','NGC 224','Andromeda Galaxy','Spiral galaxy','Autumn',3.39999999999999991,'And','Andromeda','Andromeda','00:42:44.35','+41:16:08.6','2,500,000','180,0'' x 63,0''',NULL,NULL,1,2023.0);
INSERT INTO MessierObjects VALUES(32,'M32','NGC 221','Andromeda Satellite #1','Dwarf elliptical galaxy','Autumn',8.09999999999999964,'And','Andromeda','Andromeda','00:42:41.83','+40:51:55.0',NULL,'7,6'' x 5,8''','Le Gentil',1749.0,0,NULL);
INSERT INTO MessierObjects VALUES(33,'M33','NGC 598','Triangulum/Pinwheel Galaxy','Spiral galaxy','Autumn',5.70000000000000017,'Tri','Triangle','Triangulum','01:33:50.89','+30:39:36.8','2,723,000','62,0. x 39,0''','Messier',1764.0,0,NULL);
INSERT INTO MessierObjects VALUES(34,'M34','NGC 1039','Spiral Cluster','Open cluster','Autumn',5.5,'Per','Perseus','Perseus','02:42:07.40','+42:44:46.1','1,450','35,0''','Messier',1764.0,0,NULL);
INSERT INTO MessierObjects VALUES(35,'M35','NGC 2168','Shoe-Buckle Cluster','Open cluster','Winter',5.29999999999999982,'Gem','Twins','Gemini','06:09:05.06','+24:20:19.1','2,800','30,0''','Chéseaux',1746.0,0,NULL);
INSERT INTO MessierObjects VALUES(36,'M36','NGC 1960','Pinwheel Cluster','Open cluster','Winter',6.29999999999999982,'Aur','Charioteer','Auriga','05:36:17.74','+34:08:26.7','3,700','12,0''','Hodierna',1654.0,0,NULL);
INSERT INTO MessierObjects VALUES(37,'M37','NGC 2099','Salt and Pepper Cluster','Open cluster','Winter',6.20000000000000017,'Aur','Charioteer','Auriga','05:52:18.35','+32:33:10.8','3,600','24,0''','Hodierna',1654.0,0,NULL);
INSERT INTO MessierObjects VALUES(38,'M38','NGC 1912','Starfish Cluster','Open cluster','Winter',7.40000000000000035,'Aur','Charioteer','Auriga','05:28:42.49','+35:51:17.7','2,750','21,0''','Hodierna',1654.0,0,NULL);
INSERT INTO MessierObjects VALUES(39,'M39','NGC 7092','–','Open cluster','Autumn',4.59999999999999964,'Cyg','Swan','Cygnus','21:31:48.32','+48:26:17.4','880','32,0''','Le Gentil',1750.0,0,NULL);
INSERT INTO MessierObjects VALUES(40,'M40',NULL,'Winnecke 4','Optical Double','Spring',8.40000000000000035,'Sgr','Archer','Sagittarius',NULL,NULL,NULL,NULL,'Hevelius',1660.0,0,NULL);
INSERT INTO MessierObjects VALUES(41,'M41','NGC 2287','Little Beehive Cluster','Open cluster','Winter',4.5,'CMa','Great Dog','Canis Major','06:45:59.94','-20:45:15.2','1,600','30,0''','Hodierna',1654.0,0,NULL);
INSERT INTO MessierObjects VALUES(42,'M42','NGC 9176','Great Orion Nebula','H II region nebula','Winter',4.0,'Ori','Orion, Hunter','Orion','05:35:16.48','-05:23:22.8','1,500','30,0''','Peiresc',1610.0,1,2023.0);
INSERT INTO MessierObjects VALUES(43,'M43','NGC 1982','De Mairan''s Nebula','H II region nebula (part of the Orion Nebula)','Winter',9.0,'Ori','Orion, Hunter','Orion','05:35:31.38','-05:16:02.9','1,500','20,0'' x 15,0''','Mairan',1750.0,0,NULL);
INSERT INTO MessierObjects VALUES(44,'M44','NGC 2632','Beehive Cluster or Praesepe','Open cluster','Spring',3.70000000000000017,'Cnc','Crab','Cancer','08:40:22.20','+19:40:19.4','520','70,0''',NULL,NULL,0,NULL);
INSERT INTO MessierObjects VALUES(45,'M45',NULL,'Pleiades,  Seven Sisters or Subaru','Open cluster','Winter',1.60000000000000008,NULL,NULL,'Taurus',NULL,NULL,'410','120,0''',NULL,NULL,1,2024.0);
INSERT INTO MessierObjects VALUES(46,'M46','NGC 2437','–','Open cluster','Winter',6.0,'Pup','Stern,Poop deck','Puppis','07:41:46.82','-14:48:36.0','3,200','24,0''','Messier',1771.0,0,NULL);
INSERT INTO MessierObjects VALUES(47,'M47','NGC 2422','–','Open cluster','Winter',4.40000000000000035,'Pup','Stern,Poop deck','Puppis','07:36:35.02','-14:28:57.4','1,750','22,0''','Hodierna',1654.0,0,NULL);
INSERT INTO MessierObjects VALUES(48,'M48','NGC 2548','–','Open cluster','Winter',5.5,'Hya','Hydra, Sea Snake','Hydra','08:13:43.18','-05:45:01.6','1,500','42''','Messier',1771.0,0,NULL);
INSERT INTO MessierObjects VALUES(49,'M49','NGC 4472','–','Elliptical galaxy','Spring',8.40000000000000035,'Vir','Virgin','Virgo','12:29:46.76','+08:00:01.7','41,000,000','8,9'' x 7,4''','Messier',1771.0,0,NULL);
INSERT INTO MessierObjects VALUES(50,'M50','NGC 2323','Heart-Shaped Cluster','Open cluster','Winter',5.90000000000000035,'Mon','Unicorn','Monoceros','07:02:40.47','-08:21:50.5','2,950','16,0. x 5,5''','Cassini',1710.0,0,NULL);
INSERT INTO MessierObjects VALUES(51,'M51','NGC 5194','Whirlpool Galaxy','Spiral galaxy','Spring',8.40000000000000035,'CVn','Hound Dogs','Canes Venatici','13:29:52.71','+47:11:42.6','37,000,000','11,0'' x 7,8''','Messier',1773.0,1,2023.0);
INSERT INTO MessierObjects VALUES(52,'M52','NGC 7654','Scorpion Cluster','Open cluster','Autumn',7.29999999999999982,'Cas','Cassiopeia','Cassiopeia','23:24:48.40','+61:35:35.4','3,000','13,0''','Messier',1774.0,0,NULL);
INSERT INTO MessierObjects VALUES(53,'M53','NGC 5024','–','Globular cluster','Spring',7.59999999999999964,'Com','Hair of Berenice','Coma Berenices','13:12:55.23','+18:10:08.8','69,000','14,4''','Bode',1775.0,0,NULL);
INSERT INTO MessierObjects VALUES(54,'M54','NGC 6715','–','Globular cluster','Summer',7.59999999999999964,'Sgr','Archer','Sagittarius','18:55:03.27','-30:28:42.6','49,000','5,5''','Messier',1778.0,0,NULL);
INSERT INTO MessierObjects VALUES(55,'M55','NGC 6809','Specter Cluster','Globular cluster','Summer',6.29999999999999982,'Sgr','Archer','Sagittarius','19:39:59.40','-30:57:43.5','20,000','14,8''','Lacaille',1751.0,0,NULL);
INSERT INTO MessierObjects VALUES(56,'M56','NGC 6779','–','Globular cluster','Summer',8.30000000000000071,'Lyr','Lyre','Lyra','19:16:35.51','+30:11:04.2','45,600','2,4''','Messier',1779.0,0,NULL);
INSERT INTO MessierObjects VALUES(57,'M57','NGC 6720','Ring Nebula','Planetary nebula','Summer',8.80000000000000071,'Lyr','Lyre','Lyra','18:53:35.01','+33:01:42.9','1,410','71''''','Darquier',1779.0,0,NULL);
INSERT INTO MessierObjects VALUES(58,'M58','NGC 4579','–','Barred Spiral galaxy','Spring',9.69999999999999928,'Vir','Virgin','Virgo','12:37:43.52','+11:49:05.5','41,000,000','5,4'' x 4,4''','Messier',1779.0,0,NULL);
INSERT INTO MessierObjects VALUES(59,'M59','NGC 4621','–','Elliptical galaxy','Spring',9.59999999999999964,'Vir','Virgin','Virgo','12:42:02.24','+11:38:49.3','41,000,000','5,1'' x 3,4''','Koehler',1779.0,0,NULL);
INSERT INTO MessierObjects VALUES(60,'M60','NGC 4649','–','Elliptical galaxy','Spring',8.80000000000000071,'Vir','Virgin','Virgo','12:43:39.98','+11:33:09.7','41,000,000','7,2'' x 6,2''','Koehler',1779.0,0,NULL);
INSERT INTO MessierObjects VALUES(61,'M61','NGC 4303','Swelling Spiral','Spiral galaxy','Spring',9.69999999999999928,'Vir','Virgin','Virgo','12:21:54.90','+04:28:25.1','41,000,000','6,0'' x 5,5''','Oriani',1779.0,0,NULL);
INSERT INTO MessierObjects VALUES(62,'M62','NGC 6266','Flickering Globular','Globular cluster','Summer',6.5,'Oph','Serpent Holder','Ophiuchus','17:01:12.60','-30:06:44.5','22,500','6,3''','Messier',1771.0,0,NULL);
INSERT INTO MessierObjects VALUES(63,'M63','NGC 5055','Sunflower Galaxy','Spiral galaxy','Spring',8.59999999999999964,'CVn','Hound Dogs','Canes Venatici','13:15:49.33','+42:01:45.4','23,800,000','12,0'' x 7,6''','Méchain',1779.0,1,2023.0);
INSERT INTO MessierObjects VALUES(64,'M64','NGC 4826','Black Eye Galaxy','Spiral galaxy','Spring',8.5,'Com','Hair of Berenice','Coma Berenices','12:56:43.64','+21:40:58.7','11,800,000','9,3'' x 5,4''','Bode',1775.0,0,NULL);
INSERT INTO MessierObjects VALUES(65,'M65','NGC 3623','Leo Triplet','Barred Spiral galaxy','Spring',9.30000000000000071,'Leo','Lion','Leo','11:18:55.92','+13:05:32.5','29,000,000','10,0'' x 3,3''','Méchain',1780.0,0,NULL);
INSERT INTO MessierObjects VALUES(66,'M66','NGC 3627','Leo Triplet','Barred Spiral galaxy','Spring',8.90000000000000035,'Leo','Lion','Leo','11:20:14.96','+12:59:29.5','29,000,000','8,7'' x 4,4''','Méchain',1780.0,1,2023.0);
INSERT INTO MessierObjects VALUES(67,'M67','NGC 2682','King Cobra or Golden Eye Cluster','Open cluster','Spring',6.09999999999999964,'Cnc','Crab','Cancer','08:51:20.13','+11:48:43.0','2,600','27,0''','Koehler',1778.0,0,NULL);
INSERT INTO MessierObjects VALUES(68,'M68','NGC 4590','–','Globular cluster','Spring',7.79999999999999982,'Hya','Hydra, Sea Snake','Hydra','12:39:28.01','-26:44:34.9','36,000','9,8''','Méchain',1780.0,0,NULL);
INSERT INTO MessierObjects VALUES(69,'M69','NGC 6637','–','Globular cluster','Summer',7.59999999999999964,'Sgr','Archer','Sagittarius','18:31:23.23','-32:20:52.7','23,500','3,8''','Lacaille',1751.0,0,NULL);
INSERT INTO MessierObjects VALUES(70,'M70','NGC 6681','–','Globular cluster','Summer',7.90000000000000035,'Sgr','Archer','Sagittarius','18:43:12.64','-32:17:30.8','65,000','4,1''','Messier',1780.0,0,NULL);
INSERT INTO MessierObjects VALUES(71,'M71','NGC 6838','Angelfish Cluster','Globular cluster','Summer',8.19999999999999929,'Sge','Arrow','Sagitta','19:53:46.11','+18:46:42.2','13,000','6,1''','Chéseaux',1746.0,0,NULL);
INSERT INTO MessierObjects VALUES(72,'M72','NGC 6981','–','Globular cluster','Autumn',9.30000000000000071,'Aqr','Water Bearer','Aquarius','20:53:27.91','-12:32:13.4','62,000','5,1''','Méchain',1780.0,0,NULL);
INSERT INTO MessierObjects VALUES(73,'M73','NGC 6994','–','Asterism','Autumn',9.0,'Aqr','Water Bearer','Aquarius','20:58:55.97','-12:38:07.8',NULL,'2,8''','Messier',1780.0,0,NULL);
INSERT INTO MessierObjects VALUES(74,'M74','NGC 628','Phantom Galaxy[91]','Spiral galaxy','Autumn',9.40000000000000035,'Psc','Fishes','Pisces','01:36:41.75','+15:47:01.2','26,000,000','10,0'' x 9,6''','Méchain',1780.0,0,NULL);
INSERT INTO MessierObjects VALUES(75,'M75','NGC 6864','–','Globular cluster','Summer',8.5,'Sgr','Archer','Sagittarius','20:06:04.84','-21:55:20.0','78,500','4,6''','Méchain',1780.0,0,NULL);
INSERT INTO MessierObjects VALUES(76,'M76','NGC 650','Little Dumbbell Nebula','Planetary nebula','Autumn',10.0999999999999996,'Per','Perseus','Perseus','01:42:19.69','+51:34:31.7','8,200','65''''','Méchain',1780.0,0,NULL);
INSERT INTO MessierObjects VALUES(77,'M77','NGC 1068','Cetus A or Squid Galaxy','Spiral galaxy','Autumn',8.90000000000000035,'Cet','Sea-monster','Cetus','02:42:40.71','-00:00:47.8','52,000,000','6,9'' x 5,9''','Méchain',1780.0,0,NULL);
INSERT INTO MessierObjects VALUES(78,'M78','NGC 2068','–','Diffuse nebula','Winter',8.30000000000000071,'Ori','Orion, Hunter','Orion','05:46:45.82','+00:04:45.5','1,630','8,0'' x 6,0''','Méchain',1780.0,0,NULL);
INSERT INTO MessierObjects VALUES(79,'M79','NGC 1904','–','Globular cluster','Winter',7.70000000000000017,'Lep','Hare','Lepus','05:24:10.59','-24:31:27.2','43,400','7,8''','Méchain',1780.0,0,NULL);
INSERT INTO MessierObjects VALUES(80,'M80','NGC 6093','–','Globular cluster','Summer',7.29999999999999982,'Sco','Scorpion','Scorpius','16:17:02.51','-22:58:30.4','36,000','5,1''','Messier',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(81,'M81','NGC 3031','Bode''s Galaxy','Spiral galaxy','Spring',6.90000000000000035,'UMa','Big Bear','Ursa Major','09:55:33.17','+69:03:55.1','8,500,000','26,0'' x 14,0''','Bode',1774.0,0,NULL);
INSERT INTO MessierObjects VALUES(82,'M82','NGC 3034','Cigar Galaxy','Starburst galaxy','Spring',8.40000000000000035,'UMa','Big Bear','Ursa Major','09:55:52.73','+69:40:45.8','8,500,000','11,0'' x 4,6''','Bode',1774.0,0,NULL);
INSERT INTO MessierObjects VALUES(83,'M83','NGC 5236','Southern Pinwheel Galaxy','Barred Spiral galaxy','Spring',7.59999999999999964,'Hya','Hydra, Sea Snake','Hydra','13:37:00.95','-29:51:55.5','8,500,000','11,0'' x 10,0''','Lacaille',1751.0,0,NULL);
INSERT INTO MessierObjects VALUES(84,'M84','NGC 4374','–','Lenticular galaxy','Spring',9.09999999999999964,'Vir','Virgin','Virgo','12:25:03.74','+12:53:13.1','41,000,000','5,0'' x 4,4''','Messier',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(85,'M85','NGC 4382','–','Lenticular galaxy','Spring',9.09999999999999964,'Com','Hair of Berenice','Coma Berenices','12:25:24.11','+18:11:29.4','41,000,000','7,1'' x 5,2''','Méchain',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(86,'M86','NGC 4406','–','Lenticular galaxy','Spring',8.90000000000000035,'Vir','Virgin','Virgo','12:26:11.74','+12:56:46.4','20,000,000','7,4'' x 5,5''','Messier',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(87,'M87','NGC 4486','Virgo A or Smoking Gun Galaxy','Elliptical galaxy','Spring',8.59999999999999964,'Vir','Virgin','Virgo','12:30:49.42','+12:23:28.0','63,000,000','7,2'' x 6,8''','Messier',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(88,'M88','NGC 4501','–','Spiral galaxy','Spring',9.59999999999999964,'Com','Hair of Berenice','Coma Berenices','12:31:59.16','+14:25:13.4','41,000,000','6,9'' x 3,9''','Messier',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(89,'M89','NGC 4552','–','Elliptical galaxy','Spring',9.80000000000000071,'Vir','Virgin','Virgo','12:35:39.81','+12:33:22.8','41,000,000','4,2'' x 4,2''','Messier',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(90,'M90','NGC 4560','–','Spiral galaxy','Spring',9.5,'Vir','Virgin','Virgo','12:36:49.79','+13:09:46.6','41,000,000','9,5'' x 4,7''','Messier',1781.0,1,2024.0);
INSERT INTO MessierObjects VALUES(91,'M91','NGC 4548','–','Barred Spiral galaxy','Spring',10.1999999999999992,'Com','Hair of Berenice','Coma Berenices','12:35:26.45','+14:29:46.8','37,000,000','5,4'' x 4,4''','Messier',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(92,'M92','NGC 6341','–','Globular cluster','Summer',6.40000000000000035,'Her','Hercules','Hercules','17:17:07.27','+43:08:11.5','28,400','12,2''','Bode',1777.0,0,NULL);
INSERT INTO MessierObjects VALUES(93,'M93','NGC 2447','Critter Cluster','Open cluster','Winter',6.0,'Pup','Stern,Poop deck','Puppis','07:44:29.23','-23:51:11.1','3,600','22,0''','Messier',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(94,'M94','NGC 4736','Crocodile Eye or Cat''s Eye Galaxy','Spiral galaxy','Spring',8.19999999999999929,'CVn','Hound Dogs','Canes Venatici','12:50:53.06','+41:07:13.6','32,600,000','11,0'' x 9,1''','Méchain',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(95,'M95','NGC 3351','–','Barred Spiral galaxy','Spring',9.69999999999999928,'Leo','Lion','Leo','10:43:57.70','+11:42:13.7','20,300,000','7,4'' x 5,1''','Méchain',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(96,'M96','NGC 3368','–','Spiral galaxy','Spring',9.19999999999999928,'Leo','Lion','Leo','10:46:45.74','+11:49:11.8','29,300,000','7,1'' x 5,1''','Méchain',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(97,'M97','NGC 3587','Owl Nebula','Planetary nebula','Spring',9.90000000000000035,'UMa','Big Bear','Ursa Major','11:14:47.71','+55:01:08.5','10,000','194''''','Méchain',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(98,'M98','NGC 4192','–','Spiral galaxy','Spring',10.0999999999999996,'Com','Hair of Berenice','Coma Berenices','12:13:48.29','+14:54:01.2','36,000,000','9,5'' x 3,2''','Méchain',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(99,'M99','NGC 4254','St. Catherine’s Wheel','Spiral galaxy','Spring',9.90000000000000035,'Com','Hair of Berenice','Coma Berenices','12:18:49.60','+14:24:59.4','41,000,000','5,4'' x 4,8''','Méchain',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(100,'M100','NGC 4321','Mirror Galaxy','Spiral galaxy','Spring',9.30000000000000071,'Com','Hair of Berenice','Coma Berenices','12:22:54.83','+15:49:18.5','41,000,000','6,9'' x 6,2''','Méchain',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(101,'M101','NGC 5457','Pinwheel Galaxy','Spiral galaxy','Spring',7.90000000000000035,'UMa','Big Bear','Ursa Major','14:03:12.54','+54:20:56.2','23,000,000','27,0'' x 26,0''','Méchain',1781.0,1,2023.0);
INSERT INTO MessierObjects VALUES(102,'M102','NGC 5866','Spindle Galaxy','Lenticular galaxy','Spring',9.90000000000000035,NULL,NULL,'Draco',NULL,NULL,'23,000,000','5,2'' x 2,3''','Méchain',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(103,'M103','NGC 581','–','Open cluster','Autumn',7.40000000000000035,'Cas','Cassiopeia','Cassiopeia','01:33:21.81','+60:39:28.8','8,500','5,0''','Méchain',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(104,'M104','NGC 4594','Sombrero Galaxy','Spiral galaxy','Spring',8.0,'Crv','Crow','Corvus','12:39:59.43','-11:37:23.0','40,000,000','8,9'' x 4,1''','Méchain',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(105,'M105','NGC 3379','–','Elliptical galaxy','Spring',9.30000000000000071,'Leo','Lion','Leo','10:47:49.59','+12:34:53.8','21,500,000','4,5'' x 4,0''','Méchain',1781.0,0,NULL);
INSERT INTO MessierObjects VALUES(106,'M106','NGC 4258','–','Spiral galaxy','Spring',8.40000000000000035,'CVn','Hound Dogs','Canes Venatici','12:18:57.50','+47:18:14.3','20,000,000','18,0'' x 7,9''','Méchain',1781.0,1,2023.0);
INSERT INTO MessierObjects VALUES(107,'M107','NGC 6171','Crucifix Cluster','Globular cluster','Summer',7.90000000000000035,'Oph','Serpent Holder','Ophiuchus','16:32:31.92','-13:03:13.1','19,200','7,8''','Méchain',1782.0,0,NULL);
INSERT INTO MessierObjects VALUES(108,'M108','NGC 3556','Surfboard Galaxy','Barred Spiral galaxy','Spring',10.0,'UMa','Big Bear','Ursa Major','11:11:30.97','+55:40:26.8','23,500,000','8,3'' x 2,5''','Méchain',1782.0,0,NULL);
INSERT INTO MessierObjects VALUES(109,'M109','NGC 3992','Vacuum Cleaner Galaxy','Barred Spiral galaxy','Autumn',9.80000000000000071,'UMa','Big Bear','Ursa Major','11:57:35.98','+53:22:28.3','27,000,000','7,6'' x 4,9''','Méchain',1782.0,0,NULL);
INSERT INTO MessierObjects VALUES(110,'M110','NGC 205','–','Dwarf elliptical galaxy','Autumn',8.5,'And','Andromeda','Andromeda','00:40:22.08','+41:41:07.1','2,250,000','17,0, x 9,8''','Messier',1773.0,0,NULL);
COMMIT;
