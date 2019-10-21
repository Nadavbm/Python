drop table if exists address;
create table address (
	id integer primary key autoincrement,
	name text not null
);

drop table if exists person;
create table person (
	id integer primary key autoincrement,
	address_id integer,
	name text not null
);

drop table if exists profession;
create table profession (
	id integer primary key autoincrement,
	person_id integer,
	title text not null
);
