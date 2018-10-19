Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> word = "abc"
>>> word.isupper()
False
>>> word.islower()
True
>>> word = "aBc"
>>> word.islower()
False
>>> word.isupper()
False
>>> not word.islower()
True
>>> text2[-2:]

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    text2[-2:]
NameError: name 'text2' is not defined
>>> import ntlk

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    import ntlk
ImportError: No module named ntlk
>>> import nltk
>>> from nltk.book import *
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
>>> text2[-2:]
[u'THE', u'END']
>>> [w for w in text5 if len(w)==4]
[u'left', u'with', u'this', u'name', u'PART', u'well', u'NICK', u'name', u'U121', u'golf', u'clap', u'JOIN', u'that', u'nice', u'JOIN', u'PART', u'golf', u'clap', u'fuck', u'U121', u'PART', u'PART', u'clap', u'your', u'PART', u'dont', u'even', u'know', u'what', u'that', u'that', u'chat', u'JOIN', u'drew', u'cast', u'PART', u'sexy', u'U115', u'JOIN', u'PART', u'drew', u'girl', u'with', u'legs', u'hope', u'draw', u'PART', u'head', u'legs', u'JOIN', u'JOIN', u'good', u'JOIN', u'PART', u'take', u'have', u'docs', u'Slip', u'away', u'Fade', u'away', u'Days', u'away', u'feel', u'have', u'back', u'U115', u'U129', u'U115', u'chat', u'with', u'PART', u'JOIN', u'JOIN', u'fast', u'U116', u'bowl', u'bong', u'JOIN', u'well', u'glad', u'hard', u'from', u'here', u'back', u'PART', u'PART', u'JOIN', u'U121', u'name', u'hard', u'very', u'fire', u'from', u'here', u'JOIN', u'PART', u'itch', u'JOIN', u'U133', u'ogan', u'male', u'JOIN', u'JOIN', u'show', u'will', u'talk', u'PART', u'haha', u'opps', u'JOIN', u'PART', u'U115', u'nice', u'warm', u'guys', u'with', u'cams', u'play', u'sits', u'JOIN', u'JOIN', u'guyz', u'chat', u'U126', u'PART', u'chat', u'PART', u'gooo', u'sure', u'U126', u'JOIN', u'what', u'feel', u'like', u'room', u'yeee', u'JOIN', u'want', u'pics', u'look', u'U139', u'PART', u'PART', u'JOIN', u'here', u'JOIN', u'PART', u'JOIN', u'U139', u'PART', u'JOIN', u'U138', u'U139', u'make', u'U139', u'that', u'U126', u'late', u'lmao', u'ahah', u'PART', u'U121', u'U121', u'does', u'like', u'that', u'guys', u'male', u'JOIN', u'U139', u'well', u'what', u'yeah', u'know', u'U136', u'hell', u'with', u'U139', u'U101', u'like', u'when', u'plan', u'PART', u'JOIN', u'gold', u'jeep', u'make', u'sure', u'nice', u'ring', u'U115', u'isnt', u'that', u'U136', u'hell', u'have', u'have', u'doin', u'U139', u'U121', u'many', u'Just', u'fine', u'that', u'like', u'PART', u'hiya', u'room', u'lmao', u'doin', u'Deep', u'Show', u'that', u'love', u'that', u'Turn', u'take', u'Hand', u'just', u'even', u'look', u'hang', u'PART', u'that', u'such', u'word', u'U141', u'hear', u'!!!!', u'PART', u'JOIN', u'PART', u'deaf', u'here', u'dont', u'U115', u'U115', u'....', u'hugs', u'chat', u'with', u'baby', u'Only', u'U121', u'U121', u'PART', u'have', u'away', u'from', u'U121', u'what', u'read', u'here', u'with', u'JOIN', u'read', u'have', u'here', u'JOIN', u'want', u'chat', u'talk', u'U121', u'JOIN', u'U121', u'VBox', u'PART', u'take', u'that', u'JOIN', u'PART', u'hate', u'when', u'U121', u'U115', u'lmao', u'PART', u'your', u'know', u'what', u'your', u'what', u'JOIN', u'love', u'more', u'than', u'ELSE', u'serg', u'well', u'most', u'love', u'JOIN', u'know', u'that', u'what', u'lmao', u'well', u'have', u'eyes', u'lmao', u'know', u'JOIN', u'girl', u'jerk', u'kids', u'guys', u'type', u'much', u'shut', u'fuck', u'girl', u'nice', u'shut', u'fuck', u'PART', u'dont', u'want', u'JOIN', u'want', u'U115', u'what', u'miss', u'much', u'work', u'nice', u'U116', u'PART', u'PART', u'heyy', u'U148', u'hate', u'boys', u'JOIN', u'U148', u'hate', u'what', u'PART', u'hate', u'U121', u'fuck', u'your', u'ugly', u'JOIN', u'bein', u'PART', u'What', u'U115', u'whys', u'that', u'deep', u'U121', u'what', u'JOIN', u'tape', u'Your', u'sexs', u'best', u'phil', u'said', u'ugly', u'PART', u'date', u'feel', u'your', u'they', u'form', u'PART', u'sits', u'JOIN', u'sits', u'with', u'hmph', u'hate', u'does', u'that', u'mean', u'want', u'room', u'this', u'been', u'PART', u'JOIN', u'U115', u'U116', u'your', u'here', u'talk', u'wait', u'that', u'perv', u'lets', u'hope', u'U121', u'PART', u'U115', u'!!!!', u'lets', u'chat', u'JOIN', u'rule', u'land', u'wont', u'then', u'find', u'need', u'this', u'HUGE', u'perv', u'that', u'deal', u'????', u'JOIN', u'shit', u'hell', u'lmao', u'PART', u'hell', u'JOIN', u'here', u'guys', u'have', u'U121', u'JOIN', u'U155', u'only', u'Poor', u'U121', u'love', u'pick', u'much', u'that', u'PART', u'PART', u'sits', u'with', u'U121', u'nads', u'JOIN', u'from', u'pick', u'your', u'pick', u'your', u'nose', u'pick', u'your', u'nose', u'JOIN', u'face', u'with', u'PART', u'U115', u'owww', u'PART', u'JOIN', u'U116', u'PART', u'does', u'want', u'talk', u'head', u'gags', u'even', u'U121', u'neck', u'Meep', u'U115', u'LAst', u'time', u'that', u'wash', u'your', u'dude', u'gets', u'JOIN', u'U121', u'dang', u'just', u"pm's", u'that', u'1.99', u'....', u'yeah', u'nice', u'neck', u'U115', u'like', u'shut', u'free', u'JOIN', u'goes', u'wash', u'lmao', u'Lies', u'lmao', u'U115', u'lick', u'very', u'lmao', u'U115', u'ummm', u'U109', u'dont', u'dead', u'more', u'than', u'call', u'just', u'case', u'dead', u'good', u'neck', u'talk', u'what', u'ummm', u'else', u'wont', u'bite', u'U115', u'yeah', u'wait', u'yeah', u'PART', u'your', u'want', u'have', u'sexy', u'bite', u'lmao', u'call', u'have', u'free', u'call', u'mins', u'JOIN', u'nite', u'lool', u'know', u'that', u'kina', u'give', u'away', u'then', u'room', u'call', u'yeah', u'U155', u'PART', u'U115', u'more', u'U115', u'guys', u'baby', u'U109', u'fuck', u'case', u'know', u'were', u'girl', u'JOIN', u'baby', u'what', u'U109', u'guys', u'chat', u'have', u'have', u'sext', u'piff', u'dont', u'talk', u'read', u'dang', u'lazy', u'dont', u'read', u'PART', u'JOIN', u'mean', u'fine', u'....', u'busy', u'work', u'okay', u'dont', u'talk', u'calm', u'down', u'busy', u'busy', u'want', u'chat', u'arms', u'kids', u'name', u'PART', u'sits', u'down', u'eats', u'JOIN', u'hugs', u'want', u'U121', u'near', u'just', u'PART', u'JOIN', u'PART', u'hell', u'yeah', u'U115', u'near', u'near', u'good', u'smax', u'JOIN', u'haha', u'only', u'>:->', u'near', u'PART', u'piff', u'VVil', u'JOIN', u'free', u'wont', u'cold', u'U121', u'cell', u'runs', u'thru', u'back', u'hair', u'eyes', u'neck', u'yeah', u'caps', u'PART', u'JOIN', u'PART', u'PART', u'U165', u'jump', u'U165', u'baby', u'here', u'over', u'your', u'good', u'PART', u'that', u'left', u'room', u'este', u'U115', u'will', u'PART', u'U121', u'U165', u'lmao', u'PART', u'PART', u'very', u'guys', u'wana', u'chat', u'chik', u'from', u'mean', u'chat', u'well', u'PART', u'that', u'dont', u'shit', u'U165', u'U165', u'left', u'room', u'with', u'your', u'JOIN', u'U115', u'what', u'list', u'wish', u'cmon', u'U128', u'nice', u'JOIN', u'list', u'PART', u'list', u'U115', u'good', u'lmao', u'U128', u'hehe', u'hows', u'bout', u'good', u'hear', u'U165', u'have', u'JOIN', u'good', u'PART', u'JOIN', u'wats', u'they', u'PART', u'piff', u'aint', u'know', u'shut', u'much', u'good', u'PART', u'JOIN', u'JOIN', u'yeah', u'lost', u'like', u'same', u'well', u'work', u'what', u'Boyz', u'rock', u'what', u'hehe', u'went', u'back', u'some', u'then', u'came', u'back', u'home', u'PART', u'what', u'they', u'coat', u'nice', u'read', u'many', u'nice', u'hehe', u'lmao', u'even', u'JOIN', u'well', u'talk', u'nite', u'what', u'very', u'time', u'What', u'kind', u'....', u'nite', u'PART', u'Eyes', u'Dawn', u'last', u'song', u'LIVE', u'cool', u'good', u'nite', u'mauh', u'nite', u'mike', u'keep', u'must', u'girl', u'seem', u'pick', u'else', u'....', u'take', u'your', u'your', u'JOIN', u'lmao', u'just', u'days', u'late', u'with', u'room', u'JOIN', u'PART', u'good', u'ques', u'lmao', u'JOIN', u'that', u'like', u'dont', u'quit', u'what', u'your', u'4.20', u'PART', u'like', u'mine', u'over', u'cali', u'good', u'this', u'year', u'NICK', u'whoa', u'have', u'have', u'have', u'what', u'boys', u'gosh', u'that', u'ruff', u'what', u'PART', u'hell', u'rock', u'roll', u'PART', u'with', u'like', u'that', u'nope', u'....', u'rest', u'rock', u'roll', u'....', u'....', u'sing', u'from', u'kids', u'....', u'mame', u'nada', u'cali', u'here', u'that', u'cool', u'kids', u'cool', u'JOIN', u'with', u'from', u'said', u'alot', u'JOIN', u'year', u'band', u'JOIN', u'NICK', u'cool', u'nice', u'here', u'hair', u'hard', u'what', u'type', u'does', u'your', u'band', u'play', u'hair', u'yeah', u'what', u'doin', u'....', u'with', u'hand', u'what', u'JOIN', u'room', u'....', u'sexy', u'PART', u'dumb', u'they', u'wont', u'chat', u'with', u'lmao', u'damn', u'what', u'orgy', u'orgy', u'lmao', u'what', u'word', u'some', u'easy', u'PART', u'JOIN', u'back', u'orgy', u'lmao', u'PART', u'lets', u'play', u'room', u'PART', u'JOIN', u'JOIN', u'were', u'damn', u'PART', u'good', u'call', u'what', u'like', u'just', u'late', u'date', u'know', u'push', u'PART', u'lose', u'name', u'shit', u'head', u'long', u'time', u'said', u'shit', u'lost', u'baby', u'then', u'JOIN', u'PART', u'JOIN', u'What', u'sure', u'JOIN', u'sure', u'lmao', u'this', u'room', u'....', u'....', u'your', u'....', u'lmao', u'that', u'yeah', u'have', u'many', u'lmao', u'sexy', u'stay', u'keep', u'lmao', u'with', u'hair', u'like', u'that', u'....', u'down', u'door', u'prob', u'....', u'hair', u'lmao', u'JOIN', u'sexy', u'just', u'this', u'life', u'just', u'PART', u'room', u'with', u'hair', u'like', u'what', u'from', u'here', u'said', u'wild', u'....', u'even', u'from', u'JOIN', u'cool', u'sexy', u'JOIN', u'sexy', u'only', u'none', u'sexy', u'whew', u'sexy', u'hell', u'have', u'shut', u'sexy', u'damn', u'sexy', u'dark', u'have', u'seen', u'have', u'just', u'JOIN', u'does', u'waht', u'else', u'next', u'JOIN', u'test', u'self', u'JOIN', u'room', u'here', u'well', u'that', u'what', u'pass', u'once', u'that', u'been', u'JOIN', u'PART', u'over', u'over', u'book', u'word', u'PART', u'must', u'PART', u'JOIN', u'just', u'home', u'from', u'work', u'Well', u'keep', u'time', u'here', u'PART', u'over', u'....', u'know', u'PART', u'JOIN', u'PART', u'that', u'lmao', u'they', u'cant', u'come', u'with', u'line', u'then', u'they', u'stay', u'away', u'from', u'lmao', u'ummm', u'yeah', u'dang', u'even', u'that', u'PART', u'some', u'with', u'male', u'chat', u'boot', u'JOIN', u'book', u'....', u'away', u'from', u'....', u'stop', u'that', u'JOIN', u'slap', u'hiom', u'back', u'....', u'PART', u'used', u'live', u'next', u'door', u'PART', u'PART', u'live', u'HAHA', u'cute', u'....', u'that', u'lmao', u'dman', u'damn', u'even', u'PART', u'just', u'PART', u'that', u'PART', u'....', u'holy', u'crap', u'that', u'took', u'What', u'hate', u'what', u'took', u'crap', u'ever', u'left', u'JOIN', u'Well', u'days', u'....', u'When', u'even', u'know', u'what', u'that', u'....', u'talk', u'babe', u'park', u'lmao', u'them', u'jail', u'even', u'been', u'lmao', u'soon', u'tell', u'cops', u'guys', u'PART', u'been', u'once', u'stop', u'then', u'hate', u'yeah', u'JOIN', u'Sure', u'hate', u'want', u'lmao', u'good', u'look', u'much', u'JOIN', u'love', u'very', u'much', u'....', u'over', u'PART', u'Come', u'down', u'hogs', u'over', u'peek', u'girl', u'help', u'know', u'MORE', u'TIME', u'this', u'just', u'that', u'look', u'like', u'here', u'what', u'care', u'JOIN', u'JOIN', u'play', u'....', u'this', u'room', u'real', u'LMAO', u'from', u'soul', u'like', u'have', u'done', u'time', u'then', u'that', u'that', u'like', u'O.k.', u'what', u'fine', u'JOIN', u'make', u'here', u'Well', u'PART', u'luck', u'here', u'....', u'need', u'help', u'....', u'PART', u'much', u'else', u'want', u'back', u'baby', u'hows', u'that', u'loud', u'keep', u'PART', u'....', u'o.k.', u'once', u'PART', u'....', u'what', u'hell', u'yeah', u'JOIN', u'JOIN', u'hair', u'PART', u'over', u'hair', u'Sexy', u'lets', u'will', u'....', u'does', u'hair', u'then', u'lmao', u'good', u'take', u'like', u'look', u'....', u'ride', u'PART', u'JOIN', u'have', u'such', u'room', u'luck', u'sure', u'make', u'PART', u'Ctrl', u'PART', u'give', u'Well', u'O.k.', u'take', u'your', u'word', u'that', u'mama', u'Nice', u'nope', u'nope', u'nope', u'that', u'hots', u'with', u'your', u'hook', u'with', u'them', u'word', u'know', u'well', u'have', u'work', u'LMAO', u'have', u'hugs', u'awww', u'have', u'good', u'have', u'work', u'here', u'have', u'good', u'nite', u'nite', u'nite', u'Need', u'what', u'hold', u'PART', u'lady', u'with', u'hair', u'frst', u'like', u'Only', u'been', u'time', u'live', u'hook', u'your', u'like', u'shut', u'wish', u'here', u'such', u'tell', u'1200', u'best', u'love', u'....', u'soft', u'....', u'this', u'room', u'....', u'like', u'them', u'ohio', u'Like', u'whip', u'crop', u'know', u'each', u'....', u'love', u'like', u'bomb', u'baby', u'come', u'Pour', u'some', u'babe', u'JOIN', u'hiya', u'bend', u'want', u'room', u'also', u'hiya', u'book', u'....', u'read', u'....', u'same', u'with', u'pour', u'some', u'when', u'need', u'JOIN', u'this', u'comp', u'sure', u'some', u'have', u'room', u'free', u'your', u'mind', u'with', u'nice', u'free', u'your', u'free', u'gets', u'some', u'free', u'your', u'they', u'free', u'well', u'like', u'long', u'Swim', u'Hard', u'read', u'book', u'open', u'PART', u'some', u'just', u'some', u'book', u'full', u'wear', u'work', u'JOIN', u'have', u'much', u'need', u'JOIN', u'will', u'your', u'book', u'just', u'that', u'make', u'PART', u'that', u'back', u'toss', u'hiya', u'....', u'they', u'just', u'tell', u'that', u'left', u'high', u'ouch', u'....', u'they', u'wear', u'work', u'PART', u'away', u'JOIN', u'well', u'find', u'yeah', u'toss', u'....', u'PART', u'back', u'with', u'many', u'evil', u'twin', u'left', u'eeek', u'JOIN', u'JOIN', u'what', u'????', u'some', u'just', u'thru', u'said', u'look', u'nice', u'room', u'tjhe', u'burp', u'that', u'JOIN', u'Well', u'....', u'like', u'....', u'fart', u'JOIN', u'true', u'just', u'!!!!', u'room', u'that', u'here', u'!!!!', u'PART', u'JOIN', u'PART', u'mean', u'!!!!', u'room', u'10th', u'heee', u'good', u'dont', u'from', u'PART', u'your', u'have', u'peel', u'soon', u'land', u'PART', u'fock', u'JOIN', u'here', u'kool', u'just', u'back', u'from', u'hiya', u'come', u'kiss', u'what', u'kool', u'with', u'cold', u'????', u'....', u'were', u'doin', u'Kold', u'soon', u'JOIN', u'exit', u'land', u'....', u'cool', u'kool', u'that', u'kold', u'....', u'well', u'....', u'they', u'this', u'3:45', u'MRIs', u'what', u'what', u'your', u'with', u'nice', u'JOIN', u'good', u'PART', u'amen', u'PART', u'....', u'buff', u'what', u'like', u'well', u'from', u'PART', u'were', u'love', u'plus', u'....', u'them', u'when', u'....', u'they', u'were', u'JOIN', u'know', u'also', u'here', u'this', u'tory', u'What', u'blew', u'knee', u'left', u'that', u'heya', u'what', u'JOIN', u'damn', u'comp', u'fall', u'ever', u'date', u'ouch', u'name', u'kids', u'were', u'OOPS', u'none', u'with', u'PART', u'that', u'much', u'gets', u'JOIN', u'this', u'oooh', u'lala', u'some', u'very', u'hugs', u'they', u'need', u'fake', u'into', u'with', u'like', u'mind', u'eyes', u'none', u'like', u'JOIN', u'eyes', u'back', u'have', u'eyes', u'roll', u'know', u'ever', u'come', u'with', u'hugs', u'with', u'JOIN', u'cool', u'from', u'wait', u'ssid', u'none', u'JOIN', u'PART', u'PART', u'your', u'yeah', u'that', u'some', u'such', u'need', u'evil', u'twin', u'room', u'PART', u'this', u'yeah', u'nice', u'from', u'here', u'this', u'JOIN', u'need', u'have', u'some', u'temp', u'work', u'nice', u'JOIN', u'PART', u'blue', u'PART', u'room', u'JOIN', u'corn', u'poot', u'poop', u'line', u'bird', u'JOIN', u'corn', u'well', u'PART', u'PART', u'hope', u'lets', u'Hiya', u'have', u'been', u'rain', u'plow', u'....', u'....', u'here', u'have', u'with', u'take', u'main', u'room', u'your', u'they', u'....', u'MODE', u'fine', u'here', u'JOIN', u'JOIN', u'this', u'Yeah', u'fall', u'good', u'back', u'PART', u'pick', u'JOIN', u'from', u'pool', u'nice', u'JOIN', u'JOIN', u'nice', u'PART', u'JOIN', u'hiya', u'just', u'hiya', u'sexy', u'hiya', u'hiya', u'JOIN', u'hiya', u'deop', u'MODE', u'JOIN', u'hugs', u'hiya', u'hiya', u'hiya', u'hiya', u'must', u'time', u'hiya', u'love', u'PART', u'hows', u'just', u'left', u'hiya', u'full', u'here', u'fine', u'here', u'have', u'work', u'fine', u'thnx', u'JOIN', u'good', u'hiya', u'just', u'roof', u'roof', u'roof', u'fire', u'that', u'doin', u'PART', u'PART', u'good', u'hear', u'that', u'....', u'your', u'hear', u'that', u'just', u'card', u'hear', u'that', u'....', u'hugs', u'have', u'been', u'here', u'JOIN', u'Hugs', u'lost', u'((((', u'))))', u'PART', u'Lord', u'uyes', u'give', u'damn', u'benz', u'just', u'well', u'week', u'lost', u'sure', u'feel', u'just', u'cash', u'PART', u'PART', u'does', u'PART', u'hear', u'sing', u'away', u'JOIN', u'PART', u'....', u'said', u'....', u'come', u'with', u'Hiya', u'wait', u'were', u'call', u'Hiya', u'that', u'into', u'good', u'nice', u'here', u'JOIN', u'<~~~', u'will', u'play', u'nice', u'grrr', u'pics', u'from', u'Hiya', u'miss', u'ears', u'wait', u'they', u'have', u'that', u'nice', u'disc', u'LONG', u'does', u'this', u'take', u'Been', u'over', u'hour', u'nice', u'real', u'life', u'play', u'nice', u'....', u'long', u'time', u'many', u'that', u'come', u'From', u'long', u'time', u'know', u'with', u'long', u'been', u'last', u'PART', u'been', u'Will', u'this', u'well', u'know', u'porn', u'well', u'yeah', u'like', u'that', u'know', u'good', u'luck', u'back', u'will', u'work', u'have', u'PART', u'CHAT', u'just', u'hiya', u'JOIN', u'just', u'call', u'heya', u'yeah', u'told', u'last', u'have', u'week', u'hows', u'your', u'goin', u'back', u'....', u'boss', u'from', u'well', u'time', u'last', u'call', u'dont', u'work', u'heal', u'girl', u'away', u'will', u'hour', u'talk', u'like', u'were', u'pain', u'your', u'quit', u'work', u'JOIN', u'JOIN', u'....', u'down', u'time', u'PART', u'main', u'room', u'find', u'your', u'game', u'such', u'like', u'what', u'bloe', u'????', u'PART', u'blow', u'here', u'hooo', u'Dang', u'PART', u'know', u'....', u'hiya', u'babe', u'this', u'game', u'ciao', u'they', u'cant', u'read', u'PART', u'here', u'many', u'DOES', u'take', u'????', u'U520', u'lick', u'kick', u'good', u'PART', u'thje', u'same', u'yeah', u'U520', u'hell', u'good', u'know', u'U520', u'good', u'U520', u'U520', u'were', u'last', u'ever', u'come', u'back', u'Jess', u'came', u'back', u'Yeah', u'back', u'hear', u'nick', u'like', u'that', u'PART', u'U520', u'JOIN', u'JOIN', u'yeah', u'typo', u'ummm', u'yeah', u'typo', u'NICK', u'what', u'ride', u'JOIN', u'with', u'when', u'came', u'name', u'like', u'even', u'glad', u'back', u'like', u'lmao', u'like', u'ahhh', u'know', u'yeah', u'have', u'JOIN', u'JOIN', u'said', u'used', u'with', u'like', u'look', u'pink', u'JOIN', u'lmao', u'pink', u'took', u'long', u'time', u'JOIN', u'PART', u'JOIN', u'come', u'back', u'just', u'with', u'long', u'term', u'with', u'this', u'girl', u'over', u'last', u'they', u'beer', u'PART', u'JOIN', u'hiya', u'JOIN', u'PART', u'JOIN', u'lmao', u'Stop', u'room', u'amen', u'PART', u'JOIN', u'JOIN', u'PART', u'what', u'JOIN', u'PART', u'well', u'then', u'Tina', u'here', u'....', u'want', u'left', u'love', u'your', u'cool', u'here', u'with', u'pink', u'nice', u'....', u'soft', u'long', u'time', u'type', u'....', u'lmao', u'down', u'stop', u'with', u'room', u'cool', u'away', u'lmao', u'ooer', u'damn', u'....', u'that', u'cool', u'hate', u'babe', u'they', u'seem', u'long', u'ahem', u'much', u'last', u'HALO', u'hows', u'Awww', u'dear', u'!!!!', u'hola', u'cool', u'What', u'doin', u'Dang', u'well', u'tell', u'stop', u'anal', u'PART', u'good', u'....', u'busy', u'very', u'busy', u'good', u'good', u'dear', u'love', u'that', u'call', u'good', u'eric', u'back', u'Drop', u'caps', u'what', u'dont', u'take', u'over', u'cool', u'yeah', u'well', u'hope', u'dojn', u'fine', u'babe', u'rock', u'long', u'know', u'same', u'busy', u'busy', u'then', u'wubs', u'mkay', u'this', u'fast', u'just', u'babe', u'just', u'your', u'butt', u'here', u'then', u'word', u'from', u'your', u'what', u'need', u'like', u'take', u'ride', u'JOIN', u'last', u'spat', u'said', u'that', u'what', u'call', u'your', u'soon', u'poor', u'will', u'gone', u'same', u'have', u'real', u'once', u'hehe', u'babe', u'imma', u'make', u'gees', u'JOIN', u'know', u'Drew', u'hawT', u'many', u'hate', u'hate', u'Drew', u'have', u'only', u'long', u'town', u'that', u'PART', u'even', u'JOIN', u'JOIN', u'damn', u'even', u'have', u'hola', u'hugs', u'hiya', u'sore', u'with', u'back', u'cold', u'runs', u'cold', u'yes.', u'that', u'with', u'like', u'puts', u'book', u'from', u'fish', u'JOIN', u'when', u'tell', u'Well', u'know', u'size', u'with', u'hawt', u'LMAO', u'hugs', u'from', u'goes', u'look', u'haha', u'Live', u'39.3', u'2006', u'Elev', u'Wind', u'back', u'High', u'1980', u'back', u'goes', u'look', u'your', u'that', u'Live', u'64.8', u'want', u'says', u'That', u'AKDT', u'2006', u'Elev', u'Wind', u'nice', u'AKDT', u'AKDT', u'pfft', u'PART', u'sigh', u'PART', u'from', u'dang', u'cold', u'syck', u'JOIN', u'tere', u'said', u'talk', u'here', u'suck', u'even', u'good', u'here', u'ohhh', u'U542', u'sent', u'PART', u'only', u'talk', u'know', u'like', u'goes', u'look', u'45.5', u'98.5', u'2006', u'Elev', u'1299', u'hits', u'Wind', u'chat', u'1900', u'shit', u'High', u'1930', u'JOIN', u'know', u'list', u'that', u'only', u'talk', u'KoOL', u'LMAO', u'tell', u'Werd', u'PART', u'Rofl', u'hiya', u'....', u'lmao', u'yeah', u'well', u'then', u'wont', u'talk', u'only', u'kool', u'such', u'have', u'have', u'lead', u'mode', u'want', u'does', u'that', u'make', u'chat', u'make', u'feel', u'days', u'PART', u'nawt', u'your', u'lmao', u'dang', u'come', u'back', u'that', u'feel', u'yeah', u'awww', u'what', u'your', u'know', u'past', u'life', u'DING', u'DING', u'DING', u'imma', u'want', u'make', u'love', u'JOIN', u'then', u'your', u'okay', u'same', u'then', u'talk', u'love', u'baby', u'cant', u'Love', u'JOIN', u'good', u'####', u'yeah', u'MODE', u'What', u'your', u'sign', u'woof', u'many', u'were', u'same', u'JOIN', u'they', u'just', u'nose', u'cold', u'love', u'when', u'take', u'ever', u'were', u'even', u'gets', u'damn', u'sum1', u'ghet', u'yeah', u'keep', u'here', u'chat', u'even', u'brad', u'PART', u'keep', u'jerk', u'this', u'PART', u'PART', u'here', u'note', u'your', u'just', u'lmao', u'like', u'meat', u'offa', u'hard', u'like', u'some', u'guys', u'pass', u'does', u'help', u'that', u'that', u'what', u'most', u'roll', u'tell', u'were', u'same', u'room', u'rule', u'most', u'JOIN', u'well', u'....', u'make', u'jump', u'jump', u'PART', u'shes', u'Dood', u'face', u'then', u'tell', u'JOIN', u'just', u'out.', u'want', u'tell', u'like', u'know', u'tell', u'feel', u'chat', u'dont', u'like', u'play', u'with', u'your', u'meat', u'....', u'!!!.', u'late', u'lmao', u'your', u'done', u'with', u'call', u'more', u'dont', u'like', u'that', u'lmao', u'LOUD', u'need', u'even', u'JOIN', u'sink', u'from', u'here', u'hiya', u'PART', u'dang', u'some', u'know', u'look', u'make', u'that', u'wall', u'PART', u'ohhh', u'imma', u'look', u'just', u'bend', u'over', u'will', u'lmao', u'your', u'poor', u'wall', u'JOIN', u'JOIN', u'JOIN', u'just', u'yeah', u'butt', u'your', u'FINE', u'they', u'they', u'PART', u'argh', u'fart', u'away', u'oops', u'lmao', u'JOIN', u'gawd', u'head', u'just', u'keep', u'hiya', u'they', u'they', u'sure', u'hell', u'PART', u'haha', u'JOIN', u'PART', u'pfft', u'care', u'they', u'lead', u'yeah', u'away', u'song', u'seen', u'just', u'dead', u'cums', u'LMAO', u'PART', u'PART', u'good', u'whoa', u'that', u'some', u'loss', u'....', u'sits', u'need', u'that', u'with', u'limp', u'rent', u'over', u'limp', u'Have', u'seen', u'good', u'been', u'cant', u'wait', u'cars', u'come', u'NICK', u'cars', u'Yeah', u'that', u'nick', u'love', u'NICK', u'just', u'love', u'JOIN', u'lmao', u'Life', u'hiya', u'love', u'JOIN', u'hiya', u'PART', u'chat', u'NICK', u'PART', u'lady', u'NICK', u'like', u'that', u'Damn', u'wrap', u'give', u'them', u'NICK', u'need', u'PART', u'PART', u'PART', u'left', u'real', u'fast', u'JOIN', u'JOIN', u'NICK', u'good', u'JOIN', u'NICK', u'were', u'NICK', u'PART', u'cant', u'have', u'good', u'hear', u'your', u'name', u'PART', u'were', u'Tell', u'this', u'time', u'hide', u'were', u"PM's", u'just', u'JOIN', u'PART', u'kids', u'once', u'went', u'into', u'Talk', u'tell', u'true', u'what', u'want', u'over', u'okey', u'back', u'worl', u'PART', u'JOIN', u'have', u'good', u'were', u'full', u'half', u'lets', u'next', u'shop', u'your', u'your', u'love', u'cmon', u'make', u'like', u'your', u'JOIN', u'JOIN', u'PART', u'JOIN', u'hiya', u'back', u'need', u'heal', u'soul', u'Hold', u'PART', u'come', u'PART', u'hiya', u'room', u'Hiya', u'hiya', u'hugs', u'JOIN', u'gone', u'PART', u'cant', u'help', u'lmao', u'good', u'dont', u'that', u'PART', u'hugs', u'))))', u'tell', u'good', u'says', u'some', u'pics', u'sure', u'aint', u'such', u'good', u'JOIN', u'lmao', u'well', u'....', u'cepn', u'well', u'with', u'that', u'your', u'good', u'well', u'lmao', u'ouch', u'lots', u'dear', u'JOIN', u'haha', u'have', u'seen', u'Mary', u'hiya', u'PART', u'JOIN', u'mary', u'hiya', u'hiya', u'that', u'U172', u'hiya', u'JOIN', u'nawp', u'aint', u'seen', u'oops', u'only', u'mary', u'lmao', u'more', u'like', u'PART', u'addy', u'pics', u'hiya', u'will', u'long', u'lake', u'have', u'come', u'with', u'been', u'bout', u'JOIN', u'know', u'what', u'mean', u'JOIN', u'must', u'back', u'room', u'here', u'room', u'ROOM', u'sigh', u'sigh', u'JOIN', u'lmao', u'good', u'!!!!', u'tell', u'said', u'that', u'ello', u'back', u'room', u'hugs', u'that', u'good', u'were', u'heyy', u'hiya', u'find', u'back', u'room', u'lmao', u'room', u'here', u'hugs', u'tell', u'slip', u'mind', u'fall', u'open', u'your', u'eyes', u'PART', u'lmao', u'....', u'lead', u'mite', u'lmao', u'busy', u'busy', u'busy', u',,,,', u'JOIN', u'ello', u'hiya', u'what', u'hear', u'back', u'JOIN', u'lmao', u'meet', u'hope', u'name', u'lost', u'last', u'wood', u'lmao', u'like', u'knew', u'with', u'good', u'lord', u'long', u'have', u'said', u'this', u'stay', u'away', u'till', u'this', u'over', u'even', u'just', u'call', u'lmao', u'lmao', u'....', u'tell', u'they', u'lose', u'that', u'PART', u'<---', u'even', u'they', u'hell', u'aint', u'####', u'make', u'have', u'pick', u'five', u'....', u'that', u'just', u'lmao', u'dont', u'them', u'orta', u'good', u'like', u'JOIN', u'will', u'wins', u'hiya', u'some', u'sell', u'your', u'soul', u'will', u'ebay', u'nice', u'coem', u'like', u'come', u'haha', u'damn', u'what', u'gets', u'well', u'they', u'were', u'only', u'only', u'near', u'....', u'goes', u'find', u'....', u'giva', u'1.98', u'JOIN', u'here', u'JOIN', u'year', u'....', u'life', u'this', u'last', u'year', u'best', u'hiya', u'hiya', u'pick', u'rule', u'does', u'that', u'make', u'PART', u'good', u'rule', u'JOIN', u'here', u'!!!!', u'what', u'goes', u'....', u'PART', u'))))', u'ball', u'<<<<', u'hick', u'city', u'hick', u'PART', u'good', u'then', u'like', u'gets', u'hick', u'back', u'from', u'ally', u'with', u'wine', u'with', u'JOIN', u'know', u'when', u'....', u'JOIN', u'PART', u'find', u'yard', u'when', u'JOIN', u'MODE', u'hiii', u'know', u'true', u'just', u'that', u'here', u'sure', u'Judy', u'deop', u'ever', u'MODE', u'JOIN', u'lmao', u'hiya', u'stay', u'came', u'dang', u'yall', u'quit', u'much', u'perv', u'here', u'call', u'PART', u'that', u'they', u'have', u'good', u'PART', u'cyas', u'yall', u'PART', u'JOIN', u'took', u'care', u'dont', u'much', u'that', u'they', u'ever', u'seen', u'know', u'were', u'will', u'grrl', u'PART', u'lmao', u'heya', u'they', u'lost', u'....', u'perv', u'when', u'name', u'shup', u'keep', u'perv', u'heya', u'fall', u'JOIN', u'PART', u'JOIN', u'mean', u'perv', u'main', u'room', u'cant', u'read', u'tooo', u'heya', u'back', u'look', u'what', u'lmao', u'>:->', u'hear', u'hiya', u'hiya', u'JOIN', u'will', u'take', u'over', u'room', u"pm'n", u'hear', u'heya', u'lmao', u'home', u'sick', u'want', u'choc', u'chip', u'chip', u'PART', u'sure', u'your', u'crap', u'bear', u'bare', u'case', u'mmmm', u'here', u'PART', u'they', u'wher', u'been', u'bare', u'aint', u'that', u'made', u'ones', u'good', u'lord', u'some', u'awww', u'dont', u'PART', u'from', u'room', u'here', u'JOIN', u'nope', u'this', u'time', u'foot', u'hold', u'PART', u'PART', u'been', u'life', u'last', u'hour', u'whoo', u'dint', u'send', u'that', u'need', u'hiya', u'hour', u'said', u'time', u'damn', u'well', u'like', u'lmao', u'PART', u'nice', u'hour', u'lmao', u'time', u'well', u'just', u'make', u'PART', u'that', u'have', u'lmao', u'with', u'that', u'yeah', u'that', u'till', u'have', u'comp', u'over', u'stop', u'kids', u'with', u'that', u'good', u'time', u'lost', u'PART', u'that', u'PART', u'full', u'perv', u'JOIN', u'tend', u'lost', u'lost', u'vote', u'full', u'need', u'hiya', u'full', u'then', u'PART', u'sits', u'down', u'perv', u'here', u'JOIN', u'with', u'hiya', u'hiii', u'PART', u'then', u'here', u'much', u'legs', u'ever', u'uses', u'help', u'with', u'DONT', u'they', u'will', u'next', u'legs', u'menu', u'tell', u'time', u'PART', u'will', u'send', u'JOIN', u'what', u'time', u'this', u'room', u'that', u'work', u'your', u'....', u'hand', u'lust', u'hiya', u'hugs', u'nods', u'have', u'with', u'JOIN', u'JOIN', u'JOIN', u'PART', u'JOIN', u'JOIN', u'here', u'just', u'they', u'live', u'wont', u'stop', u'when', u'PART', u'JOIN', u'PART', u'PART', u'JOIN', u'Liam', u'This', u'what', u'; ..', u'this', u'song', u'been', u'.. .', u'this', u'song', u'JOIN', u'PART', u'JOIN', u'room', u'JOIN', u'well', u'PART', u'JOIN', u'cool', u'NAME', u'PART', u'PART', u'have', u'them', u'this', u'kept', u'male', u'know', u'that', u'alot', u'like', u'that', u'PART', u'JOIN', u'name', u'bout', u'once', u'name', u'chat', u'with', u'JOIN', u'PART', u'JOIN', u'PART', u'JOIN', u'PART', u'PART', u'PART', u'once', u'more', u'Your', u'name', u'male', u'name', u'JOIN', u'like', u'JOIN', u'PART', u'JOIN', u'what', u'like', u'PART', u'Liam', u'This', u'what', u'Come', u'this', u'song', u'been', u'.. .', u'this', u'song', u'this', u'room', u'sits', u'hits', u'love', u'JOIN', u'PART', u'mine', u'good', u'even', u'PART', u'Same', u'here', u'PART', u'dont', u'feel', u'cant', u'left', u'feet', u'what', u'into', u'PART', u'PART', u'rock', u'good', u'here', u'seen', u'away', u'free', u'xbox', u'with', u'PART', u'scuk', u'raed', u'them', u'JOIN', u'xbox', u'Song', u'JOIN', u'JOIN', u'dont', u'like', u'xbox', u'huge', u'make', u'hand', u'PART', u'dont', u'need', u'xbox', u'they', u'chat', u'PART', u'PART', u'PART', u'JOIN', u'JOIN', u'JOIN', u'MODE', u'Then', u'what', u'like', u'have', u'true', u'JOIN', u'yall', u'wack', u'JOIN', u'JOIN', u'like', u'play', u'Liam', u'This', u'what', u'; ..', u'Like', u'this', u'song', u'been', u'.. .', u'this', u'song', u'love', u'rule', u'woot', u'JOIN', u'JOIN', u'some', u'good', u'JOIN', u'very', u'true', u'PART', u'Have', u'guys', u'PART', u'what', u'have', u'yeah', u'dont', u'know', u'much', u'bugs', u'work', u'your', u'blah', u'blah', u'blah', u'just', u'made', u'JOIN', u'true', u'like', u'just', u'your', u'sort', u'like', u'PART', u'that', u'what', u'game', u'have', u'idea', u'what', u'JOIN', u'PART', u'haha', u'JOIN', u'even', u'know', u'what', u'your', u'that', u'dude', u'just', u'that', u'said', u'that', u'nice', u'PART', u'PART', u'guys', u'free', u'JOIN', u'even', u'work', u'PART', u'PART', u'just', u'days', u'rent', u'many', u'want', u'free', u'like', u'that', u'shes', u'same', u'huge', u'game', u'nerd', u'know', u'talk', u'make', u'play', u'PART', u'used', u'JOIN', u'gets', u'them', u'like', u'have', u'hard', u'time', u'good', u'like', u'girl', u'game', u'JOIN', u'love', u'play', u'JOIN', u'hate', u'girl', u'like', u'Hill', u'Evil', u'well', u'best', u'like', u'like', u'good', u'play', u'full', u'game', u'JOIN', u'PART', u'JOIN', u'Yeah', u'girl', u'play', u'love', u'PART', u'nice', u'JOIN', u'PART', u'saME', u'Nice', u'what', u'JOIN', u'2Pac', u'Time', u'good', u'U110', u'with', u'must', u'game', u'then', u'nice', u'your', u'girl', u'PART', u'JOIN', u'PART', u'pimp', u'U108', u'JOIN', u'hope', u'girl', u'have', u'been', u'like', u'that', u'park', u'PART', u'PART', u'that', u'suck', u'free', u'just', u'Liam', u'This', u'what', u'; ..', u'this', u'song', u'been', u'.. .', u'this', u'song', u'Lies', u'JOIN', u'JOIN', u'shot', u'lies', u'hear', u'lies', u'snow', u'huge', u'JOIN', u'what', u'does', u'know', u'hurt', u'What', u'PART', u'haaa', u'mind', u'Stop', u'sick', u'girl', u'sick', u'girl', u'JOIN', u'JOIN', u'what', u'have', u'temp', u'JOIN', u'U119', u'JOIN', u'JOIN', u'wish', u'then', u'have', u'work', u'good', u'98.6', u'PART', u'JOIN', u'JOIN', u"it's", u'JOIN', u'Mono', u'from', u'Liam', u'This', u'what', u'; ..', u'this', u'song', u'been', u'.. .', u'this', u'song', u'well', u'have', u'that', u'nice', u'PART', u'mono', u'what', u'heck', u'that', u'best', u'luck', u'JOIN', u'made', u'with', u'team', u'PART', u'much', u'U119', u'PART', u'JOIN', u'whud', u'room', u'ahhh', u'PART', u'PART', u'team', u'PART', u'PART', u'whud', u'room', u'JOIN', u'MODE', u'were', u'JOIN', u'PART', u'Bone', u'Days', u'JOIN', u'PART', u'JOIN', u'U122', u'U122', u'U122', u'MODE', u'U122', u'PART', u'JOIN', u'JOIN', u'JOIN', u'JOIN', u'JOIN', u'U122', u'U122', u'U122', u'MODE', u'U122', u'U122', u'U122', u'MODE', u'PART', u'JOIN', u'MODE', u'PART', u'back', u'PART', u'JOIN', u'MODE', u'PART', u'PART', u'opps', u'JOIN', u'MODE', u'PART', u'PART', u'JOIN', u'MODE', u'from', u'made', u'with', u'team', u'that', u'team', u'JOIN', u'PART', u'JOIN', u'MODE', u'PART', u'JOIN', u'MODE', u'room', u'that', u'PART', u'U122', u'U122', u'U122', u'MODE', u'U122', u'U122', u'U122', u'MODE', u'JOIN', u'MODE', u'U122', u'hiya', u'PART', u'PART', u'JOIN', u'MODE', u'JOIN', u'JOIN', u'U122', u'U122', u'U122', u'MODE', u'U122', u'U122', u'U122', u'MODE', u'knew', u'PART', u'U122', u'U122', u'U122', u'MODE', u'U122', u'U122', u'U122', u'MODE', u'PART', u'JOIN', u'JOIN', u'MODE', u'JOIN', u'PART', u'JOIN', u'Liam', u'This', u'what', u'; ..', u'Hero', u'They', u'Came', u'this', u'song', u'been', u'.. .', u'this', u'song', u'.op.', u'dont', u'talk', u'PART', u'PART', u'have', u'away', u'from', u'lost', u'What', u'hell', u'U122', u'here', u'That', u'alot', u'MODE', u'PART', u'alot', u'PART', u'PART', u'U122', u'JOIN', u'U119', u'U122', u'sick', u'here', u'hott', u'PART', u'PART', u'cool', u'PART', u'PART', u'hiya', u'PART', u'that', u'have', u'Hott', u'mean', u'ugly', u'JOIN', u'MODE', u'PART', u'PART', u'JOIN', u'MODE', u'PART', u'with', u'They', u'PART', u'JOIN', u'JOIN', u'PART', u'Same', u'here', u'PART', u'JOIN', u'come', u'left', u'PART', u'PART', u'Liam', u'This', u'what', u'; ..', u'Down', u'Joey', u'this', u'song', u'been', u'.. .', u'this', u'song', u'PART', u'PART', u'JOIN', u'Jane', u'JOIN', u'JOIN', u'PART', u'span', u'long', u'JOIN', u'feel', u'your', u'pain', u'JOIN', u'JOIN', u'JOIN', u'your', u'just', u'.. .', u'want', u'some', u'They', u'have', u'chat', u'just', u'like', u'what', u'evil', u'JOIN', u'PART', u'PART', u'PART', u'yeah', u'that', u'will', u'just', u'PART', u'PART', u'PART', u'JOIN', u'they', u'want', u'stay', u'this', u'room', u'PART', u'true', u'JOIN', u'chat', u'with', u'girl', u'PART', u'PART', u'like', u'chat', u'PART', u'PART', u'sort', u'JOIN', u'seen', u'much', u'JOIN', u'PART', u'JOIN', u'used', u'work', u'JOIN', u'talk', u'sore', u'room', u'JOIN', u'PART', u'PART', u'PART', u'PART', u'PART', u'JOIN', u'woot', u'back', u'boss', u'wore', u'time', u'Liam', u'This', u'what', u'; ..', u'this', u'song', u'been', u'.. .', u'this', u'song', u'JOIN', u'PART', u'JOIN', u'JOIN', u'JOIN', u'note', u'QUIT', u'pasa', u'Same', u'here', u'your', u'boss', u'barn', u'JOIN', u'boss', u'play', u'joke', u'dont', u'know', u'what', u'JOIN', u'Kick', u'that', u'feat', u'Back', u'chat', u'kick', u'PART', u'feel', u'like', u'even', u'more', u'Lets', u'PART', u'JOIN', u'best', u'ever', u'have', u'baby', u'give', u'good', u'PART', u'need', u'here', u'ahem', u'what', u'dork', u'heyy', u'girl', u'guys', u'JOIN', u'give', u'good', u'when', u'type', u'just', u'wait', u'home', u'Liam', u'This', u'what', u'; ..', u'When', u'this', u'song', u'been', u'.. .', u'this', u'song', u'JOIN', u'dont', u'cant', u'PART', u'JOIN', u'JOIN', u'JOIN', u'chat', u'JOIN', u'PART', u'only', u'with', u'with', u'home', u'best', u'PART', u'rule', u'like', u'chat', u'that', u'like', u'laid', u'that', u'U122', u'back', u'with', u'that', u'have', u'club', u'well', u'that', u'JOIN', u'U122', u'JOIN', u'lost', u'mine', u'JOIN', u'PART', u'Home', u'JOIN', u'PART', u'that', u'ways', u'have', u'herd', u'have', u'with', u'part', u'PART', u'JOIN', u'PART', u'just', u'Born', u'PART', u'PART', u'guys', u'here', u'Liam', u'This', u'what', u'; ..', u'Away', u'Tide', u'this', u'song', u'been', u'.. .', u'this', u'song', u'hate', u'adds', u'they', u'keep', u'room', u'JOIN', u'PART', u'guys', u'wana', u'chat', u'take', u'away', u'last', u'hope', u'here', u'jush', u'Cute', u'GrlZ', u'just', u'does', u'mean', u'have', u'soul', u'told', u'sure', u'bout', u'that', u'JOIN', u'hear', u'perv', u'tell', u'here', u'chat', u'with', u'PART', u'haha', u'JOIN', u'PART', u'PART', u'PART', u'JOIN', u'have', u'lung', u'JOIN', u'SOME', u'U156', u'PART', u'dont', u'mind', u'call', u'U156', u'good', u'main', u'room', u'find', u'blah', u'your', u'game', u'your', u'chat', u'room', u'chat', u'PART', u'JOIN', u'JOIN', u'JOIN', u'Here', u'Poor', u'girl', u'JOIN', u'Lion', u'When', u'Here', u'JOIN', u'hawt', u'lets', u'make', u'with', u'with', u'brat', u'PART', u'JOIN', u'hell', u'yeah', u'away', u'from', u'just', u'have', u'back', u'each', u'want', u'chat', u'move', u'come', u'Down', u'only', u'road', u'born', u'walk', u'PART', u'girl', u'JOIN', u'PART', u'from', u'PART', u'guys', u'cute', u'here', u'from', u'home', u':o *', u'PART', u'face', u'JOIN', u'what', u'....', u'from', u'lose', u'when', u'pfft', u'JOIN', u'PART', u'PART', u'JOIN', u'JOIN', u'MODE', u'MODE', u'land', u'sits', u'PART', u'JOIN', u'haha', u'JOIN', u'PART', u'MUAH', u'heya', u'JOIN', u'heya', u'oops', u'JOIN', u'PART', u'JOIN', u'JOIN', u'PART', u'nice', u'what', u'miss', u'what', u'fawk', u'goin', u'much', u'PART', u'much', u'dust', u'time', u'chat', u'kick', u'back', u'fool', u'Help', u'PART', u'JOIN', u'felt', u'like', u'seth', u'glad', u'that', u'have', u'good', u'PART', u'ever', u'gets', u'dont', u'PART', u'JOIN', u'haha', u'haha', u'PART', u'JOIN', u'lmao', u'many', u'U105', u'Heya', u'U105', u'U105', u'JOIN', u'U105', u'JOIN', u'U105', u'does', u'your', u'hang', u'here', u'U105', u'last', u'time', u'JOIN', u'over', u'back', u'U107', u'U107', u'that', u'wOOt', u'wOOt', u'chat', u'then', u'bone', u'come', u'fine', u'wait', u'....', u'lose', u'PART', u'U105', u'....', u'JOIN', u'PART', u'Like', u'U107', u'over', u'does', u'wack', u'what', u'that', u'abou', u'tthe', u'rest', u'over', u'head', u'U105', u'nope', u'JOIN', u'your', u'easy', u'beat', u'true', u'true', u'PART', u'yawn', u'lost', u'hawt', u'PART', u'JOIN', u'comp', u'damn', u'PART', u'JOIN', u'PART', u'U105', u'PART', u'that', u'area', u'just', u'here', u'PART', u'JOIN', u'JOIN', u'here', u'PART', u'?!?!', u'from', u'from', u'here', u'PART', u'here', u'U103', u'JOIN', u'U105', u'well', u'U105', u'well', u'said', u'Even', u'that', u'lost', u'here', u'Ohio', u'here', u'?!?!', u'says', u'that', u'U105', u'tell', u'ohio', u'easy', u'beat', u'just', u'have', u'hook', u'U107', u'herE', u'near', u'live', u'Hail', u'hail', u'hail', u'hail', u'best', u'KoOL', u'JOIN', u'from', u'lmao', u'U105', u'yeah', u'from', u'live', u'lmao', u'U112', u'U105', u'U107', u'that', u'show', u'lmao', u'U105', u'PART', u'male', u'<---', u'halo', u'very', u'grrl', u'PART', u'that', u'show', u'that', u'yeah', u'####', u'sits', u'LMAO', u'damn', u'U105', u'male', u'seem', u'date', u'boys', u'mama', u'from', u'lose', u'sits', u'with', u'lmao', u'girl', u'true', u'U107', u'year', u'JOIN', u'<---', u'talk', u'make', u'good', u'Lets', u'make', u'nice', u'meet', u'U107', u'!!!!', u'PART', u'JOIN', u'PART', u'male', u'U105', u'PART', u'wait', u'....', u'know', u'JOIN', u'PART', u'U105', u'U115', u'U105', u'dude', u'girl', u'U105', u'lmao', u'PART', u'JOIN', u'JOIN', u'PART', u'grrr', u'JOIN', u'....', u'been', u'busy', u'PART', u'this', u'many', u'comp', u'JOIN', u'grrr', u'pork', u'U105', u'busy', u'DONT', u'lmao', u'JOIN', u'next', u'time', u'U115', u'near', u'U105', u'even', u'kent', u'hiya', u'well', u'lmao', u'care', u'chat', u'look', u'have', u'well', u'told', u'once', u'cute', u'just', u'your', u'1cos', u'U115', u"yw's", u'JOIN', u'face', u'PART', u'U119', u'face', u'like', u'U107', u'your', u'mark', u'U115', u'PART', u'blue', u'U105', u'like', u'lmao', u'U115', u'know', u'wait', u'over', u'with', u'sick', u'them', u'humm', u'here', u'lmao', u'dotn', u'U105', u'newp', u'hate', u'sits', u'back', u'JOIN', u'room', u'hugs', u'U115', u'JOIN', u'tell', u'U107', u'PART', u'JOIN', u'This', u'sure', u'JOIN', u'PART', u'from', u'here', u'PART', u'talk', u'very', u'JOIN', u'does', u'vote', u'know', u'know', u'slap', u'That', u'show', u'U107', u'know', u'what', u'that', u'JOIN', u'good', u'ones', u'even', u'vote', u'PART', u'have', u'name', u'from', u'want', u'gays', u'have', u'U120', u'JOIN', u'nose', u'U107', u'nose', u'<<<<', u'gays', u'MODE', u'U112', u'PART', u'MODE', u'PMSL', u'PART', u'JOIN', u'JOIN', u'PART', u'PART', u'pmsl', u'JOIN', u'PART', u'they', u'PART', u'PART', u'JOIN', u'ohhh', u'PART', u'JOIN', u'JOIN', u'JOIN', u'fire', u'....', u'JOIN', u'PART', u'JOIN', u'PART', u'gift', u'PART', u'U115', u'U105', u'PART', u'PART', u'PART', u'U105', u'PART', u'lmao', u'hate', u'this', u'zone', u'will', u'JOIN', u'haha', u'U103', u'when', u'that', u'have', u'hint', u'left', u'PART', u'U129', u'JOIN', u'hmmm', u'U105', u'here', u'hint', u'PART', u'JOIN', u'U129', u'U129', u'sure', u'well', u'girl', u'hell', u'outs', u'comp', u'hiii', u'U105', u'U128', u'JOIN', u'U130', u'U130', u'just', u'!!!.', u'U105', u'U115', u'PART', u'JOIN', u'U130', u'open', u'good', u'U105', u'busy', u'busy', u'good', u'does', u'chat', u'here', u'JOIN', u'lady', u'like', u'talk', u'JOIN', u'U129', u'from', u'PART', u'PART', u'busy', u'busy', u'good', u'good', u'that', u'here', u'find', u'JOIN', u'PART', u'lmao', u'((((', u'Paul', u'))))', u'PART', u'JOIN', u'PART', u'male', u'PART', u'JOIN', u'PART', u'JOIN', u'PART', u'))))', u'PART', u'JOIN', u'outa', u'PART', u'JOIN', u'just', u'send', u'have', u'PART', u'PART', u'U105', u'soon', u'send', u'PART', u'here', u'PART', u'PART', u'JOIN', u'JOIN', u'want', u'chat', u'U105', u'JOIN', u'PART', u'U115', u'PART', u'JOIN', u'PART', u'then', u'goin', u'work', u'U110', u'soon', u'also', u'have', u'good', u'good', u'lmao', u'from', u'good', u'nite', u'JOIN', u'JOIN', u'U121', u'that', u'good', u'PART', u'just', u'want', u'chat', u'York', u'JOIN', u'JOIN', u'PART', u'baby', u'PART', u'nana', u'PART', u'PART', u'shut', u'JOIN', u'From', u'JOIN', u'ello', u'U121', u'from', u'PART', u'nice', u'well', u'U121', u'want', u'call', u'U121', u'JOIN', u'JOIN', u'that', u'chat', u'with', u'year', u'male', u'some', u'call', u'U121', u'will', u'call', u'U121', u'JOIN', u'PART', u'fine', u'fine', u'yeah', u'that', u'what', u'want', u'nick', u'name', u'JOIN', u'back', u'humm', u'PART', u'PART', u'U110', u'call', u'baby', u'JOIN', u'U104', u'JOIN', u'PART', u'room', u'guys', u'PART', u'JOIN', u'U130', u'cant', u'U121', u'kill', u'PART', u'JOIN', u'dude', u'stop', u'that', u'fuck', u'U104', u'many', u'cant', u'that', u'PART', u'love', u'fuck', u'hmmm', u'U110', u'just', u'call', u'U110', u'tell', u'that', u'they', u'long', u'lmao', u'PART', u'lmao', u'JOIN', u'U110', u'runs', u'over', u'hugs', u'U110', u'that', u'PART', u'seen', u'U196', u'come', u'give', u'U104', u'U196', u'U196', u'U196', u'Last', u'seen', u'bout', u'baby', u'U110', u'baby', u'feel', u'U104', u'that', u'idea', u'care', u'chat', u'sexy', u'nana', u'runs', u'over', u'hugs', u'sexy', u'nana', u'that', u'mean', u'JOIN', u'stop', u'dont', u'that', u'lmao', u'U132', u'JOIN', u'well', u'fuck', u'U110', u'sits', u'book', u'JOIN', u'Care', u'Chat', u'that', u'from', u'lmao', u'U104', u'spin', u'over', u'U121', u'will', u'....', u'PART', u'goes', u'PART', u'stop', u'U106', u'JOIN', u'U121', u'must', u'U106', u'lady', u'whos', u'been', u'with', u'woot', u'woot', u'JOIN', u'ewww', u'stop', u'lmao', u'PART', u'Have', u'ever', u'been', u'pink', u'nope', u'U110', u'give', u'U110', u'feel', u'What', u'your', u'fear', u'PART', u'baby', u'with', u'JOIN', u'U104', u'fuck', u'U110', u'tell', u'that', u'they', u'long', u'JOIN', u'PART', u'JOIN', u'pass', u'babe', u'back', u'JOIN', u'PART', u'awww', u'JOIN', u'here', u'back', u'PART', u'JOIN', u'dies', u'know', u'U110', u'your', u'wife', u'same', u'baby', u'room', u'lady', u'dont', u'baby', u'givs', u'your', u'wife', u'haha', u'come', u'give', u'PART', u'JOIN', u'what', u'goes', u'U110', u'wife', u'seen', u'U219', u'U219', u'U219', u'U219', u'Last', u'seen', u'baby', u'room', u'chat', u'when', u'that', u'want', u'chat', u'need', u'that', u'U133', u'wife', u'what', u'U110', u'cool', u'they', u'male', u'fuck', u'seen', u'girl', u'with', u'nice', u'bust', u'seen', u'girl', u'PART', u'cool', u'JOIN', u'what', u'does', u'deaf', u'xmas', u'PART', u'that', u'JOIN', u'dont', u'need', u'wall', u'more', u'good', u'enuf', u'haha', u'nope', u'dont', u'wall', u'PART', u'LoVe', u'wall', u'Love', u'JOIN', u'lmao', u'hell', u'been', u'some', u'kick', u'then', u'some', u'this', u'more', u'well', u'your', u'your', u'wont', u'that', u'they', u'more', u'U121', u'haha', u'feel', u'that', u'come', u'then', u'mean', u'your', u'isnt', u'that', u'joke', u'seen', u'your', u'love', u'seen', u'your', u'pics', u'joke', u'well', u'will', u'that', u'eeww', u'U121', u'mmmm', u'hell', u'turn', u'back', u'????', u'pies', u'pies', u'here', u'what', u'like', u'dick', u'haha', u'ever', u'this', u'room', u'haha', u'damn', u'that', u'fair', u'cant', u'with', u'stop', u'lyin', u'doll', u'then', u'love', u'beer', u'yeah', u'just', u'some', u'even', u'come', u'guys', u'lois', u'U121', u'cold', u'beer', u'guys', u'says', u'what', u'awww', u'U110', u'cuss', u'nope', u'says', u'drop', u'have', u'hand', u'runs', u'thru', u'back', u'hair', u'eyes', u'neck', u'sits', u'down', u'guys', u'LATE', u'THEY', u'GOOD', u'were', u'rape', u'U114', u'girl', u'that', u'LMAO', u'awww', u'geez', u'U110', u'well', u'last', u'shut', u'tart', u'dont', u'like', u'hgey', u'fuck', u'what', u'last', u'mean', u'hump', u'gimp', u'lick', u'caan', u'play', u'lick', u'....', u'else', u'U133', u'good', u'U110', u'!!!!', u'what', u'want', u'love', u'days', u'used', u'call', u'yeah', u'gimp', u'your', u'lmao', u'what', u'dumb', u'like', u'were', u'PART', u'JOIN', u'well', u'PART', u'PART', u'JOIN', u'JOIN', u'will', u'PART', u'awww', u'make', u'hump', u'JOIN', u'PART', u'PART', u'JOIN', u'this', u'room', u'good', u'JOIN', u'U110', u'U110', u'away', u'U104', u'yeah', u'have', u'make', u'good', u'yeah', u'hump', u'your', u'face', u'PART', u'JOIN', u'stay', u'chat', u'damn', u'know', u'lets', u'just', u'know', u'hmmm', u'....', u'yeah', u'spot', u'elle', u'come', u'lets', u'like', u'PART', u'yada', u'yada', u'yada', u'lame', u'suck', u'lol.', u'JOIN', u'with', u'good', u'miss', u'babe', u'seen', u'ages', u'here', u'good', u'Elle', u'went', u'with', u'PART', u'JOIN', u'PART', u'been', u'stop', u'your', u'nude', u'pics', u'JOIN', u'yeah', u'have', u'good', u'good', u'lmao', u'dont', u'have', u'wish', u'sure', u'U110', u'good', u'your', u'like', u'elle', u'allo', u'stop', u'what', u'shit', u'good', u'girl', u'some', u'PART', u'yeah', u'ugly', u'your', u'wife', u'JOIN', u'yesh', u'been', u'nice', u'guyz', u'chat', u'nice', u'want', u'chat', u'male', u'fuck', u'nice', u'lmao', u'when', u'U104', u'like', u'clue', u'alot', u'that', u'PART', u'damn', u'wind', u'must', u'have', u'JOIN', u'poor', u'doll', u'Reub', u'real', u'this', u'talk', u'!???', u'just', u'want', u'lost', u'good', u'here', u'help', u'U110', u'elle', u'????', u'have', u'sure', u'rain', u'here', u'heat', u'hard', u'seem', u'kmph', u'U114', u'pope', u'have', u'used', u'PART', u'mass', u'they', u'dont', u'even', u'goin', u'give', u'dont', u'babe', u'born', u'cant', u'will', u'fuck', u'just', u'need', u'keep', u'with', u'shut', u'JOIN', u'shit', u'Ummm', u'your', u'that', u'does', u'kill', u'just', u'some', u'will', u'fast', u'U104', u'whip', u'U110', u'U110', u'PART', u'dont', u'know', u'head', u'whos', u'shit', u'JOIN', u'LMAO', u'U104', u'PART', u'U104', u'bend', u'over', u'show', u'yeah', u'baby', u'yess', u'hiya', u'care', u'....', u'find', u'else', u'pick', u'JOIN', u'PART', u'JOIN', u'JOIN', u'JOIN', u'))))', u'Just', u'what', u'like', u'!...', u'dont', u'know', u'time', u'life', u'game', u'what', u'JOIN', u'....', u'....', u'PART', u'room', u'duet', u'pick', u'Gosh', u'hell', u'....', u',,,,', u'bout', u'PART', u'nice', u'meet', u'ahhh', u'JOIN', u'JOIN', u'need', u'perv', u'give', u'wuts', u'here', u'know', u'....', u'help', u'PART', u'will', u'perv', u'else', u'with', u'ever', u'wait', u'goin', u'flow', u'....', u'lmao', u'JOIN', u'PART', u'know', u'been', u'year', u'here', u'then', u'well', u'last', u'know', u'what', u'west', u'quiz', u'what', u'PART', u'kewl', u'JOIN', u'ahhh', u'just', u'PART', u'JOIN', u'cool', u'next', u'JOIN', u'PART', u'JOIN', u'JOIN', u'PART', u'JOIN', u'PART', u'guys', u'JOIN', u'PART', u'what', u'nick', u'name', u'PART', u'PART', u'JOIN', u'PART', u'like', u'PART', u'....', u'JOIN', u'what', u'dont', u'yall', u'PART', u'scar', u'face', u'JOIN', u'JOIN', u'ahhh', u'JOIN', u'JOIN', u'goes', u'back', u'been', u'nice', u'hate', u'JOIN', u'PART', u'JOIN', u'PART', u'PART', u'JOIN', u'PART', u'PART', u'JOIN', u'PART', u'back', u'JOIN', u'what', u'name', u'PART', u'PART', u'away', u'....', u'wine', u'well', u'porn', u'life', u'know', u'well', u'then', u'wine', u'PART', u'well', u'have', u'will', u'Girl', u'JOIN', u'JOIN', u'JOIN', u'PART', u'hiya', u'PART', u'PART', u'JOIN', u'hiya', u'....', u'hugs', u'yall', u'JOIN', u'good', u'JOIN', u'JOIN', u'baby', u'Hiya', u'PART', u'just', u'left', u'must', u'been', u'good', u'hiya', u'have', u'been', u'turn', u'JOIN', u'hiya', u'head', u'....', u'does', u'life', u'with', u'your', u'made', u'same', u'some', u'must', u'have', u'roll', u'JOIN', u'pair', u'like', u'here', u'even', u'know', u'PART', u'PART', u'hehe', u'ring', u'....', u'aint', u'what', u'they', u'used', u'....', u'sang', u'that', u'....', u'Rang', u'dont', u'know', u'some', u'????', u'mind', u'that', u'that', u'that', u'hall', u'hows', u'PART', u'PART', u'hall', u'when', u'rang', u'door', u'bell', u'show', u'ring', u'PART', u'JOIN', u'JOIN', u'than', u'....', u'hehe', u'dawg', u'than', u'mine', u'nite', u'much', u'love', u'nite', u'JOIN', u'PART', u'PART', u'JOIN', u'PART', u'JOIN', u'cant', u'play', u'crap', u'rule', u'name', u'that', u'tune', u'PART', u'PART', u'many', u'JOIN', u'....', u'name', u'that', u'tune', u'PART', u'need', u'love', u',,,,', u'door', u'back', u'were', u'good', u'that', u'sing', u'song', u'haze', u'JOIN', u'time', u'febe', u'Prof', u'does', u'stay', u'just', u'JOIN', u'PART', u'sang', u'play', u'done', u'song', u'JOIN', u'????', u'JOIN', u'good', u'PART', u'does', u'that', u'make', u'....', u'your', u'time', u'....', u'sang', u'sang', u'....', u'1996', u'with', u'PART', u'JOIN', u'song', u'1996', u'hmmm', u'dont', u'know', u'JOIN', u'PART', u'JOIN', u'PART', u'PART', u'fine', u'here', u'....', u'JOIN', u'JOIN', u'PART', u'JOIN', u'PART', u'what', u'cash', u'nick', u'name', u'know', u'that', u'when', u'sang', u'dont', u'know', u'come', u'just', u'hell', u'know', u'easy', u'what', u'nick', u'name', u'JOIN', u'JOIN', u'JOIN', u'hiya', u'hiya', u'hiya', u'your', u'girl', u'says', u'PART', u'JOIN', u'PART', u'JOIN', u'nice', u'lady', u'JOIN', u'JOIN', u'Kewl', u'from', u'PART', u'JOIN', u'even', u'what', u'song', u'hank', u'sang', u'from', u'used', u'know', u'just', u'idea', u'over', u'hehe', u'PART', u'cool', u'some', u'????', u'know', u'hank', u'hank', u'jude', u'sang', u'slow', u'hand', u'eric', u'PART', u'PART', u'good', u'yoko', u'yoko', u'yoko', u'JOIN', u'what', u'yoko', u'when', u'John', u'shot', u'lmao', u'same', u'shit', u'what', u'show', u'sing', u'heya', u'shit', u'girl', u'JOIN', u'heya', u'show', u'good', u'that', u'hiya', u'yoko', u'that', u'john', u'like', u'JOIN', u'john', u'nite', u'nope', u'that', u'PART', u'hehe', u'back', u'ohhh', u'oops', u'just', u'here', u'need', u'zone', u'JOIN', u'have', u'know', u'John', u'Yoko', u'last', u'wife', u'said', u'when', u'your', u'dead', u'wont', u'take', u'with', u'your', u'soul', u'hehe', u'that', u'good', u'just', u'here', u'will', u'stay', u'PART', u'feel', u'free', u'JOIN', u'hiya', u'seee', u'whou', u'said', u'idnt', u'like', u'nite', u'PART', u'JOIN', u'last', u'been', u'here', u'like', u'that', u'JOIN', u'down', u'well', u'sooo', u'more', u'PART', u'well', u'poor', u'pink', u'here', u'PART', u'yeah', u'hehe', u'good', u'idea', u'busy', u'chat', u'yeah', u'what', u'good', u'perk', u'like', u'took', u'yeah', u'what', u'what', u'....', u'that', u'over', u'hehe', u'your', u'nope', u'PART', u'like', u'JOIN', u'must', u'chat', u'wear', u'JOIN', u'JOIN', u'main', u'room', u'find', u'http', u'rain', u'here', u'rubs', u'LMAO', u'love', u'your', u'game', u'your', u'chat', u'room', u'PART', u'this', u'game', u'goin', u'shit', u'ROOM', u'says', u'made', u'skin', u'PART', u'JOIN', u'PART', u'JOIN', u'2DAY', u'gawd', u'need', u'meds', u'that', u'make', u'skin', u'sure', u'need', u'yell', u'what', u'....', u'????', u'else', u'says', u'till', u'caps', u'eyes', u'mang', u'good', u'when', u'take', u'cant', u'live', u'eyes', u'make', u'feel', u'JOIN', u'PART', u'JOIN', u'away', u'what', u'your', u'eyes', u'else', u'from', u'here', u'SSRI', u'girl', u'PART', u'JOIN', u'well', u'deal', u'with', u'that', u'your', u'cure', u'they', u'just', u'help', u'deal', u'with', u'real', u'awww', u'know', u'JOIN', u'wean', u'need', u'meds', u'like', u'that', u'JOIN', u'hiya', u'JOIN', u'well', u'back', u'died', u'cost', u'much', u'JOIN', u'yeah', u'just', u'JOIN', u'PART', u'PART', u'take', u'awww', u'PART', u'PART', u'PART', u'just', u'kick', u'like', u'post', u'room', u'meds', u'left', u'PART', u'what', u'DOES', u'when', u'quit', u'LMAO', u'last', u'mind', u'itch', u'your', u'JOIN', u'dont', u'want', u'live', u'just', u'JOIN', u'that', u'shut', u'many', u'bout', u'lost', u'time', u'just', u'very', u'JOIN', u'just', u'yeah', u'does', u'they', u'case', u'case', u'JOIN', u'read', u'were', u'PART', u'been', u'fine', u'been', u'what', u'long', u'have', u'been', u'much', u'PART', u'meds', u'good', u'doin', u'will', u'take', u'PART', u'PART', u'have', u'like', u'this', u'week', u'long', u'have', u'been', u'holy', u'crap', u'week', u'like', u'JOIN', u'JOIN', u'will', u'take', u'kick', u'JOIN', u'okay', u'just', u'shit', u'time', u'anti', u'talk', u'want', u'mean', u'took', u'LMAO', u'....', u'that', u'week', u'itch', u'down', u'near', u'PART', u'life', u'trip', u'well', u'yeah', u'real', u'haha', u'live', u'what', u'JOIN', u'your', u'JOIN', u'when', u'used', u'that', u'real', u'ever', u'hear', u'Ummm', u'else', u'with', u'week', u'that', u'JOIN', u'when', u'talk', u'yeah', u'bout', u'kill', u'much', u'keep', u'bout', u'kill', u'that', u'take', u'work', u'take', u'deep', u'till', u'JOIN', u'PART', u'well', u'hurt', u'hiya', u'PART', u'shut', u'bout', u'talk', u'talk', u'play', u'Gosh', u'lmao', u'PART', u'take', u'that', u'crap', u'lmao', u'PART', u'awww', u'here', u'life', u'cali', u'said', u'okay', u'noth', u'PART', u'JOIN', u'PART', u'your', u'life', u'been', u'stop', u'PART', u'very', u'that', u'many', u'have', u'been', u'wait', u'know', u'then', u'know', u'what', u'look', u'babi', u'look', u'have', u'here', u'feet', u'tall', u'PART', u'PART', u'nite', u'pray', u'hope', u'that', u'will', u'stay', u'JOIN', u'PART', u'JOIN', u'babi', u'look', u'JOIN', u'ewww', u'PART', u'PART', u'PART', u'PART', u'NICK', u'LMAO', u'PART', u'that', u'that', u'rubs', u'weed', u'icky', u'LMAO', u'JOIN', u'name', u'JOIN', u'that', u'mean', u'just', u'Rick', u'know', u'with', u'spit', u'LMAO', u'rich', u'lube', u'JOIN', u'JOIN', u'rich', u'lord', u'JOIN', u'mami', u'JOIN', u'PART', u'want', u'look', u'last', u'name', u'U102', u'U102', u'U101', u'yeah', u'U100', u'U102', u'U102', u'gold', u'hiya', u'U102', u'U102', u'here', u'U102', u'U102', u'look', u'PART', u'what', u'here', u'find', u'what', u'here', u'chat', u'room', u'JOIN', u'PART', u'guys', u'PART', u'from', u'east', u'18ST', u'JOIN', u'much', u'cost', u'room', u'slow', u'yeah', u'U102', u'fart', u'blew', u'away', u'JOIN', u'ohhh', u'sexy', u'love', u'PART', u'girl', u'that', u'JOIN', u'U106', u'PART', u'U101', u'come', u'back', u'sexy', u'love', u'over', u'else', u'JOIN', u'PART', u'JOIN', u'haha', u'U101', u'have', u'PART', u'song', u'heya', u'JOIN', u'give', u'U102', u'PART', u'guys', u'girl', u'like', u'back', u'many', u'damn', u'seat', u'dont', u'give', u'PART', u'JOIN', u'PART', u'felt', u'rock', u'hard', u'cock', u'here', u'sexy', u'love', u'meet', u'full', u'girl', u'take', u'make', u'back', u'PART', u'make', u'newp', u'PART', u'love', u'lady', u'JOIN', u'SExy', u'love', u'yeah', u'otay', u'####', u'like', u'love', u'PART', u'JOIN', u'Yeah', u'have', u'need', u'JOIN', u'JOIN', u'cool', u'cool', u'U110', u'said', u'like', u'dude', u'many', u'mine', u'JOIN', u'need', u'more', u'JOIN', u'like', u'JOIN', u'JOIN', u'JOIN', u'U115', u'firs', u'time', u'this', u'site', u'said', u'that', u'that', u'ever', u'told', u'room', u'JOIN', u'just', u'PART', u'JOIN', u'PART', u'JOIN', u'JOIN', u'PART', u'U113', u'PART', u'JOIN', u'PART', u'JOIN', u'PART', u'love', u'each', u'yall', u'room', u'mike', u'PART', u'dump', u'PART', u'PART', u'with', u'some', u'toop', u'yall', u'this', u'song', u'PART', u'what', u'song', u'just', u'that', u'PART', u'U108', u'this', u'your', u'room', u'slow', u'chat', u'room', u'here', u'that', u'with', u'four', u'does', u'want', u'chat', u'with', u'from', u'more', u'JOIN', u'U115', u'PART', u'U118', u'over', u'head', u'with', u'make', u'stop', u'make', u'stop', u'JOIN', u'room', u'U108', u'U108', u'just', u'that', u'yeah', u'type', u'JOIN', u'make', u'away', u'JOIN', u'PART', u'U116', u'find', u'U108', u'sets', u'room', u'asss', u'....', u'part', u'felt', u'most', u'that', u'lmao', u'just', u'that', u'what', u'shit', u'eyes', u'that', u'paid', u'this', u'room', u'PART', u'LMAO', u'PART', u'what', u'have', u'home', u'JOIN', u'LMAO', u'mean', u'U120', u'your', u'home', u'room', u'hell', u'JOIN', u'Iowa', u'JOIN', u'were', u'just', u'that', u'U102', u'take', u'U108', u'room', u'U120', u'PART', u'lmao', u'beat', u'with', u'your', u'back', u'PART', u'dont', u'beat', u'with', u'your', u'PART', u'Teck', u'n9ne', u'back', u'PART', u'PART', u'dont', u'with', u'JOIN', u'hour', u'from', u'hell', u'that', u'chat', u'dont', u'with', u'kewl', u'JOIN', u'JOIN', u'well', u'JOIN', u'JOIN', u'well', u'JOIN', u'chat', u'that', u'PART', u'goes', u'both', u'ways', u'dear', u'U104', u'JOIN', u'JOIN', u'PART', u'does', u'both', u'ways', u'JOIN', u'know', u'dont', u'PART', u'PART', u'nice', u'once', u'JOIN', u'have', u'been', u'been', u'JOIN', u'JOIN', u'ever', u'here', u'very', u'much', u'have', u'room', u'that', u'that', u'"...', u'hmph', u'PART', u'JOIN', u'JOIN', u'PART', u'JOIN', u'MODE', u'U132', u'U132', u'JOIN', u'like', u'U132', u'U133', u'U132', u'U132', u'hiya', u'U132', u'PART', u'JOIN', u'nick', u'JOIN', u'U132', u'come', u'like', u'like', u'PART', u'jeff', u'U104', u'PART', u'crib', u'!!!!', u'PART', u'wack', u'food', u'such', u'deop', u'MODE', u'U132', u'PART', u'U132', u'that', u'U102', u'PART', u'your', u'like', u'only', u'time', u'type', u'when', u'JOIN', u'JOIN', u'sexy', u'JOIN', u'PART', u'JOIN', u'haha', u'love', u'JOIN', u'nite', u'wife', u'love', u'want', u'PART', u'nite', u'U116', u'PART', u'JOIN', u'drug', u'talk', u'told', u'cook', u'turn', u'into', u'want', u'chat', u'JOIN', u'U138', u'hear', u'want', u'your', u'((((', u'PART', u'JOIN', u'JOIN', u'9:10', u'PART', u'JOIN', u'ladz', u'JOIN', u'hola', u'JOIN', u'PART', u'U115', u'PART', u'PART', u'JOIN', u'aime', u'JOIN', u'What', u'idea', u'over', u'JOIN', u'Ahhh', u'okay', u'chat', u'lady', u'whos', u'been', u'book', u'here', u'JOIN', u'PART', u'PART', u'PART', u'That', u'what', u'JOIN', u'guys', u'chat', u'JOIN', u'chat', u'JOIN', u'JOIN', u'JOIN', u'U119', u'pink', u'PART', u'PART', u'baby', u'with', u'PART', u'same', u'hong', u'kong', u'chat', u'PART', u'ball', u'does', u'PART', u'damn', u'like', u'have', u'good', u'time', u'PART', u'PART', u'JOIN', u'what', u'goes', u'like', u'JOIN', u'U123', u'U123', u'U123', u'MODE', u'U123', u'baby', u'JOIN', u'damn', u'guys', u'dude', u'shut', u'PART', u'blue', u'haha', u'PART', u'PART', u'Oops', u'yawn', u'haha', u'PART', u'PART', u'from', u'PART', u'joke', u'chat', u'That', u'okay', u'haha', u'yeah', u'PART', u'PART', u'love', u'PART', u'haha', u'PART', u'JOIN', u'PART', u'PART', u'guys', u'from', u'chat', u'here', u'JOIN', u'then', u'hell', u'shot', u'JOIN', u'PART', u'JOIN', u'PART', u'JOIN', u'PART', u'JOIN', u'PART', u'PART', u'shot', u'cool', u'whos', u'guys', u'talk', u'with', u'PART', u'chat', u'with', u'sexy', u'guys', u'chat', u'??!!', u'PART', u'whos', u'??!!', u'talk', u'mass', u'want', u'chat', u'....', u'damn', u'PART', u'cali', u'guys', u'chat', u'JOIN', u'PART', u'JOIN', u'real', u'have', u'tits', u'PART', u'PART', u'sexy', u'guys', u'chat', u'U108', u'PART', u'aint', u'find', u'gret', u'....', u'damn', u'PART', u'guys', u'chat', u'with', u'PART', u'take', u'life', u'PART', u'JOIN', u'that', u'shit', u'JOIN', u'haha', u'PART', u'dude', u'what', u'hell', u'JOIN', u'PART', u'what', u'girl', u'talk', u'kick', u'U111', u'JOIN', u'PART', u'them', u'guns', u'much', u'JOIN', u'Like', u'like', u'inch', u'face', u'JOIN', u'fart', u'ever', u'sean', u'PART', u'shit', u'howl', u'moon', u'yall', u'mean', u'damn', u'yeah', u'cant', u'just', u'JOIN', u'Ohio', u'even', u'STOP', u'PART', u'PART', u'what', u'JOIN', u'like', u'PART', u'JOIN', u'Take', u'JOIN', u'PART', u'here', u'JOIN', u'JOIN', u'here', u'z-ro', u'dead', u'guys', u'chat', u'wats', u'what', u'here', u'chat', u'chat', u'any1', u'what', u'good', u'with', u'U137', u'dont', u'know', u'from', u'JOIN', u'JOIN', u'cell', u'here', u'Haha', u'here', u'chat', u'JOIN', u'wana', u'chat', u'????', u'PART', u'well', u'this', u'haha', u'PART', u'dead', u'damn', u'this', u'room', u'than', u'just', u'dont', u'know', u'ball', u'talk', u'PART', u'miss', u'hell', u'PART', u'here', u'yeah', u'good', u'blue', u'guys', u'JOIN', u'U141', u'....', u'1985', u'chat', u'JOIN', u'U142', u'U142', u'U142', u'MODE', u'U142', u'PART', u'slam', u'JOIN', u'PART', u'damn', u'PART', u'like', u'damn', u'JOIN', u'here', u'PART', u'here', u'find', u'PART', u'JOIN', u'PART', u'haha', u'U144', u'like', u'kill', u'U119', u'Your', u'skin', u'....', u'dont', u'care', u'!!!!', u'kill', u'want', u'....', u'aint', u'stop', u'good', u'good', u'help', u'tell', u'love', u'will', u'boys', u'have', u'JOIN', u'will', u'sure', u'what', u'dont', u'boys', u'lets', u'kill', u'....', u'JOIN', u'ever', u'what', u'love', u'this', u'song', u'JOIN', u'live', u'kill', u'girl', u'just', u'talk', u'what', u'song', u'hmmm', u'seem', u'have', u'U119', u'JOIN', u'JOIN', u'JOIN', u'lets', u'kill', u'PART', u'here', u'from', u'pine', u'city', u'PART', u'JOIN', u'PART', u'what', u'lets', u'kill', u'PART', u'PART', u'come', u'with', u'more', u'plan', u'than', u'kill', u'with', u'JOIN', u'JOIN', u'they', u'....', u'JOIN', u'haha', u'JOIN', u'PART', u'JOIN', u'JOIN', u'JOIN', u'what', u'what', u'JOIN', u'they', u'must', u'must', u'they', u'must', u'must', u'PART', u'know', u'chat', u'here', u'here', u'JOIN', u'JOIN', u'JOIN', u'PART', u'yeas', u'like', u'PART', u'JOIN', u'what', u'puke', u'yeah', u'JOIN', u'yeah', u'over', u'....', u'JOIN', u'like', u'kids', u'want', u'talk', u'guys', u'talk', u'with', u'PART', u'JOIN', u'crap', u'that', u'PART', u'haha', u'damn', u'waaa', u'yeas', u'guyz', u'PART', u'some', u'U119', u'U145', u'good', u'time', u'PART', u'love', u'haha', u'yeah', u'U141', u'U145', u'only', u'haha', u'JOIN', u'what', u'area', u'here', u'JOIN', u'here', u'what', u'JOIN', u'hmmm', u'guys', u'chat', u'with', u'very', u'girl', u'U119', u'urls', u'PART', u'PART', u'heya', u'star', u'JOIN', u'JOIN', u'JOIN', u'room', u'kill', u'PART', u'JOIN', u'PART', u'....', u'....', u'PART', u'chat', u'U119', u'kill', u'....', u'PART', u'from', u'joke', u'lets', u'pick', u'....', u'yeah', u'PART', u'guys', u'chat', u'from', u'yall', u'suck', u'PART', u'Save', u'kids', u'chat', u'wont', u'this', u'....', u'chat', u'JOIN', u'what', u'suck', u'U119', u'kill', u'JOIN', u'here', u'suck', u'JOIN', u'haha', u'PART', u'PART', u'U154', u'JOIN', u'PART', u'teck', u'n9ne', u'back', u'take', u'damn', u'U154', u'JOIN', u'more', u'year', u'Room', u'want', u'chat', u'have', u'JOIN', u'girl', u'talk', u'guys', u'chat', u'will', u'PART', u'U114', u'hate', u'PART', u'wooo', u'PART', u'eats', u'U154', u'look', u'good', u'them', u'like', u'chat', u'here', u'want', u'your', u'here', u'sick', u'shit', u'wooo', u'sori', u'guys', u'PART', u'JOIN', u'PART', u'want', u'talk', u'JOIN', u'only', u'PART', u'into', u'U139', u'room', u'chat', u'with', u'love', u'blah', u'blah', u'spot', u'....', u'here', u'JOIN', u'sexy', u'guys', u'chat', u'PART', u'U169', u'fast', u'self', u'time', u'JOIN', u'JOIN', u'U169', u'your', u'JOIN', u'talk', u'with', u'U154', u'some', u'cali', u'guys', u'here', u'PART', u'here', u'PART', u'seen', u'U169', u'U169', u'U169', u'U169', u'last', u'seen', u'U111', u'only', u'JOIN', u'JOIN', u'here', u'hmmm', u'chat', u'U169', u'seem', u'does', u'U114', u'haha', u'nope', u'U128', u'<333', u'JOIN', u'PART', u'<333', u'want', u'swim', u'Long', u'time', u'chat', u'PART', u'true', u'PART', u'know', u'here', u'from', u'JOIN', u'PART', u'yawn', u'want', u'chat', u'PART', u'poem', u'U128', u'like', u'five', u'from', u'into', u'jack', u'PART', u'tick', u'tock', u'PART', u'tick', u'tock', u'JOIN', u'U101', u'here', u'JOIN', u'JOIN', u'ROOM', u'CHAT', u'WITH', u'FROM', u'damn', u',,,,', u'have', u'been', u'cast', u'Rule', u'type', u'CAPS', u'JOIN', u'U114', u'ball', u'have', u'want', u'chat', u'with', u'junk', u'food', u'JOIN', u'tips', u'PART', u'Have', u'been', u'much', u'time', u'that', u'lost', u'this', u'very', u'your', u'life', u'your', u'wana', u'chat', u'with', u'PART', u'JOIN', u'lmao', u'with', u'that', u'like', u'chat', u'beer', u'Hiya', u'that', u'U101', u'said', u'JOIN', u'that', u'from', u'meet', u'your', u'your', u'turn', u'your', u'back', u'This', u'will', u'even', u'this', u'very', u'good', u'rush', u'much', u'your', u'home', u'JOIN', u'Nooo', u'have', u'some', u'good', u'JOIN', u'isnt', u'play', u'JOIN', u'Troy', u'wana', u'chat', u'with', u'room', u'PART', u'What', u'hell', u'PART', u'type', u'with', u'like', u'JOIN', u'guys', u'PART', u'that', u'U101', u'like', u'what', u'yeah', u'some', u'want', u'chat', u'with', u'JOIN', u'PART', u'like', u'fool', u'U105', u'tail', u'JOIN', u'like', u'JOIN', u'Seee', u'U101', u'back', u'what', u'What', u'hell', u'come', u'from', u'lmao', u'room', u'damn', u'room', u'damn', u'runs', u'thru', u'back', u'room', u'damn', u'hair', u'eyes', u'room', u'damn', u'neck', u'PART', u'chat', u'most', u'JOIN', u'6:38', u'PART', u'want', u'chat', u'PART', u'good', u'have', u'down', u'JOIN', u'U126', u'just', u'here', u'look', u'JOIN', u'like', u'your', u'just', u'fine', u'JOIN', u'PART', u'JOIN', u'well', u'look', u'dyed', u'hair', u'told', u'what', u'just', u'left', u'PART', u'U105', u'JOIN', u'dont', u'know', u'some', u'PART', u'JOIN', u'PART', u'JOIN', u'kiss', u'your', u'chat', u'just', u'then', u'more', u'fuck', u'haha', u'PART', u'PART', u'JOIN', u'JOIN', u'spin', u'U114', u'PART', u'seen', u'U988', u'will', u'....', u'goes', u'stop', u'U114', u'must', u'with', u'fuck', u'over', u'just', u't he', u'take', u'hand', u'Yeah', u'haha', u'U988', u'U988', u'U988', u'Last', u'seen', u'!!!!', u'kiss', u'U114', u'baby', u'U114', u'baby', u'that', u'beam', u'that', u'play', u'JOIN', u'with', u'with', u'U114', u'just', u'amen', u'U114', u'puff', u'puff', u'pass', u'U114', u'with', u'daft', u'twit', u'scum', u'seen', u'seen', u'ever', u'walk', u'your', u'feet', u'U134', u'PART', u'long', u'time', u'have', u'seen', u'JOIN', u'want', u'chat', u'from', u'down', u'long', u'time', u'kiss', u'awww', u'come', u'give', u'kiss', u'Type', u'kiss', u'what', u'U114', u'town', u'WHOA', u'some', u'baby', u'....', u'PART', u'JOIN', u'PART', u'JOIN', u'hope', u'down', u'room', u'talk', u'said', u'food', u'were', u'puff', u'puff', u'here', u'take', u'toke', u'ribs', u'just', u'food', u'PART', u'PART', u'JOIN', u'JOIN', u'PART', u'JOIN', u'Eggs', u'side', u'Wyte', u'know', u'Heyy', u'room', u'U144', u'U114', u'play', u'game', u'with', u'moms', u'Over', u'song', u'when', u'both', u'ways', u'West', u'Rock', u'here', u'only', u'well', u'Heyy', u'U103', u'here', u'PART', u'JOIN', u'PART', u'JOIN', u'goof', u'work', u'some', u'more', u'PART', u'howz', u'PART', u'U101', u'with', u'here', u'rock', u'year', u'U144', u'JOIN', u'U146', u'U146', u'Have', u'ever', u'felt', u'even', u'more', u'down', u'U103', u'PART', u'U142', u"ex's", u'live', u'U143', u'PART', u'U146', u'feet', u'they', u'hurt', u'more', u'than', u'they', u'were', u'with', u'then', u'shut', u'away', u'PART', u'what', u'U146', u'good', u'hang', u'U105', u'just', u'come', u'here', u'play', u'with', u"ex's", u'back', u'yard', u'good', u'with', u'JOIN', u'Well', u'JOIN', u'PART', u'JOIN', u'ouch', u'your', u'legs', u'both', u'able', u'JOIN', u'sure', u'more', u'ones', u'PART', u'PART', u'PART', u'U145', u'stay', u'U114', u'vamp', u'PART', u'LMAO', u'JOIN', u'shut', u'make', u'your', u'self', u'down', u'talk', u'call', u'then', u'dont', u'have', u'talk', u'PART', u'PART', u'What', u'part', u'from', u'U144', u'good', u'here', u'JOIN', u'play', u'with', u'guys', u'U103', u'just', u'JOIN', u'JOIN', u'Nope', u'<---', u'live', u'Kent', u'need', u'your', u'what', u'kind', u'live', u'JOIN', u'JOIN', u'kent', u'some', u'with', u'live', u'....', u'more', u'seen', u'U989', u'they', u'talk', u'most', u'just', u'U989', u'U989', u'U989', u'Last', u'seen', u'days', u'PART', u'Cool', u'know', u'Cool', u'from', u'U156', u'PART', u'dont', u'have', u'have', u'good', u'that', u'ther', u'some', u'with', u'U114', u'U156', u'from', u'high', u'high', u'work', u'doin', u'PART', u'PART', u'U147', u'what', u'U114', u'JOIN', u'JOIN', u'room', u'JOIN', u'doin', u'JOIN', u'heyy', u'U156', u'TEXT', u'SIZE', u'JOIN', u'kent', u'good', u'....', u'room', u'heyy', u'U114', u'PART', u'U156', u'club', u'JOIN', u'even', u'PART', u'JOIN', u'U156', u'U156', u'kent', u'like', u'mins', u'from', u'U163', u'gear', u'gold', u'said', u'mind', u'heyy', u'U144', u'lmao', u'CALI', u'U114', u'Only', u'hook', u'good', u'lmao', u'that', u'PART', u'Tell', u'what', u'JOIN', u'here', u'wana', u'chat', u'room', u'need', u'some', u'that', u'here', u'like', u'have', u'U114', u'work', u'bear', u'heyy', u'wife', u'love', u'life', u'runs', u'Matt', u'Rush', u'AWAY', u'That', u'U163', u'U156', u'sexy', u'wish', u'PART', u'JOIN', u'just', u'past', u'heyy', u'U156', u'need', u'some', u'love', u'some', u'love', u'away', u'like', u'U103', u'back', u'from', u'much', u'U114', u'NTMN', u'give', u'U156', u'love', u'PART', u'JOIN', u'Kiss', u'fool', u'howz', u'lick', u'fool', u'PART', u'U158', u'JOIN', u'PART', u'JOIN', u'well', u'done', u'U156', u'your', u'grea', u'U168', u'U156', u'U156', u'runs', u'thru', u'back', u'U156', u'hair', u'eyes', u'U156', u'neck', u'U156', u'U156', u'been', u'U163', u'U168', u'mine', u'fine', u'U168', u'PART', u'JOIN', u'time', u'U168', u'dear', u'like', u'U156', u'sure', u'does', u'been', u'fine', u'U156', u'U156', u'okay', u'U156', u'want', u'like', u'cool', u'PART', u'been', u'good', u'JOIN', u'Look', u'guys', u'nice', u'jerk', u'from', u'U156', u'like', u'good', u'PART', u'U156', u'JOIN', u'home', u'want', u'know', u'U129', u'does', u'nick', u'U168', u'U168', u'....', u'here', u'kiss', u'U168', u'kiss', u'U168', u'dont', u'know', u'will', u'make', u'U168', u'PART', u'cool', u'PART', u'JOIN', u'JOIN', u'U170', u'guys', u'PART', u'PART', u'PART', u'like', u'play', u'with', u'ROOM', u'much', u'U170', u'JOIN', u'moon', u'JOIN', u'only', u'JOIN', u'nice', u'pick', u'U156', u'been', u'that', u'when', u'came', u'U156', u'what', u'guys', u'guts', u'guys', u'ones', u'U156', u'U175', u'baby', u'PART', u'this', u'more', u'jerk', u'like', u'then', u'U156', u'U144', u'runs', u'thru', u'back', u'hair', u'eyes', u'neck', u'U168', u'beer', u'JOIN', u'U156', u'baby', u'U156', u'PART', u'JOIN', u'PART', u'love', u'neck', u'JOIN', u'your', u'hang', u'they', u'U144', u'PART', u'just', u'JOIN', u'U175', u'U168', u'U168', u'nice', u'U156', u'give', u'seen', u'seen', u'chat', u'here', u'know', u'play', u'case', u'this', u'when', u'work', u'that', u'boss', u'died', u'went', u'work', u'told', u'that', u'died', u'wrek', u'give', u'told', u'suck', u'told', u'good', u'PART', u'haha', u'girl', u'JOIN', u'NICK', u'PART', u'pfft', u'just', u'!!!!', u'ciao', u'else', u'CHAT', u'WITH', u'FROM', u'cold', u'know', u'just', u'from', u'here', u'JOIN', u'Fort', u'2:55', u'AKST', u'warm', u'PART', u'know', u'warm', u'4:03', u'warm', u'need', u'some', u'root', u'gone', u'mine', u'same', u'time', u'poor', u'move', u'root', u'gone', u'poor', u'what', u'PART', u'have', u'goes', u'JOIN', u'wear', u'them', u'long', u'PART', u'mine', u'have', u'here', u'once', u'dont', u'hiya', u'keep', u'them', u'when', u'....', u'have', u'PART', u'well', u'hmmm', u'well', u'PART', u'note', u'that', u'heck', u'PART', u'heck', u'PART', u'....', u'keep', u'them', u'ahhh', u'pain', u'know', u'lmao', u'JOIN', u'JOIN', u'hiya', u'lets', u'chat', u'good', u'need', u'PART', u'back', u'hiya', u'hiya', u'name', u'hiya', u'hair', u'cute', u'that', u'tune', u'....', u'head', u'sigh', u'what', u'PART', u'JOIN', u'like', u'hiya', u'hiya', u'that', u'wire', u'????', u'back', u'here', u'have', u'been', u'burp', u'hiya', u'oops', u'give', u'just', u'mind', u'....', u'that', u'lmao', u'good', u'snow', u'cold', u'soda', u'what', u'with', u'this', u'gray', u'here', u'tlak', u'bout', u'ride', u'some', u'some', u'dont', u'what', u'they', u'JOIN', u'ahem', u'hiya', u'ltnc', u'just', u'glad', u'over', u'with', u'take', u'chat', u'PART', u'JOIN', u'this', u'gets', u'this', u'that', u'gets', u'that', u'rest', u'PART', u'JOIN', u'haha', u'have', u'list', u'room', u"ok'd", u'just', u'sayn', u'PART', u'sure', u'some', u'take', u'take', u'sock', u'here', u'evah', u'take', u'this', u'cold', u'good', u'bike', u'this', u'down', u'hill', u'went', u'stop', u'PART', u'cold', u'yeah', u'walk', u'that', u'only', u'here', u'sock', u'ohwa', u'caca', u'know', u'JOIN', u'dont', u'know', u'tyvm', u'mine', u'they', u'....', u'only', u'when', u'wear', u'them', u'week', u'time', u'them', u'they', u'need', u'luvs', u'with', u'long', u'time', u'want', u'some', u'have', u'with', u'pain', u'like', u'used', u'make', u'PART', u'dont', u'need', u'love', u'they', u'were', u'PART', u'have', u'know', u'sock', u'sock', u'have', u'have', u'have', u'been', u'much', u'prep', u'done', u'when', u'hope', u'toss', u'sock', u'when', u'find', u'sock', u'gets', u'send', u'them', u'here', u'....', u'wear', u'them', u'JOIN', u'hell', u'just', u'that', u'ball', u'make', u'some', u'from', u'what', u'does', u'that', u'wash', u'JOIN', u'will', u'dont', u'know', u'does', u'hate', u'tell', u'long', u'been', u'used', u'PART', u'they', u'sell', u'them', u'from', u'sure', u'from', u'know', u'when', u'when', u'your', u'back', u'pull', u'that', u'JOIN', u'adds', u'with', u'them', u'also', u'they', u'dirt', u'then', u'head', u'that', u'they', u'your', u'vent', u'100%', u'true', u'just', u'have', u'used', u'have', u'that', u'when', u'went', u'knew', u'what', u'live', u'dont', u'want', u'have', u'haha', u'felt', u'like', u'JOIN', u'PART', u'ahhh', u'....', u'JOIN', u'wait', u'much', u'make', u'year', u'JOIN', u'like', u'have', u'LMAO', u'PART', u'what', u'make', u'make', u'have', u'make', u'more', u'than', u'well', u'hear', u'time', u'ride', u'take', u'care', u'have', u'talk', u'soon', u'stay', u'safe', u'kiss', u'your', u'kids', u'your', u'dogs', u'PART', u'have', u'with', u'bull', u'time', u'just', u'life', u'with', u'your', u'make', u'dear', u'lord', u'fits', u'over', u'xbox', u'live', u'JOIN', u'well', u'have', u'fits', u'nice', u'work', u'week', u'what', u'mean', u'PART', u'from', u'week', u'heck', u'what', u'town', u'near', u'cant', u'real', u'asks', u'been', u'same', u'many', u'Road', u'very', u'pick', u'home', u'high', u'live', u'from', u'PART', u'that', u'JOIN', u'over', u'that', u'JOIN', u'hiya', u'hate', u'JOIN', u'seen', u'near', u'here', u'PART', u'what', u'have', u'seen', u'them', u'....', u'long', u'does', u'take', u'back', u'dang', u'work', u'chat', u'they', u'like', u'long', u'fire', u'like', u'chit', u'JOIN', u'PART', u'land', u'PART', u'PART', u'doin', u'room', u'well', u'have', u'them', u'that', u'have', u'time', u'chat', u'grin', u'dont', u'here', u'here', u'JOIN', u'haha', u'they', u'were', u'bred', u'kill', u'rats', u'Sat.', u'JOIN', u'they', u'long', u'time', u'they', u'back', u'drop', u'your', u'foot', u'guys', u'life', u'JOIN', u'what', u'samn', u'eyes', u'much', u'this', u'room', u'like', u'Phil', u'into', u'????', u'nuff', u'rose', u'PART', u'Ruth', u'good', u'hear', u'like', u'phil', u'meds', u'PART', u'JOIN', u'back', u'JOIN', u'MODE', u'MODE', u'PART', u'hows', u'PART', u'hiya', u'PART', u'hiya', u'must', u'hiya', u'many', u'like', u'open', u'that', u'with', u'doin', u'good', u'dear', u'rofl', u'!!!!', u'PART', u'here', u'hows', u'bout', u'here', u'here', u'that', u'....', u'tell', u'tell', u'days', u'ages', u'here', u'PART', u'only', u'here', u'lmao', u'well', u'that', u'PART', u'well', u'case', u'word', u'dang', u'....', u'here', u'what', u'part', u'rofl', u'like', u'grew', u'PART', u'near', u'year', u'holy', u'....', u'nice', u'from', u'<---', u'went', u'JOIN', u'love', u'....', u'like', u'from', u'PART', u'????', u'when', u'that', u'sand', u'well', u'army', u'JOIN', u'clue', u'what', u'here', u'like', u'....', u'They', u'army', u'mean', u'that', u'tell', u'only', u'they', u'they', u'lmao', u'that', u'they', u'show', u'kids', u'live', u'JOIN', u'down', u'near', u'when', u'from', u'ears', u'feel', u'best', u'....', u'away', u'from', u'well', u'from', u'hear', u'rest', u'nice', u'more', u'that', u'such', u'JOIN', u'yeah', u'luvs', u'PART', u'down', u'mena', u'ROFL', u'that', u'pool', u'like', u'lapd', u'were', u'into', u'surf', u'cant', u'even', u'swim', u'here', u'sand', u'your', u'true', u'JOIN', u'JOIN', u'hard', u'when', u'just', u'side', u'City', u'....', u'wear', u'fall', u'....', u'....', u'....', u'much', u'PART', u'what', u'JOIN', u'only', u'that', u'room', u'from', u'hazy', u'that', u'have', u'been', u'were', u'What', u'were', u'hear', u'army', u'band', u'thot', u'just', u'haze', u'left', u'over', u'from', u'very', u'warm', u'yeah', u'....', u'like', u'more', u'than', u'sing', u'here', u'dont', u'good', u'they', u'sang', u'some', u'them', u'they', u'down', u'ride', u'than', u'what', u'PART', u'nite', u'shes', u'sick', u'look', u'here', u'sing', u'lmao', u'blue', u'blue', u'acid', u'hmmm', u'here', u'knew', u'that', u'uses', u'blue', u'they', u'were', u'from', u'blue', u'main', u'room', u'find', u'PART', u'just', u'your', u'game', u'your', u'chat', u'room', u'PART', u'JOIN', u'PART', u'PART', u'PART', u'PART', u'wide', u'lost', u'went', u'JOIN', u'from', u'have', u'keys', u'here', u'lmao', u'wont', u'JOIN', u'snow', u'rock', u'salt', u'like', u'some', u'PART', u'JOIN', u'what', u'chat', u'PART', u'what', u'PART', u'much', u'JOIN', u'want', u'room', u'that', u'mess', u'PART', u'base', u'ball', u'JOIN', u'dead', u'JOIN', u'then', u'when', u'over', u'PART', u'byes', u'JOIN', u'PART', u'what', u'were', u'PART', u'some', u'PART', u'wait', u'time', u'PART', u'that', u'when', u'work', u'days', u'this', u'week', u'when', u'have', u'work', u'JOIN', u'back', u'more', u'gawd', u'must', u'love', u'PART', u'PART', u'NICK', u'room', u'PART', u'PART', u'NICK', u'then', u'work', u'NICK', u'haha', u'PART', u'dont', u'like', u'work', u'THAT', u'much', u'will', u'your', u'like', u'that', u'work', u'play', u'JOIN', u'yeah', u'....', u'know', u'JOIN', u'sick', u'part', u'have', u'work', u'make', u'near', u'what', u"RN's", u'make', u'JOIN', u'JOIN', u'only', u'dont', u'alot', u'love', u'well', u'work', u'with', u'hand', u'made', u'....', u'that', u'that', u'hour', u'haha', u'PART', u'have', u'they', u'said', u'they', u'have', u'more', u'face', u'well', u'only', u'have', u'JOIN', u'JOIN', u'haha', u'that', u'give', u'JOIN', u'have', u'JOIN', u'just', u'just', u'yout', u'have', u'with', u'this', u'lame', u'chat', u'PART', u'PART', u'well', u'just', u'come', u'here', u'hang', u'with', u'lame', u'face', u'with', u'JOIN', u'PART', u'been', u'they', u'feel', u'lame', u'numb', u'PART', u'NICK', u'life', u'good', u'mmmm', u'dont', u'want', u'your', u'face', u'what', u'each', u'make', u'flow', u'haha', u'that', u'thah', u'road', u'mahn', u'have', u'ever', u'made', u'NICK', u'PART', u'JOIN', u'PART', u'make', u'sure', u'what', u'good', u'haha', u'have', u'King', u'cold', u'that', u'JOIN', u'JOIN', u'mmmm', u'JOIN', u'here', u'seen', u'JOIN', u'with', u'PART', u'guys', u'work', u'shop', u'PART', u'that', u'just', u'trip', u'when', u'JOIN', u'....', u'some', u'road', u'were', u'JOIN', u'JOIN', u'PART', u'TALK', u'GIRL', u'WHEN', u'HOTT', u'HERE', u'JOIN', u'PART', u'good', u'soup', u'PART', u'JOIN', u'time', u'live', u'6:51', u'PART', u'from', u'here', u'here', u'take', u'girl', u'shes', u'more', u'real', u'JOIN', u'work', u'caps', u'live', u'9.53', u'tyvm', u'lmao', u'PART', u'PART', u'chat', u'with', u'PART', u'back', u'PART', u'PART', u'what', u'here', u'yeah', u'PART', u'what', u'yeah', u'only', u'yeah', u'nice', u'JOIN', u'heya', u'ltns', u'PART', u'yeah', u'life', u'know', u'yeah', u'JOIN', u'done', u'sooo', u'hope', u'sure', u'hell', u'aint', u'JOIN', u'need', u'have', u'work', u'hard', u'just', u'that', u'PART', u'Mine', u'PART', u'have', u'have', u'that', u'dont', u'need', u'vega', u'....', u'hell', u'JOIN', u'JOIN', u'JOIN', u'been', u'gone', u'long', u'does', u'many', u'pigs', u'lmao', u'from', u'than', u'....', u'####', u'were', u'here', u'JOIN', u'JOIN', u'....', u'case', u'read', u'JOIN', u'lmao', u'what', u'PART', u'dont', u'have', u'know', u'read', u'nice', u'JOIN', u'PART', u'long', u'read', u'STOP', u'room', u'then', u'JOIN', u'JOIN', u'PART', u'king', u'find', u'some', u'fast', u'easy', u'food', u'poof', u'PART', u'PART', u'PART', u'JOIN', u'sure', u'sexy', u'want', u'chat', u'good', u'like', u'that', u'JOIN', u'PART', u'that', u'JOIN', u'Yeah', u'grrr', u'take', u'back', u'NICK', u'more', u'this', u'will', u'work', u'just', u'know', u'from', u'want', u'mean', u'PART', u'them', u'JOIN', u'mean', u'like', u'JOIN', u'PART', u'PART', u'....', u'more', u'like', u'PART', u'what', u'JOIN', u'PART', u'just', u'PART', u'PART', u'PART', u'JOIN', u'JOIN', u'love', u'when', u'what', u'....', u'JOIN', u'hehe', u'they', u'know', u'NICK', u'well', u'what', u'true', u'JOIN', u'down', u'here', u'JOIN', u'PART', u'Well', u'only', u'much', u'PART', u'JOIN', u'PART', u'they', u'PART', u'like', u'JOIN', u'JOIN', u'what', u'JOIN', u'only', u'when', u'down', u'NICK', u'that', u'Nova', u'even', u'when', u'down', u'....', u'damn', u'JOIN', u'PART', u'hiya', u'nope', u'JOIN', u'PART', u'mofo', u'JOIN', u'here', u'soon', u'only', u'hate', u'wont', u'know', u'PART', u'JOIN', u'heya', u'ltns', u'know', u'yeah', u'well', u'PART', u'JOIN', u'PART', u'yeah', u'like', u'that', u'PART', u'back', u'nice', u'know', u'PART', u'dont', u'feel', u'feel', u'JOIN', u'like', u'that', u'much', u'....', u'took', u'care', u'PART', u'PART', u'JOIN', u'Ohhh', u'nice', u'know', u'room', u'hate', u'JOIN', u'PART', u'Yeah', u'real', u'flaw', u'....', u'PART', u'head', u'PART', u'PART', u'....', u'like', u'flaw', u'JOIN', u'make', u'look', u'your', u'your', u'look', u'Holy', u'crap', u'that', u'line', u'....', u'much', u'dead', u'....', u'That', u'good', u'JOIN', u'JOIN', u'PART', u'JOIN', u'Yeah', u'well', u'good', u'like', u'that', u'....', u'PART', u'PART', u'U101', u'PART', u'NICK', u'JOIN', u'what', u'that', u'JOIN', u'fast', u'hiya', u'U100', u'what', u'part', u'PART', u'JOIN', u'PART', u'PART', u'JOIN', u'back', u'nick', u'PART', u'want', u'chat', u'help', u'then', u'!!!!', u'love', u'JOIN', u'PART', u'JOIN', u'sips', u'love', u'PART', u'they', u'more', u'like', u'JOIN', u'that', u'PART', u'clay', u'stay', u'late', u'have', u'None', u'here', u'Male', u'only', u'room', u'just', u'your', u'luck', u'....', u'JOIN', u'PART', u'told', u'call', u'JOIN', u'here', u'Ahhh', u'full', u'....', u'much', u'come', u'back', u'that', u'call', u'Sure', u'....', u'down', u'till', u'this', u'PART', u'PART', u'PART', u'PART', u'told', u'JOIN', u'Well', u'here', u'dont', u'have', u'lmao', u'told', u'call', u'PART', u'have', u'PART', u'JOIN', u'JOIN', u'Well', u'call', u'when', u'want', u'PART', u'nice', u'fire', u'JOIN', u'aunt', u'well', u'that', u'PART', u'call', u'want', u'hear', u'that', u'from', u'PART', u'hope', u'gets', u'know', u'much', u'like', u'that', u'PART', u'JOIN', u'aunt', u'here', u'back', u'bacl', u'LMAO', u'PART', u'!!!!', u'keep', u'JOIN', u'know', u'JOIN', u'They', u'want', u'body', u'back', u'here', u'PART', u'dont', u'many', u'awww', u'PART', u'hard', u'JOIN', u'cool', u'PART', u'this', u'song', u'that', u'song', u'head', u'just', u'that', u'last', u'they', u'than', u'slap', u'that', u'that', u'JOIN', u'need', u'some', u'JOIN', u'here', u'song', u'that', u'akon', u'JOIN', u'oops', u'<---', u'JOIN', u'PART', u'JOIN', u'just', u'alot', u'PART', u'PART', u'PART', u'yoll', u'JOIN', u'PART', u'JOIN', u'JOIN', u'!!!!', u'PART', u'JOIN', u'U114', u'U114', u'U114', u'MODE', u'U114', u'PART', u'PART', u'goes', u'boom', u'chat', u'type', u'PART', u'here', u'your', u'line', u'JOIN', u'they', u'have', u'good', u'News', u'Maps', u'more', u'even', u'more', u'love', u'shit', u'crap', u'What', u'heck', u'lawl', u'PART', u'PART', u'JOIN', u'When', u'JOIN', u'PART', u'page', u'here', u'Okay', u'real', u'PART', u'Yeah', u'PART', u'JOIN', u'PART', u'some', u'PART', u'sick', u'JOIN', u'Tiff', u'wazz', u'from', u'Chop', u'wazz', u'from', u'PART', u'JOIN', u'toes', u'DAMN', u'JOIN', u'What', u'toes', u'here', u'TYPR', u'them', u'poll', u'PART', u'toes', u'then', u'them', u'boed', u'JOIN', u'PART', u'Dude', u'some', u'that', u'PART', u'JOIN', u'food', u'back', u'JOIN', u'U122', u'with', u'chat', u'PART', u'PART', u'Does', u'here', u'know', u'U120', u'PART', u'PART', u'JOIN', u'JOIN', u'know', u'rock', u'PART', u'When', u'show', u'chat', u'PART', u'U122', u'with', u'both', u'have', u'same', u'does', u'chat', u'PART', u'JOIN', u'U122', u'U120', u'pwns', u'with', u'bare', u'life', u'PART', u'JOIN', u'love', u'life', u'also', u'life', u'good', u'Very', u'good', u'U120', u'real', u'real', u'here', u'real', u'from', u'chat', u'PART', u'JOIN', u'PART', u'hate', u'U122', u'that', u'dont', u'mind', u'guys', u'good', u'Good', u'Okay', u'love', u'when', u'hate', u'JOIN', u'JOIN', u'U122', u'with', u'need', u'love', u'when', u'chat', u'like', u'U122', u'else', u'U121', u'PART', u'PART', u'guys', u'want', u'talk', u'want', u'talk', u'with', u'PART', u'PART', u'JOIN', u'Food', u'chat', u'name', u'PART', u'your', u'chat', u'JOIN', u'come', u'come', u'into', u'well', u'must', u'JOIN', u'JOIN', u'PART', u'PART', u'have', u'JOIN', u'guys', u'want', u'chat', u'damn', u'feet', u'PART', u'chat', u'only', u'PART', u'JOIN', u'love', u'more', u'chat', u'PART', u'JOIN', u'JOIN', u'JOIN', u'JOIN', u'PART', u'JOIN', u'PART', u'PART', u'JOIN', u'JOIN', u'PART', u'chat', u'well', u'talk', u'JOIN', u'guys', u'talk', u'with', u'from', u'were', u'sexi', u'bois', u'JOIN', u'JOIN', u'JOIN', u'talk', u'JOIN', u'JOIN', u'JOIN', u'PART', u'here', u'JOIN', u'JOIN', u'JOIN', u'JOIN', u'JOIN', u'chat', u'chat', u'U144', u'PART', u'U136', u'chat', u'PART', u'U142', u'KNOW', u'GUYS', u'THAT', u'HAVE', u'NONE', u'YALL', u'EVEN', u'SEEN', u'NONE', u'WILL', u'HAVE', u'YOUR', u'COME', u'FACE', u'THAT', u'JUST', u'YOUR', u'want', u'talk', u'what', u'they', u'want', u'PART', u'JOIN', u'huge', u'Lmao', u'JOIN', u'down', u'caps', u'suck', u'PART', u'Kids', u'PART', u'PART', u'JOIN', u'PART', u'PART', u'guys', u'PART', u'PART', u'PART', u'JOIN', u'sure', u'dead', u'here', u'JOIN', u'6:41', u'JOIN', u'this', u'just', u'bied', u'self', u'JOIN', u'talk', u'PART', u'6:53', u'JOIN', u'chat', u'guys', u'wana', u'talk', u'girl', u'guys', u'JOIN', u'dont', u'U148', u'talk', u'take', u'PART', u'PART', u'JOIN', u'PART', u'JOIN', u'PART', u'JOIN', u'good', u'room', u'JOIN', u'JOIN', u'PART', u'JOIN', u'come', u'like', u'yall', u'They', u'have', u'JOIN', u'U156', u'need', u'U117', u'U117', u'JOIN', u'U149', u'JOIN', u'JOIN', u'this', u'room', u'U153', u'must', u'U117', u'what', u'here', u'chat', u'7:45', u'like', u'U153', u'PART', u'U153', u'PART', u'JOIN', u'PART', u'will', u'this', u'any1', u'ever', u'hear', u'JOIN', u'that', u'move', u'into', u'same', u'room', u'U117', u'only', u'half', u'here', u'PART', u'good', u'need', u'soft', u'PART', u'JOIN', u'JOIN', u'then', u'JOIN', u'game', u'talk', u'here', u'JOIN', u'whos', u'game', u'guys', u'have', u'chat', u'chat', u'with', u'pics', u'want', u'read', u'JOIN', u'JOIN', u'same', u'like', u'JOIN', u'PART', u'argh', u'Uhhh', u'PART', u'that', u'game', u'guys', u'talk', u'tenn', u'hour', u'half', u'pure', u'like', u'fool', u'chat', u'JOIN', u'know', u'lawl', u'JOIN', u'PART', u'JOIN', u'U156', u'JOIN', u'U168', u'PART', u'JOIN', u'wazz', u'chat', u'many', u'does', u'PART', u'JOIN', u'JOIN', u'here', u'over', u'chat', u'PART', u'JOIN', u'PART', u'JOIN', u'chat', u'with', u'sits', u'rubs', u'chat', u'need', u'PART', u'JOIN', u'Lime', u'Song', u'your', u'your', u'song', u'PART', u'JOIN', u'guys', u'only', u'PART', u'talk', u'girl', u'JOIN', u'chat', u'U172', u'PART', u'talk', u'well', u'evil', u'PART', u'JOIN', u'chat', u'JOIN', u'PART', u'U164', u'PART', u'PART', u'what', u'hell', u'PART', u'PART', u'with', u'here', u'yeah', u'JOIN', u'PART', u'pics', u'chat', u'JOIN', u'hott', u'wana', u'with', u'know', u'U150', u'many', u'have', u'JOIN', u'PART', u'JOIN', u'PART', u'JOIN', u'JOIN', u'kool', u'PART', u'lmao', u'with', u'word', u'well', u'PART', u'PART', u'Lime', u'Song', u'dont', u'send', u'JOIN', u'JOIN', u'time', u'PART', u'JOIN', u'JOIN', u'U181', u'????', u'PART', u'JOIN', u'babe', u'PART', u'look', u'like', u'dont', u'chat', u'PART', u'gone', u'PART', u'PART', u'JOIN', u'PART', u'PART', u'PART', u'that', u'them', u'know', u'PART', u'JOIN', u'JOIN', u'PART', u'PART', u'PART', u'this', u'room', u'PART', u'PART', u'Lime', u'Song', u'PART', u'JOIN', u'JOIN', u'PART', u'JOIN', u'PART', u'PART', u'PART', u'PART', u'gals', u'PART', u'JOIN', u'woah', u'holy', u'mary', u'ussy', u'U104', u'Tisk', u'Tisk', u'JOIN', u'U190', u'tisk', u'tisk', u'NICK', u'Lime', u'Song', u'your', u'JOIN', u'JOIN', u'U104', u'U190', u'JOIN', u'What', u'what', u'JOIN', u'????', u'were', u'what', u'girl', u'same', u'girl', u'chat', u'JOIN', u'PART', u'PART', u'JOIN', u'JOIN', u'JOIN', u'JOIN', u'pics', u'chat', u'here', u'have', u'tell', u'JOIN', u'Lmao', u'knew', u'need', u'talk', u'PART', u'PART', u'knew', u'need', u'want', u'heya', u'tiff', u'JOIN', u'MODE', u'just', u'want', u'JOIN', u'Heys', u'U104', u'JOIN', u'JOIN', u'JOIN', u'U197', u'have', u'U197', u'JOIN', u'U156', u'U104', u'PART', u'U197', u'what', u'U122', u'guys', u'chat', u"<3's", u'over', u'U197', u'Lime', u'Song', u'U197', u'soon', u'name', u'list', u'JOIN', u'JOIN', u'JOIN', u'room', u'JOIN', u'PART', u'PART', u'PART', u'JOIN', u'chat', u'JOIN', u'lmao', u'PART', u'JOIN', u'PART', u'PART', u'U122', u'girl', u'chat', u'JOIN', u'MODE', u'lets', u'chat', u'lisa', u'seen', u'U819', u'U819', u'U819', u'U819', u'Last', u'seen', u'days', u'hour', u'JOIN', u'PART', u'JOIN', u'PART', u'PART', u'JOIN', u'PART', u'JOIN', u'yall', u'JOIN', u'seen', u'U820', u'U820', u'U820', u'U820', u'Last', u'seen', u'PART', u'PART', u'JOIN', u'chat', u'very', u'swim', u'brwn', u'hair', u'butt', u'some', u'chat', u'U156', u'JOIN', u'fine', u'hurr', u'find', u'Were', u'JOIN', u'U197', u'that', u'know']
>>> set([w for w in text5 if len(w)==4])
set([u'fawk', u'NAME', u'1200', u'hint', u'Nooo', u'ouch', u'four', u'luvs', u'disc', u'Take', u'skin', u'bomb', u'vega', u'hate', u'hmmm', u'9:10', u'fits', u'pope', u'zone', u'meds', u'imma', u'COME', u'hump', u':o *', u'U181', u'laid', u'send', u'ciao', u'tail', u'bike', u'hola', u'humm', u'lord', u'Song', u'sent', u'WHOA', u'cyas', u'kent', u'jerk', u'song', u'very', u'7:45', u'WHEN', u'Teck', u'45.5', u'jack', u'Elev', u'fall', u'elle', u'JOIN', u'eeek', u'cool', u'Rang', u'U163', u'LAst', u'U165', u'Just', u'U168', u'U169', u'1996', u'list', u'NTMN', u'WILL', u'sang', u'sand', u'Does', u'prep', u'oooh', u'U190', u'anal', u'Here', u'yall', u'slow', u'pork', u'says', u'pasa', u'porn', u'sigh', u"ex's", u'None', u'crop', u'sign', u'jump', u'Only', u'cost', u'roof', u'pass', u'ummm', u'sayn', u'haaa', u'hick', u'even', u'kmph', u'what', u'hide', u'ssid', u'wide', u'cast', u'nana', u'feat', u'dirt', u'9.53', u'addy', u'ltnc', u'cell', u'haze', u'daft', u'goes', u'Boyz', u'tips', u'ever', u'bird', u'told', u'junk', u'aint', u'Rush', u'full', u'coem', u'toke', u'here', u'ELSE', u'scum', u'mkay', u'sexs', u'sext', u'sink', u'nawp', u'sexy', u'<---', u'dork', u'wait', u'kids', u'News', u'Ctrl', u'tlak', u'heee', u'Back', u'herE', u'pics', u'orta', u'Kold', u'MRIs', u'pick', u'Home', u'>:->', u'king', u'love', u'64.8', u'hail', u'limp', u'smax', u'When', u'ROFL', u'offa', u'hogs', u'giva', u'Evil', u'VVil', u'gosh', u'1900', u'Nice', u'plow', u'john', u'crap', u'Oops', u'army', u'deop', u"PM's", u'dude', u'arms', u'next', u'cali', u'live', u'call', u'perv', u'typo', u'ahhh', u'2DAY', u'thru', u'type', u'tell', u'more', u'sort', u'flaw', u'babe', u'holy', u'club', u'hurr', u'haha', u'Rule', u'hurt', u'Chop', u'sore', u'warm', u',,,,', u'hgey', u'Time', u'baby', u'pmsl', u'z-ro', u'hold', u'sori', u'glad', u'must', u'town', u'QUIT', u'none', u'word', u'room', u'hour', u'givs', u'this', u'Tiff', u'ride', u'work', u'worl', u'soul', u'pour', u'Down', u'Lies', u'fock', u'Yoko', u'meet', u'male', u'root', u'Your', u'6:53', u'Male', u'6:51', u'wana', u'slip', u'give', u'YALL', u'chip', u'benz', u'fuck', u'chit', u'lol.', u'high', u'chik', u'Kiss', u'bend', u'want', u'Lord', u'scar', u'Maps', u'YOUR', u'rape', u'pink', u'HUGE', u'lame', u'pine', u'U132', u'U520', u'till', u'nuff', u'U139', u'hugs', u'U137', u'U136', u'U134', u'U133', u'syck', u'U130', u'hmph', u'U988', u'U989', u'okay', u'huge', u'mess', u'soda', u'spot', u'hong', u'Will', u'fart', u'wOOt', u'pigs', u'guyz', u'numb', u'date', u'such', u'suck', u'guys', u'Joey', u'hawT', u'neck', u'beam', u'coat', u'eats', u'Deep', u'meat', u'CALI', u'jail', u'road', u'tall', u'AWAY', u'talk', u'wine', u'cute', u'What', u'dojn', u'AKDT', u'help', u'Stop', u'over', u'move', u'sooo', u'soon', u'Same', u'kong', u'cook', u'isnt', u'1.98', u'1.99', u'hell', u'cold', u'WITH', u'Hero', u'18ST', u'allo', u'frst', u'thnx', u'LONG', u'late', u'eeww', u'cepn', u'bout', u'main', u'tory', u'Away', u'ally', u'poop', u'then', u'them', u'good', u'pure', u'gooo', u'docs', u'bein', u'U138', u'band', u'GrlZ', u'they', u'half', u'nads', u'mahn', u'GUYS', u'hall', u'halo', u'wont', u'term', u'name', u'hook', u'Came', u'tere', u'drop', u'Rofl', u'boed', u'hazy', u'mode', u'rock', u'went', u'Liam', u'bong', u'whou', u'bone', u'mean', u'DING', u'hank', u'GIRL', u'From', u'OOPS', u'U820', u'fish', u'hard', u'SOME', u'yeah', u'bois', u'ussy', u'Live', u'ball', u'hooo', u'yeas', u'year', u'hawt', u'girl', u'Save', u'cums', u'whip', u'Room', u'yes.', u'waaa', u'U170', u'((((', u'U175', u'yout', u'hehe', u'Haha', u'thot', u'39.3', u'Dood', u'wazz', u'hill', u'nite', u'okey', u'Hold', u'akon', u'Cool', u'shut', u'U147', u'shup', u'Wyte', u'This', u'cars', u'team', u'dman', u'free', u'argh', u'Judy', u'base', u'icky', u'evil', u'lisa', u'Okay', u'weed', u'Meep', u'card', u'care', u'raed', u'opps', u'yard', u'yesh', u'100%', u'days', u'keep', u'turn', u'heck', u'Chat', u'TIME', u'Ummm', u'loud', u'ooer', u'Even', u'rang', u'thje', u'LoVe', u'dont', u'feel', u'sock', u'crib', u'xmas', u'feet', u'wash', u'dint', u'done', u'fast', u'CHAT', u'Hugs', u'vote', u'Prof', u'ring', u'ways', u'miss', u'size', u'city', u'hott', u'hots', u'dump', u'bite', u'Dude', u'mami', u'!...', u'mama', u'kewl', u'legs', u'mame', u'dogs', u'soup', u't he', u'U164', u'eyes', u'gear', u'that', u'tooo', u'2:55', u'park', u'took', u'HERE', u'mmmm', u'cops', u'part', u'febe', u'Long', u'toop', u'butt', u'rain', u'thah', u'than', u'Road', u'gret', u'past', u'kind', u'hiya', u'Love', u'lmao', u'kina', u'ebay', u'serg', u'orgy', u'2Pac', u'were', u'dang', u'bare', u'10th', u'Rick', u'este', u'lick', u'piff', u'gals', u'seth', u'brwn', u'yeee', u'mine', u'slap', u'bugs', u'Jane', u'seee', u'slam', u'rent', u'have', u'need', u'seen', u'seem', u'mins', u'U158', u'sell', u'Then', u'tyvm', u'John', u'trip', u'self', u'able', u'snow', u'note', u'also', u'sexi', u'take', u'They', u'barn', u'noth', u'buff', u'surf', u'blue', u'play', u'sure', u'pain', u'"...', u'doin', u'Drop', u'HAHA', u'NONE', u'paid', u'most', u'aime', u'wire', u'plan', u'mofo', u'pair', u'knee', u'Bone', u'wats', u'lawl', u'GOOD', u'cams', u'phil', u'wore', u'salt', u'Nova', u'face', u'High', u'NICK', u'U108', u'U109', u'aunt', u'wind', u'Slip', u'teck', u'U102', u'U103', u'U100', u'U101', u'U106', u'U107', u'came', u'U105', u'shop', u'Matt', u'golf', u'Need', u'gold', u'show', u'ltns', u'Hill', u'Kent', u'TEXT', u'fear', u'fine', u'find', u'Poor', u'busy', u'ages', u'true', u'dick', u'bust', u'woof', u'LIVE', u'wood', u'tape', u'York', u'rich', u'wooo', u'mena', u'hope', u'U219', u'geez', u'lyin', u'gees', u'stop', u'Days', u'bear', u'yawn', u'Turn', u'awww', u'ones', u'sum1', u'SExy', u'gray', u'runs', u'Help', u'pimp', u'pfft', u'Over', u'lala', u'guns', u'rofl', u'; ..', u'ohio', u'Gosh', u'hiom', u'CAPS', u'ears', u'body', u'blew', u'Hott', u'fair', u'gawd', u'Very', u'Reub', u'seat', u'!!!!', u'toes', u'dumb', u'sean', u'jude', u'sips', u'Kewl', u'ladz', u'Hiya', u'jush', u'best', u'!!!.', u'yada', u'said', u'Iowa', u'ROOM', u'gags', u'That', u'lots', u'Nope', u'away', u'amen', u'ohwa', u'Rock', u'tend', u'))))', u'caan', u'wean', u'bied', u'mono', u'nope', u'grea', u'grin', u'blow', u'lazy', u'n9ne', u'Lmao', u'kool', u'U542', u'comp', u'flow', u'boss', u'City', u'gays', u'otay', u'drew', u'Werd', u'Were', u'Dang', u'U111', u'newp', u'herd', u'come', u'duet', u'HALO', u'pull', u'both', u'hits', u'wuts', u'last', u'U113', u'U148', u'brat', u'U146', u'many', u'U144', u'Hard', u'o.k.', u'nawt', u'drug', u'U141', u'pray', u'asss', u'alot', u'brad', u'swim', u'<<<<', u'Dawn', u'Lime', u'wubs', u'wear', u'vent', u'guts', u'U154', u'bell', u'wall', u"<3's", u'6:38', u'walk', u'lapd', u'twin', u'cmon', u'anti', u'Drew', u'THEY', u'sing', u'poll', u'U819', u"ok'd", u'quit', u'Sure', u'puts', u"it's", u'bloe', u'been', u'mark', u'VBox', u'beer', u'much', u'damn', u'SSRI', u'Sexy', u'byes', u'whoa', u'TALK', u'tjhe', u'U156', u'mike', u'spit', u'fire', u'mind', u'King', u'Phil', u'else', u'??!!', u'U114', u'rubs', u'bull', u'spin', u'dotn', u'firs', u'JUST', u'case', u'Cute', u'lool', u'wins', u'look', u'3:45', u'woah', u'THAT', u'TYPR', u'ahah', u'cash', u'heya', u'will', u'ugly', u'near', u'abou', u'heyy', u'wild', u'mauh', u'cock', u'scuk', u'MORE', u'fool', u'adds', u'Fade', u'Kick', u'goof', u'U142', u'Good', u'cuss', u'U143', u'lust', u'blah', u'cant', u'Kids', u'Hail', u'SEEN', u'sits', u'Tell', u'gimp', u'Eyes', u'samn', u'open', u'Born', u'make', u'Uhhh', u'bowl', u'Seee', u'same', u'nerd', u'food', u'MODE', u'inch', u'gets', u'nada', u'MUAH', u'week', u'used', u'ello', u'urls', u'itch', u'keys', u'mang', u'hang', u'Pour', u'hand', u'####', u'uses', u'puke', u'puff', u'dust', u'ruff', u'tune', u'moms', u'hows', u'safe', u'HOTT', u'kept', u'tthe', u'howz', u'well', u'Mine', u'Tide', u'Food', u'acid', u'oops', u'Have', u'sets', u'owww', u'Girl', u'LOUD', u'howl', u'left', u'woot', u'lube', u'kiss', u'just', u"pm's", u'boot', u'rest', u'wrek', u'????', u'foot', u'PART', u'kill', u'HAVE', u'vamp', u"pm'n", u'waht', u'U118', u'ewww', u'U115', u'Paul', u'U117', u'U116', u'PMSL', u'U110', u'ghet', u'U112', u'rose', u'Eggs', u'jeff', u'U119', u'lake', u'knew', u'ther', u'twit', u'lets', u'1299', u'Talk', u'easy', u'ohhh', u'!???', u'joke', u'kick', u'boom', u'real', u'Last', u'tits', u'read', u'Mono', u'98.6', u'O.k.', u'caps', u'dark', u'game', u'five', u'know', u'tick', u'lady', u'pies', u'Wind', u'ahem', u'loss', u'like', u'lost', u'Show', u'nude', u'clay', u'saME', u'xbox', u'LATE', u'Troy', u'DOES', u'nose', u'lose', u'tart', u'soft', u'page', u'clap', u'KNOW', u'tisk', u'<333', u'deal', u'doll', u'yoll', u'West', u'bacl', u'fake', u'deaf', u'back', u'dead', u'Holy', u'hair', u'born', u'kold', u'Damn', u'shes', u'Tina', u'Ahhh', u'dear', u'home', u'<~~~', u'any1', u'FINE', u'Mary', u'EVEN', u'quiz', u'Life', u'outs', u'LMAO', u'lead', u'bred', u'U196', u'moon', u'outa', u'Awww', u'does', u'exit', u'U197', u'prob', u'U149', u'enuf', u'peek', u'grrr', u'Look', u'peel', u'poem', u'corn', u'each', u'Heya', u'1930', u'burp', u'Ruth', u'Heyy', u'from', u'post', u'mite', u'grrl', u'yoko', u'SIZE', u'choc', u'?!?!', u'asks', u'KoOL', u'jeep', u'ribs', u'Elle', u'http', u'side', u'perk', u'Lion', u'plus', u'west', u'luck', u'out.', u'rats', u'tock', u'Ohio', u'tiff', u'into', u'STOP', u'lois', u'down', u'lies', u'lung', u"yw's", u'wrap', u"RN's", u'whos', u'your', u'DONT', u'east', u'wack', u'1985', u'span', u'1980', u'area', u'U150', u'U153', u'U155', u'gift', u'long', u'Hand', u'4:03', u'uyes', u'whoo', u'died', u'U145', u'DAMN', u'grew', u'Come', u'spat', u'calm', u'babi', u'6:41', u'head', u'only', u'form', u'some', u'heal', u'.op.', u'Well', u'idea', u'boys', u'heat', u'hiii', u'hear', u'Been', u'beat', u'FROM', u'line', u'with', u'AKST', u'rush', u'made', u'Sat.', u'temp', u'wish', u'....', u'whys', u'tenn', u'mary', u'Tisk', u'dawg', u'U128', u'U129', u'site', u'U126', u'Care', u'U120', u'U121', u'U122', u'U123', u'gone', u'ques', u'toss', u'life', u'deep', u'Lets', u'cure', u'dyed', u'chat', u'Ohhh', u'door', u'FACE', u'eric', u'shit', u'Swim', u'Heys', u'Type', u'shot', u'when', u'Fort', u'menu', u'wher', u'nick', u'book', u'98.5', u'whew', u'sick', u'ogan', u'test', u'mass', u'roll', u'nice', u'poor', u'draw', u'star', u'Like', u'poot', u'U172', u'pwns', u'dies', u'1cos', u'felt', u'.. .', u'stay', u'evah', u'poof', u'nods', u'4.20', u'clue', u'pool', u'goin', u'land', u'yess', u'wife', u'idnt', u'Yeah', u'rule', u'Jess', u'2006', u'U104', u'whud', u'time', u'push', u'caca', u'yell', u'once'])
>>> fdist1 = FreqDist([w for w in text5 if len(w)==4])
>>> voc1 = fdist1.keys()
>>> voc1
[u'fawk', u'NAME', u'1200', u'hint', u'Nooo', u'ouch', u'four', u'luvs', u'disc', u'Take', u'skin', u'bomb', u'vega', u'hate', u'hmmm', u'9:10', u'fits', u'pope', u'zone', u'meds', u'imma', u'COME', u'hump', u':o *', u'U181', u'laid', u'send', u'ciao', u'tail', u'bike', u'hola', u'humm', u'lord', u'Song', u'sent', u'WHOA', u'cyas', u'kent', u'jerk', u'song', u'very', u'7:45', u'WHEN', u'Teck', u'45.5', u'jack', u'Elev', u'fall', u'elle', u'JOIN', u'eeek', u'cool', u'Rang', u'U163', u'LAst', u'U165', u'Just', u'U168', u'U169', u'1996', u'list', u'NTMN', u'WILL', u'sang', u'sand', u'Does', u'prep', u'oooh', u'U190', u'anal', u'Here', u'yall', u'slow', u'pork', u'says', u'pasa', u'porn', u'sigh', u"ex's", u'None', u'crop', u'sign', u'jump', u'Only', u'cost', u'roof', u'pass', u'ummm', u'sayn', u'haaa', u'hick', u'even', u'kmph', u'what', u'hide', u'ssid', u'wide', u'cast', u'nana', u'feat', u'dirt', u'9.53', u'addy', u'ltnc', u'cell', u'haze', u'daft', u'goes', u'Boyz', u'tips', u'ever', u'bird', u'told', u'junk', u'aint', u'Rush', u'full', u'coem', u'toke', u'here', u'ELSE', u'scum', u'mkay', u'sexs', u'sext', u'sink', u'nawp', u'sexy', u'<---', u'dork', u'wait', u'kids', u'News', u'Ctrl', u'tlak', u'heee', u'Back', u'herE', u'pics', u'orta', u'Kold', u'MRIs', u'pick', u'Home', u'>:->', u'king', u'love', u'64.8', u'hail', u'limp', u'smax', u'When', u'ROFL', u'offa', u'hogs', u'giva', u'Evil', u'VVil', u'gosh', u'1900', u'Nice', u'plow', u'john', u'crap', u'Oops', u'army', u'deop', u"PM's", u'dude', u'arms', u'next', u'cali', u'live', u'call', u'perv', u'typo', u'ahhh', u'2DAY', u'thru', u'type', u'tell', u'more', u'sort', u'flaw', u'babe', u'holy', u'club', u'hurr', u'haha', u'Rule', u'hurt', u'Chop', u'sore', u'warm', u',,,,', u'hgey', u'Time', u'baby', u'pmsl', u'z-ro', u'hold', u'sori', u'glad', u'must', u'town', u'QUIT', u'none', u'word', u'room', u'hour', u'givs', u'this', u'Tiff', u'ride', u'work', u'worl', u'soul', u'pour', u'Down', u'Lies', u'fock', u'Yoko', u'meet', u'male', u'root', u'Your', u'6:53', u'Male', u'6:51', u'wana', u'slip', u'give', u'YALL', u'chip', u'benz', u'fuck', u'chit', u'lol.', u'high', u'chik', u'Kiss', u'bend', u'want', u'Lord', u'scar', u'Maps', u'YOUR', u'rape', u'pink', u'HUGE', u'lame', u'pine', u'U132', u'U520', u'till', u'nuff', u'U139', u'hugs', u'U137', u'U136', u'U134', u'U133', u'syck', u'U130', u'hmph', u'U988', u'U989', u'okay', u'huge', u'mess', u'soda', u'spot', u'hong', u'Will', u'fart', u'wOOt', u'pigs', u'guyz', u'numb', u'date', u'such', u'suck', u'guys', u'Joey', u'hawT', u'neck', u'beam', u'coat', u'eats', u'Deep', u'meat', u'CALI', u'jail', u'road', u'tall', u'AWAY', u'talk', u'wine', u'cute', u'What', u'dojn', u'AKDT', u'help', u'Stop', u'over', u'move', u'sooo', u'soon', u'Same', u'kong', u'cook', u'isnt', u'1.98', u'1.99', u'hell', u'cold', u'WITH', u'Hero', u'18ST', u'allo', u'frst', u'thnx', u'LONG', u'late', u'eeww', u'cepn', u'bout', u'main', u'tory', u'Away', u'ally', u'poop', u'then', u'them', u'good', u'pure', u'gooo', u'docs', u'bein', u'U138', u'band', u'GrlZ', u'they', u'half', u'nads', u'mahn', u'GUYS', u'hall', u'halo', u'wont', u'term', u'name', u'hook', u'Came', u'tere', u'drop', u'Rofl', u'boed', u'hazy', u'mode', u'rock', u'went', u'Liam', u'bong', u'whou', u'bone', u'mean', u'DING', u'hank', u'GIRL', u'From', u'OOPS', u'U820', u'fish', u'hard', u'SOME', u'yeah', u'bois', u'ussy', u'Live', u'ball', u'hooo', u'yeas', u'year', u'hawt', u'girl', u'Save', u'cums', u'whip', u'Room', u'yes.', u'waaa', u'U170', u'((((', u'U175', u'yout', u'hehe', u'Haha', u'thot', u'39.3', u'Dood', u'wazz', u'hill', u'nite', u'okey', u'Hold', u'akon', u'Cool', u'shut', u'U147', u'shup', u'Wyte', u'This', u'cars', u'team', u'dman', u'free', u'argh', u'Judy', u'base', u'icky', u'evil', u'lisa', u'Okay', u'weed', u'Meep', u'card', u'care', u'raed', u'opps', u'yard', u'yesh', u'100%', u'days', u'keep', u'turn', u'heck', u'Chat', u'TIME', u'Ummm', u'loud', u'ooer', u'Even', u'rang', u'thje', u'LoVe', u'dont', u'feel', u'sock', u'crib', u'xmas', u'feet', u'wash', u'dint', u'done', u'fast', u'CHAT', u'Hugs', u'vote', u'Prof', u'ring', u'ways', u'miss', u'size', u'city', u'hott', u'hots', u'dump', u'bite', u'Dude', u'mami', u'!...', u'mama', u'kewl', u'legs', u'mame', u'dogs', u'soup', u't he', u'U164', u'eyes', u'gear', u'that', u'tooo', u'2:55', u'park', u'took', u'HERE', u'mmmm', u'cops', u'part', u'febe', u'Long', u'toop', u'butt', u'rain', u'thah', u'than', u'Road', u'gret', u'past', u'kind', u'hiya', u'Love', u'lmao', u'kina', u'ebay', u'serg', u'orgy', u'2Pac', u'were', u'dang', u'bare', u'10th', u'Rick', u'este', u'lick', u'piff', u'gals', u'seth', u'brwn', u'yeee', u'mine', u'slap', u'bugs', u'Jane', u'seee', u'slam', u'rent', u'have', u'need', u'seen', u'seem', u'mins', u'U158', u'sell', u'Then', u'tyvm', u'John', u'trip', u'self', u'able', u'snow', u'note', u'also', u'sexi', u'take', u'They', u'barn', u'noth', u'buff', u'surf', u'blue', u'play', u'sure', u'pain', u'"...', u'doin', u'Drop', u'HAHA', u'NONE', u'paid', u'most', u'aime', u'wire', u'plan', u'mofo', u'pair', u'knee', u'Bone', u'wats', u'lawl', u'GOOD', u'cams', u'phil', u'wore', u'salt', u'Nova', u'face', u'High', u'NICK', u'U108', u'U109', u'aunt', u'wind', u'Slip', u'teck', u'U102', u'U103', u'U100', u'U101', u'U106', u'U107', u'came', u'U105', u'shop', u'Matt', u'golf', u'Need', u'gold', u'show', u'ltns', u'Hill', u'Kent', u'TEXT', u'fear', u'fine', u'find', u'Poor', u'busy', u'ages', u'true', u'dick', u'bust', u'woof', u'LIVE', u'wood', u'tape', u'York', u'rich', u'wooo', u'mena', u'hope', u'U219', u'geez', u'lyin', u'gees', u'stop', u'Days', u'bear', u'yawn', u'Turn', u'awww', u'ones', u'sum1', u'SExy', u'gray', u'runs', u'Help', u'pimp', u'pfft', u'Over', u'lala', u'guns', u'rofl', u'; ..', u'ohio', u'Gosh', u'hiom', u'CAPS', u'ears', u'body', u'blew', u'Hott', u'fair', u'gawd', u'Very', u'Reub', u'seat', u'!!!!', u'toes', u'dumb', u'sean', u'jude', u'sips', u'Kewl', u'ladz', u'Hiya', u'jush', u'best', u'!!!.', u'yada', u'said', u'Iowa', u'ROOM', u'gags', u'That', u'lots', u'Nope', u'away', u'amen', u'ohwa', u'Rock', u'tend', u'))))', u'caan', u'wean', u'bied', u'mono', u'nope', u'grea', u'grin', u'blow', u'lazy', u'n9ne', u'Lmao', u'kool', u'U542', u'comp', u'flow', u'boss', u'City', u'gays', u'otay', u'drew', u'Werd', u'Were', u'Dang', u'U111', u'newp', u'herd', u'come', u'duet', u'HALO', u'pull', u'both', u'hits', u'wuts', u'last', u'U113', u'U148', u'brat', u'U146', u'many', u'U144', u'Hard', u'o.k.', u'nawt', u'drug', u'U141', u'pray', u'asss', u'alot', u'brad', u'swim', u'<<<<', u'Dawn', u'Lime', u'wubs', u'wear', u'vent', u'guts', u'U154', u'bell', u'wall', u"<3's", u'6:38', u'walk', u'lapd', u'twin', u'cmon', u'anti', u'Drew', u'THEY', u'sing', u'poll', u'U819', u"ok'd", u'quit', u'Sure', u'puts', u"it's", u'bloe', u'been', u'mark', u'VBox', u'beer', u'much', u'damn', u'SSRI', u'Sexy', u'byes', u'whoa', u'TALK', u'tjhe', u'U156', u'mike', u'spit', u'fire', u'mind', u'King', u'Phil', u'else', u'??!!', u'U114', u'rubs', u'bull', u'spin', u'dotn', u'firs', u'JUST', u'case', u'Cute', u'lool', u'wins', u'look', u'3:45', u'woah', u'THAT', u'TYPR', u'ahah', u'cash', u'heya', u'will', u'ugly', u'near', u'abou', u'heyy', u'wild', u'mauh', u'cock', u'scuk', u'MORE', u'fool', u'adds', u'Fade', u'Kick', u'goof', u'U142', u'Good', u'cuss', u'U143', u'lust', u'blah', u'cant', u'Kids', u'Hail', u'SEEN', u'sits', u'Tell', u'gimp', u'Eyes', u'samn', u'open', u'Born', u'make', u'Uhhh', u'bowl', u'Seee', u'same', u'nerd', u'food', u'MODE', u'inch', u'gets', u'nada', u'MUAH', u'week', u'used', u'ello', u'urls', u'itch', u'keys', u'mang', u'hang', u'Pour', u'hand', u'####', u'uses', u'puke', u'puff', u'dust', u'ruff', u'tune', u'moms', u'hows', u'safe', u'HOTT', u'kept', u'tthe', u'howz', u'well', u'Mine', u'Tide', u'Food', u'acid', u'oops', u'Have', u'sets', u'owww', u'Girl', u'LOUD', u'howl', u'left', u'woot', u'lube', u'kiss', u'just', u"pm's", u'boot', u'rest', u'wrek', u'????', u'foot', u'PART', u'kill', u'HAVE', u'vamp', u"pm'n", u'waht', u'U118', u'ewww', u'U115', u'Paul', u'U117', u'U116', u'PMSL', u'U110', u'ghet', u'U112', u'rose', u'Eggs', u'jeff', u'U119', u'lake', u'knew', u'ther', u'twit', u'lets', u'1299', u'Talk', u'easy', u'ohhh', u'!???', u'joke', u'kick', u'boom', u'real', u'Last', u'tits', u'read', u'Mono', u'98.6', u'O.k.', u'caps', u'dark', u'game', u'five', u'know', u'tick', u'lady', u'pies', u'Wind', u'ahem', u'loss', u'like', u'lost', u'Show', u'nude', u'clay', u'saME', u'xbox', u'LATE', u'Troy', u'DOES', u'nose', u'lose', u'tart', u'soft', u'page', u'clap', u'KNOW', u'tisk', u'<333', u'deal', u'doll', u'yoll', u'West', u'bacl', u'fake', u'deaf', u'back', u'dead', u'Holy', u'hair', u'born', u'kold', u'Damn', u'shes', u'Tina', u'Ahhh', u'dear', u'home', u'<~~~', u'any1', u'FINE', u'Mary', u'EVEN', u'quiz', u'Life', u'outs', u'LMAO', u'lead', u'bred', u'U196', u'moon', u'outa', u'Awww', u'does', u'exit', u'U197', u'prob', u'U149', u'enuf', u'peek', u'grrr', u'Look', u'peel', u'poem', u'corn', u'each', u'Heya', u'1930', u'burp', u'Ruth', u'Heyy', u'from', u'post', u'mite', u'grrl', u'yoko', u'SIZE', u'choc', u'?!?!', u'asks', u'KoOL', u'jeep', u'ribs', u'Elle', u'http', u'side', u'perk', u'Lion', u'plus', u'west', u'luck', u'out.', u'rats', u'tock', u'Ohio', u'tiff', u'into', u'STOP', u'lois', u'down', u'lies', u'lung', u"yw's", u'wrap', u"RN's", u'whos', u'your', u'DONT', u'east', u'wack', u'1985', u'span', u'1980', u'area', u'U150', u'U153', u'U155', u'gift', u'long', u'Hand', u'4:03', u'uyes', u'whoo', u'died', u'U145', u'DAMN', u'grew', u'Come', u'spat', u'calm', u'babi', u'6:41', u'head', u'only', u'form', u'some', u'heal', u'.op.', u'Well', u'idea', u'boys', u'heat', u'hiii', u'hear', u'Been', u'beat', u'FROM', u'line', u'with', u'AKST', u'rush', u'made', u'Sat.', u'temp', u'wish', u'....', u'whys', u'tenn', u'mary', u'Tisk', u'dawg', u'U128', u'U129', u'site', u'U126', u'Care', u'U120', u'U121', u'U122', u'U123', u'gone', u'ques', u'toss', u'life', u'deep', u'Lets', u'cure', u'dyed', u'chat', u'Ohhh', u'door', u'FACE', u'eric', u'shit', u'Swim', u'Heys', u'Type', u'shot', u'when', u'Fort', u'menu', u'wher', u'nick', u'book', u'98.5', u'whew', u'sick', u'ogan', u'test', u'mass', u'roll', u'nice', u'poor', u'draw', u'star', u'Like', u'poot', u'U172', u'pwns', u'dies', u'1cos', u'felt', u'.. .', u'stay', u'evah', u'poof', u'nods', u'4.20', u'clue', u'pool', u'goin', u'land', u'yess', u'wife', u'idnt', u'Yeah', u'rule', u'Jess', u'2006', u'U104', u'whud', u'time', u'push', u'caca', u'yell', u'once']
>>> for w in text6:
	if w.isupper():
		print(w)

		
SCENE
KING
ARTHUR
SOLDIER
ARTHUR
I
SOLDIER
ARTHUR
I
I
SOLDIER
ARTHUR
SOLDIER
ARTHUR
SOLDIER
ARTHUR
SOLDIER
ARTHUR
SOLDIER
ARTHUR
SOLDIER
ARTHUR
SOLDIER
ARTHUR
SOLDIER
A
ARTHUR
SOLDIER
A
ARTHUR
SOLDIER
ARTHUR
SOLDIER
I
ARTHUR
I
SOLDIER
SOLDIER
SOLDIER
I
ARTHUR
SOLDIER
SOLDIER
SOLDIER
SOLDIER
SOLDIER
SOLDIER
SOLDIER
SOLDIER
SCENE
CART
MASTER
CUSTOMER
CART
MASTER
DEAD
PERSON
I
CART
MASTER
CUSTOMER
DEAD
PERSON
I
CART
MASTER
CUSTOMER
DEAD
PERSON
I
CART
MASTER
CUSTOMER
DEAD
PERSON
I
CUSTOMER
CART
MASTER
I
DEAD
PERSON
I
CUSTOMER
CART
MASTER
I
DEAD
PERSON
I
CUSTOMER
CART
MASTER
I
CUSTOMER
CART
MASTER
I
CUSTOMER
CART
MASTER
DEAD
PERSON
I
I
CUSTOMER
DEAD
PERSON
I
I
CUSTOMER
CART
MASTER
CUSTOMER
CART
MASTER
I
CUSTOMER
CART
MASTER
SCENE
ARTHUR
DENNIS
ARTHUR
DENNIS
I
ARTHUR
I
DENNIS
I
I
ARTHUR
I
DENNIS
ARTHUR
I
DENNIS
ARTHUR
I
DENNIS
I
ARTHUR
I
DENNIS
WOMAN
ARTHUR
I
WOMAN
ARTHUR
WOMAN
ARTHUR
I
WOMAN
I
I
DENNIS
A
WOMAN
DENNIS
ARTHUR
I
WOMAN
ARTHUR
WOMAN
ARTHUR
DENNIS
I
ARTHUR
DENNIS
ARTHUR
I
DENNIS
ARTHUR
DENNIS
ARTHUR
I
WOMAN
ARTHUR
I
WOMAN
I
ARTHUR
WOMAN
ARTHUR
I
I
DENNIS
ARTHUR
DENNIS
ARTHUR
DENNIS
I
I
I
ARTHUR
DENNIS
ARTHUR
DENNIS
I
ARTHUR
DENNIS
I
SCENE
BLACK
KNIGHT
BLACK
KNIGHT
GREEN
KNIGHT
BLACK
KNIGHT
GREEN
KNIGHT
BLACK
KNIGHT
BLACK
KNIGHT
GREEN
KNIGHT
GREEN
KNIGHT
BLACK
KNIGHT
GREEN
KNIGHT
BLACK
KNIGHT
ARTHUR
I
I
BLACK
KNIGHT
ARTHUR
BLACK
KNIGHT
ARTHUR
I
I
BLACK
KNIGHT
ARTHUR
I
BLACK
KNIGHT
I
ARTHUR
ARTHUR
BLACK
KNIGHT
ARTHUR
BLACK
KNIGHT
ARTHUR
BLACK
KNIGHT
ARTHUR
A
BLACK
KNIGHT
ARTHUR
BLACK
KNIGHT
I
ARTHUR
BLACK
KNIGHT
ARTHUR
BLACK
KNIGHT
ARTHUR
BLACK
KNIGHT
ARTHUR
BLACK
KNIGHT
ARTHUR
BLACK
KNIGHT
ARTHUR
BLACK
KNIGHT
I
ARTHUR
BLACK
KNIGHT
ARTHUR
BLACK
KNIGHT
ARTHUR
I
ARTHUR
BLACK
KNIGHT
BLACK
KNIGHT
I
ARTHUR
BLACK
KNIGHT
ARTHUR
BLACK
KNIGHT
I
ARTHUR
BLACK
KNIGHT
ARTHUR
BLACK
KNIGHT
BLACK
KNIGHT
ARTHUR
BLACK
KNIGHT
I
I
SCENE
MONKS
CROWD
A
A
A
A
MONKS
CROWD
A
A
A
A
A
A
A
A
A
A
A
A
A
VILLAGER
CROWD
BEDEVERE
VILLAGER
CROWD
BEDEVERE
WITCH
I
I
BEDEVERE
WITCH
CROWD
WITCH
BEDEVERE
VILLAGER
BEDEVERE
VILLAGER
VILLAGER
CROWD
BEDEVERE
VILLAGER
VILLAGER
VILLAGER
VILLAGER
VILLAGERS
VILLAGER
VILLAGER
VILLAGER
VILLAGER
A
VILLAGERS
A
VILLAGER
A
VILLAGER
RANDOM
BEDEVERE
VILLAGER
BEDEVERE
A
VILLAGER
I
VILLAGER
VILLAGER
CROWD
BEDEVERE
VILLAGER
VILLAGER
VILLAGER
CROWD
BEDEVERE
VILLAGER
VILLAGER
CROWD
BEDEVERE
VILLAGER
VILLAGER
VILLAGER
BEDEVERE
VILLAGER
B
BEDEVERE
CROWD
BEDEVERE
VILLAGER
BEDEVERE
VILLAGER
RANDOM
BEDEVERE
VILLAGER
VILLAGER
VILLAGER
CROWD
BEDEVERE
VILLAGER
VILLAGER
VILLAGER
VILLAGER
VILLAGER
VILLAGER
VILLAGER
VILLAGER
VILLAGER
ARTHUR
A
CROWD
BEDEVERE
VILLAGER
BEDEVERE
VILLAGER
A
VILLAGER
A
CROWD
A
A
VILLAGER
BEDEVERE
CROWD
BEDEVERE
CROWD
A
A
A
WITCH
VILLAGER
CROWD
BEDEVERE
ARTHUR
I
BEDEVERE
ARTHUR
BEDEVERE
I
ARTHUR
BEDEVERE
ARTHUR
I
NARRATOR
SCENE
SIR
BEDEVERE
ARTHUR
BEDEVERE
SIR
LAUNCELOT
ARTHUR
SIR
GALAHAD
LAUNCELOT
PATSY
ARTHUR
I
KNIGHTS
PRISONER
KNIGHTS
MAN
I
ARTHUR
KNIGHTS
SCENE
GOD
I
ARTHUR
GOD
I
I
ARTHUR
I
O
GOD
ARTHUR
GOD
ARTHUR
O
GOD
LAUNCELOT
A
A
GALAHAD
SCENE
ARTHUR
FRENCH
GUARD
ARTHUR
FRENCH
GUARD
ARTHUR
FRENCH
GUARD
I
I
ARTHUR
GALAHAD
ARTHUR
FRENCH
GUARD
I
ARTHUR
FRENCH
GUARD
ARTHUR
FRENCH
GUARD
I
I
GALAHAD
FRENCH
GUARD
ARTHUR
FRENCH
GUARD
I
GALAHAD
ARTHUR
FRENCH
GUARD
I
I
GALAHAD
FRENCH
GUARD
I
ARTHUR
I
FRENCH
GUARD
OTHER
FRENCH
GUARD
FRENCH
GUARD
ARTHUR
I
KNIGHTS
ARTHUR
KNIGHTS
FRENCH
GUARD
FRENCH
GUARD
ARTHUR
KNIGHTS
FRENCH
GUARD
FRENCH
GUARDS
LAUNCELOT
I
ARTHUR
BEDEVERE
I
FRENCH
GUARDS
C
A
ARTHUR
BEDEVERE
I
ARTHUR
BEDEVERE
U
I
ARTHUR
BEDEVERE
ARTHUR
KNIGHTS
CRASH
FRENCH
GUARDS
SCENE
VOICE
DIRECTOR
HISTORIAN
KNIGHT
KNIGHT
HISTORIAN
HISTORIAN
S
WIFE
SCENE
NARRATOR
MINSTREL
O
SIR
ROBIN
DENNIS
WOMAN
ALL
HEADS
MINSTREL
ROBIN
I
ALL
HEADS
MINSTREL
ROBIN
I
ALL
HEADS
I
ROBIN
W
I
I
ALL
HEADS
ROBIN
I
LEFT
HEAD
I
MIDDLE
HEAD
I
RIGHT
HEAD
I
MIDDLE
HEAD
I
LEFT
HEAD
I
RIGHT
HEAD
LEFT
HEAD
ROBIN
I
LEFT
HEAD
I
RIGHT
HEAD
MIDDLE
HEAD
LEFT
HEAD
RIGHT
HEAD
MIDDLE
HEAD
LEFT
HEAD
MIDDLE
HEAD
LEFT
HEAD
I
MIDDLE
HEAD
RIGHT
HEAD
LEFT
HEAD
MIDDLE
HEAD
RIGHT
HEAD
LEFT
HEAD
ALL
HEADS
MIDDLE
HEAD
RIGHT
HEAD
MINSTREL
ROBIN
MINSTREL
ROBIN
I
MINSTREL
ROBIN
MINSTREL
ROBIN
I
MINSTREL
ROBIN
I
MINSTREL
ROBIN
MINSTREL
ROBIN
I
CARTOON
MONKS
CARTOON
CHARACTER
CARTOON
MONKS
CARTOON
CHARACTERS
CARTOON
MONKS
CARTOON
CHARACTER
VOICE
CARTOON
CHARACTER
SCENE
NARRATOR
GALAHAD
GIRLS
ZOOT
GALAHAD
ZOOT
GALAHAD
ZOOT
GALAHAD
ZOOT
MIDGET
CRAPPER
O
ZOOT
MIDGET
CRAPPER
ZOOT
GALAHAD
I
I
ZOOT
GALAHAD
ZOOT
GALAHAD
ZOOT
GALAHAD
I
ZOOT
GALAHAD
I
I
ZOOT
I
GALAHAD
ZOOT
PIGLET
GALAHAD
ZOOT
GALAHAD
B


Traceback (most recent call last):
  File "<pyshell#20>", line 3, in <module>
    print(w)
  File "C:\Python27\lib\idlelib\PyShell.py", line 1356, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> for w in set(text6):
	if w.isupper():
		print(w)

		
PATSY
PERSON
MAN
GUARD
OF
HERBERT
CHARACTERS
A
HEAD
ROGER
MINSTREL
HEADS
PRINCE
W
B
C
MONKS
Y
OFFICER
BRIDE
LAUNCELOT
SENTRY
SUN
LEFT
CHARACTER
CAMERAMAN
RANDOM
DINGO
ZOOT
ROBIN
CART
CONCORDE
GOD
HISTORIAN
CARTOON
CRASH
PRINCESS
DENNIS
ENCHANTER
SECOND
GIRLS
I
BRIDGEKEEPER
FRENCH
MASTER
KNIGHT
SIR
VOICE
CUSTOMER
WOMAN
CROWD
VILLAGERS
AMAZING
OTHER
NARRATOR
ARTHUR
DIRECTOR
PRISONER
BORS
VILLAGER
GUEST
BROTHER
GALAHAD
ARMY
LOVELY
PARTY
LUCKY
O
CRAPPER
STUNNER
CRONE
WITCH
MIDDLE
WINSTON
ALL
GREEN
MAYNARD
MIDGET
PIGLET
NI
WIFE
KNIGHTS
BLACK
RIGHT
ANIMATOR
FATHER
THE
S
OLD
GUARDS
INSPECTOR
GUESTS
DEAD
TIM
SOLDIER
KING
SHRUBBER
SCENE
BEDEVERE
U
N
>>> for w in sorted(set(text6)):
	if w.isupper():
		print(w)

		
A
ALL
AMAZING
ANIMATOR
ARMY
ARTHUR
B
BEDEVERE
BLACK
BORS
BRIDE
BRIDGEKEEPER
BROTHER
C
CAMERAMAN
CART
CARTOON
CHARACTER
CHARACTERS
CONCORDE
CRAPPER
CRASH
CRONE
CROWD
CUSTOMER
DEAD
DENNIS
DINGO
DIRECTOR
ENCHANTER
FATHER
FRENCH
GALAHAD
GIRLS
GOD
GREEN
GUARD
GUARDS
GUEST
GUESTS
HEAD
HEADS
HERBERT
HISTORIAN
I
INSPECTOR
KING
KNIGHT
KNIGHTS
LAUNCELOT
LEFT
LOVELY
LUCKY
MAN
MASTER
MAYNARD
MIDDLE
MIDGET
MINSTREL
MONKS
N
NARRATOR
NI
O
OF
OFFICER
OLD
OTHER
PARTY
PATSY
PERSON
PIGLET
PRINCE
PRINCESS
PRISONER
RANDOM
RIGHT
ROBIN
ROGER
S
SCENE
SECOND
SENTRY
SHRUBBER
SIR
SOLDIER
STUNNER
SUN
THE
TIM
U
VILLAGER
VILLAGERS
VOICE
W
WIFE
WINSTON
WITCH
WOMAN
Y
ZOOT
>>> [w for w in set(text6) if w.endwith('ize')]

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    [w for w in set(text6) if w.endwith('ize')]
AttributeError: 'unicode' object has no attribute 'endwith'
>>> [w for w in set(text6) if w.endswith('ize')]
[]
>>> [w for w in set(text6) if w.endswith('ze')]
[]
>>> [w for w in set(text6) if w.endswith('e')]
[u'whose', u'rescue', u'force', u'here', u'Three', u'therefore', u'me', u'ere', u'example', u'Lie', u'give', u'Camaaaaaargue', u'haste', u'Blue', u'somewhere', u'Here', u'carve', u'one', u'Chaste', u'reasonable', u'side', u're', u'surprise', u'Prepare', u'ninepence', u'Please', u'sire', u'tree', u'See', u'bridge', u'mine', u'Thee', u'cope', u'Therefore', u'vache', u'de', u'illegitimate', u'miserable', u'Grenade', u'score', u'argue', u'three', u'life', u'suppose', u'gave', u'mistake', u'make', u'beside', u'couple', u'humble', u'Mine', u'Table', u'the', u'appease', u'Alice', u'Are', u'Prince', u'people', u'sponge', u'escape', u'ignore', u'Quite', u'Use', u'presence', u'Make', u'formidable', u'suffice', u'Eee', u'invincible', u'inside', u'awhile', u'tie', u'welcome', u'samite', u'dance', u'mile', u'zone', u'foe', u'scribble', u'trouble', u'Where', u'minute', u'leave', u'He', u'brave', u'True', u'change', u'grenade', u'live', u'entrance', u'clue', u'sample', u'sacrifice', u'temperate', u'maybe', u'tale', u'course', u'police', u'She', u'name', u'Welcome', u'quite', u'language', u'thine', u'place', u'There', u'Pure', u'vote', u'little', u'bite', u'anyone', u'were', u'aside', u'note', u'take', u'performance', u'sure', u'We', u'unsingable', u'where', u'Forgive', u'magne', u'come', u'those', u'case', u'these', u'single', u'middle', u'someone', u'considerable', u'same', u'Tale', u'Brave', u'snore', u'collective', u'Pie', u'nose', u'nice', u'Since', u'table', u'stone', u'violence', u'favorite', u'Message', u'there', u'hee', u'Castle', u'handsome', u'gone', u'migrate', u'examine', u'More', u'separate', u'time', u'tackle', u'Practice', u'worse', u'profane', u'large', u'Course', u'Silence', u'Bedevere', u'Providence', u'fortune', u'more', u'excuse', u'science', u'Charge', u'nine', u'sense', u'huge', u'creature', u'refuse', u'trade', u'Excuse', u'late', u'indefatigable', u'ye', u'Ere', u'die', u'everyone', u'house', u'Picture', u'since', u'None', u'forgive', u'Nine', u'terrible', u'castle', u'done', u'horse', u'bride', u'lie', u'cave', u'The', u'Bridge', u'fine', u'courage', u'nibble', u'see', u'are', u'please', u'wide', u'became', u'simple', u'mumble', u'expensive', u'fire', u'else', u'rope', u'while', u'Bedwere', u'Those', u'impersonate', u'commune', u'purpose', u'dine', u'dare', u'continue', u'Fine', u'some', u'be', u'lose', u'crone', u'ounce', u'silence', u'auntie', u'liege', u'Come', u'line', u'scrape', u'e', u'once', u'outside', u'wave', u'arrange', u'spake', u'private', u'use', u'giggle', u'ride', u'anywhere', u'rode', u'pure', u'One', u'move', u'Concorde', u'mandate', u'Supreme', u'mate', u'cause', u'Divine', u'confuse', u'scene', u'apologise', u'France', u'false', u'gentle', u'have', u'able', u'face', u'pause', u'Meanwhile', u'handle', u'Once', u'she', u'we', u'Gable', u'agree', u'Hee', u'waste', u'Battle', u've', u'strange', u'impeccable', u'Have', u'Neee', u'executive', u'Ninepence', u'Be', u'five', u'like', u'become', u'because', u'alive', u'home', u'noise', u'gurgle', u'dynamite', u'he', u'made', u'wise', u'domine', u'supreme', u'Lake', u'offensive', u'Five', u'Gorge', u'Like', u'Remove', u'chance', u'Heee', u'pestilence']
>>> [w for w in set(text6) if w.endswith('img')]
[]
>>> [w for w in set(text6) if w.endswith('ing')]
[u'bringing', u'guiding', u'groveling', u'distributing', u'preserving', u'advancing', u'writing', u'excepting', u'saying', u'sneaking', u'rejoicing', u'chickening', u'wedding', u'Bring', u'starling', u'shimmering', u'Ewing', u'wounding', u'Morning', u'appearing', u'herring', u'everything', u'asking', u'yelling', u'dying', u'Running', u'setting', u'string', u'spanking', u'bring', u'understanding', u'working', u'going', u'riding', u'repressing', u'counting', u'carving', u'entering', u'living', u'looking', u'suggesting', u'training', u'thing', u'bitching', u'Yapping', u'walking', u'anging', u'learning', u'perpetuating', u'blessing', u'Supposing', u'running', u'being', u'pissing', u'using', u'exciting', u'boing', u'having', u'Packing', u'dressing', u'enjoying', u'laughing', u'coming', u'acting', u'Leaving', u'king', u'dancing', u'nothing', u'lying', u'approaching', u'throwing', u'kneeling', u'King', u'smashing', u'meeting', u'resting', u'binding', u'shivering', u'marrying', u'crying', u'Nothing', u'chanting', u'anything', u'Everything', u'warning', u'dragging', u'dictating', u'averting', u'buggering', u'telling', u'packing', u'making', u'sing', u'singing', u'carrying', u'fooling', u'something', u'daring', u'bathing', u'doing', u'undressing', u'depressing', u'signifying', u'taunting', u'wetting', u'opening', u'taking', u'passing', u'whispering', u'Spring', u'exploiting', u'getting']
>>> [w for w in set(text6) if w.endswith('ize')]
[]
>>> [w for w in set(text6) if w.endswith('IZE')]
[]
>>> [w for w in set(text6) if w.endswith('ize')]
[]
>>> [w for w in set(text6) if w.contains('z')]

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    [w for w in set(text6) if w.contains('z')]
AttributeError: 'unicode' object has no attribute 'contains'
>>> [w for w in set(text6) if 'z' in w]
[u'zoop', u'zone', u'Fetchez', u'zoo', u'amazes', u'frozen', u'zhiv', u'zoosh']
>>> [w for w in set(text6) if 'pt' in w]
[u'excepting', u'temptation', u'Thppppt', u'Thpppt', u'Chapter', u'temptress', u'aptly', u'empty', u'ptoo', u'Thpppppt', u'Thppt']
>>> text6
<Text: Monty Python and the Holy Grail>
>>> [w for w in set(text6) if w.istitle()]
[u'Lead', u'Does', u'Until', u'Winter', u'Uhh', u'Go', u'Erbert', u'Mmm', u'Put', u'Rather', u'Mother', u'Three', u'Book', u'Stay', u'Dingo', u'Lie', u'Lord', u'Camaaaaaargue', u'A', u'Will', u'Oooh', u'All', u'Greetings', u'Speak', u'Blue', u'Stop', u'His', u'Here', u'Hic', u'Chaste', u'Woa', u'Holy', u'Uuh', u'Hold', u'Must', u'W', u'Hallo', u'Prepare', u'Please', u'Quoi', u'Man', u'Iesu', u'B', u'Splendid', u'Lancelot', u'Victory', u'See', u'Shrubberies', u'Then', u'Thee', u'Ridden', u'They', u'Ask', u'Therefore', u'Knight', u'That', u'European', u'Aah', u'Quick', u'Over', u'Dramatically', u'Run', u'Grenade', u'C', u'Bravest', u'Bring', u'Sorry', u'Caerbannog', u'Other', u'Follow', u'Nay', u'Tell', u'Thou', u'Riiight', u'Of', u'Apples', u'Bristol', u'Y', u'Mind', u'Mine', u'Table', u'Thank', u'Churches', u'Ewing', u'Or', u'Surely', u'Alice', u'Morning', u'Try', u'Bravely', u'Pendragon', u'Are', u'Prince', u'Idiom', u'Quite', u'Let', u'Ho', u'Hm', u'Ha', u'Didn', u'Thppppt', u'First', u'Use', u'Cut', u'Make', u'Amen', u'Aaagh', u'Bread', u'Defeat', u'Eee', u'Sir', u'Twenty', u'Between', u'Running', u'Yeaah', u'Aauuugh', u'Roger', u'Chicken', u'Today', u'Burn', u'Where', u'Just', u'He', u'Cherries', u'Thpppt', u'True', u'Agh', u'Quiet', u'English', u'My', u'Bors', u'Fetchez', u'Seek', u'Said', u'When', u'Hello', u'Oui', u'Our', u'Galahad', u'Britons', u'Who', u'Why', u'Yeaaah', u'Wait', u'She', u'Tower', u'Enchanter', u'Skip', u'Anthrax', u'Welcome', u'Throw', u'Rheged', u'Stand', u'Oooo', u'Even', u'Dappy', u'Yay', u'Hang', u'There', u'Black', u'Pure', u'Hmm', u'Angnor', u'Court', u'Aauuuves', u'Do', u'Halt', u'Aaaah', u'Off', u'Beyond', u'Ulk', u'Yapping', u'We', u'Ector', u'Right', u'Forgive', u'Ecky', u'Shrubber', u'Aaah', u'Death', u'Crapper', u'But', u'Schools', u'Hurry', u'Princess', u'Together', u'Action', u'Round', u'Hyy', u'Mercea', u'Aaaaugh', u'Open', u'Supposing', u'I', u'Clear', u'Is', u'It', u'In', u'Wayy', u'Cornwall', u'Tale', u'Brave', u'Pin', u'Pie', u'Since', u'Hoo', u'Listen', u'Four', u'Oooooooh', u'Chapter', u'Autumn', u'Message', u'Ni', u'No', u'Away', u'Castle', u'Joseph', u'Build', u'Hoa', u'Thursday', u'How', u'More', u'Lady', u'Great', u'Yeah', u'Practice', u'Uugh', u'Packing', u'Course', u'Actually', u'Aramaic', u'Pull', u'Arthur', u'Zoot', u'Alright', u'Silence', u'Clark', u'Bedevere', u'Exactly', u'Umhm', u'Lucky', u'Providence', u'Too', u'Aaaaaaaah', u'Cider', u'So', u'Found', u'Anarcho', u'Charge', u'Wood', u'Your', u'Loimbard', u'Don', u'Assyria', u'What', u'Iiiives', u'Excuse', u'Ere', u'Bad', u'Erm', u'Oooohoohohooo', u'Mud', u'Armaments', u'Hiyaah', u'Picture', u'Huyah', u'None', u'Leaving', u'Nine', u'Eh', u'Aaaaaaaaah', u'Father', u'Peng', u'With', u'Gallahad', u'Hand', u'Thy', u'Anybody', u'Aggh', u'Grail', u'The', u'Bridge', u'Hiyah', u'If', u'Robinson', u'Hah', u'Explain', u'Hill', u'Forward', u'Behold', u'Haw', u'French', u'Help', u'Anyway', u'For', u'Umm', u'King', u'Could', u'African', u'Launcelot', u'Aauuggghhh', u'Yes', u'Waa', u'God', u'Consult', u'Old', u'Winston', u'Bloody', u'Bedwere', u'Tis', u'Til', u'Tim', u'Those', u'Aaaaaah', u'Aaauggh', u'Tall', u'Dennis', u'On', u'Oh', u'Did', u'Ow', u'Ohh', u'Bones', u'Fine', u'Iiiiives', u'Whoa', u'Frank', u'Nothing', u'Look', u'O', u'Bon', u'Looks', u'Olfin', u'Isn', u'Everything', u'Ooh', u'Gawain', u'Every', u'Come', u'Steady', u'Badon', u'Perhaps', u'Saxons', u'To', u'May', u'Ah', u'Am', u'An', u'As', u'At', u'Ay', u'Saint', u'Not', u'Now', u'Uther', u'Fiends', u'Yup', u'Ahh', u'Back', u'Doctor', u'By', u'Huh', u'Huy', u'Chop', u'Guy', u'Torment', u'Maynard', u'Almighty', u'Beast', u'Guards', u'Aaauugh', u'One', u'Farewell', u'Himself', u'Recently', u'Concorde', u'Herbert', u'Robin', u'Summer', u'Supreme', u'Say', u'Which', u'Nador', u'Very', u'Nu', u'This', u'Auuuuuuuugh', u'Ives', u'Firstly', u'Jesus', u'Divine', u'Excalibur', u'Midget', u'France', u'Patsy', u'Peril', u'Thsss', u'Shut', u'Meanwhile', u'Chickennn', u'Psalms', u'Keep', u'Once', u'Camelot', u'Ayy', u'Aaaugh', u'Walk', u'Good', u'Arimathea', u'Hooray', u'S', u'Gable', u'Shh', u'Christ', u'Would', u'Hey', u'Hee', u'Heh', u'Get', u'Hiyya', u'Dragon', u'Honestly', u'Knights', u'And', u'Battle', u'You', u'England', u'Attila', u'Brother', u'Dis', u'Order', u'Piglet', u'Spring', u'Have', u'Neee', u'Eternal', u'Ninepence', u'Be', u'Augh', u'Far', u'Hya', u'Unfortunately', u'Two', u'Monsieur', u'Um', u'Un', u'Uh', u'Ages', u'Really', u'Aauuuuugh', u'Quickly', u'Thpppppt', u'Antioch', u'Most', u'Well', u'Thppt', u'Silly', u'Aagh', u'Britain', u'Allo', u'Lake', u'Shall', u'Never', u'Five', u'Gorge', u'Like', u'Remove', u'Swamp', u'U', u'Heee', u'N']
>>> sent = ["she", "sells", "sea", "shells", "by", "the", "sea", "shore"]
>>> for w in sent:
	if w.startswith('sh'):
		print(w)

		
she
shells
shore
>>> for w in sent:
	if len(w) > 4:
		print(w)

		
sells
shells
shore
>>> sum([len(w) for w in sent])
30
>>> sum([len(w) for w in sent])/len(sent)
3
>>> len(sent)
8
>>> from __future__ import division
>>> sum([len(w) for w in sent])/len(sent)
3.75
>>> def vocab_size(text):
	return len(set(text))

>>> vocab_size(sent)
7
>>> def vocab_size_new(text):
	return len(set([w.lower() for w in text]))

>>> vocab_size_new(sent)
7
>>> vocab_size_new(text1)
17231
>>> vocab_size(text1)
19317
>>> def vocab_size_new(text):
	return len(set([w.lower() for w in text if w.isaplha()]))

>>> vocab_size_new(text1)

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    vocab_size_new(text1)
  File "<pyshell#59>", line 2, in vocab_size_new
    return len(set([w.lower() for w in text if w.isaplha()]))
AttributeError: 'unicode' object has no attribute 'isaplha'
>>> def vocab_size_(text):
	return len(set([w.lower() for w in text if w.isalpha()]))

>>> vocab_size_(text1)
16948
>>> vocab_size_new(text1)

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    vocab_size_new(text1)
  File "<pyshell#59>", line 2, in vocab_size_new
    return len(set([w.lower() for w in text if w.isaplha()]))
AttributeError: 'unicode' object has no attribute 'isaplha'
>>> def percent(word, text):
	return len([w.lower() for w in text if w.isalpha() and w==word.lower()]) / len([w.lower() for w in text if w.isalpha()]) * 100

>>> percent("love", text1)
0.01099097366287936
>>> percent("love", whale)

Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    percent("love", whale)
NameError: name 'whale' is not defined
>>> percent("whale", text1)
0.4149092557736958
>>> percent("the", text1)
6.283631234515321
>>> percent("a", text1)
2.092406611070658
>>> fdist = FreqDist(text1)
>>> fdist["whale"]
906
>>> fdist["whale"]/len(text1)
0.003473673313677301
>>> fdist("the")

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    fdist("the")
TypeError: 'FreqDist' object is not callable
>>> fdist['the']
13721
>>> fdist['a']
4569
>>> set(sent3) < set(text1)
True
>>> set(sent3) < set(sent1)
False
>>> sent3
['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven', 'and', 'the', 'earth', '.']
>>> sent1
['Call', 'me', 'Ishmael', '.']
>>> ['a', 'a', 'a', 'a'] < ['b', 'c']
True
>>> 
