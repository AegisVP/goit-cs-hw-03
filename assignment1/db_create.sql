create database goit_hw03;

use goit_hw03;

create table
    users (
        `id` serial primary key,
        `fullname` varchar(100) not null,
        `email` varchar(100),
        `created_at` timestamp not null default current_timestamp,
        constraint `un_email` unique (email)
    );

create table
    status (
        `id` serial primary key,
        `name` varchar(50) not null,
        `created_at` timestamp not null default current_timestamp,
        constraint `un_name` unique (name)
    );

insert into
    status (name)
values
    ('new'),
    ('in progress'),
    ('completed');

create table
    tasks (
        `id` serial primary key,
        `title` varchar(100) not null,
        `description` text not null,
        `status_id` serial,
        `user_id` serial,
        `created_at` timestamp not null default current_timestamp,
        foreign key (status_id) references `status` (id) on delete set null on update cascade,
        foreign key (user_id) references `users` (id) on delete cascade on update cascade
    );