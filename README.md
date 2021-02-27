# Mordvin

CLI aimed at transliterating text in Mordvinic languages Erzya and Moksha from cyrillic alphabet to latin alphabet.

Text to be transliterated should be put in file "to_translit.txt".

Basic transformation rules for the two languages can be checked in .yml files with corresponding names. 

Rules involving sequences of letters are applied first. This implies that the transformation rule for the individual letter (e.g. "т" -> "t") only applies in case the letter isn't combined with any of the letters specified in the multiple transformations (e.g. "та","тя","те,"тэ,"ты,"ти,"ту,"тю,"то,"тё"): usually the only remaining case is the final position in a word.

When one of the accented consonants (e.g. "ť") is preceeded by the same consonant without an accent in the final latin text, this one takes an accent as well ("tť"->"ťť").

Some additional rules are applied in Moksha, which depend on the position of the letter inside a word (first/last letter or first/last syllable). Here as well rules for groups are applied first.

- The group "те" always maps to "ťǝ" unless in the first syllable where it maps to "ťe";

- The letter "е" always maps to "ǝ" unless in the first syllable where it maps to "e" and in the last position, where it maps to "ä;

- The letter "o" always maps to "ǝ" unless in the first syllable where it maps to "e";

- The letter "э" always maps to "e" unless in the first position, where it maps to "ä;

In order to use the program type the following command in the terminal:

		python3 main.py [-h] language filepath_input [-o filepath_output]

where <language> is either Moksha or Erzya and <filepath_input> is the path to the file containing the text, typically "to_translate.txt". The optional argument -h or --help shows a description of the arguments. The optional argument -o filepath_output allows to save the transliterated text into the file <filepath_output>.

For example, the command:

		python3 main.py Moksha "to_translate.txt" -o "transliterated.txt"

transliterates in Moksha the text contained in "to_translate.txt" and saves it in a file named "transliterated.txt".




