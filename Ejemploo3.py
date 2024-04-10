def main():
    Lado1 = 4
    Lado2 = 6
    rect_area = f(Lado1, Lado2)
    print("Área del rectángulo:", rect_area)

    base = 5
    altura = 8
    tri_area = g(base, altura)
    print("Área del triángulo:", tri_area)

#A.rectángulo
def f(BaseMenor, BaseMayor):
    result = BaseMenor * BaseMayor
    return result

# A.triángulo
def g(BaseDelTriangulo, AlturaDelTriangulo):
    r = 0.5 * BaseDelTriangulo * AlturaDelTriangulo
    return r
main()
