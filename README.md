# processor
AX - zwykly rejestr, adres - 0011 (out), 0101 (in)
AL - zwykly rejestr, adres - 0010 (out), 0100 (in)
AH - zwykly rejestr, adres - 0001 (out), 0001 (in)

BH - rejestr obliczeniowy(arytmetyka), adres - 0011 (in)   B number
CH - rejestr obliczeniowy 2(arytmetyka), adres - 0010 (in) A number
wybór operacji + lub -, jeżeli - to należy wywołać - 10000 (out)

EAX - rejestr przechowywujacy wyniki obliczen, adres - 0100 (out)

CM - rejestr porównujący (A), adres - 0110 (in)
DM - rejestr porównujący (B), adres - 1000 (in)

wyjście z komparatora: a < b - adres, 0101 (out)
wyjście z komparatora: a = b - adres, 0110 (out)
wyjście z komparatora: a > b - adres, 0111 (out)

wyjście pin 0, adress, 1001 (out)
wyjście pin 1, adress, 1010 (out)

instrukcje w sram nr:1  pierwsze 4bit - rejestry out, drugie 4bit rejestry in
intrukcje w sram nr: 0 tylko pierwsze 4bit (literały)

![image](https://github.com/michal95pl/processor/assets/85219287/f1e321aa-fb1c-429b-9b37-975bc1a37cd3)
