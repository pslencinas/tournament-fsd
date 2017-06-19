
CREATE DATABASE tournament

\c tournament

CREATE TABLE players (
    player_id SERIAL primary key, 
    player_name text
    );

-- table for matches
CREATE TABLE matches (
    match_id SERIAL primary key,
    winner INTEGER references players(player_id), 
    loser INTEGER references players(player_id)
    );


CREATE VIEW standings AS
	SELECT p.player_id as player_id, p.player_name,
	(SELECT count(*) FROM matches WHERE matches.winner = p.player_id) as won,
	(SELECT count(*) FROM matches WHERE p.player_id in (winner, loser)) as played
	FROM players p
	GROUP BY p.player_id
	ORDER BY won DESC;