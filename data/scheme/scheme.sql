CREATE TABLE famous (
	id int AUTO_INCREMENT PRIMARY KEY;
	name varchar(255),
	job varchar(255),
	img varchar(2083),
	birth_date date,
	birth_place TEXT,
	about TEXT,
	before_fame TEXT,
	curiosities TEXT,
	family_life TEXT,
	association TEXT
);

CREATE TABLE config (
	image_route varchar(2083)
)

CREATE UNIQUE INDEX famous_index
ON famous (id, name, job, img, birth_date, birth_place, about, before_fame, curiosities, family_life, association);
