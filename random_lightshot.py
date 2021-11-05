import webbrowser
import random
values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4','5','6','7','8','9']

for i in range(25):
    final = ''
    final = final.join(random.choices(values, k=6))
    webbrowser.open(("https://prnt.sc/{}".format(final)))


