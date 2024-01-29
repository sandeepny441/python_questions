SELECT p.page_id
FROM pages p left join page_likes pl  
ON p.page_id = pl.page_id
where pl.liked_date is NULL

session_id	user_id	session_starttime	session_endtime	platform
