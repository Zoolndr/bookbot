def count_characters(file_contents):
	letter_count = {}
	lowercase_string = file_contents.lower()

	for letter in lowercase_string:
		if letter.isalpha():
			if letter not in letter_count:
				letter_count[letter] = 1
			else:
				letter_count[letter] += 1
		
	return letter_count


def main():
	with open("/home/zoolender/workspace/github.com/ZOOLNDR/bookbot/books/frankenstein.txt") as f: 
		file_contents = f.read()
		character_counts = count_characters(file_contents)
		words = file_contents.split()
		wordcount = 0
		for word in words:
			wordcount += 1
		generate_report(wordcount, character_counts)
		


def sort_on(dict): 
	return dict["num"]

def sort_list(char_list):

	char_list.sort(reverse=True, key=sort_on)



def generate_report(wordcount, letter_count):
	char_list = []

	for letter, count in letter_count.items():
		char_dict = {'char': letter, 'num': count}
		char_list.append(char_dict)

	sort_list(char_list)
	print("--- Begin report of books/frankenstein.txt ---")
	print(f"{wordcount} words found in the document\n")

	for char_dict in char_list:
		print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
	
	print("--- End report ---")






main()



















