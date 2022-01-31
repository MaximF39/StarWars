from python.Static.cfg.cfg_main import cfg_fixed

def toFixed(numObj, digits=cfg_fixed):
    return float(f"{numObj:.{digits}f}")
