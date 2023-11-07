class GarderieException(Exception):
    """
    Exception provoqué par une anomalie dans le taitement des donnèes
    """
    def __str__ (self):
        return "{0} {1}".format(self.__doc__, Exception.__str__(self))