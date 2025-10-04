import string

huruf = string.ascii_uppercase
huruf = list(huruf)
sandi = ['._/','_.../','_._./','_../','./','.._./','_ _./','..../','../','._ _ _/','_ . _/','._../','_ _/','_./','_ _ _/','._ _./','_ _ . _/','._./','.../','_/','.._/', '..._/','._ _/','_ .. _/','_._ _/','_ _ ../' ]
print(f"huruf : {huruf}")
print(f"sandi : {sandi}")

kalimat= input(str("masukan pesanmu :"))
sandi_morse = ""

for letter in kalimat :
    index = huruf.index(letter)
    sandi_morse += sandi[index]

print(f"pesanmu adalah {kalimat}")
print(f"samdi morsenya adalah {sandi_morse}")