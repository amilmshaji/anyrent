BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "accounts_account" (
	"password"	varchar(128) NOT NULL,
	"is_superuser"	bool NOT NULL,
	"id"	integer NOT NULL,
	"fname"	varchar(100),
	"lname"	varchar(100),
	"email"	varchar(100) NOT NULL UNIQUE,
	"phone_number"	bigint NOT NULL,
	"date_joined"	datetime NOT NULL,
	"last_login"	datetime NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_admin"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"is_superadmin"	bool NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "accounts_account_groups" (
	"id"	integer NOT NULL,
	"account_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("account_id") REFERENCES "accounts_account"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "accounts_account_user_permissions" (
	"id"	integer NOT NULL,
	"account_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("account_id") REFERENCES "accounts_account"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "accounts_account"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "products_category" (
	"id"	integer NOT NULL,
	"category_name"	varchar(50) NOT NULL UNIQUE,
	"slug"	varchar(100) NOT NULL UNIQUE,
	"description"	text NOT NULL,
	"cat_image"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "products_other_product" (
	"id"	integer NOT NULL,
	"ad_title"	varchar(200) NOT NULL UNIQUE,
	"slug"	varchar(200) NOT NULL UNIQUE,
	"add_info"	text NOT NULL,
	"rent"	integer NOT NULL,
	"images"	varchar(100) NOT NULL,
	"is_available"	bool NOT NULL,
	"is_featured"	bool NOT NULL,
	"type"	varchar(200) NOT NULL,
	"created_date"	datetime NOT NULL,
	"modified_date"	datetime NOT NULL,
	"category_id"	bigint NOT NULL,
	"user_id"	integer,
	FOREIGN KEY("category_id") REFERENCES "products_category"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "accounts_account"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "products_house_product" (
	"id"	integer NOT NULL,
	"ad_title"	varchar(200) NOT NULL UNIQUE,
	"slug"	varchar(200) NOT NULL UNIQUE,
	"add_info"	text NOT NULL,
	"rent"	integer NOT NULL,
	"bedroom"	integer NOT NULL,
	"bathroom"	integer NOT NULL,
	"builtup"	integer NOT NULL,
	"capacity"	integer NOT NULL,
	"type"	varchar(200) NOT NULL,
	"furnish"	varchar(200) NOT NULL,
	"images"	varchar(100) NOT NULL,
	"is_available"	bool NOT NULL,
	"is_featured"	bool NOT NULL,
	"created_date"	datetime NOT NULL,
	"modified_date"	datetime NOT NULL,
	"category_id"	bigint NOT NULL,
	"user_id"	integer,
	FOREIGN KEY("user_id") REFERENCES "accounts_account"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("category_id") REFERENCES "products_category"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "products_furn_product" (
	"id"	integer NOT NULL,
	"ad_title"	varchar(200) NOT NULL UNIQUE,
	"slug"	varchar(200) NOT NULL UNIQUE,
	"add_info"	text NOT NULL,
	"rent"	integer NOT NULL,
	"images"	varchar(100) NOT NULL,
	"is_available"	bool NOT NULL,
	"is_featured"	bool NOT NULL,
	"type"	varchar(200) NOT NULL,
	"created_date"	datetime NOT NULL,
	"modified_date"	datetime NOT NULL,
	"category_id"	bigint NOT NULL,
	"user_id"	integer,
	FOREIGN KEY("category_id") REFERENCES "products_category"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "accounts_account"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "products_car_product" (
	"id"	integer NOT NULL,
	"ad_title"	varchar(200) NOT NULL UNIQUE,
	"slug"	varchar(200) NOT NULL UNIQUE,
	"add_info"	text NOT NULL,
	"rent"	integer NOT NULL,
	"brand"	varchar(200) NOT NULL,
	"driven"	integer NOT NULL,
	"own"	varchar(200) NOT NULL,
	"fuel"	varchar(200) NOT NULL,
	"images"	varchar(100) NOT NULL,
	"is_available"	bool NOT NULL,
	"is_featured"	bool NOT NULL,
	"created_date"	datetime NOT NULL,
	"modified_date"	datetime NOT NULL,
	"category_id"	bigint NOT NULL,
	"user_id"	integer,
	FOREIGN KEY("category_id") REFERENCES "products_category"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "accounts_account"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "products_bike_product" (
	"id"	integer NOT NULL,
	"ad_title"	varchar(200) NOT NULL UNIQUE,
	"slug"	varchar(200) NOT NULL UNIQUE,
	"add_info"	text NOT NULL,
	"rent"	integer NOT NULL,
	"brand"	varchar(200) NOT NULL,
	"driven"	integer NOT NULL,
	"own"	varchar(200) NOT NULL,
	"images"	varchar(100) NOT NULL,
	"is_available"	bool NOT NULL,
	"is_featured"	bool NOT NULL,
	"created_date"	datetime NOT NULL,
	"modified_date"	datetime NOT NULL,
	"category_id"	bigint NOT NULL,
	"user_id"	integer,
	FOREIGN KEY("category_id") REFERENCES "products_category"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "accounts_account"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2022-11-03 14:37:02.170939');
INSERT INTO "django_migrations" VALUES (2,'contenttypes','0002_remove_content_type_name','2022-11-03 14:37:02.263868');
INSERT INTO "django_migrations" VALUES (3,'auth','0001_initial','2022-11-03 14:37:02.462197');
INSERT INTO "django_migrations" VALUES (4,'auth','0002_alter_permission_name_max_length','2022-11-03 14:37:02.560356');
INSERT INTO "django_migrations" VALUES (5,'auth','0003_alter_user_email_max_length','2022-11-03 14:37:02.650921');
INSERT INTO "django_migrations" VALUES (6,'auth','0004_alter_user_username_opts','2022-11-03 14:37:02.732122');
INSERT INTO "django_migrations" VALUES (7,'auth','0005_alter_user_last_login_null','2022-11-03 14:37:02.820096');
INSERT INTO "django_migrations" VALUES (8,'auth','0006_require_contenttypes_0002','2022-11-03 14:37:02.900264');
INSERT INTO "django_migrations" VALUES (9,'auth','0007_alter_validators_add_error_messages','2022-11-03 14:37:02.990050');
INSERT INTO "django_migrations" VALUES (10,'auth','0008_alter_user_username_max_length','2022-11-03 14:37:03.070764');
INSERT INTO "django_migrations" VALUES (11,'auth','0009_alter_user_last_name_max_length','2022-11-03 14:37:03.163907');
INSERT INTO "django_migrations" VALUES (12,'auth','0010_alter_group_name_max_length','2022-11-03 14:37:03.261297');
INSERT INTO "django_migrations" VALUES (13,'auth','0011_update_proxy_permissions','2022-11-03 14:37:03.350075');
INSERT INTO "django_migrations" VALUES (14,'auth','0012_alter_user_first_name_max_length','2022-11-03 14:37:03.434115');
INSERT INTO "django_migrations" VALUES (15,'accounts','0001_initial','2022-11-03 14:37:03.734210');
INSERT INTO "django_migrations" VALUES (16,'admin','0001_initial','2022-11-03 14:37:03.991917');
INSERT INTO "django_migrations" VALUES (17,'admin','0002_logentry_remove_auto_add','2022-11-03 14:37:04.091860');
INSERT INTO "django_migrations" VALUES (18,'admin','0003_logentry_add_action_flag_choices','2022-11-03 14:37:04.272815');
INSERT INTO "django_migrations" VALUES (19,'products','0001_initial','2022-11-03 14:37:04.588838');
INSERT INTO "django_migrations" VALUES (20,'sessions','0001_initial','2022-11-03 14:37:04.757676');
INSERT INTO "django_migrations" VALUES (21,'accounts','0002_alter_account_email_alter_account_fname_and_more','2022-11-03 15:15:44.842180');
INSERT INTO "django_migrations" VALUES (22,'products','0002_alter_bike_product_add_info_alter_bike_product_brand_and_more','2022-11-03 15:15:45.433025');
INSERT INTO "django_migrations" VALUES (23,'products','0003_alter_house_product_category_and_more','2022-11-03 17:28:53.135879');
INSERT INTO "django_migrations" VALUES (24,'products','0004_alter_bike_product_user','2022-11-03 17:34:56.057026');
INSERT INTO "django_content_type" VALUES (1,'accounts','account');
INSERT INTO "django_content_type" VALUES (2,'products','category');
INSERT INTO "django_content_type" VALUES (3,'products','other_product');
INSERT INTO "django_content_type" VALUES (4,'products','house_product');
INSERT INTO "django_content_type" VALUES (5,'products','furn_product');
INSERT INTO "django_content_type" VALUES (6,'products','car_product');
INSERT INTO "django_content_type" VALUES (7,'products','bike_product');
INSERT INTO "django_content_type" VALUES (8,'products','all_products');
INSERT INTO "django_content_type" VALUES (9,'admin','logentry');
INSERT INTO "django_content_type" VALUES (10,'auth','permission');
INSERT INTO "django_content_type" VALUES (11,'auth','group');
INSERT INTO "django_content_type" VALUES (12,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES (13,'sessions','session');
INSERT INTO "auth_permission" VALUES (1,1,'add_account','Can add account');
INSERT INTO "auth_permission" VALUES (2,1,'change_account','Can change account');
INSERT INTO "auth_permission" VALUES (3,1,'delete_account','Can delete account');
INSERT INTO "auth_permission" VALUES (4,1,'view_account','Can view account');
INSERT INTO "auth_permission" VALUES (5,2,'add_category','Can add category');
INSERT INTO "auth_permission" VALUES (6,2,'change_category','Can change category');
INSERT INTO "auth_permission" VALUES (7,2,'delete_category','Can delete category');
INSERT INTO "auth_permission" VALUES (8,2,'view_category','Can view category');
INSERT INTO "auth_permission" VALUES (9,3,'add_other_product','Can add other_ product');
INSERT INTO "auth_permission" VALUES (10,3,'change_other_product','Can change other_ product');
INSERT INTO "auth_permission" VALUES (11,3,'delete_other_product','Can delete other_ product');
INSERT INTO "auth_permission" VALUES (12,3,'view_other_product','Can view other_ product');
INSERT INTO "auth_permission" VALUES (13,4,'add_house_product','Can add house_ product');
INSERT INTO "auth_permission" VALUES (14,4,'change_house_product','Can change house_ product');
INSERT INTO "auth_permission" VALUES (15,4,'delete_house_product','Can delete house_ product');
INSERT INTO "auth_permission" VALUES (16,4,'view_house_product','Can view house_ product');
INSERT INTO "auth_permission" VALUES (17,5,'add_furn_product','Can add furn_ product');
INSERT INTO "auth_permission" VALUES (18,5,'change_furn_product','Can change furn_ product');
INSERT INTO "auth_permission" VALUES (19,5,'delete_furn_product','Can delete furn_ product');
INSERT INTO "auth_permission" VALUES (20,5,'view_furn_product','Can view furn_ product');
INSERT INTO "auth_permission" VALUES (21,6,'add_car_product','Can add car_ product');
INSERT INTO "auth_permission" VALUES (22,6,'change_car_product','Can change car_ product');
INSERT INTO "auth_permission" VALUES (23,6,'delete_car_product','Can delete car_ product');
INSERT INTO "auth_permission" VALUES (24,6,'view_car_product','Can view car_ product');
INSERT INTO "auth_permission" VALUES (25,7,'add_bike_product','Can add bike_ product');
INSERT INTO "auth_permission" VALUES (26,7,'change_bike_product','Can change bike_ product');
INSERT INTO "auth_permission" VALUES (27,7,'delete_bike_product','Can delete bike_ product');
INSERT INTO "auth_permission" VALUES (28,7,'view_bike_product','Can view bike_ product');
INSERT INTO "auth_permission" VALUES (29,8,'add_all_products','Can add all_ products');
INSERT INTO "auth_permission" VALUES (30,8,'change_all_products','Can change all_ products');
INSERT INTO "auth_permission" VALUES (31,8,'delete_all_products','Can delete all_ products');
INSERT INTO "auth_permission" VALUES (32,8,'view_all_products','Can view all_ products');
INSERT INTO "auth_permission" VALUES (33,9,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES (34,9,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES (35,9,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES (36,9,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES (37,10,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES (38,10,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES (39,10,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES (40,10,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES (41,11,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES (42,11,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES (43,11,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES (44,11,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES (45,12,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES (46,12,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES (47,12,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES (48,12,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES (49,13,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES (50,13,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES (51,13,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES (52,13,'view_session','Can view session');
INSERT INTO "accounts_account" VALUES ('pbkdf2_sha256$390000$2ALhgfF6e6AR7Ec2ELYpca$nc/BgecoMP6w6GbeIxDHCfW+qvU3DnyeifKKgnoLU4s=',0,1,'Diya','Jacob','diya@gmail.com',9747979988,'2022-11-03 14:39:08.959368','2022-11-08 10:35:59.659511',1,1,1,1);
INSERT INTO "accounts_account" VALUES ('pbkdf2_sha256$390000$e6dRAsUsOomDe0VS5rnDLI$HEKRtYQjKL8h1mvsiN/oseaf6+BzekrhoFIq1hgCrWk=',0,2,'aysha','kathoon','aysha@gmail.com',9747927631,'2022-11-03 16:11:34.757966','2022-11-04 06:09:29.070014',1,0,1,0);
INSERT INTO "accounts_account" VALUES ('pbkdf2_sha256$390000$vgxUjdMa5b7Tb43wKT6XOM$M7lcBoW+fgWfjUxSQI8oLwkeC+NOP+s8awUC3za+3Fc=',0,3,'Divya','Jacob','diyamoljacob2023a@mca.ajce.in',9747927631,'2022-11-04 06:16:35.556096','2022-11-04 06:26:51.976603',1,0,1,0);
INSERT INTO "accounts_account" VALUES ('pbkdf2_sha256$390000$9LUyRivL5AdiowY1zeab9b$06uOrms/eHDOL8u4NUFeKMCCY9ekUW4E3sO1DZTEtJg=',0,4,'Diyamol','Jacob','diyajacob1952001@gmail.com',9747927631,'2022-11-04 07:20:54.237787','2022-11-04 07:21:22.703887',1,0,1,0);
INSERT INTO "django_admin_log" VALUES (1,'1','House and Appartments',1,'[{"added": {}}]',2,1,'2022-11-03 15:23:29.257604');
INSERT INTO "django_admin_log" VALUES (2,'2','Car',1,'[{"added": {}}]',2,1,'2022-11-03 15:24:47.224863');
INSERT INTO "django_admin_log" VALUES (3,'3','Bikes',1,'[{"added": {}}]',2,1,'2022-11-03 15:25:36.729544');
INSERT INTO "django_admin_log" VALUES (4,'4','Furniture',1,'[{"added": {}}]',2,1,'2022-11-03 15:26:08.303560');
INSERT INTO "django_admin_log" VALUES (5,'5','Other',1,'[{"added": {}}]',2,1,'2022-11-03 15:26:28.739162');
INSERT INTO "django_admin_log" VALUES (6,'2','aysha@gmail.com',2,'[{"changed": {"fields": ["Is active"]}}]',1,1,'2022-11-03 16:12:19.900317');
INSERT INTO "django_admin_log" VALUES (7,'1','Furnished House for Rent in Kannur city',3,'',4,1,'2022-11-03 16:29:50.689128');
INSERT INTO "django_admin_log" VALUES (8,'1','House and Appartments',2,'[{"changed": {"fields": ["Cat image"]}}]',2,1,'2022-11-03 16:55:42.204133');
INSERT INTO "django_admin_log" VALUES (9,'2','Car',2,'[{"changed": {"fields": ["Cat image"]}}]',2,1,'2022-11-03 16:55:58.728949');
INSERT INTO "django_admin_log" VALUES (10,'3','Bikes',2,'[{"changed": {"fields": ["Cat image"]}}]',2,1,'2022-11-03 16:56:09.296317');
INSERT INTO "django_admin_log" VALUES (11,'4','Furniture',2,'[{"changed": {"fields": ["Cat image"]}}]',2,1,'2022-11-03 16:56:22.178892');
INSERT INTO "django_admin_log" VALUES (12,'3','1BHK house for Rent in Balamrai',2,'[{"changed": {"fields": ["Is available"]}}]',4,1,'2022-11-04 02:59:35.863648');
INSERT INTO "django_admin_log" VALUES (13,'3','1BHK house for Rent in Balamrai',2,'[{"changed": {"fields": ["Is available"]}}]',4,1,'2022-11-04 02:59:57.275213');
INSERT INTO "django_admin_log" VALUES (14,'2','Cars',2,'[{"changed": {"fields": ["Category name", "Slug", "Description"]}}]',2,1,'2022-11-04 05:04:22.798171');
INSERT INTO "django_admin_log" VALUES (15,'3','Good Condition',2,'[{"changed": {"fields": ["Is available"]}}]',7,1,'2022-11-04 06:21:05.330803');
INSERT INTO "products_category" VALUES (1,'House and Appartments','House-and-Appartments','House and Appartments','photos/categories/house_lV3JnPq.webp');
INSERT INTO "products_category" VALUES (2,'Cars','Cars','Cars','photos/categories/cat_car1_fpu2z6O.jpg');
INSERT INTO "products_category" VALUES (3,'Bikes','Bikes','Bikes','photos/categories/cat_bike1_Pt6KhEv.jpg');
INSERT INTO "products_category" VALUES (4,'Furniture','Furniture','Furniture','photos/categories/s_6GHCPa2.jpg');
INSERT INTO "products_category" VALUES (5,'Other','Other','Other','photos/categories/f2_A2ramhw.jpg');
INSERT INTO "products_house_product" VALUES (2,'Newly built 3 bhk 1500 sqft beautiful house for sale at North paravur','newly-built-3-bhk-1500-sqft-beautiful-house-for-sale-at-north-paravur','3.5 cent 1500 sqft 3 bhk beautiful house for sale at North paravur  3 bhk with bath attached  Home loan and NRi loan available  Our complete assistance in loans  Ground floor :  Sitout  1 bhk with bath attached  Living and dining room  Kitchen  Work area etc ..',15000,2,3,4000,2500,'Apartments','Semi-Furnished','photos/house/h5.jpg',1,0,'2022-11-03 16:16:35.879155','2022-11-03 16:16:35.879155',1,2);
INSERT INTO "products_house_product" VALUES (3,'1BHK house for Rent in Balamrai','1bhk-house-for-rent-in-balamrai','I want to give my House for rent, it has small pooja room, Hall with False cealing, kitchen, bed room with attached Bathroom, and 1 extra bathroom in balcony, Car parking facility also available, WhatsApp or call me',8000,1,1,5000,4500,'House & Floors','Unfurnished','photos/house/h3.jpg',1,0,'2022-11-03 16:19:53.906700','2022-11-04 02:59:57.115928',1,2);
INSERT INTO "products_house_product" VALUES (4,'House for rent newly constructed 14000 rupees per month','house-for-rent-newly-constructed-14000-rupees-per-month','House for rent newly constructed house Rifa Colony near Exon School Campbell road kozhikod',14000,3,2,4500,4000,'Apartments','Unfurnished','photos/house/h1.jpg',1,0,'2022-11-03 16:26:49.942378','2022-11-03 16:26:49.942378',1,2);
INSERT INTO "products_house_product" VALUES (5,'Furnished House for Rent in Kannur city','furnished-house-for-rent-in-kannur-city','Fully furnished 2BHK flat is available for rent in Kannur city near Savitha Film city. It is a 3 BHK flat, one BR converted to Dining room next to Kitchen.',9000,2,2,4000,3800,'House & Floors','Semi-Furnished','photos/house/h2.jpg',1,0,'2022-11-03 16:30:56.284605','2022-11-03 16:30:56.284605',1,1);
INSERT INTO "products_house_product" VALUES (6,'excellent','excellent','House',3000,2,2,4000,3500,'Apartments','Semi-Furnished','photos/house/h2_pGBu5BO.jpg',1,0,'2022-11-04 07:23:58.709780','2022-11-04 07:23:58.709780',1,4);
INSERT INTO "products_furn_product" VALUES (1,'Sofa set for rent','sofa-set-for-rent','Sofa in excellent condition',500,'photos/house/f2.jpg',1,0,'sofa','2022-11-03 16:51:34.242671','2022-11-03 16:51:34.242671',4,2);
INSERT INTO "products_furn_product" VALUES (2,'DOUBLE BED WITH STORAGE','double-bed-with-storage','WE MAKE METAL BED WITH AND WITHOUT STORAGE AND CUSTOM SIZE ALSO WE MAKE  SIZE 6 X 5  PRICE IS WITHOUT MATRESS BUT WITH STORAGE',400,'photos/house/cot.jpg',1,0,'Cot','2022-11-03 16:54:13.113285','2022-11-03 16:54:13.113285',4,2);
INSERT INTO "products_car_product" VALUES (1,'Maruti Suzuki Ciaz (2015)','maruti-suzuki-ciaz-2015','MARUTI Suzuki Ciaz Zdi SHVS 2015 Vehicle Is In Excellent Condition Location For galaxy Cars Nashik Please call me for more details ADDITIONAL VEHICLE INFORMATION: Accidental: No Adjustable External Mirror: Power Adjustable Steering: Yes Air Conditioning: With Heater Number of Airbags: 2 airbags Alloy Wheels: Yes',15000,'Maruthi Suzuki',68000,'1st','Diesel','photos/house/image.jpg',1,0,'2022-11-03 16:32:40.930340','2022-11-03 16:32:40.930340',2,1);
INSERT INTO "products_car_product" VALUES (2,'Hyundai Santro (2022)','hyundai-santro-2022','Hyundai santro manual car for rent. In good condition and maintained well.',17000,'Hyundayi',45000,'1st','Petrol','photos/house/hundai.jpg',1,0,'2022-11-03 16:42:50.160093','2022-11-03 16:42:50.160093',2,2);
INSERT INTO "products_bike_product" VALUES (1,'CLASSIC 350','classic-350','good condition vehicle',9000,'Royal Enfield',45000,'2','photos/house/b1_amTOoEg.jpg',1,0,'2022-11-03 16:46:09.343246','2022-11-03 16:46:09.343246',3,2);
INSERT INTO "products_bike_product" VALUES (2,'XPULSE 200 (2021) (ABS)','xpulse-200-2021-abs','First Owner-1 Showroom Condition  No Scratches  2 keys 5 years insurance valid  Next To New CONDITION  Single Handed Used  Loan Facility Available  Credit card Facility Also Available',15000,'Hero',7000,'1','photos/house/b2_IdJ5aht.jpg',1,0,'2022-11-03 16:47:29.955989','2022-11-03 16:47:29.955989',3,2);
INSERT INTO "products_bike_product" VALUES (3,'Good Condition','good-condition','bike',600,'Hero',45876,'1','photos/house/b2_cK1b1Xc.jpg',0,0,'2022-11-04 06:19:38.224829','2022-11-04 06:21:05.122955',3,3);
INSERT INTO "django_session" VALUES ('sg37qp5p74utfrtajjvqr3l0ctyvpg6g','.eJxVjs0OwiAQhN-FsyFsAQFPxrvP0CwLbdG2JP05GOO7C0kPepudb3Yyb9bivg3tvsalTYFdGLDTr-eRnnGuIDxw7jOnPG9L8rxG-EFXfs8hjrcj-1cw4DqU73OjwJCTWkNnFWkQyggMGJy0UoPzxhbqNXnjoZPQUUMOrQy2KClMKY0TprEOSS-89vUoYyb2-QKFTz-Z:1oqbxP:eeaRklreLMp0G2yLmgA77EZe-Rfpp4UTrny2im7CrCQ','2022-11-17 15:16:39.934984');
INSERT INTO "django_session" VALUES ('m2ekk0ge2y08wi8fauu651yuxth1yrfl','.eJxVjs0OwiAQhN-FsyFsAQFPxrvP0CwLbdG2JP05GOO7C0kPepudb3Yyb9bivg3tvsalTYFdGLDTr-eRnnGuIDxw7jOnPG9L8rxG-EFXfs8hjrcj-1cw4DqU73OjwJCTWkNnFWkQyggMGJy0UoPzxhbqNXnjoZPQUUMOrQy2KClMKY0TprEOSS-89vUoYyb2-QKFTz-Z:1oruaH:F2fFfSGZ8bpujE2NjOBEZ_vgBrFq5_ZtiTJbrKqSh60','2022-11-21 05:22:09.381694');
INSERT INTO "django_session" VALUES ('sj3zmmxlhfevct5eccq5ibvynvnl0fsr','.eJxVjs0OwiAQhN-FsyFsAQFPxrvP0CwLbdG2JP05GOO7C0kPepudb3Yyb9bivg3tvsalTYFdGLDTr-eRnnGuIDxw7jOnPG9L8rxG-EFXfs8hjrcj-1cw4DqU73OjwJCTWkNnFWkQyggMGJy0UoPzxhbqNXnjoZPQUUMOrQy2KClMKY0TprEOSS-89vUoYyb2-QKFTz-Z:1osLxX:yfMK__trgIfqPYuw6iVC8wyzRxYuU6kMS0xgCJaWyb4','2022-11-22 10:35:59.769457');
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "accounts_account_groups_account_id_group_id_f64165b0_uniq" ON "accounts_account_groups" (
	"account_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "accounts_account_groups_account_id_52f14852" ON "accounts_account_groups" (
	"account_id"
);
CREATE INDEX IF NOT EXISTS "accounts_account_groups_group_id_7c6a6bd1" ON "accounts_account_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "accounts_account_user_permissions_account_id_permission_id_9af93c14_uniq" ON "accounts_account_user_permissions" (
	"account_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "accounts_account_user_permissions_account_id_816f9bde" ON "accounts_account_user_permissions" (
	"account_id"
);
CREATE INDEX IF NOT EXISTS "accounts_account_user_permissions_permission_id_24620205" ON "accounts_account_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "products_other_product_category_id_08074593" ON "products_other_product" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "products_other_product_user_id_b09aa41b" ON "products_other_product" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "products_house_product_category_id_bd9808ac" ON "products_house_product" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "products_house_product_user_id_0aab1eb0" ON "products_house_product" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "products_furn_product_category_id_78d6a11c" ON "products_furn_product" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "products_furn_product_user_id_e4b9eb12" ON "products_furn_product" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "products_car_product_category_id_e5566729" ON "products_car_product" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "products_car_product_user_id_7c48754d" ON "products_car_product" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "products_bike_product_category_id_f33a0e2c" ON "products_bike_product" (
	"category_id"
);
CREATE INDEX IF NOT EXISTS "products_bike_product_user_id_9e96cee7" ON "products_bike_product" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
COMMIT;
