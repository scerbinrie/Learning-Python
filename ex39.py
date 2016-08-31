# create a mapping of state tpo abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'JAcksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '_' * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

#print some states
print '_' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the then cities dict
print '_' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Michigan']]

# print every state abbreviation
print '_' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '_' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '_' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])

print '_' * 10
# safely get an abbreviation by the state that might not be there
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas"

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is %s" % city 

