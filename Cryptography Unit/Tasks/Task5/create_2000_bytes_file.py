with open('2000_bytes_long.txt', 'w') as f:
	num_characters = 2000

	for i in range(num_characters):
		f.write(str(i%10))
