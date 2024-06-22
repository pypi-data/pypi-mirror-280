import random
import pkg_resources

def random_chess_game(length: int = None, min_length: int = None, startswith: str = None, endswith_move: str = None, endswith_mate: bool = False,
                   cleargame: bool = False) -> str:
    """
    Returns a random chess game from a file.

    Params:
    - length (int): The desired length of the chess game in number of moves.
    - min_length (int): The minimum length of the chess game in number of moves.
    - startswith (str): The desired starting move(s) of the chess game.
    - endswith_move (str): The desired ending move(s) of the chess game.
    - endswith_mate (bool): Whether the chess game should end with a checkmate.
    - file (str): The path to the file containing the chess games (default: 'games.pgn').
    - cleargame (bool): Whether to remove move numbers from the selected game (default: False).


    """
    def no_movechars(game : str):
        """
        Removes move numbers from a chess game.

        Params:
        
            game (str): The chess game to remove move chars from.

        """
        return ' '.join([el for el in game.split() if not el.endswith('.')])

    file = pkg_resources.resource_filename('randomchessgame', 'GAMES.pgn')

    with open(file, 'r') as plik:
        games = [game.strip() for game in plik.readlines() if game.strip()]

    if length:
        games = [game for game in games if len(no_movechars(game).split()) == length]

    if min_length:
        games = [game for game in games if len(no_movechars(game).split()) >= min_length]

    if startswith:
        games = [game for game in games if no_movechars(game).startswith(startswith)]

    if endswith_move:
        games = [game for game in games if no_movechars(game).endswith(endswith_move)]

    if endswith_mate:
        games = [game for game in games if game.endswith('#')]

    try:
        random_game = random.choice(games)
    
    except IndexError:
        return 'No games found with the given criteria.'

    if cleargame:
        return no_movechars(random_game)

    return random_game

