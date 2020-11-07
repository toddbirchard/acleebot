from logger import LOGGER


def bot_events(bot):
    """Apply listeners to bot object."""

    @bot.on_message_delete
    def on_message_delete(room, user, message):
        """Log message deletions"""
        LOGGER.warning(
            f"[{room.name}] [{user.name.title()}]: {user.name} had message deleted from {room.name}: {message.body}"
        )

    @bot.on_mod_add
    def on_mod_add(room, user):
        """User is granted moderator privileges."""
        LOGGER.warning(
            f"[{room.name}] [{user.name.title()}]: {user.name} was modded in {room.name}."
        )

    @bot.on_mod_remove
    def on_mod_remove(room, user):
        """Moderator privileges are revoked from user."""
        LOGGER.warning(
            f"[{room.name}] [{user.name.title()}]: {user.name} was demodded in {room.name}."
        )

    @bot.on_join
    def on_join(room, user):
        """User joins room."""
        LOGGER.warning(
            f"[{room.name}] [{user.name.title()}]: {user.name} joined {room.name}."
        )

    def on_leave(room, user, puid):
        """User explicitly leaves room."""
        LOGGER.warning(
            f"[{room.name}] [{user.name.title()}]: {user.name} left {room.name}."
        )

    def on_flood_warning(room):
        """Bot receives warning prior to spam-ban."""
        LOGGER.error(f"Bot is about to be banned for spamming {room.name}.")

    def on_disconnect(room):
        """Bot client is disconnected from room."""
        LOGGER.error(f"Disconnected from {room}. Attempting to rejoin...")

    def on_login_fail(room):
        """Called on login failure, disconnects after."""
        LOGGER.error(f"Failed to log-in while joining {room.name}.")

    def on_flood_ban(room):
        """Bot is spam-banned from room."""
        LOGGER.error(f"Bot was spam banned from {room.name}.")

    def on_connect(room):
        """Bot successfully connects to room."""
        LOGGER.success(
            f"[{room.name}] [{self._name}]: Successfully connected to {room.name}"
        )

    def on_connect_fail(room):
        """Bot failed to join room."""
        LOGGER.error(f"Failed to connect to {room}. Retying...")

    def on_ban(room, user, target):
        """User gets banned."""
        LOGGER.warning(
            f"[{room.name}] [{user.name.title()}]: {target} was banned from {room.name} by {user.name}."
        )

    def on_unban(room, user, target):
        """User is unbanned."""
        LOGGER.warning(
            f"[{room.name}] [{user.name.title()}]: {target} was unbanned from {room.name} by {user.name}."
        )