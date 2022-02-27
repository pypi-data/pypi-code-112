from dataclasses import dataclass
from typing import Tuple

@dataclass(repr=True)
class Logo:
    name: str
    sportsdb_leagueid: int
    url: str
    sport: str
    shorthand: str
    apisportsid: int
    sportsdbid: int
    sportsipyid: int

baseball_teams = {
 'SFG': 'San Francisco Giants',
 'LAD': 'Los Angeles Dodgers',
 'TBR': 'Tampa Bay Rays',
 'HOU': 'Houston Astros',
 'MIL': 'Milwaukee Brewers',
 'CHW': 'Chicago White Sox',
 'BOS': 'Boston Red Sox',
 'NYY': 'New York Yankees',
 'TOR': 'Toronto Blue Jays',
 'STL': 'St. Louis Cardinals',
 'SEA': 'Seattle Mariners',
 'ATL': 'Atlanta Braves',
 'OAK': 'Oakland Athletics',
 'CIN': 'Cincinnati Reds',
 'PHI': 'Philadelphia Phillies',
 'CLE': 'Cleveland Indians',
 'SDP': 'San Diego Padres',
 'DET': 'Detroit Tigers',
 'NYM': 'New York Mets',
 'LAA': 'Los Angeles Angels',
 'COL': 'Colorado Rockies',
 'KCR': 'Kansas City Royals',
 'MIN': 'Minnesota Twins',
 'CHC': 'Chicago Cubs',
 'MIA': 'Miami Marlins',
 'WSN': 'Washington Nationals',
 'PIT': 'Pittsburgh Pirates',
 'TEX': 'Texas Rangers',
 'ARI': 'Arizona Diamondbacks',
 'BAL': 'Baltimore Orioles'
}
logo_map = {'Arizona Diamondbacks': Logo(name='Arizona Diamondbacks', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/sutyqp1431251804.png', sport='Baseball', shorthand='ARI', apisportsid=2, sportsdbid=135267, sportsipyid=None),
 'Atlanta Braves': Logo(name='Atlanta Braves', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/yjs76e1617811496.png', sport='Baseball', shorthand='ATL', apisportsid=3, sportsdbid=135268, sportsipyid=None),
 'Baltimore Orioles': Logo(name='Baltimore Orioles', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/ytywvu1431257088.png', sport='Baseball', shorthand='BAL', apisportsid=4, sportsdbid=135251, sportsipyid=None),
 'Boston Red Sox': Logo(name='Boston Red Sox', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/stpsus1425120215.png', sport='Baseball', shorthand='BOS', apisportsid=5, sportsdbid=135252, sportsipyid=None),
 'Chicago Cubs': Logo(name='Chicago Cubs', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/wxbe071521892391.png', sport='Baseball', shorthand='CHC', apisportsid=6, sportsdbid=135269, sportsipyid=None),
 'Chicago White Sox': Logo(name='Chicago White Sox', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/yyz5dh1554140884.png', sport='Baseball', shorthand='CWS', apisportsid=7, sportsdbid=135253, sportsipyid=None),
 'Cincinnati Reds': Logo(name='Cincinnati Reds', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/wspusr1431538832.png', sport='Baseball', shorthand='CIN', apisportsid=8, sportsdbid=135270, sportsipyid=None),
 'Cleveland Indians': Logo(name='Cleveland Indians', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/fp39hu1521904440.png', sport='Baseball', shorthand='CLE', apisportsid=9, sportsdbid=135254, sportsipyid=None),
 'Colorado Rockies': Logo(name='Colorado Rockies', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/wvbk1d1550584627.png', sport='Baseball', shorthand='COL', apisportsid=10, sportsdbid=135271, sportsipyid=None),
 'Detroit Tigers': Logo(name='Detroit Tigers', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/9dib6o1554032173.png', sport='Baseball', shorthand='DET', apisportsid=12, sportsdbid=135255, sportsipyid=None),
 'Houston Astros': Logo(name='Houston Astros', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/miwigx1521893583.png', sport='Baseball', shorthand='HOU', apisportsid=15, sportsdbid=135256, sportsipyid=None),
 'Kansas City Royals': Logo(name='Kansas City Royals', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/ii3rz81554031260.png', sport='Baseball', shorthand='KC', apisportsid=16, sportsdbid=135257, sportsipyid=None),
 'Los Angeles Angels': Logo(name='Los Angeles Angels', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/vswsvx1432577476.png', sport='Baseball', shorthand='LAA', apisportsid=17, sportsdbid=135258, sportsipyid=None),
 'Los Angeles Dodgers': Logo(name='Los Angeles Dodgers', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/rrdfmw1617528853.png', sport='Baseball', shorthand='LAD', apisportsid=18, sportsdbid=135272, sportsipyid=None),
 'Miami Marlins': Logo(name='Miami Marlins', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/0722fs1546001701.png', sport='Baseball', shorthand='MIA', apisportsid=19, sportsdbid=135273, sportsipyid=None),
 'Milwaukee Brewers': Logo(name='Milwaukee Brewers', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/08kh2a1595775193.png', sport='Baseball', shorthand='MIL', apisportsid=20, sportsdbid=135274, sportsipyid=None),
 'Minnesota Twins': Logo(name='Minnesota Twins', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/necd5v1521905719.png', sport='Baseball', shorthand='MIN', apisportsid=22, sportsdbid=135259, sportsipyid=None),
 'New York Mets': Logo(name='New York Mets', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/rxqspq1431540337.png', sport='Baseball', shorthand='NYM', apisportsid=24, sportsdbid=135275, sportsipyid=None),
 'New York Yankees': Logo(name='New York Yankees', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/wqwwxx1423478766.png', sport='Baseball', shorthand='NYY', apisportsid=25, sportsdbid=135260, sportsipyid=None),
 'Oakland Athletics': Logo(name='Oakland Athletics', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/wsxtyw1432577334.png', sport='Baseball', shorthand='OAK', apisportsid=26, sportsdbid=135261, sportsipyid=None),
 'Philadelphia Phillies': Logo(name='Philadelphia Phillies', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/3xrldf1617528682.png', sport='Baseball', shorthand='PHI', apisportsid=27, sportsdbid=135276, sportsipyid=None),
 'Pittsburgh Pirates': Logo(name='Pittsburgh Pirates', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/kw6uqr1617527138.png', sport='Baseball', shorthand='PIT', apisportsid=28, sportsdbid=135277, sportsipyid=None),
 'San Diego Padres': Logo(name='San Diego Padres', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/6wt1cn1617527530.png', sport='Baseball', shorthand='SD', apisportsid=30, sportsdbid=135278, sportsipyid=None),
 'San Francisco Giants': Logo(name='San Francisco Giants', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/mq81yb1521896622.png', sport='Baseball', shorthand='SF', apisportsid=31, sportsdbid=135279, sportsipyid=None),
 'Seattle Mariners': Logo(name='Seattle Mariners', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/39x9ph1521903933.png', sport='Baseball', shorthand='SEA', apisportsid=32, sportsdbid=135262, sportsipyid=None),
 'St. Louis Cardinals': Logo(name='St. Louis Cardinals', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/uvyvyr1424003273.png', sport='Baseball', shorthand='STL', apisportsid=33, sportsdbid=135280, sportsipyid=None),
 'St.Louis Cardinals': Logo(name='St. Louis Cardinals', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/uvyvyr1424003273.png', sport='Baseball', shorthand='STL', apisportsid=33, sportsdbid=135280, sportsipyid=None),
 'Tampa Bay Rays': Logo(name='Tampa Bay Rays', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/littyt1554031623.png', sport='Baseball', shorthand='TB', apisportsid=34, sportsdbid=135263, sportsipyid=None),
 'Texas Rangers': Logo(name='Texas Rangers', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/qt9qki1521893151.png', sport='Baseball', shorthand='TEX', apisportsid=35, sportsdbid=135264, sportsipyid=None),
 'Toronto Blue Jays': Logo(name='Toronto Blue Jays', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/f9zk3l1617527686.png', sport='Baseball', shorthand='TOR', apisportsid=36, sportsdbid=135265, sportsipyid=None),
 'Washington Nationals': Logo(name='Washington Nationals', sportsdb_leagueid=4424, url='https://www.thesportsdb.com/images/media/team/badge/wpqrut1423694764.png', sport='Baseball', shorthand='WAS', apisportsid=37, sportsdbid=135281, sportsipyid=None),
 'Atlanta Hawks': Logo(name='Atlanta Hawks', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/q3bx641635067495.png', sport='Basketball', shorthand='ATL', apisportsid=132, sportsdbid=134880, sportsipyid=None),
 'Boston Celtics': Logo(name='Boston Celtics', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/051sjd1537102179.png', sport='Basketball', shorthand='BOS', apisportsid=133, sportsdbid=134860, sportsipyid=None),
 'Brooklyn Nets': Logo(name='Brooklyn Nets', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/h0dwny1600552068.png', sport='Basketball', shorthand='BKN', apisportsid=134, sportsdbid=134861, sportsipyid=None),
 'Charlotte Hornets': Logo(name='Charlotte Hornets', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/xqtvvp1422380623.png', sport='Basketball', shorthand='CHA', apisportsid=135, sportsdbid=134881, sportsipyid=None),
 'Chicago Bulls': Logo(name='Chicago Bulls', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/yk7swg1547214677.png', sport='Basketball', shorthand='CHI', apisportsid=136, sportsdbid=134870, sportsipyid=None),
 'Cleveland Cavaliers': Logo(name='Cleveland Cavaliers', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/a2pp4c1503741152.png', sport='Basketball', shorthand='CLE', apisportsid=137, sportsdbid=134871, sportsipyid=None),
 'Dallas Mavericks': Logo(name='Dallas Mavericks', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/yqrxrs1420568796.png', sport='Basketball', shorthand='DAL', apisportsid=138, sportsdbid=134875, sportsipyid=None),
 'Denver Nuggets': Logo(name='Denver Nuggets', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/8o8j5k1546016274.png', sport='Basketball', shorthand='DEN', apisportsid=139, sportsdbid=134885, sportsipyid=None),
 'Detroit Pistons': Logo(name='Detroit Pistons', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/lg7qrc1621594751.png', sport='Basketball', shorthand='DET', apisportsid=140, sportsdbid=134872, sportsipyid=None),
 'Golden State Warriors': Logo(name='Golden State Warriors', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/irobi61565197527.png', sport='Basketball', shorthand='GSW', apisportsid=141, sportsdbid=134865, sportsipyid=None),
 'Houston Rockets': Logo(name='Houston Rockets', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/yezpho1597486052.png', sport='Basketball', shorthand='HOU', apisportsid=142, sportsdbid=134876, sportsipyid=None),
 'Indiana Pacers': Logo(name='Indiana Pacers', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/v6jzgm1503741821.png', sport='Basketball', shorthand='IND', apisportsid=143, sportsdbid=134873, sportsipyid=None),
 'Los Angeles Clippers': Logo(name='Los Angeles Clippers', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/jv7tf21545916958.png', sport='Basketball', shorthand='LAC', apisportsid=144, sportsdbid=134866, sportsipyid=None),
 'Los Angeles Lakers': Logo(name='Los Angeles Lakers', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/spa6c11621594682.png', sport='Basketball', shorthand='LAL', apisportsid=145, sportsdbid=134867, sportsipyid=None),
 'Memphis Grizzlies': Logo(name='Memphis Grizzlies', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/m64v461565196789.png', sport='Basketball', shorthand='MEM', apisportsid=146, sportsdbid=134877, sportsipyid=None),
 'Miami Heat': Logo(name='Miami Heat', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/5v67x51547214763.png', sport='Basketball', shorthand='MIA', apisportsid=147, sportsdbid=134882, sportsipyid=None),
 'Milwaukee Bucks': Logo(name='Milwaukee Bucks', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/olhug01621594702.png', sport='Basketball', shorthand='MIL', apisportsid=148, sportsdbid=134874, sportsipyid=None),
 'Minnesota Timberwolves': Logo(name='Minnesota Timberwolves', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/5xpgjg1621594771.png', sport='Basketball', shorthand='MIN', apisportsid=149, sportsdbid=134886, sportsipyid=None),
 'New Orleans Pelicans': Logo(name='New Orleans Pelicans', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/f341s31523700397.png', sport='Basketball', shorthand='NOP', apisportsid=150, sportsdbid=134878, sportsipyid=None),
 'New York Knicks': Logo(name='New York Knicks', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/wyhpuf1511810435.png', sport='Basketball', shorthand='NYK', apisportsid=151, sportsdbid=134862, sportsipyid=None),
 'Oklahoma City Thunder': Logo(name='Oklahoma City Thunder', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/xpswpq1422575434.png', sport='Basketball', shorthand='OKC', apisportsid=152, sportsdbid=134887, sportsipyid=None),
 'Orlando Magic': Logo(name='Orlando Magic', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/txuyrr1422492990.png', sport='Basketball', shorthand='ORL', apisportsid=153, sportsdbid=134883, sportsipyid=None),
 'Philadelphia 76ers': Logo(name='Philadelphia 76ers', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/71545f1518464849.png', sport='Basketball', shorthand='PHI', apisportsid=154, sportsdbid=134863, sportsipyid=None),
 'Phoenix Suns': Logo(name='Phoenix Suns', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/qrtuxq1422919040.png', sport='Basketball', shorthand='PHX', apisportsid=155, sportsdbid=134868, sportsipyid=None),
 'Portland Trail Blazers': Logo(name='Portland Trail Blazers', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/mbtzin1520794112.png', sport='Basketball', shorthand='POR', apisportsid=156, sportsdbid=134888, sportsipyid=None),
 'Sacramento Kings': Logo(name='Sacramento Kings', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/5d3dpz1611859587.png', sport='Basketball', shorthand='SAC', apisportsid=157, sportsdbid=134869, sportsipyid=None),
 'San Antonio Spurs': Logo(name='San Antonio Spurs', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/obucan1611859537.png', sport='Basketball', shorthand='SAS', apisportsid=158, sportsdbid=134879, sportsipyid=None),
 'Toronto Raptors': Logo(name='Toronto Raptors', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/ax36vz1635070057.png', sport='Basketball', shorthand='TOR', apisportsid=159, sportsdbid=134864, sportsipyid=None),
 'Utah Jazz': Logo(name='Utah Jazz', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/9p1e5j1572041084.png', sport='Basketball', shorthand='UTA', apisportsid=160, sportsdbid=134889, sportsipyid=None),
 'Washington Wizards': Logo(name='Washington Wizards', sportsdb_leagueid=4387, url='https://www.thesportsdb.com/images/media/team/badge/rhxi9w1621594729.png', sport='Basketball', shorthand='WAS', apisportsid=161, sportsdbid=134884, sportsipyid=None),
 'Arizona Cardinals': Logo(name='Arizona Cardinals', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/xvuwtw1420646838.png', sport='American Football', shorthand='ARI', apisportsid=0, sportsdbid=134946, sportsipyid=None),
 'Atlanta Falcons': Logo(name='Atlanta Falcons', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/rrpvpr1420658174.png', sport='American Football', shorthand='ATL', apisportsid=0, sportsdbid=134942, sportsipyid=None),
 'Baltimore Ravens': Logo(name='Baltimore Ravens', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/einz3p1546172463.png', sport='American Football', shorthand='BAL', apisportsid=0, sportsdbid=134922, sportsipyid=None),
 'Buffalo Bills': Logo(name='Buffalo Bills', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/6pb37b1515849026.png', sport='American Football', shorthand='BUF', apisportsid=0, sportsdbid=134918, sportsipyid=None),
 'Carolina Panthers': Logo(name='Carolina Panthers', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/xxyvvy1420940478.png', sport='American Football', shorthand='CAR', apisportsid=0, sportsdbid=134943, sportsipyid=None),
 'Chicago Bears': Logo(name='Chicago Bears', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/uwtwtv1420941123.png', sport='American Football', shorthand='CHI', apisportsid=0, sportsdbid=134938, sportsipyid=None),
 'Cincinnati Bengals': Logo(name='Cincinnati Bengals', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/qqtwwv1420941670.png', sport='American Football', shorthand='CIN', apisportsid=0, sportsdbid=134923, sportsipyid=None),
 'Cleveland Browns': Logo(name='Cleveland Browns', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/squvxy1420942389.png', sport='American Football', shorthand='CLE', apisportsid=0, sportsdbid=134924, sportsipyid=None),
 'Dallas Cowboys': Logo(name='Dallas Cowboys', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/wrxssu1450018209.png', sport='American Football', shorthand='DAL', apisportsid=0, sportsdbid=134934, sportsipyid=None),
 'Denver Broncos': Logo(name='Denver Broncos', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/upsspx1421635647.png', sport='American Football', shorthand='DEN', apisportsid=0, sportsdbid=134930, sportsipyid=None),
 'Detroit Lions': Logo(name='Detroit Lions', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/lgsgkr1546168257.png', sport='American Football', shorthand='DET', apisportsid=0, sportsdbid=134939, sportsipyid=None),
 'Green Bay Packers': Logo(name='Green Bay Packers', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/rqpwtr1421434717.png', sport='American Football', shorthand='GB', apisportsid=0, sportsdbid=134940, sportsipyid=None),
 'Houston Texans': Logo(name='Houston Texans', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/wqyryy1421436627.png', sport='American Football', shorthand='HOU', apisportsid=0, sportsdbid=134926, sportsipyid=None),
 'Indianapolis Colts': Logo(name='Indianapolis Colts', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/wqqvpx1421434058.png', sport='American Football', shorthand='IND', apisportsid=0, sportsdbid=134927, sportsipyid=None),
 'Jacksonville Jaguars': Logo(name='Jacksonville Jaguars', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/0mrsd41546427902.png', sport='American Football', shorthand='JAX', apisportsid=0, sportsdbid=134928, sportsipyid=None),
 'Kansas City Chiefs': Logo(name='Kansas City Chiefs', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/936t161515847222.png', sport='American Football', shorthand='KC', apisportsid=0, sportsdbid=134931, sportsipyid=None),
 'Las Vegas Raiders': Logo(name='Las Vegas Raiders', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/xqusqy1421724291.png', sport='American Football', shorthand='OAK', apisportsid=0, sportsdbid=134932, sportsipyid=None),
 'Los Angeles Chargers': Logo(name='Los Angeles Chargers', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/wbhu3a1548320628.png', sport='American Football', shorthand='LAC', apisportsid=None, sportsdbid=135908, sportsipyid=None),
 'Los Angeles Rams': Logo(name='Los Angeles Rams', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/8e8v4i1599764614.png', sport='American Football', shorthand='LA', apisportsid=None, sportsdbid=135907, sportsipyid=None),
 'Miami Dolphins': Logo(name='Miami Dolphins', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/trtusv1421435081.png', sport='American Football', shorthand='MIA', apisportsid=0, sportsdbid=134919, sportsipyid=None),
 'Minnesota Vikings': Logo(name='Minnesota Vikings', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/qstqqr1421609163.png', sport='American Football', shorthand='MIN', apisportsid=0, sportsdbid=134941, sportsipyid=None),
 'New England Patriots': Logo(name='New England Patriots', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/xtwxyt1421431860.png', sport='American Football', shorthand='NE', apisportsid=0, sportsdbid=134920, sportsipyid=None),
 'New Orleans Saints': Logo(name='New Orleans Saints', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/nd46c71537821337.png', sport='American Football', shorthand='NO', apisportsid=0, sportsdbid=134944, sportsipyid=None),
 'New York Giants': Logo(name='New York Giants', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/vxppup1423669459.png', sport='American Football', shorthand='NYG', apisportsid=0, sportsdbid=134935, sportsipyid=None),
 'New York Jets': Logo(name='New York Jets', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/hz92od1607953467.png', sport='American Football', shorthand='NYJ', apisportsid=0, sportsdbid=134921, sportsipyid=None),
 'Philadelphia Eagles': Logo(name='Philadelphia Eagles', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/pnpybf1515852421.png', sport='American Football', shorthand='PHI', apisportsid=0, sportsdbid=134936, sportsipyid=None),
 'Pittsburgh Steelers': Logo(name='Pittsburgh Steelers', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/2975411515853129.png', sport='American Football', shorthand='PIT', apisportsid=0, sportsdbid=134925, sportsipyid=None),
 'San Francisco 49ers': Logo(name='San Francisco 49ers', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/bqbtg61539537328.png', sport='American Football', shorthand='SF', apisportsid=0, sportsdbid=134948, sportsipyid=None),
 'Seattle Seahawks': Logo(name='Seattle Seahawks', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/wwuqyr1421434817.png', sport='American Football', shorthand='SEA', apisportsid=0, sportsdbid=134949, sportsipyid=None),
 'Tampa Bay Buccaneers': Logo(name='Tampa Bay Buccaneers', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/2dfpdl1537820969.png', sport='American Football', shorthand='TB', apisportsid=0, sportsdbid=134945, sportsipyid=None),
 'Tennessee Titans': Logo(name='Tennessee Titans', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/m48yia1515847376.png', sport='American Football', shorthand='TEN', apisportsid=0, sportsdbid=134929, sportsipyid=None),
 'Washington Football Team': Logo(name='Washington', sportsdb_leagueid=4391, url='https://www.thesportsdb.com/images/media/team/badge/1m3mzp1595609069.png', sport='American Football', shorthand='WAS', apisportsid=0, sportsdbid=134937, sportsipyid=None),
 'Anaheim Ducks': Logo(name='Anaheim Ducks', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/6g9t721547289240.png', sport='Ice Hockey', shorthand='ANA', apisportsid=670, sportsdbid=134846, sportsipyid=None),
 'Arizona Coyotes': Logo(name='Arizona Coyotes', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/3n1yqw1635072720.png', sport='Ice Hockey', shorthand='ARI', apisportsid=1460, sportsdbid=134847, sportsipyid=None),
 'Boston Bruins': Logo(name='Boston Bruins', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/vuspuq1421791546.png', sport='Ice Hockey', shorthand='BOS', apisportsid=673, sportsdbid=134830, sportsipyid=None),
 'Buffalo Sabres': Logo(name='Buffalo Sabres', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/3m3jhp1619536655.png', sport='Ice Hockey', shorthand='BUF', apisportsid=674, sportsdbid=134831, sportsipyid=None),
 'Calgary Flames': Logo(name='Calgary Flames', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/v8vkk11619536610.png', sport='Ice Hockey', shorthand='CGY', apisportsid=675, sportsdbid=134848, sportsipyid=None),
 'Carolina Hurricanes': Logo(name='Carolina Hurricanes', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/v07m3x1547232585.png', sport='Ice Hockey', shorthand='CAR', apisportsid=676, sportsdbid=134838, sportsipyid=None),
 'Chicago Blackhawks': Logo(name='Chicago Blackhawks', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/tuwyvr1422041801.png', sport='Ice Hockey', shorthand='CHI', apisportsid=678, sportsdbid=134854, sportsipyid=None),
 'Colorado Avalanche': Logo(name='Colorado Avalanche', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/wqutut1421173572.png', sport='Ice Hockey', shorthand='COL', apisportsid=679, sportsdbid=134855, sportsipyid=None),
 'Columbus Blue Jackets': Logo(name='Columbus Blue Jackets', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/ssytwt1421792535.png', sport='Ice Hockey', shorthand='CBJ', apisportsid=680, sportsdbid=134839, sportsipyid=None),
 'Dallas Stars': Logo(name='Dallas Stars', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/qrvywq1422042125.png', sport='Ice Hockey', shorthand='DAL', apisportsid=681, sportsdbid=134856, sportsipyid=None),
 'Detroit Red Wings': Logo(name='Detroit Red Wings', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/1c24ow1546544080.png', sport='Ice Hockey', shorthand='DET', apisportsid=682, sportsdbid=134832, sportsipyid=None),
 'Edmonton Oilers': Logo(name='Edmonton Oilers', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/uxxsyw1421618428.png', sport='Ice Hockey', shorthand='EDM', apisportsid=683, sportsdbid=134849, sportsipyid=None),
 'Florida Panthers': Logo(name='Florida Panthers', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/8qtaz11547158220.png', sport='Ice Hockey', shorthand='FLA', apisportsid=684, sportsdbid=134833, sportsipyid=None),
 'Los Angeles Kings': Logo(name='Los Angeles Kings', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/uvwtvx1421535024.png', sport='Ice Hockey', shorthand='LAK', apisportsid=685, sportsdbid=134852, sportsipyid=None),
 'Minnesota Wild': Logo(name='Minnesota Wild', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/swtsxs1422042685.png', sport='Ice Hockey', shorthand='MIN', apisportsid=687, sportsdbid=134857, sportsipyid=None),
 'Montreal Canadiens': Logo(name='Montreal Canadiens', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/stpryx1421791753.png', sport='Ice Hockey', shorthand='MTL', apisportsid=688, sportsdbid=134834, sportsipyid=None),
 'Nashville Predators': Logo(name='Nashville Predators', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/twqyvy1422052908.png', sport='Ice Hockey', shorthand='NSH', apisportsid=689, sportsdbid=134858, sportsipyid=None),
 'New Jersey Devils': Logo(name='New Jersey Devils', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/z4rsvp1619536740.png', sport='Ice Hockey', shorthand='NJD', apisportsid=690, sportsdbid=134840, sportsipyid=None),
 'New York Islanders': Logo(name='New York Islanders', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/hqn8511619536714.png', sport='Ice Hockey', shorthand='NYI', apisportsid=691, sportsdbid=134841, sportsipyid=None),
 'New York Rangers': Logo(name='New York Rangers', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/bez4251546192693.png', sport='Ice Hockey', shorthand='NYR', apisportsid=692, sportsdbid=134842, sportsipyid=None),
 'Ottawa Senators': Logo(name='Ottawa Senators', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/2tc1qy1619536592.png', sport='Ice Hockey', shorthand='OTT', apisportsid=693, sportsdbid=134835, sportsipyid=None),
 'Philadelphia Flyers': Logo(name='Philadelphia Flyers', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/qxxppp1421794965.png', sport='Ice Hockey', shorthand='PHI', apisportsid=695, sportsdbid=134843, sportsipyid=None),
 'Pittsburgh Penguins': Logo(name='Pittsburgh Penguins', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/dsj3on1546192477.png', sport='Ice Hockey', shorthand='PIT', apisportsid=696, sportsdbid=134844, sportsipyid=None),
 'San Jose Sharks': Logo(name='San Jose Sharks', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/yui7871546193006.png', sport='Ice Hockey', shorthand='SJS', apisportsid=697, sportsdbid=134853, sportsipyid=None),
 'Seattle Kraken': Logo(name='Seattle Kraken', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/zsx49m1595775836.png', sport='Ice Hockey', shorthand=None, apisportsid=1436, sportsdbid=140082, sportsipyid=None),
 'St. Louis Blues': Logo(name='St. Louis Blues', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/rsqtwx1422053715.png', sport='Ice Hockey', shorthand='STL', apisportsid=698, sportsdbid=134859, sportsipyid=None),
 'Tampa Bay Lightning': Logo(name='Tampa Bay Lightning', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/swysut1421791822.png', sport='Ice Hockey', shorthand='TBL', apisportsid=699, sportsdbid=134836, sportsipyid=None),
 'Toronto Maple Leafs': Logo(name='Toronto Maple Leafs', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/mxig4p1570129307.png', sport='Ice Hockey', shorthand='TOR', apisportsid=700, sportsdbid=134837, sportsipyid=None),
 'Vancouver Canucks': Logo(name='Vancouver Canucks', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/xqxxpw1421875519.png', sport='Ice Hockey', shorthand='VAN', apisportsid=701, sportsdbid=134850, sportsipyid=None),
 'Vegas Golden Knights': Logo(name='Vegas Golden Knights', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/7fd4521619536689.png', sport='Ice Hockey', shorthand='VGK', apisportsid=702, sportsdbid=135913, sportsipyid=None),
 'Washington Capitals': Logo(name='Washington Capitals', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/u17iel1547157581.png', sport='Ice Hockey', shorthand='WSH', apisportsid=703, sportsdbid=134845, sportsipyid=None),
 'Winnipeg Jets': Logo(name='Winnipeg Jets', sportsdb_leagueid=4380, url='https://www.thesportsdb.com/images/media/team/badge/bwn9hr1547233611.png', sport='Ice Hockey', shorthand='WPG', apisportsid=704, sportsdbid=134851, sportsipyid=None)}