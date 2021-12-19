class Shoot:
    DROID_MUZZLE_INDEX_SHIFT: int = 10
    DROID_DESTROYED_INDEX_SHIFT: int = 10
    DROID_DAMAGED_INDEX_SHIFT: int = 30
    DESTROYED_TARGET_NO: int = 0
    DESTROYED_TARGET_THIS: int = 1
    DESTROYED_TARGET_DROID_1: int = 11
    DESTROYED_TARGET_DROID_2: int = 12
    DESTROYED_TARGET_DROID_3: int = 13
    DESTROYED_TARGET_DROID_4: int = 14
    DESTROYED_TARGET_DROID_5: int = 15
    DESTROYED_TARGET_DROID_6: int = 16
    DESTROYED_TARGET_DROID_7: int = 17
    DESTROYED_TARGET_DROID_8: int = 18
    DESTROYED_TARGET_DROID_9: int = 19
    DESTROYED_TARGET_DROID_10: int = 20
    DESTROYED_TARGET_DROID_11: int = 21
    DESTROYED_TARGET_DROID_12: int = 22
    classNumber: int
    damage: int
    destroyedTarget: int
    targetId: int
    targetType: int
    muzzleIndex: int
    