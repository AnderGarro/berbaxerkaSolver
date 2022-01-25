DROP TABLE IF EXISTS `hitzak`;

CREATE TABLE hitzak (
lema VARCHAR(100),
agerpenkopurua INT,
maiztasuna FLOAT,
maiztasunlogaritmoa FLOAT,
kategoria VARCHAR(40),
hitzkopurua INT,
luzeera INT
);

LOAD DATA LOCAL INFILE "./Ehme_lemak.csv" INTO TABLE db.hitzak
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(lema,agerpenkopurua,maiztasuna,maiztasunlogaritmoa,kategoria,hitzkopurua,luzeera);
