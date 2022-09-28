def fun(a,b):
  fname = a.title()
  lname = b.title()
  #return fname+lname
#we can also return in this way
  return f"{fname} {lname}"

print(fun("sam","huj"))
