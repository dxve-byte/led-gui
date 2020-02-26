'''
Das ist die "Compare File" um bestimmte Stichwörter zu Filtern damit die Sprachsteuerung
weiß was Sie damit auswerten soll

!!!ALLES KLEIN SCHREIBEN!!!

'''


#searchintgroup
Agroup = ['suche', 'kannst', 'du', 'finden', 'was', 'ist', 'such', 'sind', 'im', 'nach', 'internet', 'netz']

#welcomegroup
Bgroup = ['hallo', 'hey', 'hi', 'guten tag', 'servus', 'die', 'ahoi', 'Huhu', 'moin', 'grüß dich', 'hallöchen', 'na']

#timegroup
Cgroup = ['was', 'wieviel', 'wie', 'ist', 'es', 'zeit', 'uhrzeit', 'clock', 'wird', 'spät']

#weathergroup
Dgroup = ['was', 'wie', 'sagt', 'das', 'wetter', 'wird', 'klima', 'wird', 'in']

#howareyougroup
Egroup = ['wie', "geht's", 'es', 'dir', 'gehts', 'sag']

#whereareyougroup
Fgroup = ['wer', 'bist', 'denn', 'stell', 'dich', 'mal', 'vor']

#insultgroup
Ggroup = ['spasst', 'huhrensohn', 'hitler', 'neger', 'dumme', 'sau', 'bitch', 'dünnbrettbohrer', 'blöd',
				'poltergeist', 'hasse', 'dich', 'du', 'bist', 'scheisse']

#sleeptruegroup
Hgroup = ['sleepmode','schlafmode','schlafmodus', 'silentmode', 'ruhemodus', 'ein', 'anschalten', 'einschalten', 'du', 'kannst', 'reden']

#sleepfalsegroup
Igroup = ['sleepmode','schlafmode', 'silentmode', 'schlafmodus', 'ruhemodus', 'aus','ausschalten', 'sei', 'ruhig', 'stop',
					'hör', 'auf', 'zu', 'reden', 'sei', 'ruhig']

#whatcanyoudogroup
Jgroup = ['was', 'kannst', 'du', 'alles', 'für', 'bist', 'zuständig']

#consolegroup
Kgroup = ['konsolenmodus', 'ein', 'starte', 'console', 'kontrollmodus', 'controlemode', 'programmiermodus']

#randomnumbgroup
Lgroup = ['zufallszahl', 'nenne', 'sage', 'zufall']

#music
Mgroup = ['playlist', 'spiele', 'songs', 'lied', 'song', 'lieblingslied', 'lieblingsplaylist', 'meine', 'mein']

Ngroup = ['nehme', 'auf', 'kannst', 'du', 'dir', 'merken', 'speicher', 'notiz', 'nimm']


groups = [Agroup, Bgroup, Cgroup, Dgroup,
			Egroup, Fgroup, Ggroup, Hgroup,
			Igroup, Jgroup, Kgroup, Lgroup, 
			Mgroup, Ngroup]
			
			
			
groupsdic = {
	'Agroup': Agroup,
	'Bgroup': Bgroup,
	'Cgroup': Cgroup,
	'Dgroup': Dgroup,
	'Egroup': Egroup,
	'Fgroup': Fgroup,
	'Ggroup': Ggroup,
	'Hgroup': Hgroup,
	'Igroup': Igroup,
	'Jgroup': Jgroup,
	'Kgroup': Kgroup,
	'Lgroup': Lgroup,
	'Mgroup': Mgroup,
	'Ngroup': Ngroup,
}
