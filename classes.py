class Television:
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self):
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        """
        Initially sets the TV to the minimal channel and volume and sets the tv to be turned off
        """

    def power(self):
        if not self.__status:
            self.__status = True
        else:
            self.__status = False
        """
        This method turns the tv on and off
        """

    def channel_up(self):
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
        else:
            pass

        """
        This method moves the channel up one until it hits the maximum channel then resets it to the minimum channel.
        """

    def channel_down(self):
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel += 1
        else:
            pass

        """
        This method moves the channel down by one until it hits the minimum channel and then resets it to he maximum
        channel
        """
        pass

    def volume_up(self):
        if self.__status:
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1
        else:
            pass

        """
        This method moves the volume up one each time it is called. When it hits the maximum volume it will not go up
        any further and stay on the maximum volume.
        """
    def volume_down(self):
        if self.__status:
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume -= 1
        else:
            pass
        """
        This method moves the volume down each time it is called. When it reaches the minimum volume it will not go down
        any further and will stay on the minimum volume.
        """

    def __str__(self):
        """
        Method to display the tv status, current channel and current volume.
        :return: TV status, current channel and current volume
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
