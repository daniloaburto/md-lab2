LABORATORIO 2 - MINERÍA DE DATOS
================================

Repositorio en: <https://github.com/daniloaburto/md-lab2>

- **Profesor**: Max Chacón
- **Ayudante**: Felipe Bello
- Integrantes: 
    - Iván Abarca
    - Danilo Aburto
- Fecha: 05 de Agosto de 2013

Modo de uso
-----------
```sh
  $ python lab2.py <archivo_names> <archivo_data> <num_reglas> <soporte> [--classes=<tipo_busqueda>]
```

Donde:

- **archivo_names**: es la ruta hasta el archivo de extensión '.names'
- **archivo_data**:  es la ruta hasta el archivo de extensión '.data'
- **num_reglas**:    es el número de mejores reglas a generar
- **soporte**:       es el soporte mínimo, toma valores entre 0 y 1
- **tipo_busqueda**: (opcional) indica si se buscan reglas sólo con consecuentes de tipo Clase. Toma los valores True o False
    
Ejemplos:

```sh
  $ python lab2.py datasets/prueba.names datasets/prueba.data 10 0.2
  $ python lab2.py datasets/prueba.names datasets/prueba.data 10 0.2 --classes=True
```


**NOTA:**
Se recomiendo utilizar soporte mayor a 20% para obtener tiempos de
usuario rápidos y luego posteriormente disminuirlo.
