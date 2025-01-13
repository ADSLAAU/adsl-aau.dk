#!/usr/bin/python3

from os import listdir;
from os.path import isfile, isdir, join;
from textwrap import indent;

def walk(folder: str) -> str:
    output: str = "";
    output += "<ul>\n";
    entries = listdir(folder);
    entries.sort(reverse=True);
    for entry in entries:
        path = join(folder, entry);
        if isfile(path):
            output += f"\t<li><a href=\"{path}\">{entry}</a></li>\n";
        elif isdir(path):
            output += f"\t<li><details>"
            output += f"\t<summary>{entry}</summary>\n";
            output += indent(walk(path), '\t\t');
            output += f"\t</details></li>\n";
        else:
            raise ValueError(f"Entry \"{entry}\" at \"{path}\" is neither a file nor directory");
    output += "</ul>\n";
    return output;
            
        

print('''
<!DOCTYPE html>
<html lang="da">
	<head>
		<link rel="stylesheet" href="../base.css"/>
		<link rel="icon" href="../logo.png"/>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta charset="UTF-8">
		<title>ADSLs regnskab</title>
	</head>
	<body>
		<nav>
			<ul>
				<li><a href=".."><img class="logo" src="../logo.png"></a></li>
				<li><a href="../regnskab">Regnskab</a></li>
				<li><a href="../vedtægter">Vedtægter</a></li>
				<li><a href="../referat">Referater</a></li>
				<li><p>lasaga</p></li>
				<li><a href="../ADSL_Ansøgningsskema.docx">Pengeformular</a></li>
			</ul>
		</nav>
		<main>
			<h1>ADSLs Regnskab</h1>
			<p>ADSL har politik om 100% åbent regnskab.</p>
			<p>Regnskabet bliver presenteret til hver generelforsamling, og I kan finde de tidligere her:</p>
''');

print(indent(walk("documents"), '\t'*3));

print('''
		</main>
	</body>
</html>
''');
