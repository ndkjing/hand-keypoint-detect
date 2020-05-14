from enum import IntEnum


class FingerCurled(IntEnum):
    """
    定义手指弯曲
    """
    NoCurl = 0   # 无弯曲
    HalfCurl = 1   # 微弯曲
    FullCurl = 2   #全弯曲

    @staticmethod
    def get_finger_curled_name(finger_curled):
        finger_curled_name = ''
        if finger_curled == FingerCurled.NoCurl:
            finger_curled_name = 'No Curl'
        elif finger_curled == FingerCurled.HalfCurl:
            finger_curled_name = 'Half Curl'
        elif finger_curled == FingerCurled.FullCurl:
            finger_curled_name = 'Full Curl'
        return finger_curled_name