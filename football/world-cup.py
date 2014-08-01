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


def find_element(search,
                 content):  # returns the first element in content that contains the element to be found - search
    # this can then be used to work out the result of the matches and build the table
    return [element for element in content if element[0] == search or element[2] == search]


def get_fixtures():
    with open('fixtures.txt') as fixturesfile:
        fixtureslist = fixturesfile.read().split()
    print(fixtureslist)
    return fixtureslist


def clean_up(fixtures_messy):
    # remove half time scores
    for entry in fixtures_messy:
        if '(' in entry:
            assert isinstance(entry, object)
            fixtures_messy.remove(entry)
    return fixtures_messy


def split_matches(fixtures_blob, n):  # split fixtures list into individual matches
    # I expect n to be 3
    if n < 1:
        n = 1
    fixtures_split = [fixtures_blob[i:i + n] for i in range(0, len(fixtures_blob), n)]
    # print("SCORES are :", fixtures_split)
    home_goals = fixtures_split[0][1][0]
    # print("Home Goals: ", home_goals)
    results_copy = fixtures_split
    for result in fixtures_split:
        if str(result[1]) == "-":
            pass
            # print(result[1])
        else:
            home_goals = result[1][0]
            away_goals = result[1][2]
            result[1] = home_goals
            result.append(away_goals)
            # print("home goals:", home_goals, "away:", away_goals, "result: ", result)
            # result.append(results_copy[][1][1])
            # result[1] = results_copy[1][1][0]
            # print("scores: ", result[1], result[3])

    return fixtures_split


def process_results(results) -> object:
    for result in results:
        return
    return


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
print("fixtures before results are split is called: ", fixtures)
results = split_matches(results, 3)
print("these are the results so far ", results)
process_results(results)