class Television:
    """
    A class to represent a television
    :cvar MIN_VOLUME: Minimum volume level of the television
    :cvar MAX_VOLUME: Maximum volume level of the television
    :cvar MIN_CHANNEL: Minimum channel of the television
    :cvar MAX_CHANNEL: Maximum channel of the television
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, status=False, muted=False, volume=MIN_VOLUME, channel=MIN_CHANNEL) -> None:
        """
        Method to set default values of television object
        :param status: Whether the television is on or off
        :param muted: Whether the is muted or unmuted
        :param volume: The level of the television volume
        :param channel: The channel value of the television
        """
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel

    def power(self) -> None:
        """
        Method to toggle power
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Method to toggle mute
        """
        if self.__status:
            if not self.__muted:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self) -> None:
        """
        Method to switch channel up and wrap around
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to switch channel down and wrap around
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to turn volume up
        """
        if self.__status:
            self.__muted = False
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Method to turn volume down
        """
        if self.__status:
            self.__muted = False
            self.__volume -= 1
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Method to return television details

        Returns: Strings containing television details
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return  f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

