from gasture_utils.FingerCurled import FingerCurled
from gasture_utils.FingerPosition import FingerPosition
from gasture_utils.FingerDataFormation import FingerDataFormation


def determine_position(curled_positions, finger_positions, known_finger_poses, min_threshold):
    obtained_positions = {}

    for finger_pose in known_finger_poses:
        score_at = 0.0
        for known_curl, known_curl_confidence, given_curl in \
                zip(finger_pose.curl_position, finger_pose.curl_position_confidence, curled_positions):
            if len(known_curl) == 0:
                if len(known_curl_confidence) == 1:
                    score_at += known_curl_confidence[0]
                    continue

            if given_curl in known_curl:
                confidence_at = known_curl.index(given_curl)
                score_at += known_curl_confidence[confidence_at]

        for known_position, known_position_confidence, given_position in \
                zip(finger_pose.finger_position, finger_pose.finger_position_confidence, finger_positions):
            if len(known_position) == 0:
                if len(known_position_confidence) == 1:
                    score_at += known_position_confidence[0]
                    continue

            if given_position in known_position:
                confidence_at = known_position.index(given_position)
                score_at += known_position_confidence[confidence_at]

        if score_at >= min_threshold:
            obtained_positions[finger_pose.position_name] = score_at

    return obtained_positions


def get_position_name_with_pose_id(pose_id, finger_poses):
    for finger_pose in finger_poses:
        if finger_pose.position_id == pose_id:
            return finger_pose.position_name
    return None


def create_known_finger_poses():
    """
    建立已知的手势的姿态信息
    :return:
    """
    known_finger_poses = []

    ####### 1 Simple Thumbs up   大拇指向上
    simple_thumbs_up = FingerDataFormation()
    simple_thumbs_up.position_name = 'Simple Thumbs Up'
    simple_thumbs_up.curl_position = [
        [FingerCurled.NoCurl],  # Thumb
        [FingerCurled.FullCurl],  # Index
        [FingerCurled.FullCurl],  # Middle
        [FingerCurled.FullCurl],  # Ring
        [FingerCurled.FullCurl]  # Little
    ]
    simple_thumbs_up.curl_position_confidence = [
        [1.0],  # Thumb
        [1.0],  # Index
        [1.0],  # Middle
        [1.0],  # Ring
        [1.0]  # Little
    ]
    simple_thumbs_up.finger_position = [
        [FingerPosition.VerticalUp, FingerPosition.DiagonalUpLeft, FingerPosition.DiagonalUpRight],  # Thumb
        [FingerPosition.HorizontalLeft, FingerPosition.HorizontalRight],  # Index
        [FingerPosition.HorizontalLeft, FingerPosition.HorizontalRight],  # Middle
        [FingerPosition.HorizontalLeft, FingerPosition.HorizontalRight],  # Ring
        [FingerPosition.HorizontalLeft, FingerPosition.HorizontalRight]  # Little
    ]
    simple_thumbs_up.finger_position_confidence = [
        [1.0, 0.25, 0.25],  # Thumb
        [1.0, 1.0],  # Index
        [1.0, 1.0],  # Middle
        [1.0, 1.0],  # Ring
        [1.0, 1.0]  # Little
    ]
    simple_thumbs_up.position_id = 0
    known_finger_poses.append(simple_thumbs_up)

    ####### 2 Thumbs up right
    thumbs_up_right = FingerDataFormation()
    thumbs_up_right.position_name = 'Thumbs Up Right'
    thumbs_up_right.curl_position = [
        [FingerCurled.NoCurl],  # Thumb
        [FingerCurled.FullCurl],  # Index
        [FingerCurled.FullCurl],  # Middle
        [FingerCurled.FullCurl],  # Ring
        [FingerCurled.FullCurl]  # Little
    ]
    thumbs_up_right.curl_position_confidence = [
        [1.0],  # Thumb
        [1.0],  # Index
        [1.0],  # Middle
        [1.0],  # Ring
        [1.0]  # Little
    ]
    thumbs_up_right.finger_position = [
        [FingerPosition.HorizontalLeft, FingerPosition.DiagonalUpLeft, FingerPosition.DiagonalDownLeft],  # Thumb
        [FingerPosition.VerticalUp, FingerPosition.DiagonalUpRight, FingerPosition.DiagonalUpLeft],  # Index
        [FingerPosition.VerticalUp, FingerPosition.DiagonalUpRight, FingerPosition.DiagonalUpLeft],  # Middle
        [FingerPosition.VerticalUp, FingerPosition.DiagonalUpRight, FingerPosition.DiagonalUpLeft],  # Ring
        [FingerPosition.VerticalUp, FingerPosition.DiagonalUpRight, FingerPosition.DiagonalUpLeft]  # Little
    ]
    thumbs_up_right.finger_position_confidence = [
        [1.0, 0.25, 0.25],  # Thumb
        [1.0, 0.25, 0.25],  # Index
        [1.0, 0.25, 0.25],  # Middle
        [1.0, 0.25, 0.25],  # Ring
        [1.0, 0.25, 0.25]  # Little
    ]
    thumbs_up_right.position_id = 1
    known_finger_poses.append(thumbs_up_right)

    ####### 3 Spock
    spock = FingerDataFormation()
    spock.position_name = 'Spock'
    spock.curl_position = [
        [FingerCurled.NoCurl],  # Thumb
        [FingerCurled.NoCurl],  # Index
        [FingerCurled.NoCurl],  # Middle
        [FingerCurled.NoCurl],  # Ring
        [FingerCurled.NoCurl]  # Little
    ]
    spock.curl_position_confidence = [
        [1.0],  # Thumb
        [1.0],  # Index
        [1.0],  # Middle
        [1.0],  # Ring
        [1.0]  # Little
    ]
    spock.finger_position = [
        [FingerPosition.DiagonalUpLeft, FingerPosition.HorizontalLeft],  # Thumb
        [FingerPosition.DiagonalUpLeft],  # Index
        [FingerPosition.DiagonalUpLeft],  # Middle
        [FingerPosition.DiagonalUpRight],  # Ring
        [FingerPosition.DiagonalUpRight]  # Little
    ]
    spock.finger_position_confidence = [
        [1.0, 0.5],  # Thumb
        [1.0],  # Index
        [1.0],  # Middle
        [1.0],  # Ring
        [1.0]  # Little
    ]
    spock.position_id = 2
    known_finger_poses.append(spock)

    ####### 4 I Love you
    i_love_you = FingerDataFormation()
    i_love_you.position_name = 'I love you'
    i_love_you.curl_position = [
        [FingerCurled.NoCurl],  # Thumb
        [FingerCurled.NoCurl],  # Index
        [FingerCurled.FullCurl],  # Middle
        [FingerCurled.FullCurl],  # Ring
        [FingerCurled.NoCurl]  # Little
    ]
    i_love_you.curl_position_confidence = [
        [1.0],  # Thumb
        [1.0],  # Index
        [1.0],  # Middle
        [1.0],  # Ring
        [1.0]  # Little
    ]
    i_love_you.finger_position = [
        [FingerPosition.DiagonalUpLeft],  # Thumb
        [FingerPosition.DiagonalUpLeft, FingerPosition.VerticalUp],  # Index
        [FingerPosition.DiagonalUpRight],  # Middle
        [FingerPosition.DiagonalUpRight],  # Ring
        [FingerPosition.DiagonalUpRight, FingerPosition.VerticalUp]  # Little
    ]
    i_love_you.finger_position_confidence = [
        [1.0],  # Thumb
        [1.0, 0.25],  # Index
        [1.0],  # Middle
        [1.0],  # Ring
        [1.0, 0.25]  # Little
    ]
    i_love_you.position_id = 3
    known_finger_poses.append(i_love_you)

    ####### 5 Pointer 大拇指和食指向上
    pointer = FingerDataFormation()
    pointer.position_name = 'Pointing Up'
    pointer.curl_position = [
        [FingerCurled.NoCurl],  # Thumb
        [FingerCurled.NoCurl],  # Index
        [FingerCurled.FullCurl],  # Middle
        [FingerCurled.FullCurl],  # Ring
        [FingerCurled.FullCurl]  # Little
    ]
    pointer.curl_position_confidence = [
        [1.0],  # Thumb
        [1.0],  # Index
        [1.0],  # Middle
        [1.0],  # Ring
        [1.0]  # Little
    ]
    pointer.finger_position = [
        [FingerPosition.VerticalUp, FingerPosition.DiagonalUpLeft],  # Thumb
        [FingerPosition.VerticalUp, FingerPosition.DiagonalUpLeft],  # Index
        [FingerPosition.VerticalUp],  # Middle
        [FingerPosition.VerticalUp],  # Ring
        [FingerPosition.VerticalUp]  # Little
    ]
    pointer.finger_position_confidence = [
        [1.0, 0.5],  # Thumb
        [1.0, 0.3],  # Index
        [1.0],  # Middle
        [1.0],  # Ring
        [1.0]  # Little
    ]
    pointer.position_id = 4
    known_finger_poses.append(pointer)

    ####### 6 Ok
    ok_pos = FingerDataFormation()
    ok_pos.position_name = 'Okay'
    ok_pos.curl_position = [
        [FingerCurled.HalfCurl],  # Thumb
        [FingerCurled.HalfCurl],  # Index
        [FingerCurled.NoCurl],  # Middle
        [FingerCurled.NoCurl],  # Ring
        [FingerCurled.NoCurl]  # Little
    ]
    ok_pos.curl_position_confidence = [
        [1.0],  # Thumb
        [1.0],  # Index
        [1.0],  # Middle
        [1.0],  # Ring
        [1.0]  # Little
    ]
    ok_pos.finger_position = [
        [FingerPosition.DiagonalUpLeft, FingerPosition.HorizontalLeft],  # Thumb
        [FingerPosition.DiagonalUpLeft, FingerPosition.HorizontalLeft],  # Index
        [FingerPosition.VerticalUp],  # Middle
        [FingerPosition.VerticalUp],  # Ring
        [FingerPosition.VerticalUp]  # Little
    ]
    ok_pos.finger_position_confidence = [
        [1.0, 0.5],  # Thumb
        [1.0, 0.2],  # Index
        [1.0],  # Middle
        [1.0],  # Ring
        [1.0]  # Little
    ]
    ok_pos.position_id = 5
    known_finger_poses.append(ok_pos)

    ####### 7 Victory  V 手势
    victory = FingerDataFormation()
    victory.position_name = 'Victory'
    victory.curl_position = [
        [FingerCurled.FullCurl, FingerCurled.NoCurl],  # Thumb
        [FingerCurled.NoCurl],  # Index
        [FingerCurled.NoCurl],  # Middle
        [FingerCurled.FullCurl],  # Ring
        [FingerCurled.FullCurl]  # Little
    ]
    victory.curl_position_confidence = [
        [1.0, 1.0],  # Thumb
        [1.0],  # Index
        [1.0],  # Middle
        [1.0],  # Ring
        [1.0]  # Little
    ]
    victory.finger_position = [
        [FingerPosition.VerticalUp, FingerPosition.HorizontalLeft],  # Thumb
        [FingerPosition.DiagonalUpLeft, FingerPosition.VerticalUp],  # Index
        [FingerPosition.DiagonalUpRight],  # Middle
        [FingerPosition.DiagonalUpRight],  # Ring
        [FingerPosition.DiagonalUpRight]  # Little
    ]
    victory.finger_position_confidence = [
        [0.5, 1.0],  # Thumb
        [1.0, 0.4],  # Index
        [1.0],  # Middle
        [1.0],  # Ring
        [1.0]  # Little
    ]
    victory.position_id = 6
    known_finger_poses.append(victory)


    ####### 8 1  食指向上
    one = FingerDataFormation()
    one.position_name = 'One'
    one.curl_position = [
        [FingerCurled.FullCurl],  # Thumb
        [FingerCurled.NoCurl],  # Index
        [FingerCurled.FullCurl],  # Middle
        [FingerCurled.FullCurl],  # Ring
        [FingerCurled.FullCurl]  # Little
    ]
    one.curl_position_confidence = [
        [1.0],  # Thumb
        [1.0],  # Index
        [1.0],  # Middle
        [1.0],  # Ring
        [1.0]  # Little
    ]
    one.finger_position = [
        [FingerPosition.VerticalUp, FingerPosition.DiagonalUpLeft],  # Thumb
        [FingerPosition.VerticalUp, FingerPosition.DiagonalUpLeft],  # Index
        [FingerPosition.VerticalUp],  # Middle
        [FingerPosition.VerticalUp],  # Ring
        [FingerPosition.VerticalUp]  # Little
    ]
    one.finger_position_confidence = [
        [1.0, 0.5],  # Thumb
        [1.0, 0.3],  # Index
        [1.0],  # Middle
        [1.0],  # Ring
        [1.0]  # Little
    ]
    one.position_id = 7
    known_finger_poses.append(one)

    ####### 9   3  3 手势
    three = FingerDataFormation()
    three.position_name = 'Three'
    three.curl_position = [
        [FingerCurled.FullCurl, FingerCurled.NoCurl],  # Thumb
        [FingerCurled.NoCurl],  # Index
        [FingerCurled.NoCurl],  # Middle
        [FingerCurled.NoCurl],  # Ring
        [FingerCurled.FullCurl]  # Little
    ]
    three.curl_position_confidence = [
        [1.0, 1.0],  # Thumb
        [1.0],  # Index
        [1.0],  # Middle
        [1.0],  # Ring
        [1.0]  # Little
    ]
    three.finger_position = [
        [FingerPosition.VerticalUp, FingerPosition.HorizontalLeft],  # Thumb
        [FingerPosition.DiagonalUpLeft, FingerPosition.VerticalUp],  # Index
        [FingerPosition.DiagonalUpLeft, FingerPosition.VerticalUp],  # Middle
        [FingerPosition.DiagonalUpLeft, FingerPosition.VerticalUp],  # Ring
        [FingerPosition.DiagonalUpRight]  # Little
    ]
    three.finger_position_confidence = [
        [0.5, 1.0],  # Thumb
        [1.0, 0.4],  # Index
        [1.0,1.0],  # Middle
        [1.0,1.0],  # Ring
        [1.0]  # Little
    ]
    three.position_id = 8
    known_finger_poses.append(three)

    return known_finger_poses