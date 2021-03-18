from rest_framework.throttling import UserRateThrottle

class LimitedRateThrottle(UserRateThrottle):
    scope = 'limited'

class BurstRateThrottle(UserRateThrottle):
    scope = 'burst'


