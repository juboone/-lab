class television:
    """
    A class representing details for a Television object
    """
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create initial state of a Television object
        """
        self.__tv_channel = self.MIN_CHANNEL
        self.__tv_volume = self.MIN_VOLUME
        self.__status = True

    def power(self) -> None:
        """
        Method to access the power status of the Television.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def channel_up(self) -> None:
        """
        Method to turn the channel up by one.
           """
        if self.__status:
            self.__tv_channel = (self.__tv_channel + 1) % self.MAX_CHANNEL

    def channel_down(self) -> None:
        """
        Method to turn the channel down by one.
        """
        if self.__status:
            self.__tv_channel = abs((self.__tv_channel - 1) % self.MAX_CHANNEL)

    def volume_up(self) -> None:
        """
        Method to turn the volume up by one.
        """
        if self.__status:
            if self.__tv_volume < self.MAX_VOLUME:
                self.__tv_volume += 1

    def volume_down(self) -> None:
        """
        Method to turn the volume down by one.
        """
        if self.__status:
            if self.__tv_volume > self.MIN_VOLUME:
                self.__tv_volume -= 1

    def __str__(self) -> str:
        """
        Method to access a Television's string
        :return: Tv status
        """
        return f"TV status: Is on = {self.__status}, Channel = {self.__tv_channel}, Volume = {self.__tv_volume}"
