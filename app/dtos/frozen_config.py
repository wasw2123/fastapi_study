from pydantic import ConfigDict

FROZEN_CONFIG = ConfigDict(frozen=True)
# frozen -> 선언 후 불변함 : 튜플같은 느낌
