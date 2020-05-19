def prefix_function(s):
	n = len(s)
	pi = [0] * n #Массив префикс-функций
	for i in range(1, n):
		j = pi[i - 1]
		while j > 0 and s[i] != s[j]:
			j = pi[j - 1]
		if s[i] == s[j]:
			j += 1
		pi[i] = j
	return pi

def kmp(pattern, text):
	n = len(text)
	k = len(pattern)
	pi = prefix_function(pattern)
	pattern_pos = []
	i = 0
	j = 0
	while i < n:
		if text[i] == pattern[j]:
			i += 1
			j += 1
		if j == k:
			pattern_pos.append(i - j) #Подстрока найдена на позиции i - j
			j = pi[j - 1]
		elif i < n and text[i] != pattern[j]:
			if j != 0:
				j = pi[j - 1]
			else:
				i += 1
	return pattern_pos

def main():
	pattern = input("Input pattern: ")
	text = input("Input text: ")
	ans = kmp(pattern, text)
	for i in ans:
		print("Pattern found at " + str(i) + " position in text")


if __name__ == "__main__":
	main()
