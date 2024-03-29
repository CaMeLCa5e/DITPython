""" Dive into Python
example of methods and doc strings
"""

def info(object, spacing = 10, collapse = 1):

# 	print method and doc strings 
# 	takes module, class, list, dictionary or string

	methodList = [method for method in dir(object) if callable(getattr(object, method))]
	processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
	print '\n'.join(['%s %s' %
						(method.1just(spacing),
						processFunc(str(getattr(object, method).__doc__)))
					for method in methodList])
					
if__name__ == "__main__":
	print info.doc
	
	