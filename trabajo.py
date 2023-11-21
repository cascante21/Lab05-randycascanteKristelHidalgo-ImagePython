import argparse
from PIL import Image
import matplotlib.pyplot as plt
import cv2

class PILManipuladorImagen:
    def mostrar_imagen(self, ruta):
        imagen = Image.open(ruta)
        imagen.show()

class MatplotlibManipuladorImagen:
    def mostrar_imagen(self, ruta):
        imagen = plt.imread(ruta)
        plt.imshow(imagen)
        plt.show()

class OpenCVManipuladorImagen:
    def mostrar_imagen(self, ruta):
        imagen = cv2.imread(ruta)
        cv2.imshow('Imagen', imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def parse_args():
    parser = argparse.ArgumentParser(description="Procesamiento de Imágenes")
    parser.add_argument("--biblioteca", choices=["PIL", "Matplotlib", "OpenCV"], help="Especifica la biblioteca a utilizar.")
    parser.add_argument("--imagen", required=True, help="Ruta de la imagen a procesar.")
    return parser.parse_args()

def main():
    args = parse_args()

    if args.biblioteca == 'PIL':
        manipulador = PILManipuladorImagen()
    elif args.biblioteca == 'Matplotlib':
        manipulador = MatplotlibManipuladorImagen()
    elif args.biblioteca == 'OpenCV':
        manipulador = OpenCVManipuladorImagen()
    else:
        print("Biblioteca no válida. Selecciona PIL, Matplotlib u OpenCV.")
        return

    try:
        manipulador.mostrar_imagen(args.imagen)
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado - {args.imagen}")
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")

if __name__ == "__main__":
    main()
