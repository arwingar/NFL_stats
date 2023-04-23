import mysql.connector
from graphics import *

conn = mysql.connector.connect(
    host="localhost",
    database="nfl_stats",
    user="root",
    password="Buddies3$" )

cursor = conn.cursor()



def delay(d):
    for i in range(d):
        for i in range(100000):
            pass

def is_button(click, rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    if (click.getX() > p1.getX()) and (click.getX() < p2.getX()):
        if (click.getY() > p1.getY()) and (click.getY() < p2.getY()):
            return True
        else:
            return False
    else:
        return False
    
    
def createHome():
    winHome = GraphWin('Final Project',1450,832)
    winHome.setBackground('lightgray')
    redRect = Rectangle(Point(0,0), Point(850,50))
    redRect.setFill('red')
    redRect.draw(winHome)
    blueRect = Rectangle(Point(850,0), Point(1450,50))
    blueRect.setFill('blue')
    blueRect.draw(winHome)
    homeTxt = Text(Point(200,25), "NFL Offensive Data - Home")
    homeTxt.setTextColor('white')
    homeTxt.setSize(24)
    homeTxt.draw(winHome)

    statsBtn = Rectangle(Point(200,250), Point(600,450))
    statsBtn.setOutline('black')
    statsBtn.draw(winHome)
    statsTxt = Text(Point(400,350), 'See Stats')
    statsTxt.setSize(30)
    statsTxt.draw(winHome)

    dataBtn = Rectangle(Point(800,250), Point(1200,450))
    dataBtn.setOutline('black')
    dataBtn.draw(winHome)
    dataTxt = Text(Point(1000,350), 'Add Data')
    dataTxt.setSize(30)
    dataTxt.draw(winHome)

    while True:
        click = winHome.getMouse()
        if is_button(click, dataBtn):
            dataBtn.setFill('darkgray')
            delay(150)
            dataBtn.setFill('lightgray')
            print('To Data page.')
            createData()
        elif is_button(click, statsBtn):
            statsBtn.setFill('darkgray')
            delay(150)
            statsBtn.setFill('lightgray')
            print("To Stats Page.")
            createStats()
    winHome.close()


def createStats():
    winStats = GraphWin('Final Project',1450,832)
    winStats.setBackground('lightgray')
    redRect = Rectangle(Point(0,0), Point(362,50))
    redRect.setFill('red')
    redRect.draw(winStats)
    blueRect = Rectangle(Point(362,0), Point(1087,50))
    blueRect.setFill('blue')
    blueRect.draw(winStats)
    statsTxt = Text(Point(150,25), "NFL - See Stats")
    statsTxt.setTextColor('white')
    statsTxt.setSize(24)
    statsTxt.draw(winStats)
    homeBtn = Rectangle(Point(1087,0), Point(1450,50))
    homeBtn.setFill('red')
    homeBtn.draw(winStats)
    homeTxt = Text(Point(1225,25), 'Home')
    homeTxt.setTextColor('white')
    homeTxt.setSize(24)
    homeTxt.draw(winStats)

    inputTxt = Text(Point(350,100), 'Enter team name:')
    inputTxt.setSize(30)
    inputTxt.draw(winStats)
    inputBox = Entry(Point(750,100), 20)
    inputBox.setFill('white')
    inputBox.setSize(30)
    inputBox.draw(winStats)
    goBtn = Rectangle(Point(1000,75), Point(1100,125))
    goBtn.setFill('lightgreen')
    goBtn.draw(winStats)
    txtGo = Text(Point(1050,100), 'GO')
    txtGo.setSize(30)
    txtGo.draw(winStats)

    while True:
        click = winStats.getMouse()
        if is_button(click, homeBtn):
            break
        elif is_button(click, goBtn):
            goBtn.setFill('green')
            delay(150)
            goBtn.setFill('lightgreen')
            team = inputBox.getText()
            teamID = nameToID(team)
            sqlQuery = "SELECT * FROM stats WHERE team_id = '" + teamID + "'"
            headers = Text(Point(685,150), 'Ranking    Week    Points Scored    Total Yards    First Downs    Passes Completed    Passes Attempted    Passing Yards    Yards Per Pass Attempt    Rushing Yards    Penalties    Expected Points')
            headers.setStyle('bold')
            headers.setSize(11)
            headers.draw(winStats)
            cursor.execute(sqlQuery)
            results = []
            x = 30
            for row in cursor:
                results.append(row[1:])  
            for i in range(12):
                data = ''
                for j in range(len(results)):
                    if len(results) <= 7:
                        data = data + str(results[j][i]) + '\n\n\n'
                        txt = Text(Point(x,400), data)
                    elif len(results) > 7 and len(results) <= 10:
                        data = data + str(results[j][i]) + '\n\n'
                        txt = Text(Point(x,550), data)
                    elif len(results) > 10:
                        data = data + str(results[j][i]) + '\n'
                        txt = Text(Point(x,700), data)
                txt.draw(winStats)
                if i in (5,6,7):
                    x += 148
                elif i in (2,4,8,9,10):
                    x += 123
                else:
                    x += 73
    winStats.close()

def nameToID(name):
    query = "SELECT team_id FROM teams WHERE name LIKE'%" + name + "%'"
    cursor.execute(query)
    for row in cursor:
        return str(row[0])

    
    

def createData():
    winData = GraphWin('Final Project',1450,832)
    winData.setBackground('lightgray')
    redRect = Rectangle(Point(0,0), Point(362,50))
    redRect.setFill('red')
    redRect.draw(winData)
    blueRect = Rectangle(Point(362,0), Point(1087,50))
    blueRect.setFill('blue')
    blueRect.draw(winData)
    statsTxt = Text(Point(150,25), "NFL - Add Data")
    statsTxt.setTextColor('white')
    statsTxt.setSize(24)
    statsTxt.draw(winData)
    homeBtn = Rectangle(Point(1087,0), Point(1450,50))
    homeBtn.setFill('red')
    homeBtn.draw(winData)
    homeTxt = Text(Point(1225,25), 'Home')
    homeTxt.setTextColor('white')
    homeTxt.setSize(24)
    homeTxt.draw(winData)

    teamTxt = Text(Point(150,100), 'Team:')
    teamTxt.setSize(16)
    teamTxt.draw(winData)
    teamBox = Entry(Point(450,100), 20)
    teamBox.setFill('white')
    teamBox.setSize(16)
    teamBox.draw(winData)

    oppTxt = Text(Point(750,100), 'Opponent:')
    oppTxt.setSize(16)
    oppTxt.draw(winData)
    oppBox = Entry(Point(1050,100), 20)
    oppBox.setFill('white')
    oppBox.setSize(16)
    oppBox.draw(winData)

    whereTxt = Text(Point(550,150), 'Home or Away (H or A):')
    whereTxt.setSize(16)
    whereTxt.draw(winData)
    whereBox = Entry(Point(725,150), 5)
    whereBox.setFill('white')
    whereBox.setSize(16)
    whereBox.draw(winData)

    weekTxt = Text(Point(150,250), 'Week number:')
    weekTxt.setSize(16)
    weekTxt.draw(winData)
    weekBox = Entry(Point(362,250), 5)
    weekBox.setFill('white')
    weekBox.setSize(16)
    weekBox.draw(winData)

    rankTxt = Text(Point(150,300), 'Ranking:')
    rankTxt.setSize(16)
    rankTxt.draw(winData)
    rankBox = Entry(Point(362,300), 5)
    rankBox.setFill('white')
    rankBox.setSize(16)
    rankBox.draw(winData)

    ptsTxt = Text(Point(150,350), 'Points scored:')
    ptsTxt.setSize(16)
    ptsTxt.draw(winData)
    ptsBox = Entry(Point(362,350), 5)
    ptsBox.setFill('white')
    ptsBox.setSize(16)
    ptsBox.draw(winData)

    ydsTxt = Text(Point(150,400), 'Total Yards:')
    ydsTxt.setSize(16)
    ydsTxt.draw(winData)
    ydsBox = Entry(Point(362,400), 5)
    ydsBox.setFill('white')
    ydsBox.setSize(16)
    ydsBox.draw(winData)

    fdTxt = Text(Point(150,450), 'First downs:')
    fdTxt.setSize(16)
    fdTxt.draw(winData)
    fdBox = Entry(Point(362,450), 5)
    fdBox.setFill('white')
    fdBox.setSize(16)
    fdBox.draw(winData)

    pcTxt = Text(Point(150,500), 'Passes completed:')
    pcTxt.setSize(16)
    pcTxt.draw(winData)
    pcBox = Entry(Point(362,500), 5)
    pcBox.setFill('white')
    pcBox.setSize(16)
    pcBox.draw(winData)

    paTxt = Text(Point(950,250), 'Passes attempted:')
    paTxt.setSize(16)
    paTxt.draw(winData)
    paBox = Entry(Point(1140,250), 5)
    paBox.setFill('white')
    paBox.setSize(16)
    paBox.draw(winData)

    pyTxt = Text(Point(950,300), 'Passing yards:')
    pyTxt.setSize(16)
    pyTxt.draw(winData)
    pyBox = Entry(Point(1140,300), 5)
    pyBox.setFill('white')
    pyBox.setSize(16)
    pyBox.draw(winData)

    yppaTxt = Text(Point(950,350), 'Yards per pass attempt:')
    yppaTxt.setSize(16)
    yppaTxt.draw(winData)
    yppaBox = Entry(Point(1140,350), 5)
    yppaBox.setFill('white')
    yppaBox.setSize(16)
    yppaBox.draw(winData)

    ryTxt = Text(Point(950,400), 'Rushing yards:')
    ryTxt.setSize(16)
    ryTxt.draw(winData)
    ryBox = Entry(Point(1140,400), 5)
    ryBox.setFill('white')
    ryBox.setSize(16)
    ryBox.draw(winData)

    penTxt = Text(Point(950,450), 'Penalties:')
    penTxt.setSize(16)
    penTxt.draw(winData)
    penBox = Entry(Point(1140,450), 5)
    penBox.setFill('white')
    penBox.setSize(16)
    penBox.draw(winData)

    eptTxt = Text(Point(950,500), 'Expected points:')
    eptTxt.setSize(16)
    eptTxt.draw(winData)
    eptBox = Entry(Point(1140,500), 5)
    eptBox.setFill('white')
    eptBox.setSize(16)
    eptBox.draw(winData)

    goBtn = Rectangle(Point(600,600), Point(700,650))
    goBtn.setFill('lightgreen')
    goBtn.draw(winData)
    txtGo = Text(Point(650,625), 'GO')
    txtGo.setSize(30)
    txtGo.draw(winData)

    txtLink = Text(Point(700,800), 'The information to fill in these boxes can be found at https://www.nfl.com/scores/')
    txtLink.draw(winData)

    while True:
        click = winData.getMouse()
        if is_button(click, homeBtn):
            break
        elif is_button(click, goBtn):
            goBtn.setFill('green')
            delay(150)
            goBtn.setFill('lightgreen')
            team = teamBox.getText()
            teamID = nameToID(team)
            opp = oppBox.getText()
            hora = whereBox.getText()
            if hora == 'H': 
                homeID = nameToID(team)
                awayID = nameToID(opp)
            elif hora == 'A':
                homeID = nameToID(opp)
                awayID = nameToID(team)
            week = weekBox.getText()
            rank = rankBox.getText()
            points = ptsBox.getText()
            yards = ydsBox.getText()
            fDown = fdBox.getText()
            cPass = pcBox.getText()
            aPass = paBox.getText()
            pYards = pyBox.getText()
            yppa = yppaBox.getText()
            rYards = ryBox.getText()
            penalty = penBox.getText()
            exPoints = eptBox.getText()
            sqlQueryStats = 'INSERT INTO stats VALUES('+ teamID + ',' + rank + ',' + week + ',' + points + ',' + yards + ',' + fDown + ',' + cPass + ',' + aPass + ',' + pYards + ',' + yppa + ',' + rYards + ',' + penalty + ',' + exPoints + ')'
            # uncomment before deployment
            # cursor.execute(sqlQueryStats)
            sqlQueryGames = 'INSERT INTO games VALUES(' + week + ',' + homeID + ',' + awayID + ')'
            # uncomment before deployment
            # cursor.execute(sqlQueryGames)
            winComplete = GraphWin('Complete',350,200)
            doneTxt = Text(Point(175,50),'Your data has been added to the database!')
            doneTxt.draw(winComplete)
            okBtn = Rectangle(Point(150,125), Point(200, 160))
            okBtn.setFill('green')
            okBtn.draw(winComplete)
            okTxt = Text(Point(175,143), 'OK')
            okTxt.setStyle('bold')
            okTxt.draw(winComplete)
            while True:
                click1 = winComplete.getMouse()
                if is_button(click1, okBtn):
                    break
                elif is_button(click1, goBtn):
                    continue
            winComplete.close()
    winData.close()

def nameToID(name):
    query = "SELECT team_id FROM teams WHERE name LIKE'%" + name + "%'"
    cursor.execute(query)
    for row in cursor:
        return str(row[0])


createHome()