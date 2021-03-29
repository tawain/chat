
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	person = None
	Morrie_word_count = 0
	Morrie_sticker_count = 0
	Morrie_image_count = 0
	邱斌銓_word_count = 0
	邱斌銓_sticker_count = 0
	邱斌銓_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Morrie':
			if s[2] == '貼圖':
				Morrie_sticker_count += 1
			elif s[2] == '圖片':
				Morrie_image_count += 1
			else:
				for m in s[2:]:
					Morrie_word_count += len(m)
		elif name == '邱斌銓':
			if s[2] == '貼圖':
				邱斌銓_sticker_count += 1
			elif s[2] == '圖片':
				邱斌銓_image_count += 1
			else:
				for m in s[2:]:
					邱斌銓_word_count += len(m)
	print('Morrie說了', Morrie_word_count)
	print('Morrie傳了', Morrie_sticker_count, '個貼圖')
	print('Morrie傳了', Morrie_image_count, '張圖片')

	print('邱斌銓說了', 邱斌銓_word_count, '個字')
	print('邱斌銓傳了', 邱斌銓_sticker_count, '個貼圖')
	print('邱斌銓傳了', 邱斌銓_image_count, '張圖片')
		# print(s)


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('[LINE]Morrie.txt')
	lines = convert(lines)
	# write_file('B', lines)

main()