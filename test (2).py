#Define Variables
#Define World Cup Football Teams
teamA="England"
teamB="Spain"
teamC="Croatia"
teamD="Italy"
#Define Game Results
#Home Team, Home Goals, Away Team, Away Goals
game1 = (teamA,1,teamB,2)
game2 = (teamA,2,teamC,1)
game3 = (teamA,0,teamD,0)
game4 = (teamB,2,teamC,1)
game5 = (teamB,0,teamD,1)
game6 = (teamC,1,teamD,1)

#Define Points etc
#Points, For, Against, Difference
teamAstats = (0,0,0,0)
teamBstats = (0,0,0,0)
teamCstats = (0,0,0,0)
teamDstats = (0,0,0,0)
game=1
def result(game):
    if game==1:
        game=game1       
    elif game==2:
        game=game2
    elif game==3:
        game=game3
    elif game==4:
        game=game4        
    elif game==5:
        game=game5        
    else:
        game=game6
    print "game 0",game[0]
    statsHome=game[0]
    statsAway=game[2]
    print "home team is",game[0]
    print "home team stats:",statsHome
    print "Away team stats:",statsAway

#print  gameID + homeTeam + awayTeam
#if gameID[1]>gameID[3]:
#    result="home"
#elif gameID[1]<game1[3]:
#    result="away"
#else:
#    result="draw"
#print "Result of Game " + result



#Print game results
print "RESULTS"
print game1
print game2
print game3
print game4
print game5
print game6
print "TABLE"
print "Team, Points,For,Against,Difference"
print teamA, teamAstats
print teamB, teamBstats
print teamC, teamCstats
print teamD, teamDstats
print "New Results"
for i in range(1,7):
    print result(i)

