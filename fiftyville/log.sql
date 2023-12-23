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
select * from interviews where year = 2021 and month = 7 and day = 28 and transcript like '%bakery%';
--Notes: theit called the accomplice and said "take the earliest flight out of Fiftyville tomorrow" and accomplice will buy the ticket
-- Earlier this morning at the ATM on Leggett Street and saw the thief there withdrawing some money
-- within in 10 minutes the thief get into a car in the bakery parking lot and drive away
-- lets search for that transacrtion that happens at the atm to get a small list of people
select p.name, p.phone_number, p.passport_number, p.license_plate from people p join bank_accounts b on p.id = b.person_id join atm_transactions a on b.account_number = a.account_number  where a.year = 2021 and a.month = 7 and a.day = 28 and a.transaction_type = 'withdraw' and a.atm_location = 'Leggett Street';
--name     phone_number    passport_number  license_plate
--Bruce    (367) 555-5533  5773159633       94KL13X
--Diana    (770) 555-1861  3592750733       322W7JE
--Brooke   (122) 555-4581  4408372428       QX4YZN3
--Kenny    (826) 555-1652  9878712108       30G67EN
--Iman     (829) 555-5269  7049073643       L93JTIZ
--Luca     (389) 555-5198  8496433585       4328GD8
--Taylor   (286) 555-6063  1988161715       1106N58
--Benista  (338) 555-6650  9586786673       8X428L0
--Let's see if we can find someone who was seen leaving the bakery around then
select * from bakery_security_logs where year = 2021 and month = 7 and day = 28 AND license_plate IN ('94KL13X', '322W7JE', 'QX4YZN3', '30G67EN', 'L93JTIZ', '4328GD8', '1106N58', '8X428L0');
--id   year  month  day  hour  minute  activity  license_plate   name     phone_number    passport_number
--261  2021  7      28   10    18      exit      94KL13X         Bruce    (367) 555-5533  5773159633
--263  2021  7      28   10    19      exit      4328GD8         Luca     (389) 555-5198  8496433585
--265  2021  7      28   10    21      exit      L93JTIZ         Iman     (829) 555-5269  7049073643
--266  2021  7      28   10    23      exit      322W7JE         Diana    (770) 555-1861  3592750733
--268  2021  7      28   10    35      exit      1106N58         Taylor   (286) 555-6063  1988161715
--So, let's narrow down our list to just those two and check the calls
select * from phone_calls where year = 2021 and month = 7 and day = 28 and caller in ('(367) 555-5533','(389) 555-5198','(829) 555-5269','(770) 555-1861', '(286) 555-6063');
--id   caller          receiver        year  month  day  duration   name     phone_number    passport_number
--233  (367) 555-5533  (375) 555-8161  2021  7      28   45         Bruce    (367) 555-5533  5773159633
--236  (367) 555-5533  (344) 555-9601  2021  7      28   120        Bruce    (367) 555-5533  5773159633
--245  (367) 555-5533  (022) 555-4052  2021  7      28   241        Bruce    (367) 555-5533  5773159633
--254  (286) 555-6063  (676) 555-6554  2021  7      28   43         Taylor   (286) 555-6063  1988161715
--255  (770) 555-1861  (725) 555-3243  2021  7      28   49         Diana    (770) 555-1861  3592750733
--284  (286) 555-6063  (310) 555-8568  2021  7      28   235        Taylor   (286) 555-6063  1988161715
--285  (367) 555-5533  (704) 555-5790  2021  7      28   75         Bruce    (367) 555-5533  5773159633
-- lets look ip flights to see who got tickets for the day after
SELECT p.passport_number FROM flights f JOIN passengers p ON f.id = p.flight_id WHERE f.year = 2021 AND f.month = 7 AND f.day = 29 and p.passport_number in (5773159633,1988161715,3592750733);
--id  origin_airport_id  destination_airport_id  year  month  day  hour  minute  flight_id  passport_number  seat
--18  8                  6                       2021  7      29   16    0       18         3592750733       4C
--36  8                  4                       2021  7      29   8     20      36         5773159633       4A
--36  8                  4                       2021  7      29   8     20      36         1988161715       6D
--now lets find the destination airporut I think its 4
select * from airports where id = 4;
--4   LGA           LaGuardia Airport  New York City