from typing import List
from dataclasses import dataclass, asdict

@dataclass
class AStatsDef:
    id: int
    name: str
    t: int
    pd: int
    i: int
    tfl: int
    fr: int
    s: int
    td: int
    ff: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class AStatsKicking:
    id: int
    name: str
    xpm: int
    xpa: int
    fgm_2029: int
    fga_2029: int
    fgm_3039: int
    fga_3039: int
    fga_4049: int
    fgm_4049: int
    fgm_u20: int
    fga_u20: int
    fgm_50: int
    fga_50: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class AStatsOther:
    id: int
    name: str
    pen: int
    y: int
    pan: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class AStatsPassing:
    id: int
    name: str
    c: int
    a: int
    y: int
    avg: float
    td: int
    i: int
    r: float
    per: float
    sacked: int
    sackedyards: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class AStatsPunting:
    id: int
    name: str
    p: int
    y: int
    a: float
    l: int
    i: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class AStatsReceiving:
    id: int
    name: str
    c: int
    y: int
    avg: float
    l: int
    tar: int
    td: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class AStatsRushing:
    id: int
    name: str
    a: int
    y: int
    avg: float
    td: int
    l: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class AStatsST:
    id: int
    name: str
    kr: int
    kry: int
    krl: int
    pr: int
    pry: int
    prl: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class HStatsDef:
    id: int
    name: str
    t: int
    pd: int
    i: int
    tfl: int
    fr: int
    s: int
    td: int
    ff: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class HStatsKicking:
    id: int
    name: str
    xpm: int
    xpa: int
    fgm_2029: int
    fga_2029: int
    fgm_3039: int
    fga_3039: int
    fga_4049: int
    fgm_4049: int
    fgm_u20: int
    fga_u20: int
    fgm_50: int
    fga_50: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class HStatsOther:
    id: int
    name: str
    pen: int
    y: int
    pan: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class HStatsPassing:
    id: int
    name: str
    c: int
    a: int
    y: int
    avg: float
    td: int
    i: int
    r: float
    per: float
    sacked: int
    sackedyards: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class HStatsPunting:
    id: int
    name: str
    p: int
    y: int
    a: float
    l: int
    i: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class HStatsReceiving:
    id: int
    name: str
    c: int
    y: int
    avg: float
    l: int
    tar: int
    td: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class HStatsRushing:
    id: int
    name: str
    a: int
    y: int
    avg: float
    td: int
    l: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class HStatsST:
    id: int
    name: str
    kr: int
    kry: int
    krl: int
    pr: int
    pry: int
    prl: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class Scoring1Q:
    team: int
    typeS: str
    time: str
    play: str
    a: int
    h: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class Scoring2Q:
    team: int
    typeS: str
    time: str
    play: str
    a: int
    h: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class Scoring3Q:
    team: int
    typeS: str
    time: str
    play: str
    a: int
    h: int

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class Scoring4Q:
    team: int
    typeS: str
    time: str
    play: str
    a: int
    h: int
    
    def to_dict(self) -> dict:
        return asdict(self)
    
@dataclass
class ScoringOT:
    team: int
    typeS: str
    time: str
    play: str
    a: int
    h: int

    def to_dict(self) -> dict:
        return asdict(self)
    

@dataclass
class Root:
    id: int
    hId: int
    aId: int
    weather: str
    hMascot: str
    aMascot: str
    hAbb: str
    aAbb: str
    hRec: str
    aRec: str
    h1Q: int
    hF: int
    a1Q: int
    a2Q: int
    a3Q: int
    a4Q: int
    aF: int
    oPOGId: int
    dPOGId: int
    oPOG: str
    dPOG: str
    aFD: int
    a3rdM: int
    a3rdA: int
    aYds: int
    aPassing: int
    aComp: int
    aAtt: int
    aYPP: float
    aRushing: int
    aRushes: int
    aYPR: float
    aPen: int
    aPenYds: int
    aTO: int
    aInt: int
    aTOP: str
    hFD: int
    h3rdM: int
    h3rdA: int
    h4thA: int
    hYds: int
    hPassing: int
    hComp: int
    hAtt: int
    hYPP: float
    hRushing: int
    hRushes: int
    hYPR: float
    hPen: int
    hPenYds: int
    hTOP: str
    scoring1Q: List[Scoring1Q]
    scoring2Q: List[Scoring2Q]
    scoring3Q: List[Scoring3Q]
    scoring4Q: List[Scoring4Q]
    scoringOT: List[ScoringOT]
    aStatsPassing: List[AStatsPassing]
    hStatsPassing: List[HStatsPassing]
    aStatsRushing: List[AStatsRushing]
    hStatsRushing: List[HStatsRushing]
    aStatsReceiving: List[AStatsReceiving]
    hStatsReceiving: List[HStatsReceiving]
    aStatsKicking: List[AStatsKicking]
    hStatsKicking: List[HStatsKicking]
    aStatsPunting: List[AStatsPunting]
    hStatsPunting: List[HStatsPunting]
    aStatsST: List[AStatsST]
    hStatsST: List[HStatsST]
    aStatsDef: List[AStatsDef]
    hStatsDef: List[HStatsDef]
    aStatsOther: List[AStatsOther]
    hStatsOther: List[HStatsOther]
    h2Q: int
    hFum: int
    aFum: int
    h4thM: int
    hTO: int
    hFumL: int
    h4Q: int
    a4thM: int
    a4thA: int
    h3Q: int
    hInt: int
    aFumL: int

    def to_dict(self) -> dict:
        return asdict(self)