__author__ = 'kathan'


def printParenthesis(result, index, n, open, close):
  if close == n:
    print result
    return
  else:
    if open > close:
        result += '}'
        printParenthesis(result, index+1, n, open, close+1)
    if open < n:
       result = result[0:index]
       result += '{'
       printParenthesis(result, index+1, n, open+1, close)

printParenthesis('', 0, 3, 0, 0)
