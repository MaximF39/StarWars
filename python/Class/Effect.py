from python.Static.Type.EffectType import EffectType
from python.Utils.JSONClass import JSONClass


class Effect(JSONClass):
    targetId: int
    effectType: int
    effect: dict

    def __init__(self, Owner, effects, data):
        super().__init__(data)
        self.Owner = Owner
        self.effects = effects

        for effect in self.effects:
            if effect['effectType'] == self.effectType:
                self.effect = effect
        if self.targetId == 0:
            self.targetId = self.Owner.id


    def get_effect(self, **kwargs):
        match self.effect:
            case EffectType.Damage:
                self.Player.get_effect(**kwargs)  # Даёт 50% дамага
            case EffectType.Shield:
                self.Player.get_effect(**kwargs)
            case EffectType.Speed:
                pass  # speed 30%
            case EffectType.Acid:
                pass  # уменьшает броню эм
            case EffectType.Slow:
                pass  # замедляет кор эм
            case EffectType.EnergyBurn:
                pass  # сжыгает энергию эм
            case EffectType.AsteroidsDestroyer:
                pass  # для пушки шоб астеры хорошо ломало
            case EffectType.Armor:
                pass  # ну типа броня
            case EffectType.SplashDamage:
                pass  # ну типа урон волной фаза
            case EffectType.ReloadTime:
                pass  # забавно но это эффект ускорения стрельбы сферой
            case EffectType.CPU:
                pass  # ну типа цп добавляет
            case EffectType.BlockShooting:
                pass  # ну наверно это эффект аглу
            case EffectType.RepairSpeed:
                pass  # ну типа жб
            case EffectType.BlockEnergyDamage:
                pass  # ну это наверно поглот
            case EffectType.ReflectDamage:
                pass  # отражатель очевидно
            case EffectType.RestoreEnergySpeed:
                pass  # не ебу че это, либо генератор, либо я хз
            case EffectType.BlockBuildDroids:
                pass  # нк очевидно блокировка дронов метаком
            case EffectType.ShootToSelf:
                pass  # метак кинутый на урон в себя
            case EffectType.Blind:
                pass  # помню что это слеповуха
            case EffectType.DestroyDroid:
                pass  # уничтожение дроида очевидно
            case EffectType.MakeDamage:
                pass  # урон фазом по цели
            case EffectType.MakeDamageInRadius:
                pass  # эм, урон фпзом в радиусе? а что тогда выше...
            case EffectType.EffectsProtection:
                pass  # защита от эффектов очевидно
            case EffectType.MissleDefence:
                pass  # не помню, чето связанное с уклонением,а... защита от ракет, точно
            case EffectType.ReturnDroids:
                pass  # вернуть дронов нитра
            case EffectType.RemoveEffects:
                pass  # снять эффекты нитра
            case EffectType.Freeze:
                pass  # заморозка нитра
            case EffectType.GetEnergy:
                pass  # восстановление енергии
            case EffectType.GetHealth:
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