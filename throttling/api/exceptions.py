from rest_framework.exceptions import APIException

class CustomAPIException(APIException):
  is_str = True

  def __init__(self, detail=None, code=None, is_str=True):
    self.is_str = is_str
    super().__init__(detail, code)

class NotExistException(CustomAPIException):
  def __init__(self, detail=None, code=404, is_str=True):
    super().__init__(detail, code, is_str)

class ValidationException(CustomAPIException):
  def __init__(self, detail=None, code=400, is_str=True):
    super().__init__(detail, code, is_str)
