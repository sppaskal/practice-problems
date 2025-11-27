-- MySQL

WITH FirstLogin AS (
    SELECT 
        player_id,
        MIN(event_date) AS first_login_date
    FROM 
        Activity
    GROUP BY 
        player_id
),
ConsecutiveLogins AS (
    SELECT 
        a.player_id
    FROM 
        Activity a
    JOIN 
        FirstLogin fl
    ON 
        a.player_id = fl.player_id
        AND a.event_date = DATE_ADD(fl.first_login_date, INTERVAL 1 DAY)
),
TotalPlayers AS (
    SELECT COUNT(DISTINCT player_id) AS total_players
    FROM Activity
),
LoggedInAgain AS (
    SELECT COUNT(DISTINCT player_id) AS consecutive_players
    FROM ConsecutiveLogins
)
SELECT 
    ROUND(
        CAST(l.consecutive_players AS FLOAT) / t.total_players, 
        2
    ) AS fraction
FROM 
    LoggedInAgain l
CROSS JOIN 
    TotalPlayers t;