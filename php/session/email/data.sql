CREATE DATABASE testmail;
use testmail;

CREATE TABLE user(
id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
username VARCHAR(20) NOT NULL DEFAULT '',
userpwd VARCHAR(32) NOT NULL  DEFAULT '',
PRIMARY KEY (id)
);

CREATE TABLE mail(
id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
uid INT(11) UNSIGNED NOT NULL DEFAULT '0',
mailtitle VARCHAR(20) NOT NULL DEFAULT '',
maildt INT(10) UNSIGNED NOT NULL DEFAULT '0',
PRIMARY KEY (id)
);

INSERT INTO user (username, userpwd) VALUES ('admin','123456');
INSERT INTO user (username, userpwd) VALUES ('user','123456');


INSERT INTO mail (uid, mailtitle, maildt) VALUES (1, 'admin mail one', 1336886600);
INSERT INTO mail (uid, mailtitle, maildt) VALUES (1, 'admin mail two', 1336887601);
INSERT INTO mail (uid, mailtitle, maildt) VALUES (1, 'admin mail three', 1336888602);
INSERT INTO mail (uid, mailtitle, maildt) VALUES (2, 'user mail one', 1336889602);
INSERT INTO mail (uid, mailtitle, maildt) VALUES (2, 'user mail two', 1336889605);

