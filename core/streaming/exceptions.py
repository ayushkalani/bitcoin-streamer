
class BaseError(Exception):
   def __init__(self,**kwargs):
       self.kwargs = kwargs

class ApplicationError(BaseError):
    pass