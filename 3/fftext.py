text = "X-DSPAM-Confidence:    0.8475";
text0 = text.find("0")
fftext = text[text0:99]
print(float(fftext))
