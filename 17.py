import inflect
import re
p = inflect.engine()
print sum([len(re.sub('[- ]', '', p.number_to_words(i))) for i in range(1,1001)])
	