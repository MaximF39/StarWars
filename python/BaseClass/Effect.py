from python.Static.Type.EffectType import EffectType

class Effect:

    def __init__(self, Owner, effect):
        self.effect = effect

    def get_effect(self, **kwargs):
        match self.effect:
            case EffectType.Damage:
                self.Player.get_effect(**kwargs)
            case EffectType.Shield:
                pass
            case EffectType.Speed:
                pass
            case EffectType.Acid:
                pass
            case EffectType.Slow:
                pass
            case EffectType.EnergyBurn:
                pass
            case EffectType.AsteroidsDestroyer:
                pass
            case EffectType.Armor:
                pass
            case EffectType.SplashDamage:
                pass
            case EffectType.ReloadTime:
                pass
            case EffectType.CPU:
                pass
            case EffectType.BlockShooting:
                pass
            case EffectType.RepairSpeed:
                pass
            case EffectType.BlockEnergyDamage:
                pass
            case EffectType.ReflectDamage:
                pass
            case EffectType.RestoreEnergySpeed:
                pass
            case EffectType.BlockBuildDroids:
                pass
            case EffectType.ShootToSelf:
                pass
            case EffectType.Blind:
                pass
            case EffectType.DestroyDroid:
                pass
            case EffectType.MakeDamage:
                pass
            case EffectType.MakeDamageInRadius:
                pass
            case EffectType.EffectsProtection:
                pass
            case EffectType.MissleDefence:
                pass
            case EffectType.ReturnDroids:
                pass
            case EffectType.RemoveEffects:
                pass
            case EffectType.Freeze:
                pass
            case EffectType.GetEnergy:
                pass
            case EffectType.GetHealth:
                pass
            case EffectType.BuildDroid:
                pass
            case EffectType.ReflectedDamage:
                pass
            case EffectType.DroidsDamage:
                pass
            case EffectType.Vampire:
                self.Player.get_health(**kwargs)
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