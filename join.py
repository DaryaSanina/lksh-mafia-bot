from bot.state import *
from telegram import Update


def join_game(update: Update, text: str, user: User) -> None:
    assert user.status == UserStatus.JOINING

    game_id = text
    if game_id not in state.game_by_id:
        update.message.reply_text(messages.NO_GAME.format(game_id=game_id))
        return
    game = state.game_by_id[game_id]
    user.join_game(game, update)

    if len(game.joined_user_ids) == len(game.roles):
        game.start_game(update)
        del state.game_by_id[game.game_id]
