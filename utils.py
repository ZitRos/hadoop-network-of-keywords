import re


regex = re.compile('[^.,;():?!"\'\s]+(?:\'[sd])?')
file_name_r = re.compile('[^/]*/?[^/]*$')

def filename_from_path(path):
	if not isinstance(path, basestring):
		return "?"
	return re.findall(file_name_r, path)[0]

def normalize_words(words):
	normalized = []
	for word in words:
		lower = word.lower()
		if lower == 'it\'s':
			normalized.append('it')
			normalized.append('is')
			continue
		if len(lower) > 2 and lower[-2] == '\'':
			if lower[-1] == 'd':
				normalized.append(lower[:-2])
				normalized.append('would')
				continue
			if lower[-1] == 's':
				lower = lower[:-2]
				if len(lower) == 0:
					continue
		normalized.append(lower)
	return normalized

def get_normalized_words(line):
	return normalize_words(regex.findall(line))
