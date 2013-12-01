# Global Variables
teams_in_group = 6

# Initialise

team1="Ukraine"
team2="Poland"
team3="England"
team4="Moldova"
team5="Montenegro"
team6="San Marino"
team_group_a = set([]) #create empty set to store teams

def init():
	for i in range(teams_in_group): #create first group
		name = eval("team"+str(i+1)) #converts string to variable name
		a_team = Team(name) #create team with name - name
		team_group_a.add(a_team) # add a_team to team group
	
	
def produce_results():
	produce_results = []
	match0 = [team1, 0, team3, 0]
	match1 = [team1, 9, team6, 0]
	match2 = [team2, 1, team5, 1]
	produce_results = [match1, match2]
	#team1	0:0	team3	
	#team6	1:5 	team2	
	#team1	9:0 	team6	
	#team2	1:1 	team5	
	#team3	4:0 	team4	
	#team4	1:1 	team2	
	#team5	0:4 	team1	
	#team5	1:1 	team3	
	#team1	2:1 	team4	
	#team2	5:0 	team6	
	#team4	0:1 	team5	
	#team6	0:8 	team3	
	#team2	1:3 	team1	
	#team5	3:0 	team6	
	#team2	1:1 	team3	
	#team1	0:1 	team5	
	#team6	0:2 	team4	
	#team4	0:0		team1	
	#team3	5:0 	team6	
	#team2	2:0 	team4	
	#team6	0:6 	team5	
	#team3	1:1 	team1	
	#team4	0:5 	team3	
	#team5	2:2 	team2	
	#team3	-	team5	
	#team1	-	team2	
	#team4	-	team6	
	#team6	-	team1	
	#team5	-	team4	
	return produce_results
		
def find_element(search, content): # returns the first element in content that contains the element to be found - search
# this can then be used to work out the result of the matches and build the table
	return [element for element in content if element[0] == search or element[2] == search ]
		
#Define classes
class Team:
	def __init__(self, name):
		self.name = name
		return

	def get_name(self):
		return self.name
		

class Result:
	def __init__(self, name):
		self.name = name
		return
	
	
		#
# Let's get started
init() 
results = produce_results()
print(results)

for team in team_group_a:
	print(team.get_name())
	if find_element(team.get_name(), results) :
		print(find_element(team.get_name(), results))
		print(team.get_name() + " have played")
	
