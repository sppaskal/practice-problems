SELECT DISTINCT player
FROM goal
JOIN game
ON matchid = id
WHERE (team1 = 'GER' OR team2 = 'GER')
	AND teamid <> 'GER';