#!/usr/local/bin/python3
import sys

HTML_BASE = '''<html>
<body>
<table border="1" bgcolor="Gainsboro">
<tr>
<th>No.</th>
<th>Country</th>
<th>Capital</th>
<th>Wiki</th>
<th>Flag</th>
</tr>
%s
</table>
</body>
</html>'''

def main():
    inp = sys.argv[1]
    with open(inp) as f:
        data = f.read().splitlines()

    html_countries = []
    for num, line in enumerate(data[1:], start=1):
        comps = line.strip('\n').split(';')
        html_comps = ["<td>%s</td>" % c for c in comps]
        html_coun = '''<tr>
<td>%s</td>
<td width="200px">%s</td>
<td>%s</td>
<td width="200px"><a href="%s" target="_blank">%s</a></td>
<td width="300px" height="150px" align="center"><a href="flags/%s" target="_blank"><img height="125px" src="flags/%s"/></a></td>
</tr>''' % (num, comps[0], comps[1], comps[2], comps[2], comps[3], comps[3])
        # html_country = "<tr>\n%s\n</tr>" % '\n'.join(html_comps)

        html_countries.append(html_coun)

    html_rows = '\n'.join(html_countries)
    full_html = HTML_BASE % html_rows

    print(full_html)

if __name__ == '__main__':
    main()