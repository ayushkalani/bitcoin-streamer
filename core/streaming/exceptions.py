
class BaseError(Exception):
   """Base class for other exceptions
   """
   def __init__(self,**kwargs):
       self.kwargs = kwargs

class ApplicationError(BaseError):
    """Class for Application logic exceptions
    """
    pass