-- Keep a log of any SQL queries you execute as you solve the mystery.
-- looking at the crime_scene_reports table
select * from crime_scene_reports;
-- specify the month year and location in the search 
select * from crime_scene_reports where year = 2021 and month = 7 and street = 'Humphrey Street';
-- Theft of the CS50 duck took place at 10:15am at the Humphrey
-- Street bakery. Interviews were conducted today with three 
-- witnesses who were present at the time – each of their 
-- interview transcripts mentions the bakery.
-- Let's look for interviews that mention this bakery specifically.
select * from interviews where year = 2021 and month = 7 and day = 28;