-- 1. 교체 시 들어오는 선수, 나가는 선수가 항상 같이 이뤄져야 함
delimiter $$
create procedure inout_of
(mid int unsigned, time char(10), club_id int unsigned,
in_player int unsigned, out_player int unsigned)
BEGIN
	declare err int default 0;
    declare continue handler for sqlexception set err = -1;
    start transaction;
    insert into in_out values(mid, 'On', time, in_player, club_id);
    insert into in_out values(mid, 'Off', time, out_player, club_id);
	if err < 0 then
		rollback;
	else
		commit;
	end if;
    select * from in_out where match_id=mid;
end$$

