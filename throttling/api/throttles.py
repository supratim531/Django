from rest_framework.throttling import UserRateThrottle

class EmployeeUserRateThrottle(UserRateThrottle):
  scope = "employee"
