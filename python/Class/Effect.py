from time import sleep

from python.Static.Type.EffectType import EffectType

class Effect:
    targetId: int
    effectType: int
    effect: dict
    Player:"DB_Player"

    def __init__(self, Owner, effects, data):
        self.__dict__.update(data)
        self.Owner = Owner
        self.effects = effects

        for effect in self.effects:
            if effect['effectType'] == self.effectType:
                self.effect = effect
        if self.targetId == 0:
            self.targetId = self.Owner.id


    def get_effect(self, **kwargs):
        match self.effect:
            case EffectType.Damage: # 1
                self.Player.effects['damage'] = 50
                self.Player.get_effect(**kwargs)  # Даёт 50% дамага
            case EffectType.Shield: #2

                self.Player.get_effect(**kwargs)
            case EffectType.Speed: #3
                self.Player.effects['speed'] = 30  # speed 30%
            case EffectType.Acid: # 4
                pass  # уменьшает броню эм
            case EffectType.Slow: #5
                pass  # замедляет кор эм
            case EffectType.EnergyBurn: #6
                pass  # сжыгает энергию эм
            case EffectType.AsteroidsDestroyer: #7
                pass  # для пушки шоб астеры хорошо ломало
            case EffectType.Armor: # 8
                pass  # ну типа броня
            case EffectType.SplashDamage: # 9
                pass  # ну типа урон волной фаза
            case EffectType.ReloadTime: # 10
                pass  # забавно но это эффект ускорения стрельбы сферой
            case EffectType.CPU: # 11
                pass  # ну типа цп добавляет
            case EffectType.BlockShooting: # 12
                # аглу 12 сек
                pass
            case EffectType.RepairSpeed: # 13
                pass  # ну типа жб
            case EffectType.BlockEnergyDamage: # 14
                pass  # ну это наверно поглот
            case EffectType.ReflectDamage: # 15
                pass  # отражатель очевидно
            case EffectType.RestoreEnergySpeed: # 16
                for i in range(3):
                    sleep(1)
                    self.Player.reduce_energy_device(40)
            case EffectType.BlockBuildDroids: # 17
                # блок дройдов 30 сек
                pass
            case EffectType.ShootToSelf: # 18
                # метак на самодамаг 8 сек
                pass
            case EffectType.Blind: # 19
                pass  # помню что это слеповуха
            case EffectType.DestroyDroid: # 20
                pass  # уничтожение дроида очевидно
            case EffectType.MakeDamage: # 21
                self.Player.ObjectToReach.get_damage_device(500)
            case EffectType.MakeDamageInRadius: # 22
                # Фазер на урон в круге 400 damage
                pass  # эм, урон фпзом в радиусе? а что тогда выше...
            case EffectType.EffectsProtection: # 23
                pass  # защита от эффектов очевидно
            case EffectType.MissleDefence: # 24
                pass  # не помню, чето связанное с уклонением,а... защита от ракет, точно
            case EffectType.ReturnDroids: # 25
                pass  # вернуть дронов нитра
            case EffectType.RemoveEffects: # 26
                pass  # снять эффекты нитра
            case EffectType.Freeze: # 27
                pass  # заморозка нитра
            case EffectType.GetEnergy: # 28
                self.Player.reduce_energy_device(300)
            case EffectType.GetHealth: # 29
                pass  # восстановление хп
            case EffectType.BuildDroid:
                pass  # вероятнее всего, турбовозврат
            case EffectType.ReflectedDamage:
                pass  # рефлект дамейдж? отражатель? а что тогда выше...
            case EffectType.DroidsDamage:
                pass  # урон по дроидам
            case EffectType.Vampire:
                self.Player.weapon_health(**kwargs)
            case EffectType.MaxHealth:
                pass
            case EffectType.DodgeEffect:
                pass
            case EffectType.RadarDistance:
                pass
            case EffectType.ToEnergy:
                pass
            case EffectType.RestoreDevices:
                pass
            case EffectType.DestroyDevices:
                pass
            case EffectType.DamageToDistace:
                pass
            case EffectType.TargetMarker:
                pass
            case EffectType.DroidsDef:
                pass
            case EffectType.RepairFromMax:
                pass
            case EffectType.RepairFromEnergy:
                pass
            case EffectType.Hiding:
                pass
            case EffectType.DamageDef:
                pass