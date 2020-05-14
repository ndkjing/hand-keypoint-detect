from enum import IntEnum


class FingerPosition(IntEnum):
    """
    定义手指姿势
    """
    VerticalUp = 0   # 垂直向上
    VerticalDown = 1  # 垂直向下
    HorizontalLeft = 2  # 水平向左
    HorizontalRight = 3  # 水平向右
    DiagonalUpRight = 4  # 右上
    DiagonalUpLeft = 5  # 左上
    DiagonalDownRight = 6  # 右下
    DiagonalDownLeft = 7  # 左下

    @staticmethod
    def get_finger_position_name(finger_position):
        if finger_position == FingerPosition.VerticalUp:
            finger_type = 'Vertical Up'
        elif finger_position == FingerPosition.VerticalDown:
            finger_type = 'Vertical Down'
        elif finger_position == FingerPosition.HorizontalLeft:
            finger_type = 'Horizontal Left'
        elif finger_position == FingerPosition.HorizontalRight:
            finger_type = 'Horizontal Right'
        elif finger_position == FingerPosition.DiagonalUpRight:
            finger_type = 'Diagonal Up Right'
        elif finger_position == FingerPosition.DiagonalUpLeft:
            finger_type = 'Diagonal Up Left'
        elif finger_position == FingerPosition.DiagonalDownRight:
            finger_type = 'Diagonal Down Right'
        elif finger_position == FingerPosition.DiagonalDownLeft:
            finger_type = 'Diagonal Down Left'
        return finger_type
