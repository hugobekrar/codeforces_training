def transform_text(text):
	voyelles = ['a','e','i','o','u','y']
	res = []
	for i in range(len(text)):
		ch = text[i].lower()
		if ch not in voyelles : 
			res.append('.')
			res.append(ch)
	return res


text = input()
transformed_text = transform_text(text)
print("".join(transformed_text))