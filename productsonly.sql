BEGIN TRANSACTION;
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
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("category_id") REFERENCES "products_category"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "accounts_account"("id") DEFERRABLE INITIALLY DEFERRED
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
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("category_id") REFERENCES "products_category"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "accounts_account"("id") DEFERRABLE INITIALLY DEFERRED
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
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("category_id") REFERENCES "products_category"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "accounts_account"("id") DEFERRABLE INITIALLY DEFERRED
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
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "accounts_account"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("category_id") REFERENCES "products_category"("id") DEFERRABLE INITIALLY DEFERRED
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
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("category_id") REFERENCES "products_category"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "accounts_account"("id") DEFERRABLE INITIALLY DEFERRED
);
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
COMMIT;
