import pandas as pd


def get_fg_made_miss(df, player_name=None, team_name=None, game_id=None):
    if player_name:
        df = df[df["PLAYER"] == player_name]
    if team_name:
        df = df[df["TEAM"] == team_name]
    if game_id:
        df = df[df["GAME_ID"] == game_id]

    fg_made = df[df["ID_ACTION"].isin(["2FGM", "3FGM"])]
    fg_miss = df[df["ID_ACTION"].isin(["2FGA", "3FGA"])]
    return fg_made, fg_miss


def plot_shot_chart(
    df, shot_chart, player_name=None, team_name=None, game_id=None, title=None
):
    fg_made_df, fg_miss_df = get_fg_made_miss(
        df, player_name=player_name, team_name=team_name, game_id=game_id
    )
    print(fg_made_df)
    shot_chart.plot_field_goal_scatter(fg_made_df, fg_miss_df, title=title)


def plot_shot_chart_temporal(
    df,
    shot_chart,
    player_name=None,
    team_name=None,
    game_id=None,
    title=None,
    gif_path="shots.gif",
):
    fg_made_df, fg_miss_df = get_fg_made_miss(
        df, player_name=player_name, team_name=team_name, game_id=game_id
    )
    shot_chart.plot_field_goal_scatter_temporal(
        fg_made_df, fg_miss_df, title=title, gif_path=gif_path
    )
