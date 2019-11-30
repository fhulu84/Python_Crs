# Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string

def mix_string(s1, s2):
  middles = s1[int(len(s1) / 2)] + s2[int(len(s2) / 2)]
  
  return s1[0] + s2[0] + middles + s1[-1] + s2[-1] 


print(mix_string('America', 'Japan'))