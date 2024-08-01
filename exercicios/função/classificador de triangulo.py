def classificador_triangulo ( ):
    a = float ( input ( "\nValor A:\t" ) )
    b = float ( input ( "Valor B:\t" ) )
    c = float ( input ( "Valor C:\t" ) )


    if ((a + b > c) or (a + c > b) or (b + c > a)) and a == b == c:
        print ( "Os valores podem ser que ser de lados de um triângulo equilátero" )
    elif a == b or a == c or b == c:
        print ( "Os valores podem ser que ser de lados de um triângulo isósceles" )
    elif a != b != c != a:
        print ( "Os valores podem ser que ser de lados de um triângulo escaleno" )
    else:
        print ( "Os valores podem não ser dos lados de um triângulo" )
classificador_triangulo ( )