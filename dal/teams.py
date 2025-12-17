import dal


class Teams:
    @classmethod
    async def create_db(cls):
        async with dal.Connection() as conn:
            await conn.execute("""
                CREATE TABLE IF NOT EXISTS teams(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                captain_id INTEGER NOT NULL,
                team_name TEXT,
                score INTEGER NOT NULL DEFAULT 0
                )
            """)

    @classmethod
    async def get_team_by_captain_id(cls, captain_id):
        async with dal.Connection() as conn:
            await conn.execute("""
                SELECT *
                FROM teams
                WHERE captain_id = ?
                LIMIT 1
            """, (captain_id,))

            team = await conn.fetchone()

            if not team:
                return None
            else:
                return dict(team)

    @classmethod
    async def get_team_by_name(cls, name):
        async with dal.Connection() as conn:
            await conn.execute("""
                SELECT *
                FROM teams
                WHERE team_name = ?
                LIMIT 1
            """, (name,))

            team = await conn.fetchone()

            if not team:
                return None
            else:
                return dict(team)

    @classmethod
    async def get_all_teams(cls):
        async with dal.Connection() as conn:
            await conn.execute("""
                SELECT *
                FROM teams
            """)
            teams = await conn.fetchall()

            if not teams:
                return None
            else:
                return [dict(team) for team in teams]

    @classmethod
    async def create_team(cls, captain_id, name):
        async with dal.Connection() as conn:
            await conn.execute("""
                INSERT INTO teams (captain_id, team_name)
                VALUES (?, ?)
            """, (captain_id, name))

    @classmethod
    async def increase_score_by_name(cls, name, score_increase):
        async with dal.Connection() as conn:
            await conn.execute("""
                UPDATE teams
                SET score = score + ?
                WHERE team_name = ?
                RETURNING team_name, score
            """, (score_increase, name))
            increased_team = await conn.fetchone()

            if not increased_team:
                return None
            else:
                return dict(increased_team)
