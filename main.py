#airport tickets
"""
JA to FA,
FA to GA,
GA to SF
SF to LA

Tell me where you are, and where you came from (JA to LA)

make a function, of which the arguments are [{"JA": "FA"}, {"FA":"GA
return a dict with key start and end.  start is a key that points to JA, end is a key that points to LA
"""

#my tickets
ticket_dictionary = {0:"JA", 1:"FA", 2:"GA", 3:"SF", 4:"LA"}

#algorithm to determine where i started and where I am
def where_am_i(start_name, end_name):

	#get starting key using start_name, store in new dict
	for temp_key_start, name in ticket_dictionary.items():
		if start_name == name:
			start_key = temp_key_start
			i_am_here = {0:start_name}

	#get ending key using end_name, store in new dict
	for temp_key_end, name in ticket_dictionary.items():
		if end_name == name:
			end_key = temp_key_end
			i_am_here[1] = end_name

	#return dict of start and end
	return i_am_here


#unit test
def test_where(expect, dictionary):
    if expect == dictionary[1]:
        print ("Pass")
    else:
        print ("Fail, expected ", expect, ", got ", dictionary[1])

#pass tests
test_where("SF", where_am_i("JA", "SF"))
test_where("GA", where_am_i("FA", "GA"))
test_where("LA", where_am_i("JA", "LA"))

#fail tests
test_where("FA", where_am_i("JA","GA"))
test_where("SF", where_am_i("FA","LA"))
test_where("JA", where_am_i("JA","SF"))
