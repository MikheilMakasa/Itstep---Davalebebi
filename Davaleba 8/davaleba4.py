palindromia = lambda s: s == s[::-1]


strings = ['ანა', 'ვეფხისტყაოსანი', 'როგორ', 'პასუხი']


palindromebi = list(filter(palindromia, strings))

print(palindromebi)