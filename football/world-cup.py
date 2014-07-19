# Global Variables
teams_in_group = 6

# Initialise

team1 = "Ukraine"
team2 = "Poland"
team3 = "England"
team4 = "Moldova"
team5 = "Montenegro"
team6 = "San Marino"
team_group_a = set([])  # create empty set to store teams


def init():
    for i in range(teams_in_group):  # create first group
        name = eval("team" + str(i + 1))  # converts string to variable name
        a_team = Team(name)  # create team with name - name
        team_group_a.add(a_team)  # add a_team to team group


def produce_results(fixtureslist):
    match4 = [team1, 0, team3, 0]
    match1 = [team1, 9, team6, 0]
    match2 = [team2, 1, team5, 1]
    match3 = [team1, 0, team3, 0]
    produce_results = [match1, match2, match3, match4]
    return produce_results


def find_element(search,
                 content):  # returns the first element in content that contains the element to be found - search
    # this can then be used to work out the result of the matches and build the table
    return [element for element in content if element[0] == search or element[2] == search]


def get_fixtures():
    with open('fixtures.txt') as fixturesfile:
        fixtureslist = fixturesfile.read().split()
    print(fixtureslist)
    return fixtureslist


def clean_up(fixtures):
    # remove half time scores
    for entry in fixtures:
        if '(' in entry:
            assert isinstance(entry, object)
            fixtures.remove(entry)
    return fixtures

def split_matches(fixtures, n): # split fixtures list into individual matches
    n = 3
    print('fixtures:', fixtures)
    if n < 1:
        n = 1
    temp_result = [fixtures[i:i + n] for i in range(0, len(fixtures), n)]
    print("these are what i think is the result so far ", temp_result)
    return temp_result

# Define classes
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
fixtures = get_fixtures()
results = clean_up(fixtures)
print("fixtures before produce results is called: ", fixtures)
# results = produce_results(fixtures)
print("these are the results so far ", split_matches(results, 3))


	
