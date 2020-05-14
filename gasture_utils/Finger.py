from enum import IntEnum


class Finger(IntEnum):
    Thumb = 0
    Index = 1
    Middle = 2
    Ring = 3
    Little = 4

    @staticmethod
    def get_array_of_points(finger):
        finger_array = None
        if finger == Finger.Thumb:
            finger_array = [(0, 1), (1, 2), (2 ,3), (3, 4)]
        elif finger == Finger.Index:
            finger_array = [(0, 5), (5, 6), (6, 7), (7, 8)]
        elif finger == Finger.Middle:
            finger_array = [(0, 9), (9, 10), (10, 11), (11, 12)]
        elif finger == Finger.Ring:
            finger_array = [(0, 13), (13, 14), (14, 15), (15, 16)]
        else:
            finger_array = [(0, 17), (17, 18), (18, 19), (19, 20)]
        return finger_array

    @staticmethod
    def get_finger_name(finger):
        finger_name = ''
        if finger == Finger.Thumb:
            finger_name = 'Thumb'
        elif finger == Finger.Index:
            finger_name = 'Index'
        elif finger == Finger.Middle:
            finger_name = 'Middle'
        elif finger == Finger.Ring:
            finger_name = 'Ring'
        elif finger == Finger.Little:
            finger_name = 'Little'
        return finger_name