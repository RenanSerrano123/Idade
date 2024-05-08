ano=int(input('Qual ano voce nasceu?'))
idade=2024-ano
if idade<=12:
  print('Voce tem', idade ,'anos e, portanto, e crianca.')
elif 13<=idade<=17:
  print('Voce tem', idade ,'anos e, portanto, e adolescente.')
elif 18<=idade<=64:
  print('Voce tem', idade ,'anos e, portanto, e adulto.')
else:
  print('Voce tem', idade ,'anos e, portanto, e experiente.')