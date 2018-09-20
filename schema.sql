drop table if exists users;
    create table users (
    id integer primary key autoincrement,
    username text not null,
    password text not null
);

drop table if exists userdetails;
create table userdetails (
	id integer primary key autoincrement,
	username text not null,
	password text not null,
	age integer not null,
	image text not null,
	gender text not null,
	email text not null,
	description text not null
);

drop table if exists onesided;
create table onesided(
	id integer primary key autoincrement,
	likedby text not null,
	liked text not null
);

drop table if exists matches;
create table matches(
	id integer primary key autoincrement,
	groom text not null,
	bride text not null
);



-- Data Entered for tests
insert into users (username,password) values ("Hrithik","abcd");
insert into userdetails (username,password,age,image,gender,email,description) values ("Hrithik","abcd",20,"/static/hrithik.JPG","M","hrithik@gmail.com","Sexiest Asian Man!!");

insert into users (username,password) values ("Angelina","abcd");
insert into userdetails (username,password,age,image,gender,email,description) values ("Angelina","abcd",20,"/static/angelina.JPG","F","angelina@gmail.com","Pitt-ega tu");

insert into users (username,password) values ("Shahid","abcd");
insert into userdetails (username,password,age,image,gender,email,description) values ("Shahid","abcd",20,"/static/shahid.JPG","M","shahid@gmail.com","Main Rajput XD");

insert into users (username,password) values ("Rachel","abcd");
insert into userdetails (username,password,age,image,gender,email,description) values ("Rachel","abcd",20,"/static/jennifer.JPG","F","rachel@gmail.com","On a break (Hope Ross isn't around)");

insert into users (username,password) values ("Alia","abcd");
insert into userdetails (username,password,age,image,gender,email,description) values ("Alia","abcd",20,"/static/alia.JPG","F","alia@gmail.com","......");

insert into users (username,password) values ("Kate","abcd");
insert into userdetails (username,password,age,image,gender,email,description) values ("Kate","abcd",20,"/static/kate.JPG","F","kate@gmail.com","Titanic Waali :)");
