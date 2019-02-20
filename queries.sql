select * from yakkerevents.event limit 100;

select count(*) from yakkerevents.event;

select distinct (event_name),COUNT(event_name) from yakkerevents.event group by event_name;